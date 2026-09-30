# Skill: probe the data lineage

**What this is:** how the source layer of [[10-Business/data-lineage]] gets rewritten from live connector calls instead of from memory. Run it weekly. The consumer layer is hand-maintained; **this routine never touches it.**

**Why it exists.** [[00-Meta/id-conventions]] went stale on all six registers inside 48 hours and would have reissued roughly ninety live IDs if anyone had trusted it. A page that describes live state and is updated by hand always ends up lying. The fix that worked there was "the file is the authority, not the description." The equivalent here is: **the connector is the authority, not the table.** So the table gets regenerated, not edited.

**A script cannot do this.** MCP tools are callable by Claude, not by python. This is a routine Claude runs, and the honest version of "automated" is "runs on a schedule with a human-readable diff," not "a cron job writes the file."

## When to run it

- **Weekly**, as step 7 of [[90-Skills/weekly-brain-review]].
- **Before** any piece of work that will quote a portfolio figure, if the page's probe date is more than seven days old.
- **After** any connector is added, switched or re-authenticated.

## The probe, in order

1. **Rent Manager reporting API.** Call `list_reports`. Record every report's `name`, `reportId` and one-line purpose. **Diff against the table on the page.** A report that appeared or disappeared is a finding, not a formatting change — say so in the report at the end.
2. **RentViewer warehouse.** Call `get_schema`. Record every model with its measure count, what it covers, and the traps stated in its own `description` field — the descriptions carry the real warnings (repeated reservation totals, the missing property ID on the reservation feed, the 10% of service issues with no property). **Diff the model list.** The 2026-09-09 run found six models the vault had never recorded; assume that can happen again.
3. **Plaud.** Call `get_current_user` to confirm auth, then `list_files` for the recording count. **Plaud failed silently through the whole 2026-09-03 close and hid nine recordings that produced two findings the next morning.** A silent outage here is expensive, so it gets probed every run even when nothing needs it.
4. **Microsoft 365.** One Outlook folder read and one calendar read. Confirm mail is still read-only by attempting nothing — the `Mail.ReadWrite` gap is recorded, not re-tested.
5. **Gmail a2zcp, Dropbox, Google Drive, ClickUp, Ramp.** One cheap call each. Dropbox in particular has dropped mid-session before.
6. **Write the results back** into the source-layer tables of [[10-Business/data-lineage]] with the probe date on every row. **A connector you could not reach is marked unreachable with the date — never left showing the previous run's result.**

## The rules

- **Never write a row you did not get from a call this run.** A carried-forward row is marked as carried forward with its original date. This is the entire point of the page.
- **A failure is a result.** Record the error text, not "unavailable." `run_query` returning a member-validation error means the semantic layer is live; a timeout means it is not. Those are different facts.
- **Do not re-test known-broken things every week.** RM report 51 `GeneralLedger` is recorded as HTTP 500. Re-test it monthly or when someone needs it, not every run.
- **The consumer layer changes only when a human says so.** If a dashboard's feed changed, that is a conversation, not a probe result.
- **New capability is not a recommendation.** A model that appears gets recorded and flagged. Whether to use it is Austin's call.

## The report

Five lines or fewer, plus a diff:

- what changed in the source layer since last run
- anything that could not be reached, with the error
- any new report or model, and the one thing it makes possible
- any consumer feed that now points at something that no longer exists

Add one line to `00-Meta/log.md` and, if anything changed materially, a row to the audit log.

## Related

- [[10-Business/data-lineage]] — the page this rewrites
- [[10-Business/connector-status]] — connector identity and the blocked list, which this does not touch
- [[90-Skills/weekly-brain-review]] — the routine this hangs off
