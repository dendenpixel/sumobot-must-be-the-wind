# SumoBot — Hardware Spec Sheet

**Measured 11 Sep 2026. Written as a session handoff. Wiring layout section (§8) and staleness flags added 22 Sep 2026, as-built state added 23 Sep 2026.**

This file is the authoritative source for every **physically calipered** dimension on the bot. Where it disagrees with `SumoBot_Chassis_CAD_Brief.md`, `SumoBot_Wheel_v3_Spec.md`, `SumoBot_Parts_On_Hand.md` or `SumoBot_Documentation_Master_Plan.md`, **this file wins** — those contain seller figures and estimates, this contains the parts in hand.

`MEASURED_PARTS.md` remains the raw measurement log and the "how to measure" protocol. This file is the distilled version plus the consequences.

> **22 Sep 2026 — what changed.** §8 is new: the drive-only roof layout as re-run through `layout.py` v11.2 against the printed v11 base. Three older sections are now **STALE** and marked as such in place: §4-A (expansion PCB — there is no expansion PCB, the v11 design uses one PCF8574 in the lid and protoboard cuts), §4-F (ESC saddle at (+50, −38) — the ESC is on the left wellcap in v11), §7 (chassis context from the old brief — v11 is a 249 mm superellipse with ToF noses). The measurements in §2 are unchanged and still win. **One measurement matters for wiring:** the MP1584 buck is **13.86 × 9.95 mm** (§2.4). The v11 wiring guide's part card said ~22 × 17. That figure was wrong and both wiring guides now carry the measured one.

> **23 Sep 2026, as built.** Every printed part on the bot is the latest revision: v11 base, v11 lid (PETG translucent), carriers **v13**, wheel hub **v6.2** (ABS), battery frame v2 (clip), wellcaps +2, clamp ring v2 (ABS). Tyres are cast Mold Star 15 from the v1 ring mould, OD 46.8. The drive-only harness is wired, with the Brain on a breadboard on top of the bot for now instead of the right wellcap pocket in §8. The whole bot weighs **765 g** on a scale (23 Sep, before ToF & line sensors, breadboard aboard), see `MASS_BUDGET.md`. Of the four MP1584 bucks, one is in use, one burnt & two are spare. Of the four DRV8871s, two are in use & two are spare.

---

## 0. How to use this file

1. Read **§4 Open conflicts** first. Several of them block CAD work.
2. §3 is a copy-paste CAD variable block. Use those numbers, not the ones in the chassis brief.
3. §5 lists what is still unmeasured. Don't invent values for those, each one is a 30-second caliper job.
4. Everything in §2 is a **literal caliper reading with no clearance added**. Clearance is applied in CAD per the policies in §1.
5. **For the roof layout, read §8.** The board envelopes also exist in machine form in `hardware/cad/v11/layout/interfaces.json` (v11.2).

---

## 1. Standing policies (Den, 11 Sep)

**Tolerance.** Every number here is literal. Clearance goes in the CAD, never in the register. Defaults: bores for shafts/bosses +0.2–0.25 on Ø · pockets for boards/modules +0.5 per side · M3 clearance Ø3.4 · stacking dimensions +1–2 end clearance · **print a coupon before any fit that matters**.

**Assembly.** The person building this must never choose a part variant. One insert size everywhere, one pilot everywhere. Variation is absorbed in CAD, not at the bench.

**Bounding box.** Populated PCBs are modelled as generous rectangles. Don't model around individual caps.

**Print shrinkage.** This printer delivers holes ~0.2 mm under nominal (see §4-B). Every hole dimension in §3 is a **target printed size** — add the measured shrinkage offset before cutting CAD.

**The fan gets one shot (Den, 17 Sep).** There is **one** XFly 1413 EDF and no spare. **Do not bench-test it loose.** Verify all wiring and code first, plug it in last, one shot.

---

## 2. Measured parts

