# Decision log

> **Superseded at project close (16 Oct 2026).** The log ends 23 Sep 2026. Later decisions (ESP-NOW start, v2.5 fight logic, final fan setting) are in [`status/2026-10-16_project_final.md`](status/2026-10-16_project_final.md).

Newest first. Current state is `README.md` & `docs/chassis/v11/START_HERE.md`, this file is *why*. Rows marked *(Superseded, see 6–23 Sep.)* were right when written and have since been replaced.

## 6–23 Sep 2026: v11 build, first drive

| Item | Decision | Reason |
|---|---|---|
| Brain | **LilyGO T-Display S3 (ESP32-S3)**, pins in `docs/PIN_MAP.md` | It's the TTGO board in hand, and the pin map was rewritten for it |
| Chassis | **v11**, a 249 × 249 mm superellipse base with a continuous 15° wedge & rim 0.5 mm off the floor, the plenum is the whole base. Printed parts on the bot are all the latest revisions, v11 base, v11 lid (PETG translucent), carriers **v13**, wheel hub **v6.2** (ABS), battery frame **v2 clip**, wellcaps **+2**, clamp ring **v2** (ABS) | Replaces the 200 mm sealed-core sombrero concept, see `docs/chassis/v11/CHANGELOG.md` for every revision |
| Claws & climb ramps | **Dropped** from v6 onward, absorbed into the continuous wedge | The claw sectors left no rim for 164° of the perimeter, which broke both the rim armour & the seal loop (`docs/chassis/archive/v5-v8_POSTMORTEM.md`) |
| Motors | **JGA25-371 12 V 130 rpm with Hall encoder**, bought after the 2 Sep order, measured 17 Sep. The old pair is bench spares only | The on-hand pair's ratio was unknown & the carriers are sized for the new pair's 58.84 mm body |
| Encoders | **Single channel A per motor**, GPIO 21 (L) & 44 (R), no quadrature. Confirmed counting on both sides 23 Sep | Both B leads are folded back & direction comes from the commanded sign, so one pin per motor does the job |
| Wheels | **Cast silicone (Mold Star 15) from the v1 ring mould on a printed hub**, effective OD 46.8 mm | Rigid hub + stiff tyre keeps the load on the tread, see the 4–5 Sep rows below |
| Motor drivers | **2× DRV8871**, MX1508 fully retired | The MX1508 is 10 V max & can't sit on 3S |
| `setMotor(0)` | **Brake**, both IN pins high | A stop that holds the bot where it is, coast would roll on |
| Electronics build | **No PCB.** Cut protoboards (Boards A, B & L), hand-wired. For the 23 Sep first drive the Brain sits on a breadboard on top of the bot until it moves to protoboard | The v11 layout fits the modules on protoboard cuts, so the area problem a PCB was solving no longer exists (`docs/hardware/HARDWARE_SPEC_SHEET.md`) |
| 5 V feed | **MP1584 buck straight to the Brain's 5V pin, no diode** | Decided not needed 23 Sep. The rule "never USB with the key in" still stands |
| Capacitors | **220 µF on each DRV8871's supply, 1000 µF bulk at the XT60 input.** Low-ESR parts ordered | The general-purpose assortment was all that was in hand, low-ESR parts replace them for the fan |
| Line sensors | **4× bare TCRT5000 into ADC1 on GPIO 1/2/3/10**, LM393 comparator modules not used, own firmware module | GPIO 36–39 don't exist on the S3 & an analogue threshold can be calibrated on the arena |
| Opponent sensors | **7× VL53L0X**, XSHUT on one PCF8574 (P0–P6), start button on P7. The expander is handled by the ToF module | Modules are split by objective & only merged when they share hardware. The expander exists for the ToFs, so it lives with them |
| Battery | **One Ovonic 3S 2200 mAh 120C XT60 pack on the bot**, the second one charges | Supplier substituted 2200 mAh for the 1500 mAh ordered, at the same price |
| Battery monitoring | **No LVC divider & no ADC pin for one on the S3.** Pack voltage is watched by a plug-in LiPo alarm on the balance lead (location & trip voltage unconfirmed, not wired yet) | No free pin left, see `docs/PIN_MAP.md` |
| Fan | **One EDF, no spare, one-shot policy.** Tested on the finished bot only, every wire & the code verified first, fan mated last | A loose bench test risks the only fan, which also retires the mid-Sep kitchen-scale kill gate |
| Staff rulings | **ESC as a motor controller: allowed. Fan pre-spool: allowed.** Suction approved 8 Sep ([`docs/admin/DESIGN_APPROVALS.md`](admin/DESIGN_APPROVALS.md)) | All confirmed by 23 Sep |
| First drive | **Timed open-loop build**, full power out & back with a brake between. Encoder-counted drive is the next step, for straightness | It's the simplest build that proves the drivetrain |
| Git | **One branch per task → PR → Den merges.** `main` is unprotected, honour system | One pattern to learn, the same for every task |

