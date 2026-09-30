# Jhosua

**What this is:** the Make.com operator in the automation stack — besides Austin, the only person who can touch it.

**Status:** current — 2026-08-30

## The facts

- Runs Make.com in Parakeet's automation stack. Not on the December-2025 org chart.
- **The stack he sits in the middle of:** Rent Manager CSV exports flowing into SharePoint via Power Automate, Make.com orchestration on top of that, and the portfolio dashboard at the end of it.
- **Besides Austin, the only person who can touch Make.com.** That is a concentration risk worth naming: the orchestration layer between the system of record and the reporting layer has a bench of two, one of whom is the CEO.
- **What he decides without Austin:** how a given automation is built and maintained inside Make.com. What the automations are for is Austin's call.
- **Related structural gap:** the 600s Systems / IT / Reporting band in the SOP library is empty, so none of the automation stack — Power Automate flows, Make.com scenarios, the dashboard refresh — has a documented process behind it. The mitigation for the two-person bench is documentation in that band, and a named second operator.
- Power Automate now runs under dedicated server accounts rather than individual drive access, which centralises control and restricts broad data access.
- **How to work with him:** he is the build layer, not the requirements layer. Bring him a defined flow, not a problem statement.

## Decisions

- 2026-08-20 — Power Automate runs under dedicated server accounts rather than individual drive access, centralising control and restricting broad data access. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-lucky-clover-site-visit]])

## Sources

- [[00-Meta/austin-operating-manual]] — the automation stack and his role in it.
- Austin, in the Structure Interview, 2026-08-30.