### 2.1 Drivetrain

**Motors — old faded pair (×2, identical).** Bench spares.

| | Measured |
|---|---|
| Body length, faceplate → back of housing | **39.29** |
| Gearbox (grey) length | 21.00 |
| Motor can (silver) length | 17.53 |
| Faceplate boss Ø | 7.05 |
| Boss/collar height above faceplate | 2.36 |
| Shaft Ø, round | **4.10** (min 4.07) |
| Shaft across flat | 3.46 |
| Shaft length, collar top → tip | 10.0 (2.0 round + **8.0 flat**) |
| Total shaft stick-out from faceplate | 12.36 |
| Mounting holes | **17.0 c-c, tapped M3** (two rounds: 16.90, 16.88) |
| Fitted Phillips screws | 12.08 c-c, head Ø ~3.4 |
| Encoder | 6-pin at the back of the can |

**Not a 371.** A 370 can is ~30 mm; this is 17.53, which is 310-class. Lower power than assumed, and the "12 V" rating is unconfirmed. The **new pair has arrived and is measured** (below) — `motor_len = 65` in the brief is dead; the real figure is **58.84**.

**Motors — new pair, BRINGSMART JGA25-371 "130 rpm" (×2). Measured 17 Sep; A and B near identical.** The drive pair.

| | Measured |
|---|---|
| Body length, faceplate → encoder end | **58.84** = gearbox 20.86 + can 32.71 + encoder cap 5.27 |
| Gearbox OD / can OD | **24.78** (reported uniform across both) |
| Overall length incl. shaft | 71.23 → **stick-out from the faceplate 12.39** |
| Faceplate boss Ø | **6.99 / 7.00** |
| Shaft Ø, round | **3.99** |
| Shaft across flat | **3.45** |
| Mounting holes | **17.11 c-c, tapped M3** (o/o 19.61, i/i 14.61; minor Ø 2.50, confirmed with a real M3 screw) |
| Fitted Phillips screws | 17.07 c-c, head Ø ~4.5 — on the axis **perpendicular** to the tapped pair (four features on a cross at r 8.54) |
| **Tapped-hole axis vs D-flat** | **3 and 9 o'clock, flat at 12** |
| Encoder connector | 6-way JST exiting **radially**, body 14.03, stands 8.45 proud. Pitch looks < 2.54 and is unconfirmed |
| Mass | **96.2 g each** incl. loom (loom alone 2.9 g) |

**Consequences, accepted 17 Sep** (since superseded by the printed carriers v13 & hub v6.2, see the 23 Sep note at the top): **v12 carriers OK — no reprint** (tail gap is 16.76, not the 6.3 the Ø25 × 69.3 envelope predicted, and a radial connector costs nothing axially) · **hub v5 OK — no change** (3/9 is what it assumed) · the ±14 stagger is still required · hub bore 4.10 → **4.05 candidate** on a Ø3.99 shaft.

**Wiring consequence (22 Sep):** with the ±14 stagger and a 58.84 body, **each motor's six wires exit on the opposite side of the bot** — Motor L's tail is at Y ≈ −20 (right side), Motor R's at Y ≈ +20 (left side). See §8.

**Still open on the new pair:** boss height above the faceplate · D-flat length from the shaft tip · Phillips head height · connector pitch and cable length · full label text · encoder cap Ø.

**Wheels — two printed versions measured.**

| | v1 | newest rim |
|---|---|---|
| Internal rim / lip Ø | 30.04 | 29.93 |
| External rim OD (tyre ID) | 38.68 | **38.1** |
| **OD with silicone tyre** | 46.62 | **46.8** |
| Rim width (tyre bed) | 28.98 | ☐ |
| Hub bore, round | **3.81** | **3.77** |
| Hub bore, across flat | 3.44 | 3.45–3.46 |
| Hub bore depth | ☐ | ~14 (estimated) |

