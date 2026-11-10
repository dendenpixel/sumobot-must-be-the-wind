# SumoBot, Mass budget (11 Sep 2026, rebuilt on measured parts 17 Sep)

**This file is the mass authority for the project.** Every other document quotes it and none of them re-derives a total.

Two parts on the robot are on a scale individually: the **drive motor pair at 192.4 g** and the **battery at 151.2 g**. The whole 23 Sep drive-only bot (before sensors) is **765 g**, see the measured checkpoint under §1. Every line below carries a tag, **MEASURED** (a literal scale reading, with its date) or **est.** (a modelled or seller figure, still unweighed), and every est. line names the document and line it came from.

**The 267 g chassis weighing is retired and must not be quoted as current anywhere.** That reading was the **v5** print (`../chassis/archive/v5-v8_POSTMORTEM.md` line 495, weighed 11 Sep), and v5 is not the robot. What is on the bench is the v11 base and lid, the v12 carriers, battery frame v2, two wellcaps and clamp ring v2, modelled at **296.4 g** (§1). That is the structure figure the rest of the repo should use.

Limit: **1000 g**. Working target: **985–995 g**, and **as bottom-heavy as possible** (ballast up to just under the line, and per the trade doc that is unconditional normal force which does not depend on the fan, the skirt, or the suction ruling). Headroom in this file is quoted against **990 g**, the middle of that band.

---

## 1. Where we are

### Printed structure, as built (v11 base and lid, v12 carriers)

| Part | Qty | g each | Total | Tag | Source line |
|---|---|---|---|---|---|
| Base, PLA | 1 | 116.8 | **116.8** | est. (114.9 cm³ solid × 1.24 × 0.82) | `../chassis/v11/REPORT_base_stage.md` line 86 |
| Lid, PLA | 1 | 128 | **128** | est. (156 g fully solid, 126.0 cm³) | `../chassis/v11/REPORT_lid_stage.md` line 15 |
| Carrier v12 L + R, PETG | 2 | 15.8 | **31.6** | est. (15 795 mm³ × 1.24) | `../chassis/v11/CARRIER_V12_CHANGE.md` line 29 |
| Battery frame v2, PETG | 1 | 3.47 | **3.47** | est. | `../chassis/v11/BATTERY_FRAME_V2_CHANGE.md` line 3 |
| Wellcap, +2 variant, PLA | 2 | 6.0 | **12.0** | est. (5.5 base, +0.5 for the +2 lift) | `../chassis/v11/REPORT_lid_stage.md` line 33 and `WELLCAP_PLUS2.md` line 9 |
| Clamp ring v2, shrinkcomp | 1 | 4.56 | **4.56** | est. | `../chassis/v11/CLAMP_RING_V2_CHANGE.md` line 39 |
| **Structure subtotal** | | | **296.4** | | 116.8 + 128 + 31.6 + 3.47 + 12.0 + 4.56 |

Two notes on that table. The clamp ring figure is computed at PETG 1.27 and the ring was actually printed in **ABS** (`../printing/PRESETS_clamp_ring_v2_ABS.md`, printed and test-fitted 17 Sep), so the real part is nearer 3.7 g. The documented 4.56 g is kept because it is the conservative number and nobody has weighed the printed ring. The wheel hubs are **not** in this table, they sit on the wheel line below.

**The "≈259 g structure" figure in `START_HERE.md` and the v11 changelog is a subset.** It counts base, lid, caps and ring only, and leaves out the two carriers (31.6 g) and the battery frame (3.47 g). The full set is 296.4 g.

### Whole bot

