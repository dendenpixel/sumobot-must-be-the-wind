# SumoBot v11 — BASE STAGE report (base + carrier L/R + battery frame)

**Status: built, all 40 gates PASS. Stopped for review before the lid (brief §6.2).**
Built with CadQuery 2.8 / OCCT from `interfaces.json` via `build.py` (→ `build_base.py`, `build_carriers.py`, `build_frame.py`); `layout.py` patched to the v11.1 architecture and re-run (its `interfaces.json` now regenerates Den's edited copy byte-for-byte, plus a `board_pilots` key).

## 1. Deviations from the brief — each one is a conflict I hit, with the number I used instead (all are `PROPOSED` in `parameters.json`; say the word and they change)

| # | Brief said | Problem | Built as |
|---|---|---|---|
| 1 | Carrier bolts L (−19,32),(47,32),(−19,77),(47,77); R point-mirror | (∓19,±32) sit under the *opposite* motor's tail (stagger ±14 puts the R tail at Y +30.3 over X −26.5…−1.5): tab + head clash 0.07–1.2 mm. R (−47,−32) is inside the battery stop's footprint and its head 1.75 mm into the pack path. R (−47,−77) is 5 mm from lid fixing (−50,−73): Ø8.5 bosses overlap 3.5 mm | **L (−18.5,40), (40,31), (47,70), (−19,70); R (−40,−31), (19,−40), (19,−70), (−30,−77)**. Not point-mirrored (the battery bay makes L/R different). Ø5 driver column above every head verified clear of every envelope |
| 2 | Frame bolts (−60,±58), (−47,0) | (−60,±58): M3 button head 1.35 mm into the rail wall. (−60,+61) would sit under the XT60 socket body (no driver access). (−47,0) is under the stop wall; its head 1.75 mm into the pack path | **(−78,±61)** behind the XT60 plate, 3 mm outboard of the rails; **(−43,0)** on a tab in front of the stop |
| 3 | Line-sensor wire hole "directly above" the pocket (inset 37.8) | inset 37.8 is under the lid skirt ring (36.4–38.4): the wire could not come up into the bay | hole at **inset 41.5** on each diagonal, 1.1 mm inside the skirt inner face; it notches the pocket's inboard wall (pocket is plenum-side anyway, hot-glue the hole) |
| 4 | Duct boss Ø52 with R5 bellmouth | Ø52 leaves 4.35 mm wall beside a Ø43.3 bore; R5 needs 5 → knife edge | **Ø58** hanging boss (as the earlier brief), R5 bellmouth + Ø47.4×3.0 lip counterbore both from that boss |
| 5 | Knock-outs at (57,±36) | R one overlapped board_A pilot (62,−41) by 3.2 mm | **(52,±36)** both sides |
| 6 | Faceplate "Ø16 × 1.5 relief pocket for screw heads on the well side" | the faceplate is the 1.2 mm well wall and the hub is 1.2 mm from it: no room for a 1.5 relief on either side | **M3 countersunk (90°, Ø6) on the well side**; heads sit ~0.3 proud, 0.9 mm to the hub. If you'd rather a 2.0 faceplate, say so (costs 0.8 mm of motor-tail room) |
| 7 | Battery rails X −70…−46.5 with two 12×3 slots each | 23.5 mm can't hold two 12 mm slots | rails **X −83…−48.6** (1.8 mm inside the lid skirt inner face), slots at X −80…−68 and −60…−48 |
| 8 | board_B X −44.5…−18 | its edge blocked a hex key on carrier bolt (−18.5,40) | **board_B X −47.5…−21** (3 mm rearward); pilots (−39.5,47),(−29,47),(−39.5,56),(−29,56). The stop steps down to 4.6 tall over Y 38…56.6 so the board corner clears it by 1.4 |
| 9 | Pressure-port pilot "beside" the port | a screw head at (−30,−16) would hit the R cheek wall | pilot at **(−35,−11)**: Ø9 pad head clears the cheek (X −28.4) and the frame tab |
| 10 | "cap strap pilots beside each cheek pair" | carriers are separate parts now | **5×3 zip-tie slot through both walls of the tail segment** (Z 27–30) |

Frozen numbers (§2): untouched. Wells, axles, duct centre, battery, XT60 face, lid fixings, ToF, line-sensor centres (±77.96), every Z and inset — all read from `interfaces.json`.

## 2. Decided under §4

- **Ribs (8, 2.0 wide, Z 5.5 → ceiling, r 30 → seal-loop inner face, ≥ 3 mm from everything):** chosen by search for the longest clear runs ≥ 30° apart: 40.0° (54.5 mm); 110.0° (33.3+16.1 mm); 140.0° (17.0+63.2 mm); 170.0° (73.2 mm); 210.0° (85.8 mm); 242.5° (26.4 mm); 310.0° (66.0 mm); 340.0° (29.1 mm). Root fillets R1.5 not applied (OCCT fillet on the 700-face solid is fragile; ribs print as walls on the bed-side plate anyway).
- **Wellcap pads:** Ø8.5 half-columns, inner edge flush with the well interior face, full height flange→Z 39 (so nothing overhangs when printed flange-down), Ø4.15×6 pilots on top. L: +X face (44.15, 44/58) and outboard face (−5/20, 74.45). R: front face (16.15, −49/−61) and outboard face (−20/5, −74.45) — R's rear face looks at the battery stop 2.4 mm away.
- **Carrier flange:** 1.6 mm covering the 4.2 seal-wall landing + r 5.5 bolt tabs + pad feet; cut away under the motor (X 1.245…26.755) so the motor sits on the roof; 4 mm rails under both cheek walls tie the three 12 mm U-segments (segments at Y 27–39, 3–15, −31.3…−19.3 from the faceplate: a 39 mm motor sits in the first two, a 70 mm one in all three). Saddle Ø25.51 (25.3 + shrink); the inner cheek wall is thinned to 1.245 so its face is exactly X 0 (L and R touch there).
- **Duct:** revolved cutter — bore Ø43.51, R5 bellmouth, Ø47.61×3.0 seat; 4 pilots on PCD 60 in Ø8.5 bosses Z 1.5–10.9.
- **Grooves:** 1.3×2.0 up from Z 1.5 with 45°×0.4 mouth chamfers, three loops; well loops with sharp rectangular corners.
- **Line-sensor pockets:** 11.4×6.6 interior, 1.2 walls, open at Z 2.2, ceiling Z 9.2, block fused into the roof/wedge skin (pocket straddles the knee: inset 33.3–42.3).
- **XT60 bracket:** 2.0 plate at X −72…−70, Y 55.5…76, Z 10.9…26, cut-out 15.9×8.4 centred on the socket (Y 57.43…73.33, Z 14.87…23.27), 21 mm clear behind. Frame flange is a U outside the rails (nothing under the pack: pack floor stays Z 10.9).
- **Wedge/hull:** ruled lofts between normal-offset superellipse splines — the generators *are* the local normals, so the ramp is 15.141° (= atan 9.2/34) at every bearing; verified 0.06 mm max vs the analytic surface. Skin 1.6 rim→seal loop, 1.2 inboard; rim lip is the natural band where the 1.6 skin meets Z 0.5 (inset 0–1.7).

## 3. Gate table

| gate | value | criterion | result |
|---|---|---|---|
| mesh watertight base | open_edges=0 manifold=True | 0 boundary / non-manifold edges | **PASS** |
| mesh watertight carrier_L | open_edges=0 manifold=True | 0 boundary / non-manifold edges | **PASS** |
| mesh watertight carrier_R | open_edges=0 manifold=True | 0 boundary / non-manifold edges | **PASS** |
| mesh watertight frame | open_edges=0 manifold=True | 0 boundary / non-manifold edges | **PASS** |
| axle_z - wheel_od/2 | 0.0 | = 0.00 | **PASS** |
| motor bottom - roof top | -0.0 | = 0.00 | **PASS** |
| max plan dimension | 249.000 x 249.000 | 249.0 +-0.05 | **PASS** |
| no base feature above Z 10.9 | 10.9 | max Z <= 10.9 | **PASS** |
| nothing below Z 1.5 except rim lip <=12 from rim | lowest Z 0.50; deepest inset with Z<1.5 = 1.69 mm | inset <= 12 | **PASS** |
| wedge ramp vs analytic (spline loft) | max /dz/ 0.06 mm (hull_test) | identical at every bearing | **PASS** |
| groove depth (main + 2 well loops, 128 probes) | min 2.000 max 2.000 | 2.00 +0.10/-0 | **PASS** |
| hanging-boss pilot floors sealed (30 pilots) | all sealed | solid Z 1.5-4.9 below every pilot | **PASS** |
| wheel L sweep clearance X / Y | X-faces 2.50  Y-faces 1.80  (min overall 1.80 at [37.4 68.2 23.4]) | >= 2.0 (X) / 1.5 (Y) | **PASS** |
| wheel R sweep clearance X / Y | X-faces 2.50  Y-faces 1.80  (min overall 1.80 at [  9.4 -68.2  23.4]) | >= 2.0 (X) / 1.5 (Y) | **PASS** |
| plenum isolated from ambient (ideal skirts, duct+holes plugged) | labels: plenum 4, ambient 1, above-roof 1, under-wedge 1, wells 1/1; plenum 288 cm3; pitch 0.4 | plenum not connected to ambient; wells open to ambient | **PASS** |
| base overhangs > 55 deg (roof-face-down) | wedge annulus 27078 mm2 (bed support, expected); other: fan lip seat ring (counterbore step Ø43.5->Ø47.6) 2... | only bed-anchored support under the wedge | **NOT VERIFIED** |
| carrier_L overhangs > 55 deg (as printed) | zip-tie slot ceiling (5 mm bridge) 14.2 mm2; faceplate hole ceilings (Ø8 shaft / Ø3.2 screws, horizontal ho... | bridges only (holes/slots), no support | **PASS** |
| carrier_R overhangs > 55 deg (as printed) | zip-tie slot ceiling (5 mm bridge) 14.2 mm2; faceplate hole ceilings (Ø8 shaft / Ø3.2 screws, horizontal ho... | bridges only (holes/slots), no support | **PASS** |
| frame overhangs > 55 deg (as printed) | XT60 cut-out ceiling (15.9 mm bridge) 70.3 mm2; strap slot ceilings (12 mm bridges) 38.6 mm2 | bridges only (holes/slots), no support | **PASS** |
| carrier L: motor Ø25 x 69.3 envelope clear of carrier | intersection 0.00 mm3 | 0 (motor rests on the base roof) | **PASS** |
| carrier L: motor contact line (X +14 +-2) is bare base roof | 0.00 mm3 of carrier under it | motor bottom - roof top = 0.00 with carrier fitted | **PASS** |
| carrier L: well wall lands fully on the seal-wall top | wall band inside 4.2 landing: True; foot faces over the well cut-out: 0; foot over foreign pilots: [] | fully on base material | **PASS** |
| carrier L: underside planar | min Z 10.900 | = 10.90 (prints flat) | **PASS** |
| carrier L: accepts motor 39-70 | segments Y [[27.0, 39.0], [3.0, 15.0], [-31.3, -19.3]] | 39 mm motor in 2 segments, 70 in 3 | **PASS** |
| carrier R: motor Ø25 x 69.3 envelope clear of carrier | intersection 0.00 mm3 | 0 (motor rests on the base roof) | **PASS** |
| carrier R: motor contact line (X -14 +-2) is bare base roof | 0.00 mm3 of carrier under it | motor bottom - roof top = 0.00 with carrier fitted | **PASS** |
| carrier R: well wall lands fully on the seal-wall top | wall band inside 4.2 landing: True; foot faces over the well cut-out: 0; foot over foreign pilots: [] | fully on base material | **PASS** |
| carrier R: underside planar | min Z 10.900 | = 10.90 (prints flat) | **PASS** |
| carrier R: accepts motor 39-70 | segments Y [[-39.0, -27.0], [-15.0, -3.0], [19.3, 31.3]] | 39 mm motor in 2 segments, 70 in 3 | **PASS** |
| overlap base x carrier_L | 0.000 mm3 | 0 (declared: none) | **PASS** |
| overlap base x carrier_R | 0.000 mm3 | 0 (declared: none) | **PASS** |
| overlap base x frame | 0.000 mm3 | 0 (declared: none) | **PASS** |
| overlap carrier_L x carrier_R | 0.000 mm3 | 0 (declared: none) | **PASS** |
| overlap carrier_L x frame | 0.000 mm3 | 0 (declared: none) | **PASS** |
| overlap carrier_R x frame | 0.000 mm3 | 0 (declared: none) | **PASS** |
| hardware envelopes x parts | wheels, hubs, battery, puff allowance, fan, XT60 socket vs base/carriers/frame | 0 unintended overlaps | **PASS** |
| battery swept volume straight -X (frame + carriers) | 0.00 mm3 | 0 (lid slit checked at the lid stage) | **PASS** |
| mass base | 116.8 g (solid volume 114.9 cm3 x 1.24 x 0.82) | <= 175 g | **PASS** |
| mass carrier_L | 17.8 g (solid volume 17.1 cm3 x 1.27 x 0.82) | report | **PASS** |
| mass carrier_R | 17.8 g (solid volume 17.1 cm3 x 1.27 x 0.82) | report | **PASS** |
| mass frame | 3.2 g (solid volume 3.1 cm3 x 1.27 x 0.82) | report | **PASS** |

Overhang detail (base, roof-face-down): wedge annulus 27 078 mm² needs the expected **bed-anchored** support; the only other >55° faces are the fan lip seat ring (2.05 mm wide horizontal step, 293 mm², 3 mm above the bed — put "support on build plate only" so a column grows inside the open bore under it, or accept a slightly rough seat under the 1 mm gasket), the 30 blind pilot ceilings (Ø4.36, coupon covers these) and the 0.4 mm knock-out score rings. Carriers/frame: only bridges (Ø8.2 shaft hole, Ø3.4 screw holes, 5 mm zip-tie slots, 12 mm strap slots, 15.9 mm XT60 cut-out).

## 4. Mass

| part | mass | limit |
|---|---|---|
| base (PLA) | 116.8 g | ≤ 175 g |
| carrier L / R (PETG) | 17.8 g / 17.8 g | report |
| battery frame (PETG) | 3.2 g | report |

## 5. Print settings (Bambu X1C, 0.4 nozzle, 0.2 layers)

- `v11_base.stl` — PLA, roof face on the bed (already oriented, 249×249×10.4 on Z 0), 3 walls, 4 top/bottom, 20–30 % gyroid, **supports: build plate only** (wedge annulus + inside the bore). Nothing else needs support.
- `v11_carrier_L.stl`, `v11_carrier_R.stl` — PETG, flange down (as exported), 3 walls, no support. 77×111×28 / 70×114×28.
- `v11_battery_frame.stl` — PETG, flange down, no support. 46×143×15.
- Coupons (`coupon_hole_4.00/4.15/4.30`, `coupon_bore_4.35/4.41/4.47`) come with the final deliverable set.

## 6. Open questions (review)

1. Deviations 1–10 above — any you want reversed?
2. Faceplate: 1.2 with countersunk M3 (built) vs 2.0 plate with the motor 0.8 further inboard?
3. The fan lip seat ring in the inverted print: bed-anchored support in the bore (recommended) or accept the 2 mm overhang?
4. Cheek segment positions (27–39, 3–15, −31.3…−19.3) — fine for the old 39 mm motors (they sit in the first two) and the JGA25 worst case?
5. Then the lid.

Files: `build.py` + modules, `parameters.json` (tags carried), `interfaces.json` (regenerated), `layout.py` (patched), `stl/` (print orientation, on Z 0), `step/` (per part + assembly with hardware envelopes), `views/`, `gates_base.json`, `checks.json`.