**Effective wheel diameter is 46.8.** Top speed at 130 rpm = π × 0.0468 × 130/60 ≈ **0.32 m/s**.

### 2.2 Power and control

**ESC — LittleBee Spring 30 A (count in hand unconfirmed, BOM lists one).** Motor pads one end, wires the opposite end.

| | Measured |
|---|---|
| Board | 35.1 × 18.16 |
| **Heatshrink envelope (what must fit)** | **41.82** × 18.16 |
| Thickness | 5.55 fattest / 4.35 thinnest |
| Motor pad span (3 pads) | 15.58 (≈7.8 c-c) |
| Power wires red/black | **~80 mm** |
| Signal lead white/black | ~152 mm |
| Mounting holes | none |

**XT60 + loop key (×5 pairs).** Yellow half = panel mount with solder tabs (whether its contacts are pins or sockets is unconfirmed, the wiring guide assumes XT60E-M pins). Black cap = removable arming key.

| | Measured |
|---|---|
| Yellow body | 15.56 L × **8.13** W |
| Yellow, over the side ridge | **9.15** ← the retention feature |
| Yellow overall height (tab tips → top) | 20.31 |
| Yellow tab span | 11.43 widest / 7.1 narrow |
| Black key external | 16.47 × 9.23 |
| Black key height (protrusion) | 9.85, **10.6** at tallest |

**LiPo voltage alarm / buzzer.** 3-digit display, one button, balance pins, two buzzer domes. *(ID from description — photo confirmation still outstanding.)*

| | Measured |
|---|---|
| Body | 33.22 × 25.72 × 12.21 |
| Overall incl. pins | 38.67 (pins ~5.4 proud) |
| Buzzer domes | c-c 12.2, ~4.7 wide each |
| Mounting holes | **none** |

**Power / start button.** Snap-fit, two side clips, 3 pins.

| | Measured |
|---|---|
| Overall height, pin tips → cap | 29.33 |
| **Body Ø** | **18.51** |
| Widest point | 19.28 |
| Panel thickness the clips grip | ☐ **critical, see §4-G** |

**Battery — Ovonic AIR 3S 2200 mAh 120C, XT60 (×2 owned, ONE fitted).** Supplier sent 2200/120C against an ordered 1500/45C — confirmed by label, barcode and 24.42 Wh. Strictly better; see `MASS_BUDGET.md` §6.

| | Measured |
|---|---|
| Body | **106.29 × 34.39 × 21.46** |
| Mass | **151.2 g** |
| Capacity | **2200 mAh, 120C, 24.42 Wh** |
| Connector | **XT60** (plan said XT30 — check the harness) |
| Balance / charge lead | ~75 mm |
| Discharge lead (heavy gauge) | ~132 mm |

Bay must allow for **puff** — see §3. Normal +0.5/side pocket policy does not apply to LiPos.

### 2.3 Sensors

**VL53L0X ToF — 8 in hand (3 old + 5 new).** **7 in the design, 1 spare** against a soldering or wiring kill. If more than one dies, the documented fallback is **front + rear only — drop the sides.**

| | Measured | vs brief |
|---|---|---|
| PCB | 24.78 × 10.32 | ~25 × 10.7 ✓ |
| Board thickness | 3.18 | |
| Mounting hole outer-to-outer | 22.73 | |
| Mounting hole inner-to-inner | 16.85 | |
| **→ hole c-c** | **19.79** | brief says "~20 apart" ✓ |
| **→ hole Ø** | **2.94** | brief assumed Ø1.8 pilots for M2 — **these are M2.5-clearance holes** |

The brief's **26 × 12 × 4 pocket fits** (board is 24.78 × 10.32 × 3.18) with ~0.6–0.8 mm slop, so the pocket locates the board and the screws only retain it. Pilots should be **Ø2.1 for M2.5 self-tappers**, not Ø1.8 for M2.

