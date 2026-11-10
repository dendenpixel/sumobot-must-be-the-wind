# Wheel hub v6 → v6.1 → v6.2 (21 Sep 2026)

**Current hub: v6.2, printed in ABS, on the bot (both wheels).** File: `hardware/cad/v11/stl/sumo_wheel_hub_v6_2.stl`. Preset: `../printing/PRESETS_hub_v6_2_ABS.md`, bundle `hardware/cad/v11/presets/SumoBot_WheelHub_v6_2_ABS.bbscfg`. The v6 and v6.1 STLs aren't in the repo, they're intermediate steps recorded here for the reasoning.

All three are mesh edits of the printed v5 hub, in the same coordinate frame as v3–v5 (motor face at Z 0, axis vertical, bbox 43 × 43 × 28.9).

Naming trap: the printed v5 came out of `sumo_wheel_hub_v4.3mf`, which is v4 **.3mf**, not "v4.3". Its mesh is v5 (9452 tris, differs from `sumo_wheel_hub_v4.stl` at 9540 tris on the motor face, identical outer profile). v6 is based on that v5 mesh.

---

## v6, taller flanges

**Why:** v5 printed fine (ABS, `filament_shrink` 100 %, fitted), but the cast silicone ring walks sideways over the flange. The lip stood only 1.0 mm above the rib peaks (r 19.0) against a tyre standing ~4.4 mm (tyre OD 46.8).

| | v5 (printed) | v6 |
|---|---|---|
| Flange OD | Ø40.0 | **Ø43.0** (688 verts r 20.0 → 21.5, radial only, z 0/1/28/28.9) |
| Lip above rib peaks | 1.0 | **2.5** (~57 % of the tyre sidewall) |
| Tyre proud of flange | 3.4 | **1.9** (margin so the flange never touches the mat when the silicone squashes) |
| Flange thickness 1.0 / 0.9, seat 27.0, length 28.9, bore, counterbore, grub channel, driver holes, ribs, flange windows | — | untouched |
| Volume | 13 295 mm³ | 13 667 mm³ → **14.2 g ABS** |

Checks: 0 open or non-manifold edges, 0 degenerate tris, the moved-vertex set equals the rim set exactly. The well is 52.8 across, so Ø43 clears.

Not done (ring width still unmeasured): thickening the flanges inward to 1.5 (seat 26). If a flange snaps, that's the next step. If the ring is wider than the 27 seat it rides on top of the flange regardless, so trim the ring.

## v6.1, captive nut, tighter D-flat, Ø6 access hole

**Why:**
1. The wheel was rotationally sloppy on the shaft before the screw went in.
2. The drum access hole was too tight for the soldering iron and insert.
3. Overtightening the set screw pulled the heat-set insert out of the core. The screw pushes on the shaft flat and the reaction pulls the insert back out the way it was pressed in, which is its weakest direction. More plastic only helps a bit, so the insert is replaced with a captive M3 nut.

| Feature | v6 | v6.1 |
|---|---|---|
| Bore flat, from centre | 1.55 (3.60 across, shaft 3.46 → 0.14 gap ≈ ±5° play) | **1.45** (3.50 across, 0.04 gap). 170 verts moved in x. Round Ø4.10 untouched |
| Thread | heat-set insert in a ~Ø2.5–3.1 pilot, 5.95 wall | **captive M3 hex nut** (assumed 5.5 AF × 2.4). Slot x 3.6–6.3 (2.7) × y ±2.9 (5.8), open at the motor face z 0, flat-to-flat against the slot walls, nut corner-up, centred z ≈ 9.0. **45° gable roof** z 12.2 → 13.55, so no flat ceiling |
| Wall behind the nut (takes the screw reaction) | — | core 6.3 → 8.0 plus a **new pad** to r 10.5 = **4.2 mm**. Pad x 6–10.5 × y ±4.5 × z 3–13.5, 45° underside (starts at z 3 to clear motor-face screw heads ≤ 3 mm, assumed) |
| Screw hole | pilot | **Ø3.4 clearance, teardrop (45° roof)**, bore to pad face, z 9 |
| Drum access hole | Ø4.5 | **Ø6.0** at z 9 (+x). Rib gap there is 7.6 mm, so 0.8 mm each side |
| Flanges Ø43, seat 27, length 28.9, driver holes, counterbore, ribs, windows | — | untouched (0 / 11 292 random containment samples differ outside the edit zone) |
| Volume | 13 667 | 13 668 mm³ → 14.2 g ABS |

