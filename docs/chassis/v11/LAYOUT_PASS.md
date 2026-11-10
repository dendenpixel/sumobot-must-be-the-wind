# SumoBot v11 — layout pass (for approval before any solid is built)

12 Sep 2026. This is shot 1 of 2: every part as an envelope, checked for overlaps and for staying inside the hull curves, rendered in plan and side view. Nothing here is a solid yet. Say yes / change X / no, then shot 2 builds base + lid against `interfaces.json` — which nobody may edit without saying so.

Frame: mm, **+X front, +Y left, Z 0 = arena floor.**

Files: `plan.png` (base / hardware / lid), `zstack.png` (side view), `interfaces.json` (the frozen numbers), `checks.json`, `layout.py` (re-run to regenerate all of it).

---

## 1. Decisions made (you delegated these) — with the number that decided each

| # | Decision | Value | Why |
|---|---|---|---|
| 1 | Footprint | **Superellipse n=4, semi-axis 124.5 → 249 × 249**, diagonal r 148.06 | 240 failed: the rear battery bay came out ~6 mm short of the lid curve with the wheel wells where they must be. 249 leaves 3.5 mm bed margin on the 256 X1C and 1 mm rule margin. Plan area 57,477 mm² |
| 2 | Fan seat plane | **Lip on the collar top (Z 14, 3 mm counterbore) → fan top Z 60, flat top Z 65.6** | A face seal with a gasket + clamp ring is the seal that works; bore-bottom seating needs a cylinder-to-bore seal. Height cost 66 mm total, CG cost ~0.5 mm |
| 3 | Clamp PCD | **Ø60, bolts at 45/135/225/315°** | With the ear cut off it's whatever we print; 60 keeps the rear bolt bosses 2.9 mm clear of the motor cheek |
| 4 | Rear ToF | **Two at 180 ± 25°, Z 50 → 7 sensors total** | Your "both see it = it's dead centre" holds out to ~0.55 m because an opponent is ~20 cm wide. Front 0/±25 at Z 48, sides ±90 at Z 48 |
| 5 | Wedge print quality | **1.6 mm skin in the rim-to-seal band, 0.12 mm layers for the top 10 mm of the inverted print, support Z-gap 0.2 / 2 interface layers**; not a separate ring | v5.3 flaked because it was a 1.0 skin on tree support. +8 g. Separate outer ring stays as plan B |
| + | Tower lean | **7.5°** (v9 had 5°, postmortem wanted 10°) | 10° shrinks the flat top to 151 mm and the TTGO window falls off its edge; 5° leaves 0.4 mm of lip. 7.5° gives a 164 mm flat top and a **4.5 mm lip at Z 53** whose widest point is inset 36.13 — 2.13 mm inboard of the base collar (rule ≥ 2.0) |
| + | Motor stagger | **±14 mm stays** (+Y motor at X +14, −Y at X −14) | 69.3 mm motors inside a sombrero cannot be collinear (25 mm overlap); Ø25 bodies need ≥ 25 + gap. Motor tail to the opposite well wall: **7.5 mm** for the encoder connector — **check the connector doesn't protrude more than ~5 mm** Update 17 Sep: the measured motor is 58.84 long with a 16.76 tail gap, and the ±14 stagger is still required. |
| + | Duct position | **(57, 0)**, bore Ø43.3, collar Ø52, bellmouth R5 | Rear edge clears the motor cheek (2.9 mm), front bolt ears clear the lid skirt (2.6 mm), grille Ø46 lands inside the flat-top edge (2.2 mm). Fan centre 57 mm forward: pressure centroid stays at the sealed-area centroid, not at the fan |
| + | Comparator boards | **Deleted.** Bare TCRT5000 phototransistors into **ADC1 on GPIO 1, 2, 3, 10** with a 10 k pull-up + 100 Ω LED resistor each on the main board | Four 33 × 15 boards would not pack anywhere; the S3's free pins are exactly ADC1. Threshold in software, calibrate on the arena. −4 boards, −16 wires |
| + | TTGO location | **On the −Y wellcap top** (X −40…23, Y −68…−40, Z 49.2–61.2), display up under a 65 × 30 window in the flat top | The S3 is ~63 mm long; every position on the roof inside the tower curve failed by 5–8 mm. The wellcap top is free, 12 mm under the flat top, and keeps the TTGO base-side so the lid needs only the **4-wire I2C plug** (PCF8574 + ToFs + button stay in the lid). Den's call 12 Sep |
| + | XT60 loop key | **Base-mounted, rear-left, socket face at X −72 facing backwards, Y 57.6–73.2, Z 15–23**; key pulls out rearward through the slit opening | No high-current wire crosses the lid joint; key reachable with the lid on; recessed 5 mm inside the tower face so it isn't a lever arm |
| + | Battery | **On the roof (floor Z 10.9), rear, long axis Y, pack X −82.5…−48.1**, guide rails + strap, slides straight out −X through a **133 × 23 slit (Y −58…+75, Z 10.9–34)** in collar + skirt + tower | Sunk tub can't slide out over the wedge (that was DEC-13). Roof-mount costs +1.1 mm CG and gains plenum area under it |
| + | Lid fixings | 4 × M3: **(70, 70), (−46, 72), (−50, −73), (70, −70)** | Rear pair pulled inboard to clear the key and the slit |
| + | Tyre width | **27** (trim 1.5 per face as specced) → `well_y = 31` | At 30 the tyre overlapped the well wall by 0.5 |
| + | Line sensors | Bare TCRT5000 at **inset 28 on each diagonal → (±84.9, ±84.9)**, face Z 2.2, pocket open downward inside the plenum ceiling, wire hole inboard of the knee | Inside the seal loop, so the pocket is just a recess in the plenum ceiling — no leak. Wedge underside there is Z 8.1: body must be ≤ 5.9 tall with leads bent flat, else a ≤ 1.5 mm local pod |
| + | Scraper blade, pitch skids, ballast pockets | **None** | Rim at Z 0.5 is the third contact and the scraper line; stick-on ballast |

