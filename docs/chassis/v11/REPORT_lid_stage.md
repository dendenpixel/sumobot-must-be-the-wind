# SumoBot v11 — LID STAGE report (13 Sep 2026)

Built in Cowork (CadQuery 2.8 / OCCT) on Astra's v11 code base, in the same folder as the base stage.
Parts in this stage: **lid**, **wellcap_L / wellcap_R**, **clamp ring**. Hubs are Den's (not built).
Gates: `gates_lid.json` — **60 PASS / 1 FAIL / 0 NOT VERIFIED** (the fail is the lid mass, first thing below).

Read with: `REPORT_base.md` (the base stage), `interfaces.json` (the frozen contract), `lid_report.json` / `caps_ring_report.json` (every number as built).

---

## 0. The gate FAIL (and one I over-tightened) — Den's call

| Gate | Result | What it means |
|---|---|---|
| **mass lid (PLA)** | **128 g** est. (156 g fully solid, 126.0 cm³) vs target ≤ 110 g | 2.0 walls + 1.6 skin + lip + 7 noses + 4 lugs. Base is 117 g vs ≤ 175, so **structure total ≈ 259 g (base 117 + lid 128 + caps 11 + ring 3) is still under the 267 g v5 figure the mass budget uses**. Levers if you want the 18 g back: wall 2.0 → 1.6 (≈ −14 g), skin 1.6 → 1.2 (≈ −9 g), slicer 3 walls / 15 % gyroid on the flat top. I did not touch the frozen 2.0 / 1.6. |
| overlap lid × XT60 key | **PASS** now; the first run failed with a **+2 mm** margin above the socket top (7.3 mm³), passes with **+1 mm** | The slit's low extension stops at Z 24.6; the XT60 socket top is Z 23.13 → **1.5 mm clear**. The loop key's shell is the socket itself, so this is fine; the first run used my own over-generous envelope. Re-run with the +1 margin is in `gates_lid.json`. |

---

## 1. What was built

### Lid (PLA, prints flat-top-down, no support). As printed 23 Sep: PETG translucent with a support interface, see `../../printing/LID_PRINT_PROFILE.md`
- Outer hull exactly per `interfaces.json`: skirt RIM INSET 36.4 / 38.4 from Z 10.9 to 20.9; tower leaning 7.5° from Z 20.9 to the flat top at **Z 65.6** (top edge inset 42.28); **anti-climb lip** widest inset **36.13 at Z 53** (flat underside, 45° upper face to Z 57.5). Wall 2.0, top skin 1.6. Bbox ±88.37 × ±88.37 × Z 10.9–65.6.
- **Nothing radially proud of the lip's widest** — min RIM INSET of every section vertex from Z 11.5 to 65.3 is **36.19** (knee is 34.0).
- **Battery slit** in the rear skirt/tower: **Y −62…+62, Z 10.9…34.0** (pack is Y −48…53, top Z 32.4) plus two **low extensions to Z 24.6**: Y 62…75 for the XT60 loop key (Y 57.6…73.2, Z 15…23.1) and Y −64…−62 for the frame bolt head at (−78, −61). The extensions stop below the rear ToF noses (bottom Z 26.4) so the noses stay whole.
- **4 lid lugs** at the frozen fixings (70,70) (−46,72) (−50,−73) (70,−70): 3 mm plate Z 10.9–13.9, 10 wide, running from 4.8 mm inboard of the bolt to the nearest wall with a full 45° gusset above (prints top-down without support), clipped 0.4 inside the outer skin; Ø3.4 bolt hole; **Ø7 driver bore** from the plate up through the flat top (a long M3 driver reaches the screw from above).
- **7 ToF "noses"** (see §2).
- Flat top: EDF grille Ø46 at (57, 0) with 3 mm bars at 9 pitch along Y; TTGO display window X −41…23.3 / Y −66.65…−39 with a 1 mm ledge; alarm hanging pocket X −58…−24 / Y 20…47 / 13 deep (1.2 walls) with a 30 × 20 display window, 2 × Ø4 buzzer vents at 12.2 c-c and a Ø8 finger hole; start-button pad Ø26 (2.0 total thickness) with a Ø18.7 hole at **(12, 22)**; PCF8574 seat: two 2 × 3 rails under the top at Y −23.6/−5, X −80…−24 with four 5 × 3.5 zip-tie slots; optional LED Ø5.2 at (30, −72); group-number label position X −35…25 / Y 49…74 (**no recess**, see §3).
- Watertight STL, 1 body, valid BRep.

