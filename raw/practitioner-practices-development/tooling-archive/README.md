# Completed batch tooling

These `.py.txt` files preserve the exact scripts used for the September 2026 practitioner batch. Three further script snapshots remain under `../extraction/`, also with `.py.txt` suffixes.

They are historical records, not reusable commands. Source IDs, editorial judgments, expected counts and destinations refer to a fixed batch. Some writers lack rerun guards; `check_integrated_practices.py.txt` even performs source-link synchronization and rewrites completion hashes before reporting. Re-running these against later integrations could damage provenance or mistake later approved edits for errors.

No script content was removed or rewritten. [Archive manifest](../../../tooling/audits/practice-tooling-archive-2026-09-27.json) records previous locations, current locations and SHA-256 hashes. Old commands in historical records describe past execution only.

Use the [maintained tooling](../../../tooling/README.md) for current checks. A new extraction requires a new batch and fresh review; the stored decisions do not authorize another integration.