| Item | Qty | g each | Total | Tag | Source line |
|---|---|---|---|---|---|
| **Printed structure** (six parts, subtotal above) | 1 set | – | **296.4** | est. | this file, §1 |
| M3 inserts, fasteners, fan gasket | ~25 | – | 30 | est. | brief C9 estimate |
| Skirt silicone sheet + adhesive | – | – | 20 | est. | brief C9 estimate |
| **Drive motors, JGA25-371, incl. loom** | 2 | **96.2** | **192.4** | **MEASURED 17 Sep** | `MEASURED_PARTS.md` line 73 |
| Wheel hub v5, printed | 2 | 16.5 | 33.0 | est. (modelled, PLA @ 1.24) | `../wheels/WHEEL_HUB_V5_CHANGE.md` line 21 |
| Cast silicone tyre ring, 46.8 OD | 2 | 20.6 | 41.2 | est., **unweighed and not yet cast** | `../WHEEL_V1.md` line 59 |
| **Battery, Ovonic AIR 3S 2200 mAh 120C** | **1** | **151.2** | **151.2** | **MEASURED 11 Sep** | `MEASURED_PARTS.md` line 347 |
| EDF 40 mm, XFly 1413 | 1 | 40 | 40 | est., **unweighed** | `MEASURED_PARTS.md` line 336 |
| ESC, LittleBee 30 A | 1 | 25 | 25 | est., **unweighed** | `MEASURED_PARTS.md` line 129 |
| Protoboard, Boards A + B + L | 3 pieces | – | 15 | est., **unweighed** | cuts in the wiring guide (not published), stock in `PARTS_AND_WIRING.md` line 37 |
| Modules and sensors (T-Display S3, 2× DRV8871, 2× MP1584, PCF8574, 7× ToF, 4× TCRT5000, caps, resistors, diode) | – | – | 50 | est., **not one of them is weighed** | brief estimate |
| Alarm, panel button, XT60 + loop key, wiring, star | – | – | 60 | est. | brief estimate |
| **TOTAL** | | | **954.2** | | |
| **Ballast headroom to the 990 g target** | | | **35.8** | | 990 − 954.2 |

```
296.4 + 30 + 20 + 192.4 + 33.0 + 41.2 + 151.2 + 40 + 25 + 15 + 50 + 60 = 954.2 g
990.0 − 954.2 = 35.8 g of ballast headroom
```

**35.8 g is the single headroom figure for this project.** Anything quoting 21, 23, 68, 127 or 135 g is stale.

### Measured checkpoint, 23 Sep 2026: 765 g

The whole bot went on a scale at **765 g** on 23 Sep (photo `media/first-drive/mass_765g_2026-09-23.jpg`). That's the drive-only build: every printed part at its latest revision (v11 base & lid, carriers v13, hub v6.2, battery frame v2 clip, wellcaps +2, clamp ring v2), both motors, both cast tyres, the pack, the ESC, both drivers, the buck & the drive harness, with the Brain on a breadboard on top.

Not on it yet: the 7 ToFs, 4 line sensors, PCF8574, panel button, alarm, lid-side wiring, Board L, the second buck & the EDF (still in the bag, ~40 g est.). The breadboard is on it & comes off when the Brain moves onto Board B.

So 765 g is a checkpoint, not a replacement for the 954.2 g prediction, and the two can't be subtracted line for line until the missing items are weighed. What it does say is that everything still to go on, fan & sensors included, has about 235 g to the 1000 g limit (225 g to the 990 g target), plus whatever the breadboard weighs once it comes off. The next scale reading worth taking is the finished bot, which closes this table for good.

The table above still carries the carrier v12 & hub v5 modelled masses. The printed v13 carriers & v6.2 hubs haven't been re-modelled or weighed separately, the 765 g reading includes them.

### There is no PCB

The old **"expansion PCB + modules, 65 g"** line is deleted because the part does not exist. The design runs three pieces score-and-snapped out of one 160 × 63.8 × 2.74 protoboard (Board A, Board B, Board L, see `../PIN_MAP.md` under "How it is built"). No board is being fabricated.

