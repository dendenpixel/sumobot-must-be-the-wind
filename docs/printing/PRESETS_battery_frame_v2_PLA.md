# Print preset — battery frame v2 (clip), PLA (15 Sep 2026)

File: `v11_battery_frame_v2_clip.stl` · 2206 facets · bbox **50.00 × 142.53 × 15.06 mm**
Preset built: **`SumoBot Battery Frame v2 PLA @BBL X1C`** (inherits `0.20mm Standard @BBL X1C`), bundle `hardware/cad/v11/presets/SumoBot_BatteryFrame_v2_PLA.bbscfg`. The frame on the bot was printed with it.

Design record: `../chassis/v11/BATTERY_FRAME_V2_CHANGE.md`. Envelope rules: `BAMBU_PRESET_RECIPE.md`.

> Material note: the change doc specs **PETG** for the snap fingers. The preset as built is **PLA**, by request. Mechanical consequence recorded under *Off-slicer* below.

## Orientation

| Orientation | Bed contact | Needs support |
|---|---|---|
| **as-is (flange down)** | **959.1 mm²** | **70.5 mm²** |
| flipped 180° X | 38.9 mm² | 990.7 mm² |
| on side 90° X | 8.3 mm² | 489.7 mm² |

As-is wins on both axes. Slope histogram: **all 70.5 mm² sits in the 0–5° bin** — every overhang is a flat ceiling, nothing is a chamfer.

## Critical Z bands + raycast evidence

| Z | Area | Feature | Footprint | Raycast below | Verdict |
|---|---|---|---|---|---|
| 4.50 | 37.0 mm² | **front strap tunnel roof** ×2 (±Y) | 11.4 × 1.6 mm each | `[(0.0, 1.5)]` at all 5 probes | 11.4 mm **bridge**, anchored both X ends |
| 6.20 | 1.7 mm² | XT60 post step | 2.0 × 0.83 mm | `[(0.0, 5.0)]` | sliver — ignore |
| 12.36 | 31.8 mm² | **XT60 bracket plate underside** | 2.0 × 15.9 mm | `[(0.0, 3.96)]` at all 7 probes | 15.9 mm **bridge**, anchored both Y ends |

Anchor proof (full-column spans, `ray_down` to +∞):

- Z4.50 roof: X −61.0 → `[(0.0, 8.0)]` (root block wall), X −47.5 → `[(0.0, 4.6)]` (stop wall). Free in Y both sides (Y 54.5 → `[]`, Y 57.2 → floor only). **Two-ended bridge across X.**
- Z12.36 plate: Y 57.0 → `[(0.0,5.0),(6.2,15.06)]` (inner post), Y 73.8 → `[(0.0, 15.06)]` (full-height outer block). Free in X both sides (X −72.3 → `[]`, X −69.7 → `[(0.0,1.6)]`). **Two-ended bridge across Y.**

## `support_on_build_plate_only = 1`

Neither band raycasts `[]` — both sit over part material — so setting `1` means **no support is generated anywhere on this part**. That is the intent:

- The Z4.50 band is the **strap tunnel**, a 1.6 mm wide × 3.0 mm deep × 11.4 mm long slot open only at its two ends. Support in there cannot be cleared and the velcro strap won't thread.
- The Z12.36 band is the gap the XT60 bracket plate spans; support stubs there are cosmetic at best.
- Both are two-ended bridges, so neither is *starved* by the setting — they bridge.

Matches v1's print recipe ("flange down, 3 walls, no support") and the v1 result (dimensions correct).

## Layer height — 0.16 mm

Landing error vs `initial_layer_print_height = 0.2`:

| Band | 0.20 | **0.16** | 0.15 | 0.12 | 0.10 |
|---|---|---|---|---|---|
| Z4.50 (37.0 mm²) | 0.100 | **0.020** | 0.050 | 0.020 | EXACT |
| Z12.36 (31.8 mm²) | 0.040 | **EXACT** | 0.010 | 0.040 | 0.040 |
| Z15.06 top | 0.060 | **0.020** | 0.010 | 0.020 | 0.040 |
| layers | 74 | **93** | 99 | 124 | 149 |

Strict largest-area tie-break picks 0.10 (Z4.50 exact). Rejected: the two bands are 37.0 vs 31.8 mm² — 5 mm² apart, so area is not decisive, and 0.10 still leaves Z12.36 off by 0.040 while costing 149 layers. **0.16 is the only height where no critical band is more than 0.020 mm off**, at 93 layers. Chosen on worst-case error, and the deviation is recorded here deliberately.

## Settings delta (vs `0.20mm Standard @BBL X1C`)

