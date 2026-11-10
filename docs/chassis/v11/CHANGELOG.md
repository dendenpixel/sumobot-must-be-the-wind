# SumoBot chassis — changelog

Append-only. Newest at the bottom. Each entry: what changed, why, Den's verdict.

## v10 (Astra, 11 Sep 2026) — rejected

Built from a reviewer's audit prompt with no shape spec. Result: 240 mm octagon slab, rim at Z 2.2, 4.6 mm ramp, vertical-walled box lid, wheels outboard in taped-on guards, ToFs bolted outside the front face, electronics on a Z 38 tray, both pitch skids on one side, 53 STLs. Kept the good process parts (CadQuery pipeline, provenance tags, 3D pressure flood test, straight-slide battery). Den: "not the shape I want." Full diagnosis: `../v10_POSTMORTEM_and_prompt_spec.md`.

## v11 layout (12 Sep 2026) — approved, solids not yet built

- Shape: sombrero restored. 249 × 249 superellipse (n=4, a=124.5), 15.13° wedge, rim Z 0.5, knee inset 34 at Z 10.9, tower lean 7.5°, lip 4.5 at Z 53, flat top Z 65.6.
- Why 249 not 240: at 240 the rear battery bay was ~6 mm short of the lid curve.
- Motor stagger ±14 kept: 69 mm JGA25-371 motors can't be collinear inside the knee (25 mm overlap). Faceplate at |Y| 39 → 7.5 mm tail gap.
- Duct at (57, 0), collar Ø52, PCD 60, clamp ring Ø56 + ears (EDF ear cut off). Fan lip seats on the collar top → fan top Z 60.
- Battery on the roof (not sunk), rear, slides out through a Y −58…+75 slit; sunk tub couldn't clear the wedge.
- XT60 loop key base-mounted rear-left facing backwards, in the slit opening.
- Comparator boards deleted: bare TCRT5000 → ADC1 on S3 GPIO 1/2/3/10.
- TTGO is a **T-Display ESP32-S3** (found 12 Sep). Doesn't fit on the roof; sits on the −Y wellcap top under a window. Lid keeps the PCF8574 (7 XSHUT + button) → one 4-wire plug.
- 7 ToFs: front 0/±25 (Z 48), sides ±90 (Z 48), rear 180±25 (Z 50).
- Line sensors at inset 28 on the diagonals (±84.9, ±84.9) in downward pockets in the plenum ceiling.
- Tyre width 27 (trimmed) → well_y 31. Lid fixings (70,70) (−46,72) (−50,−73) (70,−70).
- No scraper blade, no skids, no ballast pockets.
- Checker: 0 overlaps, 0 outside-curve, 1 near-miss (front ToF pocket ↔ fan keep-out 0.53 mm, on SELLER fan OD).
- Den's verdict: "that's the rough shape I'm looking for"; asked for TTGO on the base (done).

## v11 update (12 Sep 2026, later) — TTGO measured

- T-Display S3: 62.3 × 25.65 × 6.88 (14.6 with header pins), buttons 14 mm apart at the USB-C end. Envelope in `layout.py` updated; window 64.3 × 27.65.
- Mount: pins down, clipped to ~4 mm, hanging between two 4.5 mm rails printed on the −Y wellcap top; wires soldered to the stubs. No protoboard under it (a socket + protoboard stack would reach Z 75 against a Z 64 ceiling). 3.4 mm clearance to the flat-top underside.
- Checker: still 0 overlaps / 0 outside / 1 near-miss.

## v11 preflight (12 Sep 2026, evening) — two conflicts from the CAD session, resolved

Astra ran `layout.py` and stopped with two real conflicts before building:
1. **Line sensors vs wedge skin** — 7.0 mm body top at Z 9.2 vs the skin underside at Z 8.08 (inset 28). Fix accepted: sensors moved to **(±78, ±78)** = RIM INSET 37.8, under the flat roof plate (underside Z 9.7). Costs ~10 mm more detection lag; no pods.
2. **Roof-on-bed vs integral well walls** — well walls to Z 39 and cheeks to Z 33 would sit 28 mm below the bed when the base is inverted. Astra proposed a 28 mm bed-anchored support forest under the whole roof and wedge — **rejected** (print quality on the wedge, time, mass). Fix: **the base has nothing above Z 10.9.** Well walls + faceplate + cheeks become two bolt-on **motor/well carriers**; rails + stop + XT60 bracket become one **battery frame**; the fan lip seat is recessed into a boss hanging below the roof (fan top Z 60 → 56.9); the collar is deleted (lid locates on its 4 bolts). All carriers print right-way-up with no support. Part count 5 → 8 printed parts (+ hubs). This is the same conclusion the v10 handover reached about a "removable motor/well upper carrier" — v10 was right about that one thing.
- Checker after the change: 0 overlaps, 0 outside-curve, 1 near-miss (unchanged).