The 65 g is split above into **15 g of protoboard** and **50 g of modules**, which keeps the documented bundle total and drops the claim that does not hold. The 15 g is an estimate built like this: the three cuts were 60 × 30, 30 × 26 and 50 × 15 (Board B is now 51 × 30, which takes about 1 g off), so 3,330 mm² of the 10,208 mm² stock, at 2.74 thick that is 9.1 cm³, and perfboard runs 1.4 to 1.85 g/cm³, so **13 to 17 g**. Nobody has put the pieces on a scale.

**Where the headroom went.** The ballast line has eroded from the 75 g an earlier tracker carried. Three things moved: the printed structure is 296.4 g against the ~255 g the old line carried, the pack that arrived is the 2200 mAh at 151.2 g rather than the 1500 mAh that was costed, and the weighed motor pair is 2.4 g over its 95 g each estimate. Against the 990 g target the total now stands at 954.2 g, which leaves 35.8 g.

**Not overweight, and the ballast is not gone, but 35.8 g is thin for a strategy built on ballast.** 610.6 g of the 954.2 g total is still est. (§2), so the number can still move by more than the headroom.

---

## 2. The number that matters most is still unweighed

**The motors are closed.** 96.2 g each including the loom (93.3 g bare), weighed 17 Sep, so **192.4 g the pair** against the 190 g the old estimate carried. That is 2.4 g worse, not better. The doubt about a 310-class can is closed with it, the new pair measures 58.84 mm with a 32.71 can and A is identical to B (`MEASURED_PARTS.md` §2.1). The 39.29 mm old pair is a bench spare and **is not on the robot**, so its mass does not belong in this budget at all.

**What is still unweighed, worst first:**

| Item | g carried | Why it is still an estimate |
|---|---|---|
| Printed structure (six parts) | 296.4 | mesh volume × density × a 0.82 print factor, never on a scale as a set |
| Wheels (hub + cast ring, the pair) | 74.2 | hub modelled, tyre not cast yet |
| Alarm, button, XT60, wiring | 60 | estimate |
| Modules and sensors | 50 | no module in `MEASURED_PARTS.md` §2.8 has a mass recorded |
| EDF | 40 | `MEASURED_PARTS.md` §2.10, mass still open |
| M3 inserts, fasteners, gasket | 30 | estimate |
| ESC | 25 | `MEASURED_PARTS.md` §2.3, mass still open |
| Skirt | 20 | estimate |
| Protoboard pieces | 15 | estimate |
| **Total est.** | **610.6** | |

**610.6 g of the 954.2 g total is still held up by estimates, against 35.8 g of headroom.** A 6 % error anywhere across that 610.6 g is 36.6 g, which wipes the ballast out on its own.

**Weigh, in this order:** the six printed parts together (one reading closes the 296.4 g line) · one finished wheel with its cast tyre · the ESC · the EDF.

---

## 3. What to do if it goes over

Levers already identified in brief C9, cheapest first:

| Lever | Saving | Cost |
|---|---|---|
| Shell 2.0 → 1.6 mm with 2 mm ribs under the ramp | −25 g | more print time, some stiffness |
| Pan 6 → 4 perimeters | −10 g | pan carries the motor cradles — test first |
| Pan infill → 15 % gyroid | −8 g | minor |
| Delete the crown dome above Z 70 | −8 g | check EDF exhaust clearance (needs Z ≥ 76 over the Ø48) |

**Those levers were written against the v5 shell and pan, which are retired.** The parts on the bench are the v11 base and lid, and their own levers are in `../chassis/v11/REPORT_lid_stage.md` line 15: lid wall 2.0 to 1.6 saves about 14 g, lid skin 1.6 to 1.2 saves about 9 g, and the lid is 18 g over its own 110 g gate. Either way a saving costs a print cycle, it is not free.

**Do not save weight by dropping ballast.** Ballast is the one mass on the bot that does useful work: it's normal force, and push = μN. Everything else is overhead.

---

## 4. Batteries: parallel or series?

