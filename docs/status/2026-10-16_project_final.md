# SumoBot, final state, 16 Oct 2026

This is the closing note for the project, written the day the working repo was archived.

## Final state

- **Robot:** the v11 printed chassis, two JGA25-371 gearmotors on DRV8871 drivers, cast silicone tyres on printed v6.2 hubs, seven VL53L0X distance eyes, four TCRT5000 edge sensors, ducted-fan downforce, a 3S 2200 mAh pack & a LilyGO T-Display S3. It weighed 1.000 kg at the 13 Oct weigh-in, before the wedge got its paint coat.
- **Firmware:** competition firmware v2.5, with the fight logic rewritten as five modes (wait, search, attack, edge, stopped). Start & stop come from a laptop-side ESP-NOW sender (one key for GO, one for STOP), which took over from the lid button after it was lost. How it behaves is in [`docs/FIRMWARE_OVERVIEW.md`](../FIRMWARE_OVERVIEW.md), the source isn't published.
- **Fan:** ran at one fixed setting for the bouts, and a pack is good for about two of them.

## Competition, 15 Oct 2026

1 win, 2 losses, and one bout forfeited after a mid-bout power cycle.

## What worked

- The ESP-NOW start & stop, with no lost packets in the ring.
- Counting the front-right eye as a lock & steering instead of braking when the target slid off one eye, so the bot kept pushing through partial contact (in the ring logs it never braked during an attack, where v2 had braked for a large share of each one).
- The steady-reading lock (a few readings in a row that agree with each other), which stopped the white arena board from setting off false charges. An empty-ring test went from dozens of false attack & edge readings in a few seconds down to a single brief false lock.
- The rear-right edge sensor with a short blanking window after a forward start, so the tail squatting at launch doesn't read as an edge.
- The wedge & silicone tyres held their ground in shoves, with the downforce fan adding grip on top.

## Known issues at close

- There's no front edge sensor, so the bot can follow a pushed opponent straight over the edge.
- Two of the seven eyes were out (front-left faulty & ignored, rear-left never on the bus), and of the four edge sensors only the rear-right was trusted.
- The 45° start sits in the blind gap between two eyes, so from there the bot finds the opponent by searching.
- An eye that still answers on the bus but reads blind can't be caught in software. The only recovery found was a power cycle, which the rules don't allow mid-bout, so a hand-wave check before each start was used instead.
- There was about one day of tuning before the event, which left the final firmware with very little match time.

## Where things are

The match firmware, the laptop remote, the fallback v2 build, the older revisions, the black-box log tools & the three match-day logs aren't published here. This copy carries the hardware, the design notes & the photos.