**TCRT5000 ×5** — module PCB 31.3 × 14.2 (37.4 with pins), bare black sensor 10.01 × 5.6, 9.27 above the board incl. leg standoff; trimmer pot 7.9 tall (measured 13 Sep).

### 2.4 PCB modules

| Part | Qty | Measured (L × W × H) | CAD box | vs assumed |
|---|---|---|---|---|
| DRV8871 | ×4 | 25.17 × 21.63 × 9.6 | **26.0 × 22.5 × 10.5** | 25.4 × 20.3 → **+1.3 wider** |
| MP1584 buck | ×4 | 13.86 × 9.95 × 7.84 | **15.0 × 11.0 × 8.5** | 22 × 17 × 5 → **far smaller, 2.8 taller**. |
| PCF8574 HW-171 | ×4 | 54.64 × 15.62 × 11.29 | **56.0 × 16.6 × 12.0** | ~48 × 16 × 10 → **+6.6 longer** |
| **LilyGO T-Display S3** | ×1 | 62.3 × 25.65 × 6.88 (no pins); **14.6 over the header pins** | — | 51.5 × 25.5 assumed → **10.8 longer**. In hand, measured 12 Sep. Buttons ~14 mm apart on the USB-C short side; USB-C ~6.13 wide |

**Protoboard** — 160 × 63.8 × 2.74, breadboard pattern (5-hole columns per bank). The drive-only build's Board B is a **51 × 30 (20-column) cut** from the clean end.

### 2.5 Hardware

**M3 heat-set inserts.** 10-compartment box, **all M3 thread** (bore minor measured 2.49 / 2.50 / 2.52 vs M3 tapped minor 2.46–2.50).

| Slot | Length | Knurl OD |
|---|---|---|
| 1 short | 3.00 | 4.18 |
| 2 medium | 4.96 | 4.48 |
| 3 long | 6.99 | 4.21 |

**Slot 2 is the only insert used on this bot.** Slots 1 and 3 appear in no drawing or assembly step.

Bench rules: the insert carries the thread so screw tolerance stops mattering · **never lubricate** (brass must bond to melted PLA) · install square, seat 0.1–0.2 below flush · longer insert = more pull-out resistance, not more torque capacity — the plastic is always the limit.

**1000 µF 25 V electrolytic.** Can Ø10.38 × 16.99 · legs 21.6 / 26.8 beyond the can (long leg = positive, **stripe = negative**, go by the stripe once the legs are trimmed) · lead pitch still unmeasured. Standing height once fitted ≈ 18 mm, taller than any module on the board.

---

## 3. CAD variable block

All hole/bore values are **target printed sizes**. Add the shrinkage offset from §4-B before cutting CAD.

