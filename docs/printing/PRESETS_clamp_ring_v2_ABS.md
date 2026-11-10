# Print preset — clamp ring v2, ABS (17 Sep 2026)

Source mesh: `clamp_ring_v2_shrinkcomp.stl` (15,440 facets, binary STL)
Preset shipped: **`SumoBot Clamp Ring v2 ABS @BBL X1C`** (bundle `hardware/cad/v11/presets/SumoBot_ClampRing_v2_ABS.bbscfg`)

Design record: `../chassis/v11/CLAMP_RING_V2_CHANGE.md`. Envelope rules: `BAMBU_PRESET_RECIPE.md`.

## Geometry (measured, not eyeballed)

| | |
|---|---|
| bbox | 55.996 × 55.996 × 4.400 mm |
| bore (vertical wall) | r 22.35 → **ø44.70** |
| flange step wall | r 25.10 → **ø50.20** |
| ring OD | r 27.998 → **ø55.996** |
| lugs | 4 × diagonal ears out to r ≈ 34.7, each with a through-slot and a 1.6 mm deep top pocket |

Horizontal planes (as-modelled):

| Z | facing | area |
|---|---|---|
| 0.000 | DOWN | 665.9 mm² (bed) |
| 2.400 | DOWN | 410.0 mm² (flange underside) |
| 2.800 | UP | 100.5 mm² (lug pocket floors, 4 ×) |
| 4.400 | UP | 975.4 mm² (top face) |

Slope bins: **100 % of downfacing area is 0–5°**. No chamfers anywhere — nothing marginal to argue about.

## Orientation

| orientation | bed contact | support needed |
|---|---|---|
| as modelled | 1394.5 mm² | **410.0 mm²** |
| **flipped 180° about X** | 1339.2 mm² | **100.5 mm²** |
| on side (90° X) | 15.1 mm² | 289.6 mm² |

**Print it flipped — top face down.** Reasons:

1. Kills the 410 mm² flange underside entirely. That band is an annulus r 22.35→25.11, **2.76 mm wide, anchored on one edge only** (the bore side is open air). One-edge cantilever → per the span rules it needs support, and in ABS a 0° one-sided lip that wide curls rather than just droops.
2. Bed contact becomes the flat 975.4 mm² top face rather than the 665.9 mm² bottom — better first layer, and the elephant foot lands on the non-mating face.
3. The flange underside (the clamping face) becomes an **up-facing** surface → top-solid-layer finish instead of support scarring.

## Critical Z bands, flipped orientation

| Z | area | feature | raycast below | verdict |
|---|---|---|---|---|
| 1.60 | 100.5 mm² (4 × 25.1) | lug pocket ceilings — closed ring ledge around each slot | `[]` at all 6 probes (r 27.75 – 32.84) | open plate; **1.7 mm max inscribed width → self-supports** |

Ledge width measured by rasterising the ceiling footprint at 0.2 mm and taking the distance transform: max inscribed half-width 0.85 mm → **1.70 mm ledge**. Under the ≤ 2 mm self-support threshold, and it sits only 1.6 mm above the plate so there is nowhere to droop to.

**Effectively this part needs no support.** Support is left enabled with `support_remove_small_overhang = 1` as a cheap net; it should filter these bands out. Switching `enable_support` off entirely loses nothing.

## `support_on_build_plate_only` = **1**

Every band raycasts `[]` — open air to the plate. There is no band whose only foundation is part material, and no narrow deep cavity. Free, and it guarantees nothing lands inside the lug slots.

## Layer height = 0.20 mm

With `initial_layer_print_height = 0.2`:

| layer height | Z 1.60 (100.5 mm²) | Z 2.00 flange step (410 mm²) | Z 4.40 top (665.9 mm²) |
|---|---|---|---|
| **0.20** | **EXACT** | **EXACT** | **EXACT** |
| 0.16 | off 0.040 | off 0.040 | off 0.040 |
| 0.15 | off 0.050 | EXACT | EXACT |
| 0.12 | off 0.040 | EXACT | EXACT |
| 0.10 | EXACT | EXACT | EXACT |

0.20 lands all three exactly. 0.10 also does, at 2× the time for nothing. **0.20 wins outright — no accuracy is being traded for speed here.**

## Settings delta vs `0.20mm Standard @BBL X1C`