## v11 interface pass 2 (12 Sep 2026, night) — five conflicts from the CAD session, resolved

Astra's OCCT clash check found: wire holes under the lid skirt; carrier/frame bolts through the motors, battery and a lid lug; motor bodies overlapping the faceplate wall (and a 1.5 relief in a 1.2 wall); R5 bellmouth mouth Ø53.5 > Ø52 boss; two 12 mm slots in a 23.5 mm rail.
- Wire holes moved to (±69, ±79) via short underside channels.
- Carrier mounts re-placed (L: (−19, 37.8), (42, 33), (−19, 78), (39, 78); R point mirror); battery-frame front bolt (−42, 0).
- **Faceplates moved outboard 1 mm: outer face |Y| 40, motors seat on the inboard face at |Y| 38.8** → encoder tail gap 8.3 (3.3 after the connector). Wells Y 40…71, wheel centres ±55.7, track 111.4. No relief pocket; two Ø8 × 1.5 pads with 90° countersinks for M3 flat-head screws (head Ø6 max — new hardware requirement). Shaft engagement 6.6 mm on the flat.
- Fan seat boss Ø52 → **Ø56**.
- Rails extended to X −76…−46.5; XT60 socket +0.4 to Y 58.0.
- Checker: 0 overlaps, 0 outside-curve, 1 near-miss (unchanged).

## v11 base stage BUILT (13 Sep 2026) — Astra output in SumoBot_v11_base_stage/SumoBot_v11_build; Den printing the base

