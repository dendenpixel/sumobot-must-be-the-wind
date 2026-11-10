# SumoBot — Measured parts register (started 11 Sep 2026)

Single source of truth for **calipered** dimensions. Anything here overrides the seller numbers in `SumoBot_Chassis_CAD_Brief.md` (V/P/U) and `SumoBot_Parts_On_Hand.md`. When a value lands here, the matching CAD variable gets updated in the same session.

Status key: **☐** not measured · **✔** measured (value + date). **Everything in the 2 Sep order has arrived** (11–17 Sep 2026). A second small order (low-ESR caps, Schottky, JST-PH pair) is placed.

**Tolerance policy (Den, 11 Sep):** every number in this file is the *literal* caliper reading of the part. Clearance is added in the CAD, never here. Aim: loose enough that one bad reading doesn't scrap a print, tight enough to be worth having. Working defaults: bores for shafts/bosses +0.2–0.25 mm on Ø; pockets for boards/modules +0.5 mm per side; M3 clearance Ø3.4; anything that stacks (motor length, board heights) +1–2 mm end clearance; print a coupon before any fit that matters.

**Assembly policy (Den, 11 Sep):** the person building this must never have to choose a part variant. One insert size everywhere, one pilot everywhere. Any variation is absorbed in the CAD, not at the bench. See 2.9.1.

**Bounding-box policy (Den, 11 Sep):** for any populated PCB, treat it as a generous rectangular box rather than modelling round individual components. Tall caps and overhanging parts get swallowed by the box. Applies to DRV8871, MP1584, PCF8574, TCRT5000 modules.

---

## 0. How to measure (same rules every part)