---

## 2. Numbers that fell out

| Quantity | Value |
|---|---|
| Sealed plenum area (inside seal loop, minus two wells) | **36,516 mm²** |
| Downforce at 200 / 400 / 800 Pa (unmeasured pressures) | 7.3 / 14.6 / **29.2 N** |
| Axle Z = wheel_od/2 | 23.40; motor bottom − roof top = **0.00** |
| Wheel centres | (+14, +54.7) and (−14, −54.7); track 109.4 |
| Well interiors | L: X −11.9…39.9, Y 39…70; R: point mirror |
| Fan | body Ø43 from Z 11 to 60; clamp ring Ø56 + 4 ears Z 14–17; keep-out Ø45 to Z 64 |
| Flat top | Z 65.6, semi 82.2 on axis / 105.8 on diagonal |
| Lip | 4.5 proud at Z 53, widest at inset 36.13 |
| Motor tail → opposite well wall | 7.5 mm |
| Checks | 0 overlaps, 0 outside-curve, 1 near-miss (front ToF pocket ↔ fan keep-out 0.53 mm) |

---

## 3. What is where (the PLACED list)

**Base (one print, inverted, PLA):** superellipse rim at Z 0.5 → 15.13° wedge → roof Z 10.9; seal loop inset 20/23; two sealed wheel wells with their own loops; motor cheeks (open top) at X ±14; duct collar at (57, 0) with 4 bosses; battery rails + stop; XT60 bracket; 4 lid-fixing bosses hanging below the roof; pressure test port at (−30, −10); 4 line-sensor pockets in the wedge underside; rear slit through the collar.

**On the base roof:** motors (Z 10.9–35.9), wheels, DRV8871-L on a board cut at X −43.5…−17.5, Y 40–62.5 (rear-left); DRV8871-R + buck + TCRT resistors on a board cut at X 24–70, Y −33…−58 (front-right); bus block + 1000 µF at X −44.5…−30, Y 20–36 (beside the battery stop); ESC velcro'd on the +Y wellcap top (Z 49.2, leads exit −X to the bus, 66 mm); **TTGO on the −Y wellcap top** (display up, USB-C toward +X); battery.

