# Agent brief: [job name]

<!-- SHAPE TEMPLATE. This shows the format of an agent brief. It is not a real agent.
One file = one repeat job Claude does for the business. Format new briefs like this one. -->

**The job in one sentence:** what this agent does, stated so a stranger would understand it.

**Runs when:** what triggers it, for example the user asks, a file lands in `05-Inbox/`, a schedule, the weekly review.

## Inputs

What the agent reads before doing anything. Name exact files and folders.

- `folder-or-file`: what it takes from it.

## Steps

The job, in order. Short lines. If a step needs a decision the agent can't make alone, the step says "ask the user".

1. First step.
2. Second step.
3. Ask the user before [the thing that needs permission: deleting, sending, publishing].

## Output

Exactly what exists when the job is done, and where it lives in the vault.

## Rules for this job

Anything this agent must never do, beyond the hard rules in CLAUDE.md (which always apply).
