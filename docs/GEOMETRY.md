> **Superseded 12 Sep 2026.** The chassis is the v11 249 × 249 superellipse sombrero in `docs/chassis/v11/START_HERE.md` (no claws, no lidar, wedge on all sides). Kept for the reasoning/history.

# Chassis geometry — "sombrero" shell (rev 4 Sep 2026)

Supersedes the 200 x 200 x 72 mm box in the 2 Sep plan and the 2 Sep row in `DECISIONS.md`.
Agreed in a team design call on 4 Sep. Roughly 80 % of the structure
is common to both of the designs that were on the table; this file is the merged result.

## Shape

A round-ish base at the **250 mm rule limit**, with a ramp rising from the rim on all
sides to a high point in the centre — hence "sombrero". The outer surface is unbroken:
there is no lip, step or overhang for an opponent to get a wedge under.

| Element | Spec | Intent |
|---|---|---|
| Outer base | **250 mm**, the rule maximum | Buys ramp run. The ramp angle is set by the RUN, not by crown height |
| Electronics / fan core | **~200 mm circular**, centred | Minimise it — every mm of core is a mm of ramp not built |
| Ramp | Rises from the rim to the centre high point on all sides | Nothing to wedge under; an attacker either climbs or slides |
| Front + rear | **Symmetric pushing faces** | The bot has no bad end. No re-orientation cost after an edge escape |
| Claw | ~70-90 deg arc at front and rear, contours protruding sideways then curving back in toward the middle | A cavity an opponent gets trapped in, not a deflector |
| Claw blade profile | Enters low as a thin line, rises to **40-80 % of core height**. Start as low as possible, then curve up steeply | Get under the opponent first, then hold |
| Sides | Plain ramp, curving slightly toward front and rear, rising **almost as tall as the centre** | These are **climb ramps, not deflectors** — see below |
| Shell coating | Grip / adhesive spray on the upper surface | A lifted opponent's wheels grab the shell so we can carry them off the arena |

## The side-climb play (deliberate, not a compromise)

The sides are tall ramps *on purpose*. A flank attacker is invited to climb onto the roof.
Once they are up there they have no traction on their own wheels, and we **yaw under
software control** to slide them off into a front or rear claw cavity. The downforce fan is
the backstop for the case where the lidar is too slow and we take the flank hit flat.

This is the opposite of the usual "deflect the flank" wedge and it needs the shell coating
and the yaw routine to work together. Both are unbuilt. Treat as the highest-risk part of
the geometry.

## Suction footprint — OPEN

Suction seals **only the circular centre core**, not the full outer rim, with a centre vent
to exhaust. Sealing the whole 250 mm outside is not ruled out but has not been justified
against the complexity.

- **Committed number: 200 mm core seal**, ~0.031 m2 plenum.
- **Under investigation: 230 mm.** Area goes as D^2 and leakage as D, so 200 -> 230 mm is
  roughly **+32 % downforce for +15 % leak** — cheaper than any fan tuning. Feasibility and
  the CAD model for it are not done. **Not adopted. Do not build to 230 until this closes.**

## What this replaces

| Dropped | Why |
|---|---|
| 200 x 200 x 72 mm rectangular box | Wedge-able edges; no ramp run; leaves the 250 mm allowance unused |
| Side rails / gears | Little grip benefit and they kill turning |
| Tank treads | Friction is independent of contact area — a tread buys nothing a tyre does not, and costs a drivetrain |

## Still open

1. Lidar on the shell top, possibly plus 2 more ToF. Not in `PIN_MAP.md` yet — pin budget
   is not re-checked.
2. Ramp angle at the rim. A single slope from r=125 is unclimbable for a ~700 g rival at
   any wheel diameter, which means the current profile is over-specified for climb defence
   and under-specified for the deliberate climb-on play. A **two-slope brim** (shallow
   14 deg from the rim, then steep) is the lever if we want a real climb face.
3. Print strategy on the Bambu Lab X1C — PLA or ABS depending on the toughness the shell
   needs. 250 mm is close to the bed limit; check it fits before modelling further.
4. Yaw routine to dump a climbed opponent. No code, no test.