**Lid (one print, flat top down, PLA, no supports):** skirt ring inset 36.4/38.4 Z 10.9–20.9; tower leaning 7.5° from Z 20.9; lip at Z 53; flat top Z 65.6. Flat-top furniture: grille Ø46 at (57, 0) · TTGO window 65 × 30 at (1.5, −38) · alarm window/vents/finger hole over a pocket at (−41, 34) · start button Ø26 pad at (−38, 10) · group-number recess 60 × 25 at (−5, 61.5) · gland Ø10 at (−10, 5) for the 4-wire plug · optional LED at (30, −72). Under the top: PCF8574 (X −80…−24, Y −5…−21.6). Tower wall: 7 ToF facet pockets, 4 lid lugs.

**Two wellcaps, one clamp ring, two hubs** (PETG).

---

## 4. Wiring — how it all connects and why

Rule: the **snap button is a signal**, the **XT60 loop key is the power switch**. Key out = dead robot.

```
LiPo 3S ──XT60 lead──► loop-key socket (base, rear-left)  ← key in = live
                              │ 14 AWG
                              ▼
                        BUS BLOCK (base roof, beside the battery stop)
                        1000 µF ‖ + 220 µF ×2
          ┌───────────────────┼──────────────────────┐
          ▼                   ▼                      ▼
   ESC 30 A (wellcap top)  DRV8871 L / R (VM)     MP1584 buck → 5.00 V
   16 AWG → EDF 3-phase    20 AWG → motors             │
   BEC red wire CUT                                    ▼ 5 V + GND
                                                       ▼ 5 V
                                     TTGO S3 (on the −Y wellcap; 3V3 out) ── I2C 17/18 ──┐
                                                       ═══ 4-wire JST-XH (3V3, GND, SDA, SCL) through the gland ═══
                                                       ▼
                                     LID: PCF8574 ──► 7× ToF XSHUT + start button
                                          7× VL53L0X (VIN 3V3, SDA/SCL)
Balance lead (75 mm) ──► LiPo alarm (lid pocket, 28 mm from the pack)
```

Base-side wiring stays short: TTGO on the wellcap → the two DRV8871 inputs, the two encoders, the ESC signal and the four line sensors (ADC1, a pull-up and an LED resistor each on board_A). Only I2C + 3V3 + GND cross to the lid.

The pin-by-pin table that was here is superseded by [`docs/PIN_MAP.md`](../../PIN_MAP.md) (17 Sep): it had the ESC and encoder R the wrong way round (the bootloader drives 43 at every reset, so the ESC goes on 43), and the lid plug carries 3V3L from Buck 2, not the Brain's 3V3. The layout geometry in this file is unaffected.

Opponent indication: on the display (R6 satisfied); LED hole kept as an option. Battery voltage: the alarm buzzer, no ADC.

---

## 5. Measure before shot 2 (each one changes geometry)

| # | Measure | Changes |
|---|---|---|
| 1 | New motor actual body length + encoder connector protrusion | tail gap is 7.5 mm at 69.3 — if the connector sticks out > 5 mm the faceplate moves to 40 |
| 2 | New motor mass ×2 | 190 g of the budget |
| 3 | T-Display S3 outline (L × W) and header/USB stick-out below the board | TTGO window and pocket depth (assumed 63 × 28 × 12) |
| 4 | Bare TCRT5000 body height with leads bent flat | ≤ 5.9 fits under the wedge; else a local pod |
| 5 | Fan: body OD, lip OD + thickness, overall height, ear-cut result | collar counterbore, clamp ring, front ToF pocket (0.5 mm) |
| 6 | Button panel grip range | Ø26 pad thickness |
| 7 | Tyre width after trim | `well_y` |
| 8 | Hole-shrink coupon 4.00 / 4.15 / 4.30 | every hole |

---

## 6. Things to say yes/no to

1. Shape and proportions in `plan.png` / `zstack.png` — is this the robot?
2. TTGO on the −Y wellcap top, 4-wire plug to the lid.
3. Comparators gone, ADC threshold in software.
4. Key on the rear-left, reachable with the lid on.
5. 7 ToFs (front 0/±25, sides, rear ±25).
6. Lean 7.5° / lip 4.5.