| key | value | why |
|---|---|---|
| `layer_height` / `initial_layer_print_height` | 0.2 / 0.2 | all critical Z land exact |
| `enable_support` | 1 | net only |
| `support_type` / `support_style` | normal(auto) / snug | |
| `support_threshold_angle` | 30 | ABS |
| `support_on_build_plate_only` | 1 | all bands raycast open plate |
| `support_remove_small_overhang` | 1 | filters the 1.7 mm ledges |
| `support_top_z_distance` / `_bottom_` | 0.2 / 0.2 | ABS matrix |
| `support_interface_spacing` | 0.2 | ABS matrix |
| `support_interface_top/bottom_layers` | 2 / 2 | |
| `support_object_xy_distance` | 0.4 | ABS |
| `tree_support_wall_count` | 0 | "Support wall loops" |
| `support_filament` / `support_interface_filament` | 0 / 0 | single material |
| `wall_loops` / `top_shell_layers` / `bottom_shell_layers` | 4 / 5 / 5 | load-bearing clamp under bolt preload |
| `sparse_infill_density` / `_pattern` | 40% / grid | load-bearing |
| `wall_generator` | arachne | thin 1.7 mm ledges and 2.76 mm flange |
| `thick_bridges` | 0 | |
| `precise_outer_wall` | 1 | ø tolerance on bore/flange |
| `outer_wall_speed` | [60, 60] | accuracy |
| `outer_wall_acceleration` | [2000, 2000] | accuracy |
| `bridge_speed` | [30, 30] | ABS |
| `elefant_foot_compensation` | 0.2 | ABS |
| `xy_hole_compensation` | 0 | **ABS — shrink handles it; never stack both** |
| `xy_contour_compensation` | 0 | fixed offsets are a poor substitute for a scale factor |
| `brim_type` / `brim_width` | outer_only / 8 | ABS warp, thin 4.4 mm flat part |
| `enable_prime_tower` | 0 | single-material plate |

## Verify after slicing

- **Z 1.60** — four lug pockets. Expect **no support** generated. If it does generate, it is 1.6 mm stubs off the plate; harmless, but you can raise `support_threshold_angle` rather than fight it.
- **Z 2.00** — the flange step must be an *up*-facing surface. If it is a ceiling, the part is not flipped.
- **First layer** — must be the solid 975.4 mm² top face, one continuous region, not a 666 mm² annulus.
- Confirm no support anywhere inside the bore (ø44.70) or the four lug slots.

## Off-slicer actions

- **Chamber door CLOSED.** ABS.
- **Glue stick**, bed 90–100 °C.
- **Support interface filament:** *Bambu Support for PLA/PETG* does **not** work under ABS — wrong temperature range. If you ever want a zero-gap interface here you need *Support for ABS*. Not proposed; single-material is right for this part.
- **`filament_shrink` — do not set blindly.** It is a *filament* setting (Filament → Advanced → Shrinkage compensation), not a process setting, so it is not in the `.bbscfg`. **The mesh is named `_shrinkcomp`, and the bore/flange walls sit at ø44.70 / ø50.20 against a dead-round ø55.996 OD and 4.400 height — that pattern reads as hand-applied offsets on the internal features, not a uniform scale.** Setting `filament_shrink = 100.5 %` on top of that would double-compensate. Leave it at 100 %, print **one** part, measure the OD and the bore, then decide: `filament_shrink = 100 × nominal ÷ measured`. One part, not a plate — the dimension cannot be recovered afterwards.

## Assumptions and gaps

- **Validation against a real config could not run.** A resolved `X1C_project_settings.config` was not available — only the printer JSON, at `assets/X1C_printer_preset.json`. The envelope self-check passed (no forbidden fields, `version 2.8.0.6`, array keys correct). Key names for support/brim/elephant-foot/hole-comp/speeds/prime-tower are confirmed by `BAMBU_PRESET_RECIPE.md`. **Unverified key names:** `layer_height`, `initial_layer_print_height`, `enable_support`, `support_type`, `support_style`, `support_threshold_angle`, `support_on_build_plate_only`, `support_top_z_distance`, `support_bottom_z_distance`, `support_interface_spacing`, `support_interface_top_layers`, `support_interface_bottom_layers`, `support_object_xy_distance`, `wall_loops`, `top_shell_layers`, `bottom_shell_layers`, `sparse_infill_density`, `sparse_infill_pattern`, `brim_width`. An unrecognised key is dropped **silently** — check these in the UI after import. To make the check real next time: save any 3mf and drop `Metadata/project_settings.config` into `assets/`.
- Update 21 Sep: a resolved X1C project config was later lifted from a printed `.3mf` and used to validate the hub v6.x and v13 carrier presets. This preset hasn't been re-validated against it, and the config file isn't in the repo yet.
- Hole fit: assumed the bore and the lug slots are **clearance**, not press fits. `xy_hole_compensation` is 0 regardless because the material is ABS.
- The `.bbscfg` carries process settings only. Orientation (the 180° flip) lives in the 3mf — import the preset, select it, flip and arrange the plate, then **File → Save Project As**.

**Print result (17 Sep):** the ring was printed on this preset and test-fitted — it fits. Full result and the material consequence of ABS over PETG are recorded in `../chassis/v11/CLAMP_RING_V2_CHANGE.md`.
