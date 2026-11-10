> **Superseded 12 Sep 2026 for plenum geometry, skirt and test method.** The plenum is the v11 base (`docs/chassis/v11/START_HERE.md`) and the fan is tested once on the finished bot, the 3S derate, thermal rule and fan choice below are still current. Kept for the reasoning/history.

# Downforce fan (rev 4 Sep 2026 — derated, sombrero core plenum)

**Approved by the coordinator on 8 Sep ([`docs/admin/DESIGN_APPROVALS.md`](admin/DESIGN_APPROVALS.md)), with the caveat that
the competition timber plate isn't perfectly smooth, so expect side-leak losses.** If that ever changes, the same
parts still build the bot — just over-specified — and the fallback is ballast to 985-995 g
plus the silicone tyres, which gives 5.8 N of push at 38 % torque utilisation. See
`DECISIONS.md`.

## What changed on 4 Sep

1. **The 1200 Pa design point is deleted.** Vendor pressure figures are 4S. Running a 4S
   KV5000 on 3S costs (3/4)^2 = **0.56x pressure**. Shutoff dP on 3S is ~1200-2200 Pa, but
   after axial stall derate and pack sag the **realistic operating band is 500-800 Pa**.
2. **Thermal, not pressure, is the limit.** See the thermal rule below.
3. **The plenum is now the circular centre core of the sombrero shell**, not the full
   200 x 200 footprint. See `GEOMETRY.md`.
4. **Balloon tyres broke the whole premise** and have been replaced with cast silicone —
   `WHEEL_TYRE.md` section 1. Without that change the fan makes the bot *worse*.

## Governing equation

Downforce = dP x A. Core plenum ~0.031 m2 -> +1 kg needs dP ~ 320 Pa. The spec that matters
is **static pressure near zero flow**, not CFM: a sealed skirt puts the fan at the stall end
of its P-Q curve.

| Fan | Downforce | N_total (850 g bot) | Grip @ mu 0.70 |
|---|---|---|---|
| off | 0 | 8.3 N | 5.8 N |
| 400 Pa | 12.4 N | 20.7 N | 14.5 N |
| **800 Pa** | **24.8 N** | **33.1 N** | **23.2 N** |

Area is the cheapest multiplier. **Moving the seal line from 200 to 230 mm is ~+32 %
downforce for +15 % leak** — cheaper than any fan tuning we can do. It is *under
investigation only*; feasibility and the CAD model are not done. Do not build to it yet.

## Fan choice

| Type | dP at stall | Verdict |
|---|---|---|
| 40 mm PC axial | 10-40 Pa | no |
| 5015/5020 blower 24 V | 100-300 Pa | fallback if the ESC is refused |
| 30 mm EDF 3S 12 blade | high stall, low flow | rejected: collapses with a 1 mm skirt gap |
| **40 mm EDF 3S 12 blade (XFly 1413 KV5000)** | similar stall, **2.3x flow** | **ordered** |

Vendor data for the XFly: 3S 360 g / 15 A / 187 W; 4S 500 g / 20 A / 330 W. We run 3S.
Kill gate: <0.9 kg gain or EDF >100 C in 3 min -> drop the fan, run ballast + tyres. Updated 23 Sep: the gate
runs once, on the finished bot in early October, fan mated last (one fan, no spare). No loose bench test.

## Thermal — the real constraint

~40 W into a ~25 g stator is **3.7 K/s adiabatic**. 100 % throttle is about **34 s from cold
to 150 C**. Part throttle keeps about half the pressure for about a third of the power.

**Thermal rule (replaces running it all the time):** the fan is off while searching, on at
part throttle in short bursts only when attacking or pushing, and off again for an edge escape
(a pivot under clamp is slip-governed — see `DECISIONS.md`) and while calibrating or stopped.

Run the fan only if the last thermal check passed.

## Leakage

Cd 0.62, perimeter 0.628 m at the 200 mm core, at 800 Pa:

| Skirt gap | Leak |
|---|---|
| 1.0 mm | 30 CFM |
| 0.5 mm | 15 CFM |
| 0.2 mm | 6 CFM |

**Target 0.4-0.6 mm, set with the fan RUNNING** — tyre squat under clamp is 0.35 mm, so a
gap set statically is wrong. Below 0.4 mm buys about 5 %. Above 1.5 mm falls into the axial
stall dip.

## Electrical

ESC: LittleBee 30 A BLHeli_S on a servo-style signal lead from **GPIO 43** (15 is the S3's LCD power enable), held at
minimum throttle at boot so it arms, BEC red wire cut. Peak ~15 A at 100 %. Bus caps 470-1000 uF + 100 nF at the
ESC input, leads <20 mm.

## Airflow — straight through

Plenum below (9-10 mm cavity inside the core skirt) -> EDF intake down -> exhaust straight
up through the centre vent in the shell high point. Stationary gas means uniform pressure:
no channels, no venturi.

- Bellmouth R5 on the plenum side of the duct (a sharp hole stalls the rotor)
- Exhaust straight up through the centre vent, 3 mm grid guard 65 % open, 15 mm clear above,
  not blockable by an opponent's wedge
- 4x 15 mm bleed holes in the plenum roof, taped to tune on the scale (target EDF at 45-60 %
  of free flow)
- Print walls >= 6 perimeters, seal seams, hot-glue every wire pass
- Wheels **inside** the core, wells sealed top and rear by a 1 mm silicone flap
- A slight leak is a feature: the EDF motor is air-cooled, and dead-sealed it cooks in 2-3 min

## Skirt

Must close the gap without carrying weight. 0.8-1 mm silicone sheet, 3-4 mm overhang at
35 deg out (~2 mm interference at rest), clamped in a 1.3 x 4 mm groove with a 2 mm strip,
M2 every 40 mm. Selleys **Glass** Silicone (acetoxy) for bonding and skim-coating — not the
neutral-cure Roof & Gutter.

## Tests

> Updated 23 Sep: tests 1, 2 and 4 run on the finished bot only, once the wiring and code are verified,
> fan mated last. The EDF is never run loose on the bench.

1. **Kitchen scale.** Bot on the platform, read ~1.00 kg, fan on, delta = downforce. Sweep
   20/40/60/80/100 %, 3 readings each.
2. **Push force vs throttle**, 0 / 50 / 100 %, spring scale, pull until the wheels spin.
   **If push does not rise monotonically with throttle, something rigid is grounding** —
   this is the test that would have caught the balloon-tyre problem.
3. **Water U-tube manometer** into the plenum: 1000 Pa = 10 cm water. Separates a weak fan
   from a bad seal.
4. **Thermal.** Thermocouple on the EDF can, 3 min at 100 %, log it. Expect the 34 s number
   to be optimistic-pessimistic in both directions — measure, do not assume.
5. **Arena flatness.** Straightedge and feeler gauges on the real board before trusting any
   skirt gap. A 1 m MDF board bows 1-3 mm.
6. Ahead of any run with the real fan: cardboard mock-up of the core, shop-vac or 120 mm PC
   fan, cornflour on the floor to see leak paths. Geometry only — no number from this goes in
   the report. The EDF itself stays boxed until the wiring and code are verified: **one fan, no
   spare, one shot.**
