# Leadership lessons from running the build

## Context

From the first concept on 2 Sep 2026 to the competition on 15 Oct, I led a four-person team building an autonomous 1 kg sumo robot for a university embedded-systems course, about six weeks of build in all. I set the roles and ran the weekly loop, so most of what went right or wrong with how we worked traces back to calls I made. We finished with 1 win, 2 losses & one bout forfeited after a mid-bout restart.

## What I built

I sourced the parts, took the chassis from v5 to v11, printed every part on the robot & cast the silicone tyres. The chassis geometry itself came from AI CAD agents working to briefs I wrote, so my job there was holding the design, writing the brief, checking what came back against parts I'd measured, and deciding what got printed. I also wrote the wiring guides, the competition firmware (v2.5, the build that actually fought) and most of the documentation, and I ran the repo (80 issues & 7 pull requests).

For the team side I built a weekly loop around our Wednesday lab session. Work got assigned on the Wednesday, there was a soft deadline the following Monday, a check-in on the Tuesday, and the hard deadline landed back at the next Wednesday lab. On paper everyone had a full week & two chances to flag a problem before it cost the build anything.

## What didn't work

When a deadline slipped I picked up the piece to keep the build moving, which meant a missed slot had no visible cost. That was my choice to make and it hid the problem, because the loop only works when a miss means something & I'd quietly made sure it didn't.

I took a handover with no demo. I should have asked to see it running. A prototype I wrote to show the scope got read as finished. I didn't label it. I never defined done either, so a partial sheet got marked done.

At the start I set a hard, serious tone. It made the project feel heavier, and I didn't adjust. Later on I stopped following up because it felt like nagging, which left the check-in on the Tuesday as the one part of the loop I wasn't really running. I could see the pattern by the middle of the build & raised it with a lab facilitator, then held off, thinking the missing parts were the real blocker, and by the competition it was too late to change course.

## What I do now

- I book the check-in the day the work is assigned. Put check-ins on the calendar up front so follow-up is routine, not nagging.
- I ask for a demo, not a status, and if there's nothing to demo yet that's the update.
- Before I assign anything I write down what done looks like. Done means a working output and a test, not a status update.
- Anything I build to show scope gets labelled as a prototype, on the file and in the message that goes with it.
- After two missed cycles, escalate, in writing, the same week, then reassign or rescope within 24 hours. Covering the work yourself hides the problem from everyone.
- In the first week I agree the scope with the team, based on how much time each of us can realistically give, and write it down. A lecturer suggested this one afterwards, and it's the change I'd make first.

## The rule

The rule I use now for every handover, my own included, is show me it running. That means the thing working in front of me with a test that proves it, where a status or a promise that it's nearly there doesn't count. If it can't be shown yet then it isn't handed over yet, and the check-in stays on the calendar until it can. It's a small habit, and it would have caught the undated handover, the unlabelled prototype & the loose done before any of them cost the build anything.