> **The capacity and C figures in §4 are the ordered 1500 mAh 45C pack.** What arrived and what is fitted is a **2200 mAh 120C** pack weighed at **151.2 g**, and §6 has the real numbers. The conclusion here (one pack on the bot) does not change, §6 only strengthens it. The mass figures in §4 are corrected in place.

### Series is wrong and would destroy hardware

Two 3S packs in series = **6S = 22.2 V nominal, 25.2 V charged.**

- The drive motors are **12 V** rated. 22 V cooks them.
- The EDF is **3S rated**. The buy sheet and `SumoBot_Decisions.md` both say so explicitly — "4S rejected (3S parts)". 6S destroys it on the first spool-up.
- The whole power tree (MP1584 bucks, DRV8871s at 2–10 V motor supply) is specced around 11.1 V.

There is no configuration of this bot where series is correct.

### Parallel works electrically but you don't need it

Two packs in parallel = 3S 3000 mAh at the same 11.1 V. Valid, but:

- **+151.2 g** (weighed), against **35.8 g** of headroom. That alone ends it.
- Parallel LiPos must be at **matched voltage** before connecting or they dump current into each other — a real fire risk on a bench, not a theoretical one.
- **The capacity isn't needed.** Peak draw is ~16 A (motors 2 × 3 A stall + fan ~10 A). A 45C 1500 mAh pack is rated 67 A continuous. Runtime at 16 A is ~5.6 min theoretical, ~3 min at sensible depth of discharge. **A sumo bout is 3 minutes.**

### Verdict: one pack on the bot, second is a swap between bouts

This also matches the standing decision in `SumoBot_Wheel_Tyre_Motor_Trade.md` — *"Run ONE pack on the bot."*

### The "one pack for the fan, one for drive" idea should be dropped

The trade doc floats splitting supplies to decouple voltage sag, on the reasoning that fan pressure goes as V², so 15 % sag = 28 % pressure loss exactly at contact.

**That 15 % figure came from the old 850 mAh pack and doesn't survive the upgrade.** On a genuine 3S 1500 mAh 45C pack, internal resistance is roughly 25 mΩ. At the 16 A peak:

```
V_drop  = 16 A × 0.025 Ω ≈ 0.4 V
sag     = 0.4 / 11.1 ≈ 3.6 %
ΔP loss = 1 − (0.964)² ≈ 7 %
```

**~7 % pressure loss at peak, not 28 %.** That's inside the fan's tuning margin and nowhere near worth 151 g. The 45C pack solved the sag problem by itself — the dual-supply idea was fixing a bottleneck that no longer exists.

---

## 5. One thing to confirm

**Put the whole printed set on the scale at once.**

The 296.4 g in §1 is six modelled numbers, and each one is a mesh volume times a density times a **0.82 print factor that was itself derived from the retired v5 weighing** (`../chassis/archive/v5-v8_POSTMORTEM.md` line 400: 324.5 g solid against 267 g weighed). That factor is carrying six parts across two materials and two printers' worth of settings, and it has never been checked against a v11 print.

One reading of base + lid + carrier L + carrier R + battery frame + both wellcaps + clamp ring closes the single largest est. line in the budget. If the set comes in 5 % heavy that is 15 g out of 35.8 g of ballast, and if it comes in 12 % heavy the ballast is gone.

The old question in this section, whether the 267 g weighing covered the PETG small parts as well as the two big ones, is dead. That was the **v5** chassis and v5 is retired.

---

## 6. Battery — measured 11 Sep (Ovonic AIR 3S **2200 mAh 120C**, XT60)

| | Measured |
|---|---|
| **Mass** | **151.2 g** (estimate was 155 — 3.8 g under) |
| Capacity / rating | **2200 mAh, 120C, 24.42 Wh** — **NOT the 1500 mAh 45C that was ordered** |
| Connector | **XT60** (barcode: `...20C-2200-3S1P-XT60`) |
| Body | **106.29 × 34.39 × 21.46** |
| Balance / charge lead | ~75 mm |
| Discharge lead (heavy gauge) | ~132 mm |