## 4-5 Sep 2026 — geometry pivot, tyre physics, fan derate
Full working: `GEOMETRY.md`, `WHEEL_TYRE.md`, `WHEEL_V1.md`.

| Item | Decision | Reason |
|---|---|---|
| Chassis shape | **"Sombrero" shell replaces the 200 x 200 x 72 mm box.** Round-ish base at the 250 mm rule limit, ramp rising on all sides to a centre high point, unbroken outer surface | Agreed in a team design call, 4 Sep. No lip or step for an opponent to wedge under; 250 mm buys ramp run, and the rule allowance was going unused |
| Front / rear | **Symmetric pushing faces** with a ~70-90 deg "claw" arc each end — contours protruding sideways then curving in toward the middle, entering low as a thin line and rising to 40-80 % of core height *(Superseded, see 6–23 Sep.)* | The bot has no bad end, so an edge escape costs no re-orientation. The claw is a trap cavity, not a deflector |
| Sides | **Climb ramps, not deflectors** — almost as tall as the centre. Invite the flank attacker up, then yaw under software control to dump them into a claw. Grip/adhesive coating sprayed on the shell *(Superseded, see 6–23 Sep.)* | An opponent on our roof has no traction of their own. Coating also lets a lifted opponent's wheels grab so we can carry them off |
| Suction footprint | Seals **only the circular centre core**, not the full outer rim, with a centre vent to exhaust. **200 mm committed. 230 mm under investigation — feasibility and modelling pending, NOT adopted** *(Superseded, see 6–23 Sep.)* | Area goes as D^2 and leak as D, so 200 -> 230 is ~+32 % downforce for +15 % leak. Cheaper than any fan tuning, but unmodelled |
| Side rails / gears | **Dropped** | Little grip benefit and they kill turning |
| Tank treads | **Rejected** | Friction is independent of contact area. A tread buys nothing a tyre does not and costs a drivetrain |
| LEGO 62.4 x 20 tyres | **Dropped — they make the fan a net negative** | Pair stiffness 6.5 N/mm against 1.0 mm brim clearance: the brim grounds at ~210 Pa and then takes all further load at mu ~0.3. Net push at 800 Pa is **-3.4 N** |
| Tyre | **Cast silicone, A15-A25, 25-30 mm wide, on a rigid printed hub**, 45-52 mm OD | ~15x stiffer (~96 N/mm pair), so 0.35 mm squat at 800 Pa and the tyre keeps the load. **+23.2 N net push.** The swap is what makes the fan work at all, not an optimisation |
| Tyre mu target | **0.70 planning, check margin at 0.60.** The 2 Sep "target mu >= 1.0" is **withdrawn** | 1.0 is not achievable. Best measured silicone on smooth board is 0.75, and mu falls with contact pressure (~N^-1/3) — which is also why width stays at 25-30 mm |
| Wheel supply | **Print our own hubs, cast our own tyres. Buying tyres or mounting hubs is dropped entirely** | No bare competition tyre exists on AliExpress in any vocabulary. Only JSumo (Turkey) sells one in range, at AU$38-73 landed with an unpublished bead diameter and a shipping window that can land after 12 Oct. Casting removes both unknowns at similar cost |
| Motors | **Not the limit.** Any ratio >= ~34:1 clears it — 2.3x margin at 45:1 / D45 / 800 Pa. Characterise the on-hand pair first; buy nothing if they make >= 4.5 kg.cm *(Superseded, see 6–23 Sep.)* | Break-even fan pressure is 1096-1490 Pa, above anything the fan can hold. Grip is the constraint, not torque |
| Fan operating point | **500-800 Pa. The 1200 Pa point is deleted** | Vendor data is for 4S; running a 4S KV5000 on 3S costs (3/4)^2 = 0.56x pressure. After axial stall derate and pack sag, 500-800 Pa is what is real |
| Fan use | **Off while searching, on only when attacking or pushing, in short bursts.** Replaces running it all the time | Thermal is the real limit: ~40 W into a ~25 g stator is 3.7 K/s adiabatic — 34 s from cold to 150 C at full throttle. Part throttle keeps about half the pressure for about a third of the power |
| Skirt gap | **0.4-0.6 mm, set with the fan RUNNING** (tyre squat is 0.35 mm) | Below 0.4 mm buys ~5 %; above 1.5 mm falls into the axial stall dip |
| Battery on the bot | **One pack, not two.** Preferably one for the fan and one for drive + logic *(Superseded, see 6–23 Sep.)* | The Ovonic 3S 2200 that arrived is 151.2 g measured. Splitting the packs decouples a 5-10 Hz sag limit cycle — fan pressure goes as V^2, so a 15 % sag is 28 % pressure loss, arriving exactly at contact |
| Escape termination | **Encoder counts do not measure heading under fan clamp.** Terminate EDGE_ESCAPE on a gyro, or drop the fan to 0 for the turn. Supersedes "encoder-terminated escapes" (2 Sep) | A skid-steer pivot under clamp is slip-governed. The wheels turn; the bot does not |
| Suction legality | **Approved 8 Sep** ([`docs/admin/DESIGN_APPROVALS.md`](admin/DESIGN_APPROVALS.md)). ESC as a motor controller & pre-start spool were also allowed, confirmed by 23 Sep | If refused, the same parts still build the bot — just over-specified. At P = 0 with silicone tyres: 5.8 N push at 38 % torque utilisation, still torque-rich. Ballast to 985-995 g is the unconditional 1.4 N that does not depend on any ruling |
| Ballast | **985-995 g**, using the ~42 g freed off the rims by the wheel change | Weight off the rims is the worst place for it (rotational inertia, unsprung) and the best place for it is low, between the axles |