| Key | Value | Why |
|---|---|---|
| `layer_height` | 0.16 | above |
| `wall_loops` | **3** | **design-critical** — finger arm is 1.2 mm = exactly 3×0.4 perimeters. 4 walls makes Arachne thin them to 0.3 and changes spring rate |
| `wall_generator` | arachne | 1.2 mm arms, 1.6 mm slot roof — variable width needed |
| `top_shell_layers` / `bottom_shell_layers` | 5 / 4 | 4 solid layers over each bridge before infill resumes |
| `sparse_infill_density` / `_pattern` | 25% / grid | flat frame, mostly perimeter |
| `precise_outer_wall` | 1 | snap fit; hook overlap is 1.2 mm |
| `outer_wall_speed` / `_acceleration` | 60 / 2000 | same |
| `xy_hole_compensation` | **0** | v1 printed dimensionally correct on the stock profile — do not move XY on a known-good fit. (Skill default is 0.15; overridden on precedent.) |
| `xy_contour_compensation` | 0 | leaves the hook catch face at nominal |
| `elefant_foot_compensation` | 0.15 | PLA |
| `brim_type` / `brim_width` | outer_only / 5 | 142.5 mm long, thin section — end lift risk |
| `enable_prime_tower` | 0 | single material; "path beyond plate boundaries" has been hit from a prime tower before |
| `support_on_build_plate_only` | **1** | above |
| `support_threshold_angle` | 30 | PLA |
| `support_top/bottom_z_distance` | 0.2 / 0.2 | PLA single-material |
| `support_interface_spacing` | 0.2 | PLA |
| `support_interface_top/bottom_layers` | 2 / 2 | PLA |
| `support_object_xy_distance` | 0.35 | PLA |
| `tree_support_wall_count` | 0 | support wall loops |
| `support_remove_small_overhang` | 1 | kills the 1.7 mm² Z6.20 sliver |
| `support_filament` / `support_interface_filament` | 0 / 0 | single material |
| `bridge_speed` | 40 | both critical bands are bridges |
| `thick_bridges` | 0 | thin, flat bridge geometry |

Support interface material (Sup.PLA) considered and **declined**: only 2 distinct interface Z bands (~600 mm³ purge, ≈0.75 g — economically fine), but the Z4.50 band is inside an unreachable slot, and neither band is starved. Not worth a tool change.

## Verify after slicing

1. **Z 4.50** — strap tunnel roof must show **no support** and must slice as a bridge. Both ±Y sides.
2. **Z 12.36** — XT60 bracket underside, **no support**, bridge across Y 57.4→73.3.
3. **Z 0–5, Y 53.8–55.0** — finger arms must be **exactly 3 perimeters, no infill**. If Arachne shows 2 walls + a gap fill, the spring rate is wrong; stop and check `wall_loops`.
4. Preview should show **zero support volume** on the whole part. Any support at all means `support_on_build_plate_only` didn't take.
5. First layer: 959 mm² + 5 mm outer brim.

## Off-slicer

- Nothing to dry, chamber door any position, no glue stick, no `filament_shrink` (PLA).
- **PLA vs the PETG design**: spring rate scales with E, so ≈0.9 → ≈1.5 N/mm per finger (PLA ~3.5 GPa vs PETG ~2.1). Insertion push roughly 2 N → ~3.3 N per finger. Still light. Strain is geometry-only at ~1.0%, against PLA's ~3% yield — ~3× margin instead of PETG's ~5×. Arms bend in the layer plane, so no interlayer tension. Watch two things: PLA creeps if left deflected, and it softens near 55 °C next to a battery and motors.
- If the fingers snap or feel brittle, that's the PLA call, not the geometry — reprint in PETG using the PETG matrix (Z gap 0.4 if supports weld, threshold 35, no brim).

## Assumptions / caveats

- A resolved `X1C_project_settings.config` was **not available**, so the key-name/type validation against a live 581-key config **could not be run** (only the printer JSON exists, at `assets/X1C_printer_preset.json`). Keys were taken from the confirmed list in `BAMBU_PRESET_RECIPE.md`. Unverified against a live config: `sparse_infill_pattern`, `top_shell_layers`, `bottom_shell_layers`, `support_interface_bottom_layers`, `brim_width`. An unrecognised key is dropped **silently** on import — check these in the UI after importing. Saving any 3mf and dropping `Metadata/project_settings.config` into `assets/` makes this check real next time.
- Update 21 Sep: a resolved X1C project config was later lifted from a printed `.3mf` and used to validate the hub v6.x and v13 carrier presets. This preset hasn't been re-validated against it, and the config file isn't in the repo yet.
- Envelope self-check **passed**: no forbidden fields, `version == "2.8.0.6"`, all 14 array keys correct type, all other values strings, zip has no directory entries.
- No press fits assumed; XY left at nominal on v1 precedent rather than the 0.15 default.