**Battery bay — do not size this to the caliper reading.** LiPos swell with age, heat and depth of discharge, and a pack clamped in a tight pocket has nowhere to go but into the pack next to it. Normal pocket policy (+0.5/side) is wrong here:

```
batt_bay_l = 110.0     // 106.29 + ~2/end
batt_bay_w =  38.0     // 34.39 + ~1.8/side
batt_bay_h =  24.0     // 21.46 + 2.5 - puff allowance, NOT a press fit
```

Retain with a strap, not by pinching it between walls.

**Lead reach:** 132 mm of discharge lead is generous and not a constraint — unlike the ESC's 80 mm, this one reaches anywhere on a Ø200 core. The 75 mm balance lead needs the alarm within reach of wherever the pack sits, or it can't be plugged in without lifting the pack.

### Supplier sent a bigger pack than ordered — and it's strictly better

`SumoBot_Decisions.md` specced **2× 3S 1500 mAh 45C XT30**. What arrived is **2200 mAh 120C XT60**. Confirmed three ways: printed label, barcode, and 11.1 V × 2.2 Ah = 24.42 Wh matching the label exactly.

**Correcting an earlier analysis in this file:** a previous pass reasoned that energy density had *dropped* going from the 850 to the new pack, and explained it as the normal high-C trade. That was computed against the assumed 1500 mAh and is **wrong**. At the real capacity:

| | 850 mAh NXE (old) | **2200 mAh Ovonic (actual)** |
|---|---|---|
| Energy | 9.44 Wh | **24.42 Wh** |
| Mass | 68.1 g | 151.2 g |
| **Energy density** | ~138 Wh/kg | **~161 Wh/kg** |
| Mass per mAh | 0.080 g | **0.069 g** |
| Rated C | 30C (~25 A) | 120C nominal |
| Connector | JST-RCY, **~5 A** | **XT60** |

Density went **up**, not down, and it's lighter per mAh. The pack is better on every axis — there is no trade here to explain.

### What it changes

**Runtime.** At the ~16 A peak: 2200 mAh / 16 A = 8.25 min theoretical, **~6.6 min at 80 % DoD**. A bout is 3 minutes. Comfortably two bouts on one charge.

**Sag — even less of an issue.** 120C is a marketing figure and nobody should believe it, but derate it hard to a realistic 40C and it's still 88 A capability against a 16 A draw — about **7.3C**. Internal resistance on a high-C 2200 3S is likely 15–20 mΩ:

```
V_drop  = 16 A × 0.018 Ω ≈ 0.29 V
sag     ≈ 2.6 %
ΔP loss ≈ 5 %
```

**This closes the dual-pack question for good.** The "one pack for the fan, one for drive" idea was justified by 28 % pressure loss from sag. Real figure is ~5 %. Carry one pack.

**Connector: XT60, not the XT30 in the plan.** That's convenient — the arming loop key is already XT60, so the pack plugs straight into the disconnect with no adapter. But **check the harness plan** before anyone crimps XT30s that nothing will mate with.

### Two things to check

1. **Is the second pack also a 2200?** Confirm both match — swapping between bouts is simpler if they're identical, and a mismatched spare is a surprise on competition day.
2. **Was this a substitution or a billing error?** If invoiced for 1500 and sent 2200, it's a free upgrade and nothing to chase. Worth a glance at the order confirmation so it's not a stock error they claw back.

**Safety note, unchanged but scaled up:** 24.42 Wh is ~2.6× the stored energy of the old 850. Same rules, more reason to follow them — charge in the bag or tin, outside, on concrete, never unattended.

### No CAD change

The bay dimensions above were measured off the physical pack, so `batt_bay_l/w/h` stand as written. The mass (151.2 g) is a scale reading and is carried straight into §1, where the budget totals **954.2 g** with **35.8 g** of ballast headroom to the 990 g target.