## 2 Sep 2026 (evening) — design locked after 10-specialist review
| Item | Decision | Reason |
|---|---|---|
| CO2 flipper / spring lifter / any pneumatic | **Dropped entirely** | Weight (eats all ballast headroom), approval risk, complexity, flap slot is a plenum leak. Bench-only 80 N × 12.5 mm = 1 N·m lifts a front but never throws |
| Concept | **Fan-downforce wedge, 2WD skid-steer, ~990 g** | Last year's bots lost on grip; push = μ × N, so raise N with a fan and μ with tyres |
| Fan | **40 mm EDF, 12 blade, ~5000 KV, 3S** (XFly 1413) + **30 A BLHeli_S ESC**, BEC red wire cut | Same stall pressure as 30 mm but 2.3× flow → survives a 1 mm skirt gap. +18 g, ~15 A peak. Bigger than 40 mm buys heat and grams, not push |
| Battery vs fan size | **Battery first**: 2× Ovonic 3S 1500 mAh XT60 *(Superseded, see 6–23 Sep.)* | Old 850 mAh/JST-RCY sags ~1.2 V at 16 A and the connector is 3 A rated. 4S rejected (all parts are 3S) |
| Chassis | **200 × 200 × 72 mm**, plenum ~175 × 170 mm (0.030 m²), 9–10 mm deep, straight vertical duct at X = 150 *(Superseded, see 6–23 Sep.)* | Downforce = ΔP × A; doubling area vs 13 × 13 halves the pressure needed. Still turns in a 1 m ring |
| Motors | **Characterise first** (Fri 4 Sep). Want 1:45–1:78 (110–190 rpm @ 12 V). If on-hand pair ≥250 rpm → order known 1:78 pair *(Superseded, see 6–23 Sep.)* | Faster ratios cap push at ~24 N and waste the fan; at 1:78 (~53 N) tyres are always the limit |
| Motor driver | **DRV8871** ×2 (+1 spare clone), MX1508 retired to bench use at ≤9 V *(Superseded, see 6–23 Sep.)* | MX1508 is 10 V max, can't sit on 3S. Same IN1/IN2 interface → code is a drop-in swap |
| 5 V rail | **MP1584 buck** set to 5.00 V; LM7805 stripboard binned | 2–3 W of heat in a linear reg for nothing |
| Main disconnect | **XT60 loop key** (one male plug shorted) | Combat-bot standard, doubles as safety interlock. On-hand latching button is 1–3 A → logic arm switch only |
| Tyres | Rubber bands (from 7 Sep) → **oogoo / cast silicone sleeves** (from 14 Sep), target μ ≥ 1.0 *(Superseded, see 6–23 Sep.)* | μ 0.6 → 1.2 doubles push for free; staff said sticky tyres; last year's winner used bands |
| Line sensors | **4× digital TCRT5000 (LM393) modules on GPIO 36–39** *(Superseded, see 6–23 Sep.)* | Only clean free pins; input-only so no strapping risk; four corners so no blind rear |
| GPIO expander | **PCF8574** for XSHUT ×3, LED, buzzer only *(Superseded, see 6–23 Sep.)* | Pin budget. Edge detection must never depend on I2C |
| LVC | Divider into an ADC pin with a warn stage, a trip stage (fan off first) and a latched hard cut; plus plug-in LiPo buzzer *(Superseded, see 6–23 Sep.)* | Voltage sag mid-push tripping our own LVC was risk number one |
| Fan kill gate | **Week of 14 Sep**: <0.9 kg gain on kitchen scale, or EDF >100 °C in 3 min → drop fan, run 990 g ballast + silicone tyres + sprung lip *(Superseded, see 6–23 Sep.)* | Staff showcased an overcooked suction bot as the failure to avoid |
| Fan fallback if ESC refused | Brushed 5015/5020 blower on a third DRV8871 (~200–300 g downforce) or plain ballast *(Superseded, see 6–23 Sep.)* | Rules: only commercial board allowed is a motor controller |
| Software | One fast loop, one state machine, line check first, no blocking waits, no second RTOS task | Easy to explain, deterministic, edge-first |
| Budget | Lean cart, AliExpress for everything, 2–5 week shipping accepted | ~$185 for the cart |

## 2 Sep 2026 (midday) — after 8-reviewer red-team
Priorities that win: tyre μ · scraping front lip ≤0.5 mm on a sprung leaf · ballast to 990 g · edge-first control with encoder-terminated escapes · ToF continuous + a short target memory, flank don't charge · TTGO expansion PCB in the week of 7 Sep · demo on parts we already have. *(PCB and encoder-terminated escapes superseded, see 6–23 Sep & 4–5 Sep.)*

## 2 Sep 2026 (first meeting)
- "Tank" build: torque over speed, skid-steer, rectangular for CAD.
- Roles across the four of us: idea viability research · CAD + fan deep-dive · admin, ordering, coordinator email & GitHub (Den) · electrical.
- Ideas filtered out on viability: hydraulics, pendulum, CO2 as propulsion, ultrasonic jamming speaker.
- Use GitHub, keep `main` clean, per-workstream branches + PRs. *(Superseded, see 6–23 Sep.)*
