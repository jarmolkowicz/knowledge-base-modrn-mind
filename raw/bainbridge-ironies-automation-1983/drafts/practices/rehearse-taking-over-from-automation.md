---
status: emerging
area:
- preservation
sources:
- Bainbridge, L. (1983). Ironies of automation. Automatica, 19(6), 775–779.
source_entries:
- bainbridge-ironies-automation-1983
intended_outcomes:
- independent-capability
- accountability
---

# Rehearse taking over from automation

## Use When

A workflow relies on a person to detect a failure and resume control. Use a safe simulation or training environment appropriate to that workflow.

## Try It

1. Choose a credible failure and define the information and time available to the person expected to respond.
2. Rehearse detecting it, understanding the current state and taking the required corrective action.
3. Check what prevented recovery: missing skill, stale context, poor signals, unavailable controls or insufficient time.
4. Improve training or the system design, then repeat an appropriate exercise. Do not designate human takeover as a fallback that the person cannot realistically perform.

[Inference] This review-and-rehearsal sequence adapts Bainbridge’s recommendations to current workflows. The source does not test a language-model deployment. Controls and responsibility checks are editorial extensions of the recovery problem.

## Origin

Bainbridge, L. (1983). Ironies of automation. Automatica, 19(6), 775–779.

PDF p.3, sections 2.2 Working storage and 2.3 Long-term knowledge; extraction interleaves columns, so section labels matter. Title is editorial.

[Retained original](../../source.md). 

## Evidence and Rationale

**Basis:** Historical human-factors synthesis and training recommendations, not a controlled test of this complete routine.

**Observed or reported:** Bainbridge distinguishes maintaining skills from knowing the current process state, recommends suitable practice, and notes that fast failures may require automatic responses. Simple and high-fidelity simulators serve different learning needs.

**Intended:** independent-capability, accountability. These are curator-assigned intended benefits, not demonstrated effects.

**Untested:** The effectiveness of this exact routine in its proposed AI-use setting, including durable independent capability, better judgment and calibrated confidence. Immediate output quality, felt competence and later unaided performance are distinct outcomes.

## Limits

Unknown faults cannot all be simulated. Practice cannot compensate for an impossible response deadline. Do not create a live hazardous failure for rehearsal; preserve required accommodations and professional training standards.

## What to Notice

[Inference] Could the person detect the problem and act in the available conditions, or did the design assume impossible recovery?

## Related

- [[partial-automation-principle]]
- [[check-a-capability-without-the-assistant]]
- [[turn-a-premortem-into-actions]]

## Source roles

- [[bainbridge-ironies-automation-1983]] — origin of the research, recommendation or framework; exact editorial additions identified above.

## Review Status

Draft from supplementary review on 2026-09-27. See the per-source practice review and batch decision ledger. Not integrated.
