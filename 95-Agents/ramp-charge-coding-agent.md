# Agent brief: Ramp charge coding

**The job in one sentence:** read every uncoded or badly coded Ramp card charge, propose the GL code and the property it belongs to, and hand a reviewed batch to Accounting so spend is coded within days of being spent instead of at month end.

**Runs when:** daily, and on demand before any spend review. **Not built yet.** This brief is the scope, written 2026-09-01 on Austin's instruction: *"one aspect that we need to do is to create an agent to book Ramp charges."*

**Status:** proposed, 2026-09-01. Owner **Austin** with **David Berman**. Task `TD-0327`. Finding `KP-0003`.

## Why this exists

The books run **30 to 45 days in arrears** and Austin names it as one of his top three problems ([[10-Business/departments/accounting-and-finance]]). The stated standard is the opposite of what happens: *"when people are booking things or putting their memos and allocations in Ramp, it should be booked right away. And therefore we know where we are."*

**Read the cause honestly, because it decides whether this agent helps.** There are two separate delays stacked on each other and they have different fixes.

1. **Charges are not coded when they are made.** A field manager buys skirting and the memo is blank or unusable. Nothing downstream can be right until someone reconstructs what that charge was. **This is the half the agent can actually fix.**
2. **Ramp posts journal entries to the GL once a month.** Even a perfectly coded charge does not show up until the monthly post runs. **An agent cannot fix this.** It is a Ramp configuration question and it is `TD-0320`, still unanswered.

**So the agent is half the answer and the posting frequency is the other half.** Building the agent and leaving Ramp on a monthly post buys faster, cleaner coding and roughly the same arrears. Both, or say plainly that it is a partial fix.

## Inputs

- **Ramp:** the transaction feed, via the Ramp connector in this session. Merchant, amount, date, cardholder, card, memo, current category and allocation.
- [[10-Business/vendors/ramp]] for the GL rule and the memo format: `GL [XXXX] — [vendor or description]`, entered immediately, per SOP 105b.
- [[70-Operations/sops/105-poh-rehab]] for the rehab gates the memo format comes from: issue number and the `GL — Total Cost` UDF.
- [[60-Communities/portfolio]]: the 67 communities and their short codes, for mapping a charge to a property.
- **Rent Manager:** open issues and work orders, to match a charge to the job that caused it.
- The prior 90 days of coded Ramp charges: the training set for what this cardholder at this merchant usually means.

## Steps

1. Pull every Ramp charge from the last 24 hours plus everything still uncoded from the current period.
2. Split into three buckets: **clean** (GL code present and in format), **guessable** (no code, but merchant plus cardholder plus an open Rent Manager issue give a confident answer), and **unknown**.
3. For the guessable bucket, propose a GL code, a property and an issue number, and record the evidence for each: which prior charge, which open issue, which cardholder pattern. **A proposal with no stated evidence is an unknown, not a guess.**
4. For the unknown bucket, draft the one-line message to the cardholder asking what the charge was for. Group by cardholder so one person gets one message, not six.
5. Write the batch to `80-Finance/ramp-coding/YYYY-MM-DD.md`: clean count, proposals with evidence, unknowns with the drafted chase.
6. **Ask before anything is written back to Ramp.** Nothing is applied to a transaction without Accounting reviewing the batch.
7. Track the trend, because it is the only measure that says whether this worked: percentage coded at time of charge, days from charge to coded, unknowns per cardholder per week.

## Output

One dated file per run in `80-Finance/ramp-coding/`, and a weekly roll-up of the three trend numbers. Nothing is posted to the general ledger by this agent, ever.

## Rules for this job

- **The agent codes; a human posts.** Proposing a GL code is bookkeeping support. Posting to the ledger is the company's books, and [[CLAUDE]] rule 8 keeps that with Accounting.
- **Never invent a GL code or a property.** An unknown charge stays unknown and gets a chase message. A confidently wrong code is worse than a blank one, because a blank gets questioned and a code gets trusted.
- **Never change a card limit, issue or freeze a card, move a spend allocation, or touch a fund.** The Ramp connector can do several of these. This job does none of them.
- **Repeat unknowns from the same cardholder are a finding, not a chore.** Three weeks of chasing the same person is a training or a policy problem and belongs in front of Austin, not in the batch file.

## The decision to make before building

**Does the agent code and a human posts, or does the agent post?** Everything above assumes the first. It is a controls question rather than a technical one, and it needs Austin and David together. The answer changes the review burden, the audit story and whether this is worth building at all.

## Related

- [[10-Business/vendors/ramp]]: the card programme, the GL rule and the timing problem.
- [[10-Business/departments/accounting-and-finance]]: where the arrears finding lives.