Screw: pad face (r 10.5) to shaft flat (r 1.41) is 9.1 mm, so an **M3 × 10 grub screw**, or an M3 × 10 cap head (the Ø5.5 head passes the Ø6 hole, and there's 4.6 mm radial room between the pad and the drum inner r 15.1).

The gable and teardrop exist because both voids raycast empty to the plate. Build-plate-only auto support would otherwise grow an unremovable column up inside the 2.7 × 5.8 × 12 slot.

## v6.2, top-lip print failure fix

**What failed:** v6 and v6.1 printed with `support_on_build_plate_only = 1`, and the top flange lip (Z 28.00, 444 mm²) came out as drooped, stringy loops. The v5 precedent ("prints as concentric overhang loops") doesn't hold at Ø43. v5's lip hung 2.5 mm off the drum surface (r 17.5 → 20.0) between ribs, at Ø43 it hangs **4.0 mm** (r 17.5 → 21.5). The ribs only stand 1.5 mm proud (r 17.5 → 19), 12 of them, ~1.9 mm wide with 7.6 mm gaps.

**Precedent correction:** the old hub v4/v5 reasoning ("build-plate-only ON because the tyre groove is an unremovable cavity") doesn't hold for this hub. The tyre seat is 27 mm tall, open radially all round, with ribs only 1.5 mm deep, so a support ring there is reachable and removable, and the tyre hides any scars. For Ø43 flanges the lip must be supported.

Rejected mesh fix: a 45° cone under the lip. It's self-supporting, but it turns the retaining wall into a ramp the tyre can climb, which defeats v6.

**v6.2 mesh** (base v6.1, everything else identical), done so that with support allowed on the part nothing lands anywhere awkward:
- Pad behind the nut extended up into the web, z 3 → 16.0 (was 13.5). This removes a 25 mm² overhang whose support would have landed on the pad top 13 mm inside the hub, and it's stiffer.
- Drum access hole Ø6 → **Ø6 teardrop** (45° roof). This removes ~7 mm² of slivers that would land inside the hole.
- Watertight, 1 body, 9708 facets, 13 716 mm³ → **14.3 g ABS**. 0 / 11 692 containment samples differ from v6.1 outside those two zones.

Overhang landing map (every < 30° facet raycast down):

| Z | Area mm² | Lands on |
|---|---|---|
| 2.5 | 38.9 | plate |
| 3.0 | 27.4 | plate |
| 15.5 | 443.6 | plate |
| 28.0 | 444.4 | bottom flange top face (Z 1.0), open tyre seat, removable |

Nothing else. The nut slot (gable) and screw hole (teardrop) generate no overhang.

## Assembly (v6.2)

1. Drop an M3 hex nut (or a 5.5 × 1.8 square nut) into the slot from the motor face.
2. Start the M3 × 10 grub through the drum hole to catch the nut.
3. Fit the tyre, then the wheel onto the shaft with the flat under the screw, and tighten onto the flat.
4. Motor + wheel into the v13 carrier, see `../chassis/v11/CARRIER_V13_CHANGE.md`.

## Open / if it misbehaves

- Round bore is still Ø4.10 (CAD). The new motor pair's shaft measures Ø3.99, and the 4.05 bore coupon hasn't been printed. The tighter flat is what took out the slop.
- Flat too tight in ABS: one file stroke on the bore flat, next rev 1.48.
- Nut won't drop in: the slot is 5.8 × 2.7 nominal and ABS shrink could eat ~0.1–0.2, next rev +0.2.
- Ring width after trim is still unmeasured.
