#!/usr/bin/env bash
#
# Builds a single concatenated markdown file from the Knowledge Base.
# Output: dist/modern-mind-kb.md
#
# Default (compact mode): strips three heavy sections from each source distillation —
#   `## Key Passages`, `## Open Questions`, `## Contradicts / Extends` —
# while leaving concept, method and practice entries untouched. Source files in `sources/`
# are not modified; the canonical content stays full-fat. Compaction lives only
# at bundle-build time.
#
# Pass `--full` to bypass the compaction and produce a full-fidelity bundle
# (matches pre-2026-04-30 behavior, byte-for-byte modulo the helper notice).
#
set -euo pipefail

# --- Flags ---
FULL=0
for arg in "$@"; do
  case "$arg" in
    --full) FULL=1 ;;
    -h|--help)
      cat <<USAGE
Usage: $0 [--full]

  --full   produce a full-fidelity bundle (no source-section compaction)
USAGE
      exit 0
      ;;
    *)
      echo "unknown flag: $arg" >&2
      exit 2
      ;;
  esac
done

OUTDIR="dist"
OUTFILE="$OUTDIR/modern-mind-kb.md"

mkdir -p "$OUTDIR"

# Keep README counts in sync with current state before bundling. Best-effort —
# if the python helper is unavailable (CI without uv, etc.), the bundle still
# builds with potentially-stale README counts.
if command -v uv >/dev/null 2>&1; then
  uv run python tooling/scripts/update_readme_counts.py >/dev/null 2>&1 || true
fi

# Sections to include (order matters)
SECTIONS=("concepts" "methods" "practices" "sources")
LABELS=("Concepts" "Methods" "Practices" "Sources")

# --- Awk filters ---
#
# Frontmatter-only: strip the YAML frontmatter, print everything else.
# Used for concept, method and practice entries (and sources when --full).
read -r -d '' AWK_FRONTMATTER_ONLY <<'AWK' || true
  BEGIN { in_frontmatter=0; frontmatter_done=0 }
  /^---$/ && !frontmatter_done {
    if (in_frontmatter) { frontmatter_done=1; next }
    else { in_frontmatter=1; next }
  }
  frontmatter_done || !in_frontmatter { print }
AWK

# Frontmatter + heavy-source-section strip. Used for source entries in compact mode.
# Drops the entire body of these H2 sections (until the next H2 or H1):
#   ## Key Passages
#   ## Open Questions
#   ## Contradicts / Extends
read -r -d '' AWK_COMPACT_SOURCE <<'AWK' || true
  BEGIN { in_frontmatter=0; frontmatter_done=0; skip_section=0 }
  /^---$/ && !frontmatter_done {
    if (in_frontmatter) { frontmatter_done=1; next }
    else { in_frontmatter=1; next }
  }
  in_frontmatter && !frontmatter_done { next }
  /^## / {
    t = $0
    sub(/[[:space:]]+$/, "", t)
    if (t == "## Key Passages" || t == "## Open Questions" || t == "## Contradicts / Extends") {
      skip_section = 1
      next
    } else {
      skip_section = 0
    }
  }
  /^# / { skip_section = 0 }
  !skip_section { print }
AWK

# --- Header ---
cat > "$OUTFILE" << 'HEADER'
# Modern Mind — Knowledge Base for the AI Age

Research, practice, and professional insight translated into concepts you can teach from, apply, and verify.

Not anti-AI. Not blindly pro-AI. Pro-human.

> This file is auto-generated from the Modern Mind Knowledge Base.
> Source: https://github.com/jarmolkowicz/modrn-mind-knowledge-base
> Website: https://modrnmind.com

---

HEADER

# --- Table of Contents ---
echo "## Table of Contents" >> "$OUTFILE"
echo "" >> "$OUTFILE"

for i in "${!SECTIONS[@]}"; do
  section="${SECTIONS[$i]}"
  label="${LABELS[$i]}"
  echo "### ${label}" >> "$OUTFILE"
  echo "" >> "$OUTFILE"

  for file in "$section"/*.md; do
    [ -f "$file" ] || continue
    # Extract the H1 title from the file, fall back to filename
    title=$(grep -m1 '^# ' "$file" | sed 's/^# //' || true)
    if [ -z "$title" ]; then
      title=$(basename "$file" .md | tr '-' ' ')
    fi
    # Create anchor from filename
    anchor="${section}-$(basename "$file" .md)"
    echo "- [${title}](#${anchor})" >> "$OUTFILE"
  done
  echo "" >> "$OUTFILE"
done

echo "---" >> "$OUTFILE"
echo "" >> "$OUTFILE"

# --- Content ---
for i in "${!SECTIONS[@]}"; do
  section="${SECTIONS[$i]}"
  label="${LABELS[$i]}"

  echo "## ${label}" >> "$OUTFILE"
  echo "" >> "$OUTFILE"

  for file in "$section"/*.md; do
    [ -f "$file" ] || continue

    anchor="${section}-$(basename "$file" .md)"

    # Add anchor-compatible heading
    echo "<a id=\"${anchor}\"></a>" >> "$OUTFILE"
    echo "" >> "$OUTFILE"

    # Include file content (strip YAML frontmatter; in compact mode also strip
    # heavy H2 sections from source entries).
    if [ "$section" = "sources" ] && [ "$FULL" = "0" ]; then
      awk "$AWK_COMPACT_SOURCE" "$file" >> "$OUTFILE"
    else
      awk "$AWK_FRONTMATTER_ONLY" "$file" >> "$OUTFILE"
    fi

    echo "" >> "$OUTFILE"
    echo "---" >> "$OUTFILE"
    echo "" >> "$OUTFILE"
  done
done

# --- Stats ---
TOTAL=0
for section in "${SECTIONS[@]}"; do
  COUNT=0
  for file in "$section"/*.md; do
    [ -f "$file" ] || continue
    COUNT=$((COUNT + 1))
  done
  TOTAL=$((TOTAL + COUNT))
done

if [ "$FULL" = "1" ]; then
  MODE="full"
else
  MODE="compact (sources stripped of Key Passages / Open Questions / Contradicts-Extends)"
fi

BYTES=$(wc -c < "$OUTFILE" | tr -d ' ')
KB=$(awk "BEGIN { printf \"%.1f\", $BYTES / 1024 }")
echo "Bundle built: $OUTFILE ($TOTAL entries, ${KB} KB, mode=$MODE)"