```
// ---- motor interface (BOTH pairs measured) ----
motor_len_old      = 39.29     // 310-class, NOT the 65 in the brief
motor_len_new      = 58.84     // measured 17 Sep; the 65 in the brief is dead
motor_od_new       = 24.78     // gearbox and can, uniform
motor_boss_d_new   =  7.00     // 6.99/7.00
motor_shaft_d_new  =  3.99
motor_shaft_flat_n =  3.45
motor_stickout_new = 12.39     // faceplate -> shaft tip, incl. boss
motor_hole_cc_new  = 17.11     // tapped M3, minor 2.50; axis at 3/9 with the flat at 12
motor_boss_d       =  7.05
motor_boss_h       =  2.36
motor_shaft_d      =  4.10
motor_shaft_flat   =  3.46
motor_shaft_len    = 10.00     // from collar top; only 8.0 is flat
motor_hole_cc      = 17.00     // tapped M3

// ---- wheel hub ----
hub_bore_d         =  4.20     // OLD pair: shaft 4.10 + 0.10
// new pair: shaft 3.99 -> hub bore 4.05 CANDIDATE, settle it on the coupon
hub_bore_flat      =  3.56
hub_bore_depth     =  9.00     // only 8.0 usable flat on the shaft
hub_counterbore    =  9.00     // Ø, x 3.0 deep, clears the collar
grub_min_from_floor=  4.00     // or it bites the round section and slips
wheel_od_with_tyre = 46.80

// ---- tyre retention ----
bed_od             = 38.10     // unchanged - do not orphan cast tyres
bed_w              = tyre_width + 0.3    // TYRE WIDTH UNMEASURED
flange_h           =  2.00
flange_w           =  1.50

// ---- ESC saddle ----
esc_pocket_l       = 43.00     // 41.82 heatshrink + 1.2
esc_pocket_w       = 19.20
esc_pocket_h       =  6.10

// ---- XT60 panel cut-out ----
xt60_slot_l        = 15.90     // BODY-sized, not ridge-sized
xt60_slot_w        =  8.40
xt60_internal_clr  = 21.00
xt60_external_clr  = 11.00

// ---- power button ----
button_hole_d      = 18.70     // NOT the 12 in the brief
button_internal_clr= 27.00

// ---- LiPo alarm pocket ----
alarm_pocket       = 34.0 x 27.0 x 13.0   // flat-lying
alarm_vent_cc      = 12.20     // vents over the buzzer domes

// ---- ToF ----
tof_pocket         = 26.0 x 12.0 x 4.0    // brief's value, CONFIRMED OK
tof_pilot_cc       = 19.79
tof_pilot_d        =  2.10     // M2.5 self-tapper, not M2

// ---- M3 inserts (slot 2 only) ----
insert_pilot_d     =  4.15
insert_pilot_h     =  6.00
insert_boss_od     =  8.50
insert_chamfer     =  0.50

// ---- battery bay (PUFF ALLOWANCE, not pocket policy) ----
batt_bay_l         = 110.00    // 106.29 + ~2/end
batt_bay_w         =  38.00    // 34.39 + ~1.8/side
batt_bay_h         =  24.00    // 21.46 + 2.5 - strap it, do not pinch it

// ---- module boxes ----
drv_box            = 26.0 x 22.5 x 10.5
buck_box           = 15.0 x 11.0 x  8.5   // NOT 22 x 17
pcf_box            = 56.0 x 16.6 x 12.0
```

---

## 4. Open conflicts — READ FIRST

### A. ~~PCB area is short by a factor of two~~ — STALE (22 Sep)

Written against an expansion-PCB plan with four PCF8574s. The v11 design has **one** PCF8574 in the lid, two DRV8871s on the roof, two MP1584s, and protoboard cuts (Board B 51 × 30 front-right, Board L ~50 × 15 in the lid). The area problem no longer exists. The module measurements above are still the right ones. Kept for the record.

### B. Hole shrinkage — affects every hole on the bot

Two separately printed wheels measured **3.81** and **3.77** in a bore drawn (presumably) at 4.00. That's systematic **~0.21 mm hole shrinkage**, not a bad print. A nominal Ø4.0 hole in PLA comes out under because internal perimeters over-extrude into it.

Two errors were stacked in the wheel: the shaft is 4.10 not 4.00, *and* the printer under-delivers by ~0.21. Combined ≈ 0.3 mm interference, which is what was measured.

**Unresolved input: what is the bore value in the CAD file?** If 4.00, shrinkage = 0.21 exactly and every hole in §3 gets +0.21 before cutting.

Consequence: the brief's coupon list (`M3 insert pilot 3.9 / 4.0 / 4.1`) is **wrong on two counts** — wrong target (should be 4.15 printed for the slot-2 insert) and no shrinkage allowance.

### C. Button hole in the brief is Ø12; the button is Ø18.51

The brief specifies `Ø12 button hole` in the crown at X = −85. The actual button body is **18.51**, needing an **18.7** hole. Ø12 is not a tolerance issue, it's the wrong part size — someone specced against a different button. (v11 lid: Ø18.7 hole in a Ø26 pad at (−38, 10).)