### Wellcaps ×2 (PETG, print top-face-down)
- Footprint = the carrier's 1.2 wall outer rectangle ∪ the four Ø pad circles, +0.3 clearance, 1.0 skin; rim at **Z 40.5**, top **Z 49.2**, 1.2 ceiling. Four Ø7.5 screw columns at the carrier pads with Ø3.4 holes and Ø6.5 × 2 counterbores. Plain tops — **no TTGO / ESC rails** (still to decide: header pins on or off; the layout puts the TTGO on cap_R, the ESC on cap_L).
- cap_L bbox X −14.4…49.7 / Y 36.5…80.0; cap_R is the point-mirror. **5.5 g each.**
- Seal: the cap rim sits on a 3 mm EPDM strip compressed to ~1.5 over the carrier wall/pad tops at Z 39; the cap is not the well seal (the wells have their own silicone loops under the base).

### Clamp ring (PETG, prints flat)
- OD 56 / ID 44.5 × 3.0 on the roof (Z 10.9–13.9), Ø48.4 × 0.8 underside relief over the fan lip, 4 ears Ø9.5 on PCD 60 at 45/135/225/315° with Ø3.4 holes and Ø6.5 × 1.5 counterbores. **3.0 g.**

---

## 2. ToF noses — what changed from the brief and why

The brief's "16-wide facet recessed 1.4 mm into the tower" **cannot work on this hull**: the tower leans 7.5° and curves, the pocket (2.0 front wall + 4.5 board + pins) reaches 10 mm inboard of the facet, and that ran into the **EDF body** (F0), the **wellcaps / carrier walls** (both sides) and, at the front corners, the **lid-lug driver bores**. The first build had 1.6 cm³ of lid inside the fan.