- Built from the first revised brief plus Astra's own conflict fixes (it did not receive interface pass 2 before building). All 40 gates PASS. Base 116.8 g, carriers 17.8 g each, frame 3.2 g.
- As built (these now override earlier entries): faceplate outer face |Y| **39**, motors seat at 37.8 (encoder tail gap 6.3 → ~1.3 after the connector — **measure the connector when the motors arrive; if it doesn't fit, only the carriers reprint**); fan seat boss **Ø58**; knock-outs **(52, ±36)**; wire holes at **inset 41.5** on the diagonals; carrier bolts L (−18.5,40) (40,31) (47,70) (−19,70), R (−40,−31) (19,−40) (19,−70) (−30,−77) — not point-mirrored; frame bolts **(−78, ±61), (−43, 0)**; rails **X −83…−48.6**; board_B X −47.5…−21; pressure-port pilot (−35,−11); countersunk M3 on the faceplate; 5×3 zip-tie slot in each carrier tail segment.
- Flag for the lid stage: frame bolt (−78, −61) sits where the lid skirt lands (the rear slit only opens Y −58…+75) — the skirt or the bolt has to move.
- TCRT5000 measured 13 Sep: bare body 10.01 × 5.6, 9.27 above the module PCB (includes leg standoff; bare body ≈ 7). Pocket 11.4 × 6.6 × 7.0 fits; legs bend up the end faces.
- `layout.py` here updated to the as-built numbers.

## v11 lid stage BUILT (13 Sep 2026) — Claude in Cowork, on Astra's code base; output in SumoBot_v11_base_stage/SumoBot_v11_build (zip SumoBot_v11_lid_stage.zip)

- Lid, wellcap_L/R, clamp ring built; 60/61 gates PASS (`gates_lid.json`). Lid **128 g est.** (target ≤ 110 — the one FAIL; structure total ≈ 259 g still under the 267 g v5 figure), caps 5.5 g each, ring 3.0 g. Full report: `REPORT_lid.md` (also project doc SumoBot_v11_LidStage_Report.md).
- **ToF geometry changed** (the brief's recessed facets hit the fan, the wellcaps and the lug driver bores): each sensor is a **nose** proud of the tower at RIM INSET ≥ 36.2 (never proud of the lip), roof = lip underside Z 53, optical axis **Z 39.9**, pocket 12 × 26 × 4.5 open to the inside, slot 14 × 7.6. Final facet centres: F0 (88.30, 0) · F±25 (82.97, ±64.38) skew 12.7° · L90 (−25.17, 88.10) · R90 (32.10, −87.91) · B±25 (−81.43, ±72.14). `interfaces.json` `tof` updated; the Z-48 layout-pass points are superseded (kept under `tof_layout_pass_superseded`).
- Battery slit now Y ±62 full height (Z 10.9–34) + low extensions to Z 24.6: Y 62…75 (XT60 key) and Y −64…−62 (frame bolt (−78,−61) head) — resolves the base-stage flag.
- Button (−38,10) → **(12, 22)**; alarm pocket Y 20…47; **gland deleted**; **group-panel recess deleted** (unprintable on the bed face; label position kept); lugs 10 wide / 4.8 inboard with Ø7 driver bores through the top; wellcaps have plain tops (TTGO/ESC rails pending the header decision).
- Build lessons in REPORT_lid.md §6 (OCCT: fuse plain solids first, cut hollows one at a time; stacked glued lofts for the lip).
- Open: hubs (Den); encoder connector vs 1.3 mm tail gap; TTGO header pins; lid mass levers (wall 2.0 → 1.6, skin 1.6 → 1.2) if Den wants the 18 g.

## v11 wheel hub v4 (14 Sep 2026)

- Base file is the 29-long v3 hub (Ø39 flanges), not the Ø40 × 34 "v3" in WHEEL_V3_CHANGE.md. Mesh-edited, watertight, `sumo_wheel_hub_v4.stl`.
- Flange Ø39 → **Ø40** (lip over the bead ribs ~0.5 → ~1.0, cast ring was bulging over), length 29.0 → **28.9** (rubbing the well wall), **2 × Ø4.5 axial driver holes at r 8.5 on ±y (17.0 c-c)** so the faceplate M3s can be driven through the hub. 17.0 g PLA.
- Assembly order this enables: open the well to the top, bench-assemble motor + wheel + grub, drop in as a unit, drive both M3s through the hub. No spacer.
- Open: bore fit untested (coupon Ø3.95 / 4.05 / 4.15 next). If the real screws are Ø5.5 pan heads the holes go to Ø6.

## v11 wellcap +2 mm (14 Sep 2026)

- `v11_wellcap_L/R_plus2.stl`: every vertex above z 1.25 shifted +2.0 (tyre was rubbing the cap ceiling). Skirt 7.5 → 9.5, overall 8.7 → 10.7, head pocket 2.1 → 4.1, same screws and engagement, +0.5 g each.
- Cap roof in the robot rises Z 48 → 50. **Check the lid inner surface clears the new cap top (~Z 51.2) — needs ≥ Z 52 over the wells.** Not yet verified.

## Print presets (14 Sep 2026)

- Bambu Studio 02.08.02.61 imports a `.bbscfg` zip (printer json + process jsons + bundle_structure.json). Envelope rules in `docs/printing/BAMBU_PRESET_RECIPE.md`; two earlier attempts failed on the `version` field format.
- Four process presets: Lid PETG SupIF, PLA Parts Plate, Wheel Hub PLA, Wheel Hub ABS. Lid profile detail in `docs/printing/LID_PRINT_PROFILE.md`.

## Repo catch-up (14 Sep 2026)

- Everything from 6–14 Sep (measured parts, v10/v11, wheels v2–v4, wellcap, presets) had been living only in my project notes. Brought into `docs/` on branch `docs/v11-chassis`. CAD build files (`build.py`, STEP/STL) still to come from my local CAD folders. `docs/PIN_MAP.md` and the firmware config were for the wrong chip (classic ESP32, board is a T-Display S3) at this point.

## v12 carriers + hub v5 (15 Sep 2026) — drop-in motor/wheel unit

- Mesh-edited from `v11_carrier_L/R.stl` and `sumo_wheel_hub_v4.stl` (manifold booleans, all watertight). Files `v12_carrier_L.stl`, `v12_carrier_R.stl`, `sumo_wheel_hub_v5.stl`. Full numbers in `CARRIER_V12_CHANGE.md`; the hub has its own record in `../../wheels/WHEEL_HUB_V5_CHANGE.md` and print settings for both parts are in `../../printing/PRESETS_v5hub_v12carriers.md`.
- Carrier: faceplate **slotted downward** (8.2 wide, bore centre → Z 0) so a pre-assembled motor + hub + tyre drops in with the carrier upside down on the bench; base roof closes the slot; bore top stays intact to carry the wheel load. Two **Ø6.5 driver holes through the outer well wall** at (5.5, 12.5) and (22.5, 12.5), coaxial with the faceplate holes. Wellcap boss at (20, 74.46) **undercut** (solid from Z 16.5, 45°) because it sat in front of the x 22.5 hole — wellcap unchanged. 17.8 → 15.8 g each.
- Hub v5: driver holes Ø4.5 → **Ø6.5** (the faceplate is countersunk → M3 flat-head, head Ø5.5–6 must pass through the hub), keyholed into the counterbore so no 0.5 mm sliver is left. 17.0 → 16.5 g. **Supersedes v4.**
- Den sketched the slot going up; changed to down for the load path and sealing reasons above. Den's verdict on the plan: "go ahead".
- Tape over the two outer-wall holes after assembly: well and bay are both ambient, so it's grit control only, zero downforce cost.
- **Open, blocks nothing but check before printing the hub:** motor tapped-hole axis vs the D-flat (need 3/9 o'clock with the flat up; 12/6 means the hub holes move). Bore-fit coupon still unprinted. Driver: ≥ 40 mm shaft under Ø6.
- **Closed 17 Sep by measurement** (`../../hardware/MEASURED_PARTS.md` §2.1): tapped-hole axis reads **3/9 with the flat at 12** — hub v5 needs no change; new motor body is **58.84** not 65, tail gap 16.76, so the **v12 carriers need no reprint** either.

## v11 battery frame v2 — rear snap fingers (15 Sep 2026)

- `v11_battery_frame_v2_clip.stl`, mesh-edited from `v11_battery_frame.stl` (watertight, 3.47 g est., bbox 50.00 × 142.53 × 15.06). Everything outside the rear 15 mm of each rail is byte-identical to v1. Full numbers in `BATTERY_FRAME_V2_CHANGE.md`.
- Why: v1 printed and the sideways rattle is fine (1.85 mm per side), but the pack **slides fore-and-aft in X** — the rear is open for the slide-out and v1 relied on the strap for everything.
- Change: the rear strap tunnel on each rail is deleted and replaced by a **cantilever snap finger** — 1.2 mm arm, ~17 mm free length, square hook catch face at X −83.0 (0.5 mm play on the pack rear face), 45° lead-in ramp, hook tip overlapping the pack edge by 1.2. Front strap tunnel kept, so one strap per side still does the Z hold-down. +Y gains a block tying the XT60 bracket's inner post to the plate now the rail bar under it is gone; it doubles as the finger's over-travel stop.
- Numbers: 1.65 mm deflection to pass the pack, strain ≈ 1.0 % (PETG yields ~5 %), ≈ 0.9 N/mm per finger → ~2 N push through the ramp. Interference checks both sides: pack envelope **0 mm³**, swept finger vs the rest of the frame **0 mm³**.
- **Pack orientation is now load-bearing: leads toward the XT60 bracket end (+Y)**, matching the stop wall's notch and Board A rear-left.
- The print preset that was actually built is **PLA, not the PETG this change specs** — spring rate goes ≈0.9 → ≈1.5 N/mm, yield margin ~3× instead of ~5×, and PLA creeps if left deflected and softens near 55 °C beside the battery and motors. Preset and the full consequence in `../../printing/PRESETS_battery_frame_v2_PLA.md`. If the fingers feel brittle, reprint in PETG — the geometry is not the problem.

## EDF mount v2 — fan seat + clamp ring against the measured fan (17 Sep 2026)

First measurements of the XFly 1413 (qty 1, no spare). **This entry was rewritten after an adversarial review found four errors in the first draft; the superseded claims are listed at the bottom so the reasoning trail survives.**

**Measured, literal:** flange OD **47.71** repeated on rotation (an earlier reading gave 47.81). Flange thickness **3.31 / 3.35 / 3.40 / 3.50** — spread 0.19, exceeds the 0.10 rule. Duct OD **42.75** below the flange, **42.85 / 42.87** further up; the duct deflects ~0.15 under caliper pressure. Duct section height **26.44**, datum not stated. Motor assembly past the duct: 5.05 gap + 18.83 motor + 3.6 nub = **27.48**, measured 27.5 in one shot. Flange underside flat, not filleted. A moulded mounting ear is visible on the duct wall in the 17 Sep photos, separate from the flange.

**The governing insight: the seat floor is not a precise datum.** `REPORT_base_stage.md` §3 records it as a >55 degrees down-facing annulus 2.05 mm wide printed 3 mm above the bed — "accept a slightly rough seat". Add elephant's foot on the roof face and a `hole_shrink` of 0.21 extrapolated from a 4.15 coupon to a 47 mm feature, and the realistic as-printed seat depth is **2.8–3.4, not 3.0**. Every clamp number keys off it.

**Consequence: a 1 mm gasket cannot span the stack.** Compressed thickness is `c = relief_depth + seat_depth − flange_thickness`. Across seat depth 2.8–3.4 and flange 3.31–3.50 there is **no relief depth that keeps a 1 mm gasket both in contact and under 50 % compression** — capping the maximum at 45 % loses contact at the other corner; guaranteeing 15 % minimum goes solid at the other. The compliant element needs stroke, not precision.

**Changes (Den's authority, 17 Sep):**

| Item | Was | Now | Reason |
|---|---|---|---|
| Fan seat bore, modelled | Ø47.61 | **Ø48.26–48.31** | 47.81 worst-case flange + 0.24 per the project's own bore policy + 0.21 shrink |
| Fan seat bore, **hand-reamed** on the printed base | ≈47.4 | **48.05–48.10** | a reamed hole *is* the physical size — the 0.21 shrink term does not apply to hand work. Tighter also protects the front-ToF near-miss, which goes to zero at 48.3 |
| Fan seat depth | 3.0 | **3.0 — unchanged, no depth cut** | the flange must stand proud for the ring to grip, and the bellmouth tangent at Z 6.50 leaves only ~1.0 mm of travel anyway |
| Compliant element | 1 mm silicone, ID 44 / OD 52, under the flange | **3 mm EPDM** (or 3 × 1 mm silicone stacked), **ID 43.5 / OD 47.0**, **on top** of the flange | OD 52 never fitted a Ø47.61 pocket — it is left over from the deleted Ø52 collar. 3 mm gives the stroke to absorb the seat-depth band. ID 43.5 captures on the duct so it self-centres. Above the flange it costs zero lid headroom |
| Clamp ring thickness | 3.0 | **4.4** | to carry a 2.4 relief and still leave a 2.0 web |
| Clamp ring underside relief | Ø48.4 × 0.8 | **Ø50.0 × 2.4** | Ø50 leaves 0.95 mm of roof land against a 48.1 ream; 2.4 holds compression to **17–43 %** across the full seat-depth and flange-thickness box |
| Screws | M3 × 12 | **M3 × 8** | usable insert engagement is ~5.7 mm; M3 × 12 bottoms out ~4 mm early, which feels tight while clamping nothing |
| Screw torque | not specified | **snug, ≤ 0.2 N·m** | the counterbore floor is PETG and creeps; the gasket needs only ~50 N per screw |
| Ring OD 56 / ID 44.5, ears Ø9.5 on PCD 60 at 45/135/225/315°, Ø3.4 holes | — | **unchanged** | still correct against the measured fan |

All ring depths are integer multiples of a 0.20 mm layer (4.4 = 22 L, 2.4 = 12 L, 1.6 counterbore = 8 L) so slicing cannot shift the preload.

**Do not cut the fan's ears.** The plan of record (`LAYOUT_PASS.md` decision 3) was to cut them off, but the ear sits on the duct wall well above the flange and the ring is only 4.4 tall, so it probably never touches. Test-fit first; if it does foul, notch the ring — the ring is reprintable and the fan is not.

**Reprint:** clamp ring only. **Hand work:** seat bore ream, *after* the heat-set inserts are in, so insert heat cannot move a hand-cut datum. **Cut:** gasket from 3 mm EPDM.

**Still open — fan height, and it gates the ream.** Overall height from the flange seating face is either **53.92** or **57.42** depending on the 26.44 datum. Against a lid inner surface at Z 64.0 that is 2.18 mm of clearance or a 1.13–1.32 mm collision. The seat can give back at most 1.0 mm before cutting the R5 bellmouth (tangent verified at Z 6.50), so case B means a lid reprint with a raised blister over the grille. **One bench-to-nub-tip caliper reading resolves it, and it must be taken before anything is reamed** — resolving it by fit check would require performing the irreversible operation first. Threshold: H < 54.1 proceed as specced · 54.1–56.1 fits but under the ≥2 mm spec · H ≥ 56.1 lid change.

**Built and gate-checked (17 Sep, CadQuery 2.8 / OCCT 7.9, 64 gates PASS).** Single watertight solid, Euler −8 = genus 5, four through-features. Measured on the real B-rep, not asserted: relief 2.4000, web 2.0000, material under each ear counterbore 2.8000, bore 44.5000, holes Ø3.4000 at r 30.0000 on 45/135/225/315.000°, bbox 56.00 × 56.00 × 4.400, across-ears diagonal 69.5000. Clearances: flange 1.095, duct 0.815, roof land 0.950. **Mass 4.68 g nominal / 4.56 g shrink-compensated** (was 3.0 g at v11), against a ≤10 g gate. **Print the shrink-compensated variant.**

Gasket compression verified across the whole 16-cell box (seat depth 2.8–3.4 × flange 3.31–3.50): **17.00 % to 43.33 %**, every cell inside (0, 50). Relief 2.4 is also the only layer-exact value in the viable 2.20–2.91 window at 0.20 mm layers.

**Revisions from the build check:**
- **Screws: M3 × 8 confirmed** — 2.8 mm through the ring, **5.20 mm engaged (1.73 × D)**, 0.50 spare. M3 × 6 engages only 1.07 × D, too short. **M3 × 10 bottoms out by 1.50 mm** and would feel torqued while clamping nothing. Add M3 × 8 to the BOM.
- **Torque guidance corrected upward.** The earlier "≤ 0.2 N·m" was too low: required preload runs 40 N/screw at the soft corner to ~296 N at the stiff one, against 333 N at 0.2 N·m — only 1.12× margin. This is a displacement-controlled joint. **Cross pattern, tighten until the ears are hard down on the roof; expect 0.2 N·m, allow 0.3, never exceed 0.3.** The 2.8 mm of material under each head makes 0.3 safe.
- **The web is now the structural element, and the margin is thinner than v11's.** 13.2 MPa (SF 3.8) unconfined at 43.3 % squeeze, 26.3 MPa (SF 1.9) if the gasket confines — which it probably does, being captured by the duct lip 0.315 inboard and the seat wall 0.525 outboard. v11 ran SF 8.9. **PETG creeps: re-check the clamp after a week.** Favour the deep end of the seat band — at seat depth 3.4 it is 17 % and SF 13.9.
- **Relief Ø50.5 is the hard limit** — Ø50.0 already leaves only 0.250 mm to the ear pad tips (0.145 on the shrink-comp variant). Do not open it further.
- **Gasket loaded area is 179.7 mm², not 248.8.** ID Ø43.5 sits 0.500 mm inboard of the web edge, so 28.6 % of the gasket width is never pressed. Accepted deliberately: moving the ID out to Ø44.5 would take the section height-to-width ratio from 1.71 to 2.40, and a 3 mm tall, 1.25 mm wide rubber ring rolls instead of compressing. Use 179.7 mm² for any force calculation.
- **Ear-relief variant built and held in reserve:** `clamp_ring_v2_earslot`, two opposed slots at 0°/180°, **web-only** (`SLOT_WEB_ONLY`), which keeps the relief wall and bearing annulus continuous and retains 10.70 mm² of section against 7.70 for a full-depth slot. Full-depth slots would breach the Ø50.0 relief wall by 1.25 mm and leave two 30.8° arcs with no gasket compression, sitting midway between screw pairs. Print this one only if a test fit shows the fan's ear fouls the ring.
- **Print orientation: top face down.** Underside-down would make the relief ceiling — the gasket sealing face — a 2.25 mm unsupported overhang. 0.20 mm layers; every design depth is an integer layer count (4.4 = 22, 2.4 = 12, 1.6 = 8, web 2.0 = 10).

**PRINTED AND TEST-FITTED (17 Sep) — in ABS, not PETG.** Den printed `clamp_ring_v2_shrinkcomp.stl` on the `SumoBot Clamp Ring v2 ABS @BBL X1C` preset: 0.20 mm layers, flipped top-face-down, brim 8 outer-only, 4 walls, 40 % grid, `xy_hole_compensation = 0` (ABS shrink handles it — never stack both), `filament_shrink` left at 100 % because the mesh already carries hand-applied internal offsets.

**Result: it fits.** Small side-to-side play, which is expected and not a defect — nothing centres the ring except its four bolt holes, and the build check predicted worst-case eccentric float of **0.395 mm**. The compliant element takes it up, and once the screws are down the fan is captive. If a self-centring ring is ever wanted, a Ø48.2 spigot on the underside would do it for free.

**Material consequence of ABS over PETG.** The web stress figures above were computed for PETG (≈50 MPa). ABS is nearer 40, so the safety factor falls from 3.8 → ≈3.0 unconfined and 1.9 → ≈1.5 if the gasket confines. Still positive at the worst corner of the box, and the part is printed flat so the web bends in-plane rather than across layers, which is the strong direction for FDM. ABS also creeps less than PETG at room temperature, so long-term preload relaxation is a smaller worry than it was — but **the one-week clamp re-check still stands**, and it matters more now that SF 1.5 is the floor. Favour the deep end of the seat band when reaming: at seat depth 3.4 the squeeze is 17 % and the margin goes back above 10.

**Superseded claims from the first draft of this entry, corrected:**
1. "Ream to Ø48.3" — that is a *modelled* number; the physical ream target is 48.05–48.10.
2. "Relief 1.1 still makes contact if the seat is reamed up to 0.4 deeper" — false. Contact is lost after 0.21–0.40 mm, and at the thin flange before 0.4.
3. "At 0.50 proud the Ø48.4 × 0.8 relief never touches the flange, so the fan floats" — the arithmetic is right but the diagnosis was conditional on the gasket already being deleted. With the specced under-flange gasket the ring over-clamps instead. The real original fault was simply that a Ø52 gasket cannot fit a Ø47.61 pocket.
4. "Moving the gasket on top is the fix" — it is not. Required relief depth is identical either way; the move buys lid headroom only, which is still a good reason to do it.
5. Grip and preload were argued from the *maximum* flange thickness. Maximum thickness governs interference and height; **minimum** governs grip.

## Repo audit fixes (18 Sep 2026), no design numbers changed

Five audits over a fresh clone (firmware, docs consistency, a hostile electrical review of the wiring guide, the pin-map pull request itself, chassis status & issue triage) plus two blind reviews of the first bench build.

What changed on the arrivals branch as a result:

- The firmware build config now targets the T-Display S3. It was still set for the classic ESP32, with display pins landing on the new SDA & Motor R IN2, and the serial console would have come out on GPIO 43, the ESC pin. A duplicate stub project is deleted.
- The firmware fan settings follow `DOWNFORCE_FAN.md` instead of the pre-derate ones.
- Suction is recorded as approved 8 Sep in the five places that still said pending. Risk register rows 1, 4, 6, 8, 9, 13, 20 corrected and 21 to 25 added. `PARTS_AND_WIRING.md` §4–§5 and `LAYOUT_PASS.md` §4 carry superseded banners (classic ESP32 pins, 43/44 reversed, 100 Ω LED resistor, lid plug on the Brain's 3V3).
- Mass budget rebuilt on the two measured parts (motors 192.4 g, battery 151.2 g). Printed structure is 296.4 g for the six v11 family parts, total 954.2 g, headroom 35.8 g, and every doc now quotes that one figure. **Correction to the v11 lid entry above:** the "structure total ≈ 259 g" there omitted the two carriers & the battery frame, the full set is 296.4 g.
- Wiring guide motor card says 58.8 mm (measured), not ~65.

Not changed, deliberately: any chassis geometry, any CAD number, the first-drive motor pair choice (START_HERE still said the old pair), README's "not printed" status line. Everything the audits raised that needed a hand or a decision went on the issue list.

## Wheel hub v6 → v6.1 → v6.2 (21 Sep 2026)

- **v6:** flanges Ø40 → **Ø43**, lip 1.0 → 2.5 above the rib peaks. The printed v5 (ABS, `filament_shrink` 100 %, fitted fine) let the cast ring walk sideways over the flange. 14.2 g ABS.
- **v6.1:** heat-set insert replaced by a **captive M3 hex nut** with a 4.2 mm backing pad and an M3 × 10 grub, because overtightening pulled the insert out of the core. Bore flat 1.55 → **1.45** from centre (3.50 across) to take out the rotational slop. Drum access hole Ø4.5 → Ø6 so the iron and screw fit. Nut slot and screw hole roofed at 45° so no support grows inside them.
- **v6.2:** v6 and v6.1 printed with support on the build plate only, and the Ø43 lip drooped (it hangs 4.0 mm off the drum, v5's hung 2.5). Preset now supports the lip from the bottom flange, a removable ring in the open tyre seat. Mesh: pad raised to z 16, drum hole made a teardrop, so no support lands inside the hub. 14.3 g ABS. **On the bot, both wheels.**
- Round bore left at Ø4.10 in CAD, the 4.05 coupon is still open.
- Full record `../../wheels/WHEEL_HUB_V6_CHANGE.md`, preset `../../printing/PRESETS_hub_v6_2_ABS.md`, STL `hardware/cad/v11/stl/sumo_wheel_hub_v6_2.stl`.

## Carrier v13 (21 Sep 2026)

- v12 could only be assembled tilted. Its three cheek pairs were U-saddles under the motor (body in from the top) while the v12 faceplate slot takes the collar from the bottom, so the blades spread and the 1.5 × 4 mm tie strips snapped. A v12 design miss, not an assembly fault.
- v13 deletes the saddles and the third cheek pair (it touched nothing on the 58.84 motor) and adds **two open-bottom hoops** (radius 12.65, 0.26 radial on Ø24.78, bridge 9.98 wide at Z 25.40) joined by link walls. The motor + wheel unit now drops straight in with the carrier upside down. Faceplate, slot, driver holes, wellcap bosses and mounts unchanged. 17.3 g solid PLA.
- Interference checks all 0.000 mm³ (motor seated and swept, wheel swept, collar swept up the slot), motor top to bridge 0.51 clear.
- **Correction to the v12 entry above:** "17.8 → 15.8 g each" is wrong, 15 795 mm³ × 1.24 is 19.6 g solid. Printed mass unmeasured.
- **On the bot, both sides, PLA.** Record `CARRIER_V13_CHANGE.md`, preset `../../printing/PRESETS_v13_carriers_PLA.md`. STLs aren't in the repo.

## Layout v11.2 (22 Sep 2026)

- `layout.py` / `interfaces.json` re-run for the drive-only wiring of the first drive against the printed base, zero new overlaps. Pin map corrected to match the firmware, roof electronics re-laid to the drive-only guide's names, buck box set to the measured 15 × 11 × 8.5, new wiring block with every wire landing point in XYZ (the pin map & the wiring block aren't in the published copy). Board pilots not moved (the base is already printed). Motor envelopes kept at the 69.3 worst case, wire nodes use the measured 58.84 tail.

## State of the bot and CAD into the repo (23 Sep 2026)

- **On the bot:** v11 base (PLA), v11 lid (PETG translucent), v13 carriers, wellcaps +2, battery frame v2, clamp ring v2 (ABS), hub v6.2 (ABS) with tyres cast in Mold Star 15 from the v1 ring mould (OD 46.8). The first-drive build runs the JGA25-371 pair, with the Brain on a breadboard on top for now. The "old motor pair" line in START_HERE is closed: the first drive used the JGA25-371 pair.
- `hardware/cad/v11/` now holds the STLs, STEP for base, lid and assembly, the preset bundles and the v11.2 layout (index `hardware/cad/README.md`). Still to add: v13 carrier STLs and preset bundle, CadQuery build code (neither is in the published copy).
- START_HERE carries a "Printed parts: current revision" table. Concept docs, dead branches and superseded revisions carry banners, index in `../README.md`.