### D. Buzzer pocket in the brief is void

Brief: `32 × 14 buzzer pocket`. Actual alarm body: **33.2 × 25.7 × 12.2**. Nearly twice the width and too shallow in every orientation. Needs **34 × 27 × 13** lying flat, plus:
- **shell vents directly over the buzzer domes** (c-c 12.2) or the alarm is inaudible and pointless
- display readable and button reachable without disassembly
- ~6 mm clear off the pin edge for the balance plug
- no fixings on the part — friction pocket + strap, not glue (it comes off with the battery)

**Drive-only build:** alarm not fitted, location unconfirmed. §8 shows one suggested spot.

### E. XT60 cut-out must capture the ridge

Brief: `16.5 × 8.5`. Correct: **15.9 × 8.4** — sized for the 8.13 body, *not* the 9.15 ridge. The connector pushes in from inside until the ridge bottoms on the inner wall face, so it cannot pull through when the key is yanked. Cut it at 9.7 to clear the ridge and the whole connector exits the first time the key is pulled in a match.

The key protrudes **10.6 mm** past the panel — that's a lever arm for an opponent. Recess it into a shallow well.

### F. ~~ESC placement is capped by an 80 mm power lead~~ — position STALE, constraint still true (22 Sep)

The saddle at (+50, −38) is from the old brief. In v11 the ESC is VHB'd on the **left (+Y) wellcap top** at X −16…27, Y 41…60, Z 49.2, leads exiting −X. The 80 mm lead constraint is still real: from there to Star + at (−37, 35, 14) is ~49 mm straight line with a 38 mm climb, so the leads **only just reach** — don't shorten them, and mount the ESC at the rear edge of the cap. Don't fully enclose the ESC (heat).

### G. Snap-fit button vs a 3 mm wall

Snap-fit panel parts grip a **specific panel thickness** — the gap between the flange underside and the top of the clip barbs, typically 1.0–2.5 mm on commercial parts. The brief specifies a **3 mm wall**. If the wall is thicker than the clips' grip range, **the button never latches**, and no hole-diameter tuning fixes it.

Fix: counterbore a thin ring on the inside face around the hole, down to the clips' grip thickness. Wall stays full thickness everywhere else.

### H. The button's 3 pins are not identified

Three pins is usually **COM / NO / NC** (changeover) or **switch + LED**, not ground/active/output. Multimeter on continuity, each pair, released then pressed — 30 seconds. Wiring an NC contact into a start path gives a bot that runs until you press the button.

**And it must not carry motor or EDF current.** It's signal-rated. The XT60 loop key is the real disconnect; this button switches an MCU input or a MOSFET gate only. (The drive-only build uses the TTGO's own GPIO 14 button; the panel button comes in with the lid.)

### I. Protoboard is oversized, but don't buy another

160 × 63.8. **Perfboard cuts** — score and snap, or a hacksaw. The drive-only build cuts Board B (51 × 30, 20 columns) from the clean end; the lid stage cuts Board L. The 7805 end is scrap.

### J. Stale figures in other docs

- `SumoBot_Documentation_Master_Plan.md` says tyres are "LEGO hubs, 62.4 mm dia". Actual wheel is **46.8** and LEGO tyres are retired.
- Chassis brief C1 lists "wheel OD 45 → 52" as an open decision. Measured reality is **46.8**.
- Chassis brief ghost masses: the new motor pair is now on the scale at **96.2 g each** incl. loom (against 95 ea assumed, so +2.4 g on the pair). Wheels at 37 ea are still unverified, and so is the ESC.
- The wiring guide's part card: MP1584 size corrected to 13.86 × 9.95 (23 Sep). The `LAYOUT_PASS` pin map (enc_R 43 / ESC 44, SDA 17 / SCL 18) is also superseded: **enc_R 44, ESC 43, SDA 18, SCL 17** (matches firmware and the drive-only guide).
- `interfaces.json` / `layout.py` **before v11.2** carry the old pin map and the old board names (`board_A` front-right, `board_B` rear-left, `bus_block`). v11.2 (22 Sep) fixes both, use that.