**As built:** each sensor is a **nose** — a flat vertical facet standing proud of the leaning tower at **RIM INSET ≈ 36.2** (0.07 inboard of the lip's widest, so nothing is ever proud of the lip), from Z 26.4 up to the **lip underside at Z 53**, which becomes the nose's roof. Both ends of every facet are held at inset ≥ 36.2; where the surface normal doesn't match the yaw (F±25) the facet centre is pushed inboard and one end sinks into the tower (a wedge). The board pocket 12 × 26 × 4.5 sits behind a 2.0 front wall, **open to the inside** (board goes in from inside the lid, two Ø2.1 × 1.6 pilots at 19.79 c-c for M2 self-tappers), 14 × 7.6 optical slot. **Optical axis Z 39.9** (was 48): the pocket has to sit wholly under the lip so no hole opens above it — and 40 mm is a better height for seeing low opponents anyway.

Positions were solved automatically against keep-outs (fan body Ø43, wellcaps +1.5, lug bores +1, other noses) — `tof_place()` in `build_lid.py`:

| Tag | yaw | facet centre (x, y) | facet inset | surface normal | skew | note |
|---|---|---|---|---|---|---|
| F0 | 0 | (88.30, 0.00) | 36.20 | 0.0° | 0 | pocket floor 78.8 mm from centre → fan body (r 21.5) clear by 1.2 with 3 mm pin room |
| F+25 | +25 | (82.97, 64.38) | 38.65 | 12.3° | 12.7° | wedge facet; corner placement blocked by the (70,70) driver bore |
| F−25 | −25 | (82.97, −64.38) | 38.65 | −12.3° | 12.7° | mirror |
| L90 | +90 | (−25.17, 88.10) | 36.35 | 90.5° | 0.5° | **moved behind the +Y well** (x 0 hit cap_L / carrier) |
| R90 | −90 | (32.10, −87.91) | 36.45 | −89.0° | 1.0° | **moved in front of the −Y well** (wells are staggered ±14) |
| B+25 | 155 | (−81.43, 72.14) | 37.90 | 157.7° | 2.7° | above the slit extension, nose bottom Z 26.4 |
| B−25 | −155 | (−81.43, −72.14) | 37.90 | −157.7° | 2.7° | mirror |

`interfaces.json` `tof` entries are updated to these (z 39.9). The old x/y were the tower-surface points at Z 48 and are superseded.

---

## 3. Deviations from ASTRA_BRIEF_v11 §3.3 (all deliberate)

1. **ToF geometry**: noses instead of recessed facets; axis Z 48 → **39.9**; sides at x −25 / +32 instead of 0; F±25 at bearing 37.8° with a 12.7° skewed facet. (§2.)
2. **Start button moved (−38, 10) → (12, 22)**: its Ø24 nut hit the alarm pocket wall. Nothing above the +Y carrier there (cap top 49.2, ESC Y ≥ 41).
3. **Alarm pocket Y 21…48 → 20…47** (0.2 mm plan overlap with the label area).
4. **Harness gland deleted.** v9's Ø10 top-skin hole fed a PCF in the lid from a TTGO in the base; in v11 the TTGO is inside the lid volume on cap_R, so a hole in the armour top has no purpose. One line in `LID["gland"]` re-adds it.
5. **Group-number recess deleted** (position kept): a 0.6 mm recess in the face that lies on the print bed is a 60 × 25 ceiling 0.6 mm above the plate — it cannot print. Stick the label on the flat top.
6. **Battery slit narrowed to Y ±62 with low extensions** (was −64…75 full height) so the rear noses can come down to Z 26.4.
7. **Lug plate 12 → 10 wide, inboard 6 → 4.8**: the (−50,−73) lug touched the −Y carrier foot at (−44, −70).
8. **Wellcaps: no TTGO/ESC rails** — held for the header decision.

---

## 4. Print notes
- Lid: `stl/v11_lid.stl` is already flat-top-down on Z 0 (176.7 × 176.7 × 54.7). No support needed: every down-facing area in print orientation is a ≤ 14 mm bridge (ToF pocket/slot floors), a Ø7 bore floor, the 1 mm TTGO ledge or the lug gussets at exactly 45°. Total such area 952 mm². 3 walls, 20–25 % gyroid; the noses and lugs print solid at that wall count.
- Wellcaps: `stl/v11_wellcap_*.stl` top-down (open side up); the Ø6.5 counterbore floors are 2 mm bridges over the Ø3.4 holes.
- Clamp ring: `stl/v11_clamp_ring.stl` flat; the 0.8 relief is a 2 mm-wide bridge annulus.
- Base slicing reminder (from the base stage): supports **on build plate only**, under the wedge annulus and inside the fan bore.

## 5. Assembly / wiring reminders
- Lid screws: 4 × M3 from above through the Ø7 driver bores; heads sit on the Z 13.9 plates.
- ToF boards go in from inside before the lid goes on; wires exit the pocket into the lid volume; XSHUT lines to the PCF8574 on the rails under the top (Y −23.6…−3, X −80…−24).
- Alarm lies flat in its hanging pocket (display up, buzzer under the two vents, button under the Ø8 hole); it rides in the lid — the lid-lift gates exclude it on purpose.
- Encoder connector vs the 1.3 mm tail gap and the header-pin question on the caps are still open items from the base stage. (Closed 17 Sep: tail gap 16.76, the connector exits radially.)

## 6. Build mechanics (this cost most of the day)
- `build_lid.py` fuses **plain oversized solids first** (lugs, nose slabs, alarm box, button pad, PCF rails) and then **cuts every hollow one at a time**. One fused compound of 40 cuts, or a solid with faces 0.01 mm from the spline tower, stalls OCCT for >10 min; sequential cuts run in ~75 s.
- The outer hull is **four stacked lofts glued** (skirt, tower to Z 53, lip, tower above): fusing one tall tower loft with a separate lip loft silently *lost the lip* (OCCT spline/spline fuse). `shell()` asserts the glued volume equals the sum.
- Section-based gates use `sec.discrete` rings; trimesh's `to_2D()` shifts the origin and its `polygons_full` breaks on multi-loop sections.
- Gate results are cast to Python `bool` (a numpy bool is not `True`).

Files: `build_lid.py`, `build_caps_ring.py`, `gates_lid.py`, `render_lid.py`, `export_lid_stage.py`, `lid_report.json`, `caps_ring_report.json`, `gates_lid.json`, `step/v11_lid.step`, `step/v11_wellcap_L.step`, `step/v11_wellcap_R.step`, `step/v11_clamp_ring.step`, `step/v11_assembly_full.step`, `stl/v11_lid.stl`, `stl/v11_wellcap_*.stl`, `stl/v11_clamp_ring.stl` (+ `*_asis.stl` in assembly position), `views/lid_*.png`, `views/sec_*.png`, `views/zoom_*.png`.