1. **Zero the caliper closed before every part.** Wipe the jaws. If it doesn't read 0.00, re-zero.
2. **Three readings, write the middle one.** Rotate the part between readings. If the spread is > 0.1 mm, say so (it's a taper, a burr, or a tolerance you should know about).
3. **Record to 0.01 mm as shown, don't round.** Rounding happens in the CAD.
4. **Which jaws:** outside jaws for OD/width/length · inside (knife) jaws for bores/slots · **depth rod** for how far a boss/shaft sticks out of a face · step face (back of the moving jaw) for shoulder heights.
5. **Hole spacing = measure edge-to-edge on the *same* side of both holes.** (Left edge of hole 1 to left edge of hole 2.) That equals centre-to-centre without needing hole diameter. Never measure inside-edge to inside-edge and add a guess.
6. **Hole diameter:** inside jaws, read the *largest* value you get while gently rotating. Note if it's plated/tapped (a tapped M3 reads ~2.5 mm minor).
7. **Shafts with a D-flat:** two readings — round-to-round (Ø) and round-to-flat (across-flat). Plus flat length with the depth rod from the shaft tip.
8. **PCBs:** overall L × W (outside jaws), **total** height incl. tallest component (part on the bench, caliper held vertical), hole Ø and c-c, and which edge the connector/header is on (a photo covers that).
9. **Weigh everything** on the kitchen/jewellery scale, grams to 0.1 if it has it. The target is 990 g total and the ballast headroom is **35.8 g** (`MASS_BUDGET.md` §1, the mass authority), against a printed structure of 296.4 g that is modelled rather than weighed. Every real gram matters, and 610.6 g of the 954.2 g total is still an estimate.
10. **One photo per part** with the caliper still on the critical dimension and the readout visible. Photos also catch things a single number can't (ear shapes, connector orientation, which side the pot is on).
11. **Say which part you picked up.** Cheapest error in this whole process is measuring the right part and filing it under the wrong name.
12. **Lead pitch on through-hole parts** (caps, sensors): the two legs, centre to centre. Same-side trick — left edge of leg 1 to left edge of leg 2. This sets the PCB footprint and nothing else gives it.


---

## 1. Priority — measure in this order

| # | Part | Status | CAD variable / feature it sets |
|---|---|---|---|
| 1 | **Motor (new "130 rpm" pair)** | ✔ **measured 17 Sep** — body **58.84** (not 65), OD 24.78, mass 96.2 incl. loom; A ≡ B; tapped-hole axis 3/9 vs the flat | `motor_len` 65 → **58.84**. Carriers **OK, no reprint** (tail gap 16.76). Hub v5 unchanged. Hub bore 4.10 → **4.05** candidate on shaft Ø3.99 |
| 2 | Motor (old faded pair) | ✔ done — only Phillips head **height** outstanding | same |
| 3 | ESC | ✔ done. The saddle at (+50, −38) is stale, in v11 the ESC sits on the left wellcap. See 2.3 | ESC position on the left wellcap |
| 4 | VL53L0X ×8 (3 old + 5 new) | ✔ PCB 24.78 × 10.32 × 3.18, holes Ø2.94 at 19.79 c-c (M2.5 clearance). **Count settled: 8 in hand, 7 in the design, 1 spare.** See 2.4 | ToF pocket 26 × 12, pilots Ø2.1 |
| 5 | TCRT5000 modules | ✔ measured 13 Sep: module 31.3 × 14.2 (37.4 with pins), bare sensor 10.01 × 5.6, 9.27 above the board incl. leg standoff. See 2.5 | line-sensor pockets |
| 6 | XT60 loop key | ✔ done — cut-out must catch the ridge. See 2.6 | rear crown cut-out |
| 7 | LiPo alarm / buzzer | ✔ done — assumed pocket is void. See 2.7 | buzzer pocket **(redesign required)** |
| 8 | DRV8871 / MP1584 / PCF8574 / T-Display S3 | ✔ **all four done — the three modules 11 Sep, the T-Display S3 12 Sep.** The board-area problem in 2.8 is closed, there's no PCB. See 2.8 | module boxes, shell clearance |
| 9 | M3 inserts | ✔ done + standardised. See 2.9.1 | every M3 pilot on the bot |
| 10 | 1000 µF caps ✔ · feeler blade ☐ · silicone sheet ☐ · XT30 ☐ | cap done bar the lead pitch | — |
| 11 | **XFly 1413 EDF (×1, no spare)** | ✔ **measured 17 Sep** — flange OD 47.81 worst case, flange thickness 3.31–3.50 ⚠ (spread 0.19), duct OD 42.87, duct section 26.44 (datum unstated). **Overall height still ☐ and it gates the seat ream.** See 2.10 | clamp ring ear slots, fan seat bore + depth |
| 12 | LiPo — Ovonic AIR 3S 2200 mAh 120C XT60 | ✔ **measured 11 Sep** — 106.29 × 34.39 × 21.46, 151.2 g, **XT60** (not XT30). See 2.11 | battery bay 110 × 38 × 24 |

---

## 2. Per-part sheets

### 2.1 Motor — new pair, JGA25-371 "130 rpm" (×2, measure both, note if they differ)

| Dimension | How | Assumed now | Measured A | Measured B |
|---|---|---|---|---|
| Body length, faceplate → encoder end (incl. encoder disc/cap, excl. wires) | outside jaws, or depth rod off a flat bench | 65 (61–69 P) | **58.84** | ≡ A |
| Gearbox OD | outside jaws | 25.0 V | 24.78 ⚠ | ≡ A |
| Motor can OD | outside jaws | 24.4 V | 24.78 ⚠ | ≡ A |
| Gearbox length (faceplate → seam with the can) | outside jaws on the step | 21 (1:45) / 23 (1:75) | 20.86 (teal BRINGSMART section, shaft end) | ≡ A |
| Encoder end: Ø and how far it sticks past the can | outside jaws + depth rod | ~ | cap 5.27 past the can (derived); Ø ☐ | ≡ A |
| Faceplate boss Ø | outside jaws | 7.0 V | 6.99 / 7.00 (re-read) | ≡ A |
| **Boss height above faceplate** | depth rod, tip on the faceplate | ~2 U | ☐ | ☐ |
| Shaft Ø (round-to-round) | outside jaws | 4.0 V | **3.99** (uniform along its length) | ≡ A |
| Shaft across-flat | outside jaws | 3.5 V | **3.45** (tightest) | ≡ A |
| Shaft length from faceplate (or from boss top — say which) | depth rod | 12 V | 12.39 from faceplate incl. boss (derived) | ≡ A |
| D-flat length from shaft tip | depth rod / jaws | 8 V | ☐ | ☐ |
| Faceplate M3 hole c-c (edge-to-edge same side) | outside jaws | 17 V | **17.11** derived — o/o 19.61, i/i 14.61; minor Ø **2.50** | ≡ A |
| Faceplate hole: tapped M3 or clearance? thread depth? | eyeball + M3 screw | tapped M3 | **tapped M3** — confirmed, an M3 screw runs in. Depth ☐ | ≡ A |
| **Faceplate Phillips screw heads: Ø and height above the face** | jaws + depth rod | ~Ø4 × ? | head Ø ~**4.5** derived (o/o 21.68, i/i 12.45 → c-c 17.07, Ø 4.62; vs M3 hole o/o 15.59, i/i 8.65 → Ø 4.44). Height ☐ | ≡ A |
| Encoder connector type + pin count, cable length | eyeball / tape | 2.54 6-pin, 200 mm | 6-way JST, body 14.03 long, stands 8.45 proud **radially**; pitch ⚠ looks < 2.54; cable length ☐ | ≡ A |
| Mass | scale | 95 | **96.2** incl. loom (loom alone 2.9 → motor 93.3) | ≡ A |
| Label text (voltage / rpm / ratio) — photo | camera | "130 rpm" | ☐ | ☐ |

**Motor A notes (17 Sep, Den at the bench + photos):**
- Section split confirmed by the stickers: teal **BRINGSMART** band = gearbox (20.86), white **DC12…** band = motor can (32.71). Remainder **5.27** = encoder assembly at the rear. 20.86 + 32.71 + 5.27 = 58.84 ✓.
- Overall length including shaft **71.23** → stick-out from the faceplate **12.39** (boss + shaft, derived).
- Faceplate carries **four features on a cross**: 2 × tapped M3 at c-c 17.11 and 2 × fitted Phillips at c-c 17.07, on perpendicular axes. Cross-check: M3-centre to Phillips-centre measures 12.12 derived; two perpendicular pairs at r 8.54 predict **12.08**. Agreement 0.04 mm.
- Tapped-hole minor Ø reads **2.50** — textbook M3 tapping drill, consistent with "tapped, not clearance".
- Encoder connector exits **radially**, not axially (photo) — it does not consume the axial tail gap.
- **Tapped-hole axis vs D-flat: 3 and 9 o'clock** with the flat at 12 (Den, 17 Sep, part in hand). This is what hub v5 assumes — **hub v5 needs no change**.
- **Both motors near identical** (Den) — Measured B recorded as ≡ A.
- **Still open on A:** boss height above the faceplate · D-flat length from the shaft tip · **Phillips head height** · connector pitch + cable length · full label text · encoder cap Ø.

### 2.2 Motor — old faded pair (×2) — **measured 11 Sep, A and B identical**

Faceplate layout, confirmed: **two empty tapped M3 holes** on one axis (that's what the wheel pod bolts to), and **two Phillips screws already fitted** on the other axis (gearbox assembly screws — leave them in).

| Dimension | Measured (literal, no clearance) | Note |
|---|---|---|
| Body length, faceplate → back of housing | **39.29** | Den: "whole thing across, just the housing". Unclear if the encoder disc is included. **Not a 65 mm motor.** |
| Gearbox (grey) length | **21.00** | = the 1:45 gearbox length in the seller table |
| Motor can (silver) length | **17.53** | A 370 can is ~30 mm. 17.5 matches a **310-size can (~20 mm)** → old pair is likely JGA25-**310**, not 371. Lower power; "12 V" rating unconfirmed |
| Gearbox OD / can OD | ☐ / ☐ | not given yet — photo suggests ~25 |
| Boss Ø | **7.05** | ✓ matches drawing (7.0) |
| **Boss/collar height above faceplate** | **2.36** | measured at a slight angle → treat as **2.3–2.5**. Hub counterbore Ø9 × 3.0 clears it |
| Shaft Ø, round-to-round | **4.10** (min 4.07) | **Not 4.00.** Hub D-bore must be a variable; coupon at 4.15 / 4.20 / 4.25 |
| Shaft across-flat | **3.46** | flat sits 1.73 from centre on a Ø4.10 shaft |
| Shaft length, collar top → tip | **10.0** | round section from collar top to where the flat starts = **2.0**; total stick-out from the faceplate = 2.36 + 10.0 = **12.36** ✓ consistent with the 12 V assumption |
| D-flat length | **8.0** | **Only 8 mm of flat to drive on.** Hub D-bore useful depth ≤ 10 mm or the shaft bottoms before the hub seats on the collar |
| Tapped mounting pair — round 1: outer **19.46** / inner **14.33** · round 2: outer **19.15** / inner **14.61** | → c-c **16.90** and **16.88**, hole Ø **2.57** and **2.27** | c-c is solid: **17.0 tapped M3 confirmed**. Hole Ø spread straddles the M3 tapped minor (2.5) — knife jaws in a threaded hole always read soft, ignore it |
| Fitted Phillips screw pair (round 1): outer **15.45** / inner **8.71** | → c-c **12.08**, head Ø **3.37** | this is the real screw c-c |
| Hole → screw cross-measures (round 2): lip-to-lip near **8.41**, far-to-far **15.50**, hole far edge → screw centre **13.63** | → centre distance **≈ 12.0–12.5**, head Ø **≈ 3.4–4.8** | doesn't close cleanly against c-c 12.08 at 90° (would predict ~10.4) → axes may not be exactly perpendicular, or one reading caught a burr. **Not blocking** |
| **Phillips head height above the faceplate** | ☐ | **still needed.** The pod's motor well needs relief pockets or the faceplate won't sit flat |
| Collar edge → nearest tapped-hole edge | **3.7–3.8** | cross-check → c-c 17.1 ✓ consistent |
| Encoder connector | 6-pin at the back of the can, plus a small hole in the back | give ≥ 2–3 mm clearance behind the motor |
| Mass | ☐ | |

**CAD consequences (old pair):** interface (17 c-c M3, Ø7 boss, Ø4.10 D-shaft) matches the new pair, so they drop into the same faceplate. Body ~25 mm shorter than `motor_len = 65` — fine as a bench spare, but the cap strap / encoder cable slot won't line up. If the *new* pair also comes in short, C2 (the ±14 stagger) is unnecessary and the duct could move back toward the centre.

**Hub stack (wheel v3):** faceplate → 2.36 collar (Ø7.05) → 2.0 round shaft → 8.0 D-flat → tip. Hub = counterbore Ø9 × 3.0, then D-bore Ø4.20 × 9.0. Grub screw must land in the **last 8 mm**, ≥ 4 mm from the counterbore floor, or it bites the round section and the wheel slips.

### 2.3 ESC — LittleBee Spring 30 A (count in hand unconfirmed, BOM lists one) — **measured 11 Sep**

Layout: three motor pads/pins at one end, power + signal wires out the **opposite** end.

| Dimension | Measured | Note |
|---|---|---|
| Board width | **18.16** | ✓ matches seller's 18 |
| Length, motor pins → wire exit (board) | **35.1** | ✓ matches seller's 35 |
| **Length, motor pins → end of heatshrink** | **41.82** | **This is the envelope that has to fit.** 6.7 mm longer than the board |
| Thickness, fattest point | **5.55** | FET/cap side |
| Thickness, thinnest point | **4.35** | board tapers — pocket floor must be flat to the 5.55 |
| Motor pad span, all three across | **15.58** | ≈ 7.8 pad c-c. Needs solder access + strain relief at that end |
| Power wires (red/black) | **~80 mm** | **short — see constraint below** |
| Signal lead (white/black pair) | **~152 mm** stretched | reaches the MCU comfortably |
| Mounting holes | none mentioned | assume none — strap or pocket retention |
| Mass | ☐ | still wanted for the 990 g budget (×2) |

**Saddle redesign.** Assumed 36 × 19 × 9 — too short. New pocket:

```
esc_pocket_l = 43.0     // 41.82 heatshrink + 1.2 end clearance
esc_pocket_w = 19.2     // 18.16 + 0.5/side
esc_pocket_h = 6.1      // 5.55 fattest + 0.55
```

Height drops from 9 to ~6, which gives back 3 mm of vertical stack.

**Constraints:**
- **80 mm of power wire caps ESC placement.** From the saddle at (+50, −38) the wire must reach the PDB with slack and strain relief — call it 60 mm usable. If the PDB is further, either extend the leads (extra joint in the highest-current path) or move the saddle. **Verify against the layout before the saddle is cut.**
- **Motor-pad end faces the EDF.** Three bare pads at 7.8 c-c take mating bullets for the fan's own plugs — open access at assembly, clearance so joints aren't crushed.
- **Don't fully enclose it.** Continuous EDF draw in sealed PLA has nowhere to dump heat. Slots over the FET side or an open pocket floor.
- Cut the pocket flat at 5.55; let the 4.35 end float, don't chase the taper.

### 2.4 VL53L0X GY-VL53L0XV2 — **8 in hand** (5 new + 3 old; measure one new, one old)

**Count settled 17 Sep: 8 in hand, 7 in the design, 1 spare** against a soldering or wiring kill. Documented fallback if more than one dies: **front + rear only — drop the side sensors.**

| Dimension | How | Assumed | Measured |
|---|---|---|---|
| PCB L × W | outside jaws | ~25 × 10.7 P | **24.78 × 10.32**, 3.18 thick |
| Mounting hole Ø | inside jaws | M2? | **2.94** (M2.5 clearance, pilots Ø2.1) |
| **Hole c-c** (edge-to-edge same side) | outside jaws | ~20 U | **19.79** (o/o 22.73, i/i 16.85) |
| Hole position from each PCB edge (X and Y to hole centre) | jaws + half Ø | — | ☐ |
| Sensor window: position on board, size | ruler/photo | — | ☐ |
| Height incl. header (header fitted? which side?) | vertical | — | ☐ |
| Mass | scale | ~1 | ☐ |

### 2.5 TCRT5000 LM393 module (×5)

| Dimension | How | Assumed | Measured |
|---|---|---|---|
| Module PCB L × W | outside jaws | 32 × 14 V | **31.3 × 14.2** (37.4 with pins), 13 Sep |
| Module height incl. pot | vertical | ~10 | trimmer pot 7.9 tall, 13 Sep |
| Fixing hole Ø and position | inside jaws | one hole | ☐ |
| **Bare sensor body L × W × H** (the black TCRT5000 block) | outside jaws | 10.2 × 5.8 × 7.0 V | **10.01 × 5.6**, 9.27 above the board incl. leg standoff, 13 Sep |
| Sensor lead pitch / footprint (4 legs) | jaws | 2.54 | ☐ |
| Pin header: 4-pin? order printed (VCC GND D0 A0)? | photo | 4-pin V | ☐ |
| Sensor mounted flush to PCB or standing off? | eyeball | — | ☐ |

### 2.6 XT60 + loop key (×5 pairs) — **measured 11 Sep**

**Arrangement:** the **yellow half is the panel mount**, contacts on one face, solder tabs on the other (tabs go to the bot's wiring). The **black cap is the removable arming key**, a plug with its terminals bridged. Which half carries pins & which carries sockets is unconfirmed (this sheet said female panel / male key, the wiring guide assumes XT60E-M pins on the panel). Pulling it opens the pack.

| Dimension | Measured | Note |
|---|---|---|
| **Yellow — body length** | **15.56** | ✓ XT60 nominal 15.9 |
| **Yellow — body width, plain section** | **8.13** | ✓ XT60 nominal 8.1 |
| **Yellow — width over the side ridge/indent** | **9.15** | **this is the retention feature** |
| Yellow — overall height, solder tab tips → top | **20.31** | sets internal depth behind the panel |
| Yellow — across the tabs, widest | **11.43** | tapers to **7.1** at the narrow point |
| Yellow — female bore, across | **8.32** | |
| **Black key — external body** | **16.47** long × **9.23** wide | |
| Black key — internal (socket) length | **13.9** | |
| Black key — height | **9.85**, **10.6** at the highest point | **this protrudes past the panel face when plugged** |
| Mass per pair | ☐ | assumed 7.72 V |

**Panel cut-out — cut for the BODY, not the ridge:**

```
xt60_slot_l = 15.9      // 15.56 + 0.35
xt60_slot_w = 8.4       // 8.13 + 0.27
```

The connector pushes in **from inside** until the 9.15 ridge bottoms against the inner wall face. It then cannot pull through when the key is yanked. Retain from behind with a clip or printed capture — no screws, no adhesive in the current path.

Cutting at 9.7 to clear the ridge would let the connector push out the first time the key is pulled in a match. **Do not.** The old assumption (16.5 × 8.5) was close on width but ignored the ridge.

**Depth / protrusion budget:**
- **21 mm internal clearance** behind the wall (20.31 + margin). Nothing else may occupy it.
- **~11 mm free air outside** for the key (10.6 tallest).
- 11 mm off the back is a lever arm for an opponent. **Recess the connector into a shallow well** so the fitted key sits near flush.

### 2.7 LiPo voltage alarm / buzzer — **measured 11 Sep** (ID pending photo confirmation)

3-digit 7-seg display, one button, balance-header pins along the bottom edge, two black buzzer domes on top. Originally reported as the ESC — corrected here.

| Dimension | Measured | Note |
|---|---|---|
| Width, across the display digits | **25.72** | |
| Height, pin tips → top of the black domes | **38.67** | overall envelope incl. pins |
| Height, ignoring the metal pins | **33.22** | → **pins stand ~5.4 proud** below the body |
| Thickness | **12.21** | |
| Two black domes on top: inner-to-inner **7.48**, outer-to-outer **16.95** | → c-c **12.2**, dome width **≈ 4.7** | A second reading gave ~6 across one dome — unresolved, doesn't affect the pocket |
| Mounting holes / threads | **none** | must be trapped, strapped or pocketed |
| Mass | ☐ | |

**The assumed pocket (32 × 14 × 10) is void.** Real body is **33.2 × 25.7 × 12.2** plus ~5.4 mm of pin.

Redesign constraints:
- Lying flat, footprint **33.2 × 25.7**, only 12.2 tall → the only orientation that fits under the shell.
- **Buzzer domes must not be covered.** Top face when flat, c-c 12.2. Shell needs vents directly over them.
- **Display readable and button reachable** without disassembly.
- No fixings on the part: friction pocket + strap or printed clip. Not glue — it comes off with the battery.
- ~6 mm clear off the pin edge, plus room for the balance plug body.

### 2.8 PCB-mounted modules — **all measured 11 Sep except the TTGO**

| Part | Qty | Measured box (L × W × H) | CAD box (generous) | vs assumed |
|---|---|---|---|---|
| **DRV8871** | ×4 | 25.17 × 21.63 × 9.6 | **26.0 × 22.5 × 10.5** | 25.4 × 20.3 → **+1.3 wider** |
| **MP1584 buck** | ×4 | 13.86 × 9.95 × 7.84 | **15.0 × 11.0 × 8.5** | 22 × 17 × 5 → **much smaller footprint, 2.8 taller** |
| **PCF8574 (HW-171)** | ×4 | 54.64 × 15.62 × 11.29 | **56.0 × 16.6 × 12.0** | ~48 × 16 × 10 → **+6.6 longer** |
| **TTGO T-Display S3** | ×1 | 62.3 × 25.65 × 6.88 (no pins) · **14.6 over the header pins** | — | 51.5 × 25.5 assumed → **10.8 longer**. **In hand and measured 12 Sep** |

**Tallest module on the board is the PCF8574 at 11.29**, not the DRV8871. So shell clearance above the PCB face = 11.29 + 6 mm standoff ≈ **17.3 mm**, plus wall. (The S3 at 14.6 over its header pins is taller still, but in v11 it sits on the wellcap, not the module board.)

**Board-area problem (closed, kept for history).** Written for the expansion PCB, which no longer exists. The v11 design uses one PCF8574 in the lid, two DRV8871s & two MP1584s, on protoboard cuts (Board B 51 × 30, Board L ~50 × 15).

Rough module footprint, before any routing space, spacing or connectors:

| Module | Each | ×4 |
|---|---|---|
| PCF8574 | 56.0 × 16.6 = 930 mm² | **3 720 mm²** |
| DRV8871 | 26.0 × 22.5 = 585 mm² | **2 340 mm²** |
| MP1584 | 15.0 × 11.0 = 165 mm² | **660 mm²** |
| | | **≈ 6 700 mm²** |

A 100 × 100 board is 10 000 mm². So the modules alone eat **~67 % of a 100 × 100** with nothing routed yet — and the four PCF8574s are over half of that, purely because each is 56 mm long. Two things worth raising:

1. **Does the design actually need four PCF8574s?** That's 32 expander GPIO. If it's fewer, the board gets dramatically easier.
2. If four are needed, they may have to stand **vertically on edge or stack**, which changes the shell clearance from 17.3 mm to whatever the stack is.

#### 2.8.1 Still wanted on these modules

| Part | Outstanding |
|---|---|
| DRV8871 | which edges the header rows sit on · hole Ø + c-c (only if screwed, not soldered) · screw-terminal orientation · mass |
| MP1584 | confirm 7.84 is the **height** (tallest = black inductor marked 150) and 13.86 is pot-to-pins · pad ends (IN vs OUT) for Board B · mass |
| PCF8574 | **`pin_len`** — how far the bottom header pins stick below the board · **which of A0/A1/A2 currently has a jumper** (photo is easiest) · mass |
| TTGO T-Display S3 | measured 12 Sep (62.3 × 25.65 × 6.88; 14.6 over the pins). Outstanding: mounting hole Ø + c-c · which edge the USB-C sits on · mass |

### 2.9 Hardware

| Part | Dims wanted | Assumed | Measured |
|---|---|---|---|
| M3 heat-set inserts | — | Ø4.0 × 5.7 | **✔ see 2.9.1** |
| 1000 µF 25 V caps | — | Ø10 × 17–20 P | **✔ see 2.9.2** |
| 0.3 mm feeler blade | thickness · L × W | 0.3 × 100 × 12.7 V | ☐ |
| 1 mm silicone sheet | thickness (3 spots) · stretch feel | 1.0 V | ☐ |
| XT30 pairs | body L × W × H (harness only) | — | ☐ |
| Brass 4 mm couplers (on hand) | bore Ø · OD · length · grub screw thread | 4 mm bore | ☐ |

#### 2.9.1 M3 heat-set inserts — **arrived, measured, and STANDARDISED 11 Sep**

10-compartment assortment box, **all M3 thread**, varying body length and knurl OD. Thread confirmed by dropping a caliper jaw into the bore: minor Ø **2.49 / 2.50 / 2.52** vs M3 tapped minor 2.46–2.50 → **genuine M3**.

| Slot | Length | Knurl OD |
|---|---|---|
| 1 — short | 3.00 | 4.18 |
| 2 — medium | 4.96 | 4.48 |
| 3 — long | 6.99 | 4.21 |

**STANDARD: slot 2 (4.96 × Ø4.48) is the only insert used on this bot.**

```
insert_pilot_d = 4.15      // knurl OD 4.48 − 0.35
insert_pilot_h = 6.0       // length 4.96 + 1.0
insert_boss_od = 8.5       // ≥ 2 mm of plastic all round
insert_chamfer = 0.5       // catches displaced plastic
```

Any wall thinner than 6 mm gets a locally thickened boss. Slot 2 is the **widest** OD measured, so a pilot cut for it still accepts slot 1 or 3 if a compartment runs dry. Slots 1 and 3 appear in no drawing, BOM line or assembly step.

**Bench rules:**
- The insert carries the thread, so **screw tolerance stops mattering**. The pilot is the only variable; window ≈ ±0.15 mm.
- **Never lubricate.** Brass must bond to the melted PLA; lubricant guarantees a spinner.
- Install square with a soldering iron, seat **0.1–0.2 mm below flush**. Crooked → reheat, pull, redo.
- Longer insert = more pull-out and spin resistance, **not** more screw torque capacity. The plastic is the limit.

**Coupon before any insert goes in a real part:** one plate, three holes at Ø4.00 / 4.15 / 4.30. Melt a slot-2 insert into each, then try to spin each with an M3 screw and a driver. Tightest hole that seated without bulging sets `insert_pilot_d` for good.

#### 2.9.2 1000 µF 25 V electrolytic — **measured 11 Sep**

| Dimension | Measured | Note |
|---|---|---|
| Can Ø | **10.38** | ✓ matches Ø10 assumption |
| Can length (no legs) | **16.99** | ✓ within the 17–20 assumption |
| Overall, shorter leg | **38.6** | → ~21.6 of leg beyond the can |
| Overall, longer leg | **43.81** | → ~26.8 of leg. Longer leg = **positive**, grey stripe = **negative**, go by the stripe once the legs are trimmed |
| **Lead pitch (leg c-c)** | ☐ | still unmeasured, only matters for Board B layout now. Expect 5.0 mm for a Ø10 can |
| Mass | ☐ | |

Legs get trimmed to length at assembly, so the 38.6/43.81 numbers don't constrain anything — but **don't trim before the board exists**, and keep the long leg identifiable as positive until it's in the hole. Backwards electrolytics vent.

Standing height once fitted: ~17 mm of can above the board plus seating, so **~18 mm** — taller than every module on the board. If these stand on Board B, they, not the PCF8574, set the clearance above it.

### 2.10 XFly 1413 40 mm EDF — **qty 1, no spare** — **measured 17 Sep**

**Standing policy (Den, 17 Sep): do not bench-test the fan loose.** Verify all wiring and code first, plug it in last, one shot. There is one fan and no spare.

| Dimension | Measured | Note |
|---|---|---|
| Flange OD | **47.71** repeated on rotation; an earlier reading gave **47.81** | **Design to 47.81** — the worst case |
| Flange thickness | **3.31 / 3.35 / 3.40 / 3.50** | Spread **0.19 — exceeds the §0 rule-2 limit of 0.10 ⚠.** Design to 3.50 so the fattest section still seats |
| Flange underside | flat, not filleted | "pretty flush of a seal" |
| Duct OD | **42.75** just below the flange · **42.85 / 42.87** further up | Uncompressed; the duct deflects ~0.15 under caliper pressure |
| Duct section height, flange face → far end of duct | **26.44** | ⚠ **datum not stated** — from the flange seating face or its top face is 3.5 mm of difference |
| Motor assembly past the duct | gap/shaft **5.05** + motor body **18.83** + rear nub **3.6** = **27.48**; **27.5** measured across the whole stack | Δ 0.02 ✓ |
| Mounting ear | one moulded ear visible on the **duct wall**, separate from the flange | Position along the duct ☐ — the clamp-ring ear slots depend on it |
| **Overall height** | ☐ | **One bench-to-nub-tip reading. This gates whether the base gets reamed at all** |
| Which end is the intake | ☐ | |
| Ear: width, thickness, hole Ø, position | ☐ | |
| Mass | ☐ | ~40 g assumed |

**Still open:** overall height (blocking) · mass · which end is the intake · ear dimensions and their position along the duct.

### 2.11 Battery — Ovonic AIR 3S 2200 mAh 120C, XT60 (×2 owned, ONE fitted) — **measured 11 Sep**

The supplier substituted **up**: 2200 mAh / 120C against an ordered 1500 mAh / 45C, and **XT60, not XT30**. Confirmed by label, barcode and 24.42 Wh. Anything still saying 1500 mAh or XT30 is wrong.

| Dimension | Measured | Note |
|---|---|---|
| Body (fattest point, incl. shrink wrap) | **106.29 × 34.39 × 21.46** | |
| Mass | **151.2 g** | one pack on the bot; see `MASS_BUDGET.md` |
| Capacity | **2200 mAh, 120C, 24.42 Wh** | |
| Connector | **XT60** | the plan said XT30 — check the harness |
| Balance / charge lead | ~75 mm | JST-XH 4-pin |
| Discharge lead | ~132 mm | heavy gauge |
| Lead exit face · XT60 body position on the pack | ☐ | |

**Bay 110 × 38 × 24** — a puff allowance, not the normal +0.5/side pocket policy. Strap it, do not pinch it.

---

## 3. Log — as values come in

| Date | Part | Value(s) | CAD change made |
|---|---|---|---|
| 17 Sep | **XFly 1413 40 mm EDF** (qty 1, no spare) | **Flange thickness 3.31** (square, flange-down method — supersedes the ~4 angled reading). Flange Ø max **47.81**. Duct OD **42.75** just below the flange, **42.85 / 42.87** further up (uncompressed; the duct deflects ~0.15 under caliper pressure — 42.7 when squeezed). Motor assembly past the housing: gap/shaft **5.05** + motor body **18.83** + rear nub **3.6** = 27.48, measured **27.5** across the whole stack (Δ 0.02). Flange underside reads flat ("pretty flush of a seal"). **Round 2 (same session):** flange OD **47.71** repeated on rotation (earlier reading 47.81 — design to the 47.81 worst case). Flange thickness at three positions: **3.35 / 3.40 / 3.50**, one locally thin spot at 3.40, most of the ring 3.50. Combined with the 3.31 first reading the spread is **0.19 — exceeds the §0 rule-2 limit of 0.10, flagged.** Design to **3.50** (thickest, so the fattest section still seats). Duct section height, flange face → far end of duct: **26.44** ⚠ datum unstated (from the flange seating face or its top face — 3.5 mm of difference). Overall height still ☐ — needs one bench-to-nub-tip reading. | **Disambiguations closed:** 18.83 is the motor **length**, not a diameter; the ~5 mm gap is **axial**; the nub sits **past** the bell. Seat bore still interferes (47.81 vs ≈47.4 printed) — ream required. **Seat depth no longer the problem** (3.31 vs 3.0 pocket = 0.31 proud, not ~1). New finding: at 0.31 proud the clamp ring’s **Ø48.4 × 0.8 relief never touches the flange** — the ring bolts to the roof and the fan floats with ~0.49 mm of play. Ring relief depth must come down. Duct bore Ø43.51 modelled / ≈43.3 printed clears a 42.87 duct — no change. |
| 17 Sep | **New motor pair** (JGA25-371 "130 rpm") | body **58.84** = gearbox 20.86 + can 32.71 + encoder cap 5.27; OD 24.78; overall incl. shaft 71.23 → stick-out 12.39; boss Ø6.99; shaft Ø**3.99** / flat **3.45**; tapped M3 c-c **17.11** (minor Ø2.50); Phillips c-c 17.07, head Ø~4.5; connector **radial**, 8.45 proud, body 14.03; mass **96.2** incl. loom; A ≡ B | **Carriers OK — no reprint.** Tail gap 75.6 − 58.84 = **16.76** (was 6.3 against the Ø25×69.3 envelope); connector is radial so it costs nothing axially. **Hub v5 OK** — tapped-hole axis 3/9 with the flat at 12, exactly as v5 assumed. ±14 stagger still required (two 58.84 bodies overlap 42.08 in a 75.6 span). Mass budget +2.4 g on the pair. Open: hub bore 4.10 → 4.05 candidate; Phillips head height vs the carrier faceplate seat |
| 11 Sep | Old motor pair | body 39.29, gearbox 21.00, can 17.53, boss Ø7.05, shaft Ø4.10 / flat 3.46, holes 17 c-c tapped M3 | `shaft_d` → variable, coupon 4.15/4.20/4.25. Old pair likely a 310-class motor, not 371 |
| 11 Sep | Old motor pair (round 2) | collar 2.36, shaft 10.0 from collar top (2.0 round + 8.0 flat), tapped c-c 16.88, Phillips screws c-c 12.08 | Hub stack: counterbore Ø9 × 3.0, D-bore Ø4.20 × 9.0, grub ≥ 4 mm off the floor. Open: Phillips head **height** |
| 11 Sep | M3 heat-set inserts | all-M3 kit; 3.00 × Ø4.18, 4.96 × Ø4.48, 6.99 × Ø4.21 | **Standardised on slot 2 only.** `insert_pilot_d 4.15`, `insert_pilot_h 6.0`, `insert_boss_od 8.5` |
| 11 Sep | LiPo alarm (first reported as ESC) | 33.2 × 25.7 × 12.2 body, 38.67 incl. pins, domes c-c 12.2, no fixings | **Buzzer pocket 32 × 14 × 10 void.** Flat-lying 34 × 27 × 13 + shell vents over the domes + display access + strap |
| 11 Sep | ESC (LittleBee Spring 30 A) | board 35.1 × 18.16, envelope **41.82**, thick 5.55/4.35, power wires 80 mm | **Saddle → 43.0 × 19.2 × 6.1.** 3 mm stack recovered. **80 mm lead caps saddle-to-PDB distance** — verify layout |
| 11 Sep | XT60 + loop key | yellow 15.56 × 8.13, ridge 9.15, height 20.31; key 16.47 × 9.23 × 10.6 | **Cut-out 15.9 × 8.4 — body-sized so the ridge captures it from inside.** 21 mm internal + 11 mm external; recess the well |
| 11 Sep | DRV8871 ×4 | 25.17 × 21.63 × 9.6 | Box **26.0 × 22.5 × 10.5**. Short side 21.63 not 20.3 — **four abreast is 5.2 mm wider than the early electronics layout assumes** |
| 11 Sep | MP1584 ×4 | 13.86 × 9.95 × 7.84 | Box **15.0 × 11.0 × 8.5**. Far smaller footprint than the 22 × 17 assumed — **frees ~1 000 mm² of board area**, but 2.8 mm taller |
| 11 Sep | PCF8574 HW-171 ×4 | 54.64 × 15.62 × 11.29, board 1.16 thick | Box **56.0 × 16.6 × 12.0**. **Tallest module on the board.** Four of them = 3 720 mm², over half the module area on a 100 × 100 — **question whether four are needed** |
| 11 Sep | 1000 µF cap | can Ø10.38 × 16.99, legs 21.6 / 26.8 beyond the can | Standing height ~18 mm — **taller than any module**; sets shell clearance if board-mounted. **Lead pitch still missing** |