---

## 5. Still to measure

**Blocking CAD:**
- **Tyre width** (silicone, axial) — blocks the tyre-retention flange design
- **Phillips screw head height** above the old motor faceplate — blocks the motor well relief pockets
- **Button: panel thickness the clips grip** — blocks the button mount (§4-G)
- **The CAD bore value** for the wheel — turns §4-B from an estimate into a constant

**Blocking wiring / Board B:**
- **1000 µF cap lead pitch** (leg c-c, same-side trick)
- DRV8871: which edges the header rows sit on (IN1/IN2 vs POWER/MOTOR blocks) — decides which way each driver faces
- MP1584: pad/hole layout (IN+/IN− vs OUT+/OUT− ends)
- TTGO: where along the 62.3 mm the two 10-pin headers sit, and which edge the USB-C is on — needed to place the pin stubs in XYZ (see §8 "measure")
- Pack: which side the balance lead and discharge lead exit

**Outstanding generally:**
- **New motor pair — the leftovers only** (§2.1): boss height above the faceplate, D-flat length from the shaft tip, Phillips head height, encoder connector pitch and cable length, label text, encoder cap Ø
- **EDF — overall height** (one bench-to-nub-tip reading; it gates whether the fan seat gets reamed at all), mass, which end is the intake, ear dimensions and the ear's position along the duct
- Wheel: hub bore depth, collar counterbore Ø + depth
- Alarm ID photo confirmation
- **Mass of the individual parts other than the battery (151.2 g) and the new motor pair (96.2 g each).** Those two are the only per-part scale readings. The printed structure is 296.4 g modelled, and the 267 g that used to sit here was the retired v5 chassis, not this one. The whole bot is 765 g on a scale (23 Sep, before sensors), against a 954.2 g prediction for the finished bot. See `MASS_BUDGET.md` §1, the mass authority.

---

## 6. Coupons to print before any real part

| Coupon | Values | What it settles |
|---|---|---|
| **Hole shrinkage + hub bore** | CAD 4.35 / 4.41 / 4.47 | Caliper each printed hole → gives this printer's shrinkage constant, which then applies to **every hole on the bot**. Then try the shaft: tightest that slides on by hand with flats aligned wins |
| **M3 insert pilot** | 4.00 / 4.15 / 4.30 printed | Melt a slot-2 insert into each, try to spin with a driver. Tightest that seated without bulging sets `insert_pilot_d` |
| Pod bore | 25.1 / 25.3 / 25.5 | from the brief, unchanged |
| Skirt groove | 1.25 / 1.30 / 1.35 | from the brief, unchanged |

Run the shrinkage coupon **first** — its result changes the CAD numbers for all the others.

---

## 7. ~~Chassis context (from `SumoBot_Chassis_CAD_Brief.md`)~~ — STALE (22 Sep)

Old brief: Ø250 rim, Ø200 plenum, crown 78, three printed parts, ToF slots at X +97. **v11 is different:** 249 × 249 superellipse (n = 4) rim, roof at Z 10.9, flat lid top at Z 65.6, 8 printed parts (base, two carriers, battery frame, lid, two wellcaps, clamp ring), fan collar at (57, 0), seven ToF noses on the tower at Z 39.9, four TCRT5000 under the roof at (±78, ±78). Source of truth: `interfaces.json` (v11.2) and the v11 base/lid stage reports. Printed structure **296.4 g modelled** (the v11 set, not the retired 267 g v5 weighing), 990 g total target (`MASS_BUDGET.md` §1, the mass authority).

---

## 8. Drive-only roof layout (22 Sep 2026, `layout.py` v11.2)

