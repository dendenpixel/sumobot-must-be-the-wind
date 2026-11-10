> **Superseded 13 Sep 2026.** As-built numbers are in `docs/chassis/v11/REPORT_base_stage.md`, `docs/chassis/v11/REPORT_lid_stage.md` and `docs/chassis/v11/CHANGELOG.md`, and they override this brief. Kept for the reasoning/history.

# SumoBot v11 — CAD build brief

You are building Den's SumoBot chassis in this session. The layout is already solved and frozen; your job is to turn it into printable solids. Build in a real CAD kernel (CadQuery/OCCT), export STEP + STL, render views, and stop at the checkpoints below.

**Attached, and the only inputs you use:** `interfaces.json` (frozen numbers — read it first), `layout.py` (the envelope model that produced them; run it, it's the ground truth for every position), `plan.png`, `zstack.png` (what the robot is), `NOT_THIS.png` (a previous attempt — do not build this). Nothing else. Do not ask for, infer from, or reconstruct any earlier version.

Frame: **mm, +X front, +Y left, Z 0 = arena floor.** Every hole, bore and pilot is a *target printed size*: add `hole_shrink = 0.21` before cutting.

---

## 1. THE PICTURE

A **sombrero**. A 249 × 249 superellipse (|x/124.5|⁴ + |y/124.5|⁴ = 1) with a hard rim 0.5 mm off the floor that rises as one continuous 15.13° ramp, identical at every bearing, to a flat roof at Z 10.9 (the "knee", RIM INSET 34). Inside the knee a lid: a short vertical skirt ring, then a superellipse tower leaning inward 7.5°, a 4.5 mm anti-climb lip at Z 53, and a flat top at Z 65.6. Two wheels tucked inside the footprint in sealed wells, one each side, on a Y axle at Z 23.4. Battery low at the rear, fan straight through the roof forward of centre, electronics flat on the roof. The whole thing is 66 mm tall. `plan.png` and `zstack.png` are this robot; `NOT_THIS.png` is a flat octagon slab with a box on top — the opposite of what is wanted.

Base = the pressure vessel. Lid = armour and sensors. Everything above the roof plate is at ambient pressure.

## 2. FROZEN — may not change. If something here cannot be built, stop and say which two numbers conflict.

- Footprint, rim height, wedge angle, knee, every Z level and every RIM INSET in `interfaces.json` (`rim`, `z`, `insets`, `lean_deg`, `lip_proud`).
- Wheel axle positions, `axle_z = wheel_od/2 = 23.40` (assert it), motor stagger ±14, well rectangles, duct centre (57, 0), battery position and slit, XT60 position, ToF positions/yaws, line-sensor positions, lid fixing positions — all from `interfaces.json`.
- Part count: **base, lid, 2 motor/well carriers, 1 battery frame, 2 wellcaps, clamp ring, wheel hub ×2**. Nothing else is printed. No adapters, no guards, no coupons unless §7 asks.
- **The base has nothing above the roof plane Z 10.9.** Everything that stands on the roof is a bolt-on carrier (§3.4) so the base prints roof-face-down with no support under the roof.
- No lid surface radially proud of the base. Nothing rigid below Z 1.5 except the rim lip within 12 mm of the rim.
- Base prints in one piece, upside-down (roof face on the bed); lid prints flat-top-down with **no supports anywhere**. Bed 256 × 256 (Bambu X1C, 0.4 nozzle, 0.2 layers).
- Rules: ≤ 250 × 250 × 250, ≤ 1000 g, TTGO ESP32-S3 controls it, group-number recess and opponent display/LED exist.

## 3. PLACED — what goes where (bounds are envelopes from `layout.py`; build the printed feature that holds each one)

### 3.1 Base — integral features (PLA, one print)

| Feature | Geometry | Notes |
|---|---|---|
| Rim lip | 1.2 thick, underside Z 0.50, top edge Z 1.70, continuous 360° | the armour; scraper line |
| Wedge | straight ramp Z 1.70 at the rim → Z 10.90 at RIM INSET 34, along the local normal | skin **1.6 mm** from the rim to the seal loop (inset 0–23), **1.2 mm** inboard of that; 8 radial ribs 2.0 wide, R1.5 root fillets, Z 5.5 to the ceiling, r 30 outward to the seal loop, skipping wells/duct/bosses by ≥ 3 |
| Plenum | pan underside Z 1.50; cavity Z 1.50–9.70; roof plate Z 9.70–10.90 | nothing sunk into it |
| Main seal loop | one closed wall 3.0 thick, outer face inset 20.0 / inner 23.0, Z 1.50 up to the wedge skin, fused | a plain smooth offset — no detours |
| Skirt grooves | 1.3 wide × 2.0 deep cut upward from every seal-wall underside (open Z 1.50, floor 3.50), centred in the 3.0 wall, continuous, 45° × 0.4 mouth chamfers | three loops: main + each well |
| Wheel wells ×2 (base part) | roof cut-out = well interior L: X −11.9…39.9, Y 40…71 (R = point mirror); below the roof a 1.2 inner wall + 3.0 seal wall (outer L: X −16.1…44.1, Y 35.8…75.2) from Z 1.5 to the roof top, with its own groove; open to the floor | outside the plenum. The seal-wall top (4.2 wide, flush with the roof) is the landing for the carrier's well wall. Four Ø8.5 hanging bosses with Ø4.15 × 6 pilots for the carrier bolts at L: (−19, 37.8), (42, 33), (−19, 78), (39, 78); R: point mirror (OCCT-clash-checked) |
| Duct | bore Ø43.3 (+shrink → 43.51) through the roof at (57, 0) in a **Ø56 boss hanging below the roof** (Z 1.5–10.9): **R5 bellmouth** on the plenum side (mouth Ø53.51, 1.2 wall), and a **Ø47.4 × 3.0 counterbore down from the roof top** = the fan lip seat, so nothing stands above Z 10.9; 4 pilots Ø4.15 × 6 on PCD 60 at 45/135/225/315° in Ø8.5 bosses Z 1.5–10.9, merged into the seat boss | fan intake down, exhaust up; fan top lands at Z 56.9 |
| Knock-outs | 2 × Ø12, 0.6 mm membranes, 0.4 annular score on the bay side, at (57, ±36), sealed by default | tuneable bleed / EDF thermal path |
| Battery-frame pilots | three Ø8.5 hanging bosses with Ø4.15 × 6 pilots under the battery frame footprint (§3.4): at (−60, ±58) and (−42, 0) | frame bolts |
| Collar | **none** — the lid locates on its four M3 bolts; the roof is flat out to the knee | |
| Lid-fixing bosses ×4 | Ø8.5 bosses hanging **below** the roof (Z 1.5–10.9) at (70, 70), (−46, 72), (−50, −73), (70, −70); vertical Ø4.15 × 6.0 pilot drilled down from Z 10.9, sealed floor Z 4.9 | roof top stays flush |
| Board pilots | flush Ø4.15 × 6 pilots 8 mm inboard of the corners of board_A (X 23…70, Y −58…−33) and board_B (X −44.5…−18, Y 39…64), same hanging-boss construction | M3 nylon standoffs, no printed standoffs |
| Bus block | flat land X −44.5…−30, Y 20…36 with two pilots | |
| Line-sensor pockets ×4 | at **(±78.0, ±78.0)** (RIM INSET 37.8): pocket 11.4 (tangential) × 6.6 (radial) hanging from the roof/ramp underside (housing follows the actual underside at its outer corners, ≥ 0.32 mm over the body), walls 1.2, open downward, sensor face Z 2.2, body top Z 9.2; 3 × 3 underside channel to a Ø4.0 wire hole through the roof at **(±69, ±79)** — the hole directly above would sit under the lid skirt | the pocket is a recess in the plenum ceiling — no seal needed; wire hole hot-glued; ribs skip pocket and hole by ≥ 3 |
| Pressure test port | Ø2.0 through the roof at (−30, −10) + Ø4.15 pilot beside it for an M3 sealing screw | |
| Wire holes | Ø4.0 through the roof, one per line sensor, inboard of the knee | the only plenum→bay penetrations; budget 60 mm² total |

### 3.2 Hardware on the base (build clearance for these; do not model them in detail)

| Item | Envelope (X / Y / Z) | Retention |
|---|---|---|
| Motor L / R | X 1.5…26.5, Y −30.5…38.8 (seats on the faceplate inboard face at 38.8), Z 10.9–35.9 / point mirror | carrier cheeks + 2 × M3 flat-head into the motor's tapped holes; cap strap pilots beside each cheek pair |
| Encoder connector | 16 × 5 × 12 at each motor tail: 8.3 mm to the opposite faceplate | — |
| Wheel L / R | Ø46.8 × 27 wide, centre (±14, ±55.7, 23.4) | hub on the D-shaft; hub inner face at |Y| 41.2; shaft engagement 6.6 mm on the flat |
| Fan | Ø43 × 49, lip Ø47 × 3 sitting in the roof counterbore Z 7.9–10.9, top Z 56.9 | clamp ring on the 4 roof bosses + 1 mm gasket |
| Battery | 106.29 × 34.39 × 21.46 at X −82.5…−48.1 | strap through the rail slots |
| DRV8871 R + buck | on board_A, Z 19.6–30.1 | board on standoffs |
| DRV8871 L | on board_B | " |
| 1000 µF cap | Ø11 × 18 at (−38, 30) on the bus block | |
| ESC | 43 × 19.2 × 6.1 on the **+Y wellcap top**, X −16…27, Y 41…60, Z 49.2–55.3 | velcro |
| TTGO S3 | **62.3 × 25.65 × 6.88 MEASURED** (14.6 with pins); on the **−Y wellcap top**, X −40…22.3, Y −65.65…−40, Z 49.2–60.6, display up, USB-C + buttons at the +X end | pins down, clipped to ~4 mm, hanging between **two 4.5 mm-tall rails printed on the cap top** (rails run along X under the two header rows, 20.3 mm apart); wires soldered to the stubs; 3.4 mm to the flat-top underside |

### 3.3 Lid (PLA, one print, flat top on the bed)

| Feature | Geometry |
|---|---|
| Skirt ring | prismatic extrusion of RIM INSET 36.4 (outer) / 38.4 (inner), Z 10.9–20.9, no draft, sitting flat on the roof; **notched at the rear over Y −58…+75** for the slit. Lateral location is by the four M3 bolts |
| Tower | outer face = RIM INSET (36.4 + (Z − 20.9)·tan 7.5°) from Z 20.9 up; wall 2.0; the lean starts at Z 20.9, not 10.9 (a lean from 10.9 makes an up-facing ledge) |
| Anti-climb lip | 4.5 mm proud, widest at Z 53.0 (inset 36.13), flat horizontal underside, ~45° upper face back into the tower by Z 58; interrupted only at ToF pockets |
| Flat top | Z 65.6, skin 1.6 (inner Z 64.0), edge at RIM INSET 42.28 |
| Rear slit | through skirt + tower: Y −58…+75, Z 10.9–34.0, R1.5 corners; the XT60 key sits in the left end of it |
| Lid lugs ×4 | inward pads 12 × 12 × 3 (Z 10.9–13.9) at the four fixing positions, Ø3.4 through, Ø7 × 1.5 counterbore for an M3 button head |
| ToF pockets ×7 | at each `tof` entry: a flat facet 14 wide normal to the yaw, with a 12 (H) × 26 (V) × 4.5 deep pocket behind it, 14 × 8 optical slot, board long-axis vertical, two Ø2.1 pilots at 19.79 c-c vertical; front three at Z 48, sides Z 48, rear pair Z 50 | the three front facets form a small nose block |
| Grille | Ø46 in the flat top at (57, 0), 3 mm bars, ≥ 65 % open |
| TTGO window | 64.3 × 27.65 at X −41…23.3, Y −66.65…−39, 1.0 ledge inside for acetate; both onboard buttons reachable through it |
| Alarm pocket | 34 × 27 × 13 hanging from the flat-top underside at X −58…−24, Y 21…48; in the top above it: 30 × 20 window, two Ø4 vents at 12.2 c-c, Ø8 finger hole; strap retention |
| Start button | Ø18.7 (+shrink) hole at (−38, 10) through a Ø26 pad whose total thickness = `btn_panel_t` (default 2.0), blended into the skin over 6 mm; keep-out Ø20 column Z 36.5–64 |
| Group-number recess | 60 × 25 × 0.6 at X −35…25, Y 49…74 |
| Gland | Ø10 at (−10, 5), Ø16 × 1.0 recess — the only harness hole |
| PCF8574 seat | 56 × 16.6 × 12 under the top at X −80…−24, Y −21.6…−5; two Ø2.1 pilots or a strap slot |
| Optional LED | Ø5.2 at (30, −72) |
| **No radial holes in the tower below Z 38** except the slit | |

### 3.4 Bolt-on carriers and small parts (PETG unless noted; all print right-way-up on their flat underside, no support)

| Part | Geometry |
|---|---|
| **Motor/well carrier ×2** (L and R are point mirrors) | One piece: (a) the 1.2 mm **well wall** ring standing on the seal-wall top around the roof cut-out, up to **Z 39.0**, with four Ø8.5 insert pads on its top (a local pad that *is* the boss, blended ≥ 4 mm into the wall) for the wellcap; the inboard wall at \|Y\| 38.8–40 **is the motor faceplate**: Ø8.0 (+shrink) shaft hole at (±14, ±40, 23.40); two Ø3.2 (+shrink) holes at 17.00 c-c horizontal through the shaft centre, each in a local Ø8 pad 1.5 thick (0.3 proud on the well side) with a 90° countersink for an M3 flat-head screw (head Ø6 max) driven from the well side into the motor's tapped holes — no relief pocket; (b) the **motor cheeks**: half-round saddle Ø25.3 (+shrink), axis Y at Z 23.40, side walls 1.6, from the faceplate inboard face at \|Y\| 38.8 inward 70 mm (L: X −0.1…28.1, Y −32.2…38.8), Z 10.9–33.0, open at the top, three 12 mm segments — the saddle floor is **cut away** so the motor rests directly on the base roof (no floor under it); (c) a 1.6 mm base flange joining wall and cheeks, with four Ø3.4 holes onto the base's hanging bosses. Must accept any motor length 39–70. The two carriers' inner cheek walls may touch at X 0 — no spine, each carrier owns its own wall |
| **Battery frame ×1** | One piece on a 1.6 flange: two guide rails 1.6 × 6 tall at Y ±55…±56.6, **X −76…−46.5**, each with two 12 × 3 strap slots and 1.2 webs; the front stop 1.6 × 8 tall at X −48.1…−46.5, Y ±55; and the **XT60 bracket** (blended into the +Y rail) holding a panel socket 15.56 × 8.13 × 20.31 with its face at X −72 facing −X, **Y 58.0…73.56**, Z 15–23.1 (cut-out 15.9 × 8.4, body not ridge; socket inserted from the front so the 9.15 ridge captures; 21 mm clear behind). Three Ø3.4 holes onto the base bosses at (−60, ±58) and (−42, 0). Pack slides straight out −X; no rear wall |
| Wellcap ×2 | open-bottom box over each well: laps outside the 1.2 walls with 0.3 clearance down to Z 36; inward ledge 3.0 wide at Z 40.5–41.7 (EPDM 3 mm compressed to 1.5); ceiling underside Z 48.0, top Z 49.2, skin 1.0; four Ø3.4 through to the wall-top bosses. No outward flange. Wheel clearance ≥ 1.2. **−Y cap:** two TTGO rails 4.5 tall × 2 wide along X at Y −41.5 and −64.15 (under the header rows) with a velcro land between. **+Y cap:** plain top for the ESC |
| Clamp ring | Ø56 ring, ID 44.5, 3.0 thick + four Ø9.5 ears on PCD 60 at 45°, Ø3.4 through, Ø7 × 1.5 counterbores; sits on the roof over the fan lip; gasket 1 mm silicone ID 44 / OD 52 |
| Wheel hub ×2 | overall 29.0 (1.0 flange + 27.0 ring seat + 1.0 flange), tyre bed OD 38.1, flange Ø38.4, core Ø16 × 20, 3 mm web; D-bore Ø4.41 / flat 3.77 CAD (target printed 4.20 / 3.56), 9.0 deep; motor-face counterbore Ø9.0 × 3.0; radial M3 grub at Z 9 through a Ø4.5 access hole onto the shaft flat. Coin orientation |

## 4. SOLVE — yours to decide (and report)

Rib layout inside the skip rules · boss/gusset shapes · fillets · exact groove path around the well/seal-loop junctions · the facet-block form for the front ToF trio · how the wellcap ledge meets the wall-top pads · the XT60 bracket shape · cap-strap pilot positions · overhang treatment on the wedge underside for the inverted print.

## 5. ASK ME — stop and ask before building if any of these bite

1. Any envelope in `layout.py` that a printed feature must cross (say which two).
2. If the cheeks cannot accept a 39–70 mm motor with the faceplate at |Y| 39.
3. If the rear slit + collar notch leaves the lid without lateral register (propose a fix, don't just add one).
4. If a lid feature cannot be printed top-down without support (report the worst location by name).
5. If the 1.6 wedge skin and ribs cannot be bridged in the inverted print without support anchored to the part (support anchored to the *bed* under the wedge annulus is allowed and expected).

## 6. CHECKS — build order and gates

1. Run `layout.py`; re-derive every position from `interfaces.json` (no hand-typed coordinates).
2. **Base first, then the two carriers and the battery frame** (they define the motor and battery interfaces). Render 4 views + sections at X = 0, Y = 0, the 45° diagonal, and Z 5.5, with the carriers fitted. **STOP and show them before the lid.**
3. Gates on the base: mesh watertight (0 boundary / non-manifold edges); `axle_z − wheel_od/2 = 0.00`; motor bottom − roof top = 0.00; 3D flood fill of the plenum with ideal skirts + duct plugged stays isolated from ambient (report resolution); wheel Ø46.8 × 27 sweep clearance to every well surface ≥ 2.0 (X) / 1.5 (Y); groove depth 2.00 +0.10/−0 everywhere; no feature below Z 1.5 except the rim lip; **no base feature above Z 10.9**; max plan dimension 249.0 ± 0.05; every hanging-boss pilot floor sealed; carriers print right-way-up with no support (saddles are concave-up troughs); carrier well wall lands fully on the seal-wall top; motor bottom − roof top = 0.00 with the carrier fitted; slicer-orientation overhang report (worst location by name).
4. **Lid.** Render 4 views + sections. Gates: no support needed (≤ 55° from horizontal top-down, report worst); lip widest inset ≥ 36.0; skirt/collar radial clearance 0.40; all flat-top features inside the flat-top edge, zero overlaps (name any pair); slit clear of lugs; ToF pockets inside the wall; lid lift check at +1/+5/+15/+40 mm against every base feature.
5. **Assembly.** All parts + hardware envelopes in one STEP: 0 unintended overlaps (declared list printed); battery swept volume straight −X through the slit with the lid on; key withdrawal path; lid driver access at all 4 fixings.
6. Mass: solid volume × 1.24 × 0.82 per printed part; report against base ≤ 175, lid ≤ 110, wellcaps ≤ 8 each, ring ≤ 10.

## 7. DELIVERABLES — and their limits

- `build.py` (parametric, reads `interfaces.json`), `parameters.json` with MEASURED/SELLER/PROPOSED tags carried through.
- STEP: each part + one assembly with hardware envelopes. STL: one per printed part, in its print orientation, on Z 0: `v11_base`, `v11_lid`, `v11_carrier_L`, `v11_carrier_R`, `v11_battery_frame`, `v11_wellcap_L`, `v11_wellcap_R`, `v11_clamp_ring`, `v11_hub`. **Nine files.**
- `views/`: assembled, exploded, top, bottom, side, rear, plus the four sections for base and lid.
- `REPORT.md` ≤ 2 pages: gate table (value / criterion / PASS-FAIL-NOT VERIFIED), declared overlaps, mass table, the print settings per part, and the list of things you decided under §4.
- Coupons: **only** `coupon_hole_4.00/4.15/4.30` (blind pilot, mouth on the bed) and `coupon_bore_4.35/4.41/4.47`. Nothing else.

Done means: Den has seen the base + carrier renders and said yes, then the lid renders and said yes, then the nine STLs exist and every gate in §6 is reported.