Frame: mm, **+X front, +Y left**, Z 0 arena floor, roof top Z 10.9, board faces Z 19.64, wellcap tops Z 49.2. Re-run through the v11 envelope checker with **zero new overlaps**. Two items are suggestions (marked).

### 8.1 Where the drive-only electronics sit

| Guide name | Footprint (X, Y) | Z | Fixing | Note |
|---|---|---|---|---|
| **Brain** (T-Display S3) | −40…22.3, −40…−65.65 | 49.2 | sits in the right wellcap pocket, not glued (as built 23 Sep it's on a breadboard on top of the bot) | USB-C + buttons at the +X end. Left row (guide's naming) is the inboard edge Y ≈ −41, right row outboard Y ≈ −64 |
| **Board B** | 29…80, −29…−59 | 10.9–19.6 | hot glue, hole side up | 51 × 30, 20 columns, col 1 at the −X end (X 31.5), pitch 2.54. Rails on the top bank (Y −33): 12V 1–2, 5V 4–5, GND 7–8, 3V3 10–11, guards 3/6/9/12, 3V3L 13–14 (lid stage). Points on the bottom bank (Y −55): ENC-L 1, ENC-R 2, B5V 5. Pilots A (31…62, −50…−41) fall inside it if screws are wanted |
| **Buck 1** | 64…79, −31…−42 (cols 15–20, top-bank half) | 19.6–28 | hot glue, on its back | OUT pads toward col 15. Buck 2 (lid stage) on the bottom-bank half of the same columns |
| **Driver R** | 24.5…50.5, −60…−82.5 | 19.6–30 | hot glue, on its back | outboard of Board B |
| **Driver L** | −41…−15, 46…68.5 | 19.6–30 | hot glue, on its back | rear-left; no Board A in the drive-only build |
| **Star +** | ⌀12 at (−37, 35) | 10.9–25 | hot glue, 12 mm heatshrink | five wires + cap |
| **Star −** | ⌀12 at (−37, 5) | 10.9–25 | " | six wires + cap. 30 mm from Star + |
| **Bus Cap** | ⌀11 at (−37, 20) | 10.9–29 | legs into both blobs | |
| **ESC** | −16…27, 41…60 | 49.2–55.3 | VHB + zip tie on the left wellcap | thick leads exit −X; 3 pads at +X taped over |
| **Key Socket** | face X −72, Y 57.6…73.2 | 15–23 | bolted in the XT60 bracket | tails inside at X ≈ −64 |
| **Pack Socket** *(suggestion)* | −39.5…−24.5, 70…78 | 10.9–31 | epoxy / zip tie, opening −X | 0.5 mm from the carrier flange and the lid lug, to confirm or move |
| **Alarm** *(drive-only build, suggestion)* | −80…−47, −13…13 | 32.5–44.7 | strapped on top of the pack | comes out with the pack; lid pocket at the lid stage |
| Motor L tail (wires exit) | (14, −20) | 23.4 | — | on the RIGHT side of the bot (stagger) |
| Motor R tail | (−14, 20) | 23.4 | — | on the LEFT side |

### 8.2 Wire landing points and routing

The wire landing points and routing rules that sat here belong to the wire-by-wire build guide, which isn't published. The block-level wiring is in [`WIRING_OVERVIEW.md`](WIRING_OVERVIEW.md).

### 8.3 Open items

1. Pack Socket and Alarm positions above are suggestions from the envelope check, not measured fits.
2. Because of the ±14 stagger, each motor's wires exit on the *opposite* side. Swapping the drivers' physical spots (Driver L front-right beside Board B, Driver R rear-left) would shorten the motor leads from ~90–105 mm to ~40–60 mm at no cost. The drive-only guide was NOT changed for this.
3. The TTGO header X-position, DRV8871 block edges, MP1584 pad ends and the pack's lead exit side are "measure" items — they set the last 10–20 mm of every signal wire.
