# Print preset, wheel hub v6.2 (ABS)

Built 21 Sep 2026. Preset **`SumoBot Wheel Hub v6.2 ABS @BBL X1C`**, bundle `hardware/cad/v11/presets/SumoBot_WheelHub_v6_2_ABS.bbscfg`. Part `hardware/cad/v11/stl/sumo_wheel_hub_v6_2.stl`, one per wheel. Inherits `0.20mm Standard @BBL X1C`. This is the preset the hubs on the bot were printed with.

Design record (v6 → v6.1 → v6.2): `../wheels/WHEEL_HUB_V6_CHANGE.md`. Supersedes the hub half of `PRESETS_v5hub_v12carriers.md`. Envelope rules: `BAMBU_PRESET_RECIPE.md`.

## Geometry

bbox 43 × 43 × 28.9, 9708 facets, watertight, 1 body. Print as-is (motor face down).

| Orientation | Bed contact mm² | Needs support mm² |
|---|---|---|
| **as-is** | 820.4 | 988.6 |
| flipped 180° X | 735.6 | 1123.4 |
| on side | 8.6 | 1334.8 |

(Areas measured on v6.1. v6.2 only adds to the pad and reshapes the drum hole, so the ranking doesn't change.)

## Critical Z bands (v6.2)

| Z | Area mm² | Feature | Lands on | Verdict |
|---|---|---|---|---|
| 2.5 | 38.9 | centre pocket ceiling | plate | support from plate |
| 3.0 | 27.4 | pocket shoulder | plate | support from plate |
| 15.5 | 443.6 | web underside r 8–14 | plate | support from plate |
| **28.0** | **444.4** | top flange lip, r 17.5 → 21.5 (4.0 mm hang) | bottom flange top face (Z 1.0) | **support on the part**, a ring in the open tyre seat, removable |

Nut slot (gable roof) and screw hole and drum hole (teardrops) generate no overhang.

**`support_on_build_plate_only = 0`.** This is the one change from the v6 / v6.1 preset, and the reason v6.2 exists. With it set to 1 the Ø43 lip printed as drooped, stringy loops. The tyre seat is open radially and the ribs are only 1.5 deep, so the ring that stands on the bottom flange is reachable and its scars sit under the tyre.

**Layer height 0.10**, which lands Z 2.5, 15.5 and 28.0 all exactly (0.15 leaves Z 28 off by 0.05, 0.20 leaves Z 15.5 off by 0.10). Z 28 is now nearly as large as Z 15.5 and it's the functional lip, so both matter.

## Settings delta vs `0.20mm Standard @BBL X1C`

| Key | Value | Note |
|---|---|---|
| `layer_height` | 0.1 | exact landing, see above |
| `wall_loops` | 4 | |
| `top_shell_layers` / `top_shell_thickness` | 7 / 0.8 | |
| `bottom_shell_layers` | 5 | |
| `sparse_infill_density` / pattern | 40 % / grid | |
| `wall_generator` / `wall_sequence` | arachne / inner then outer | |
| `precise_outer_wall` | 1, outer wall 60 mm/s @ 2000 | |
| `enable_support` / type / style | 1 / normal(auto) / snug | |
| `support_threshold_angle` | 30 | |
| `support_on_build_plate_only` | **0** | the v6.2 change |
| Z gaps / XY distance / interface | 0.2 / 0.4 / 2 layers | ABS single-material |
| `elefant_foot_compensation` | 0.2 | ABS |
| `brim_type` / `brim_width` | outer_only / 8 | ABS warp |
| `xy_hole_compensation` | 0 | ABS, never stack with shrink |
| `overhang_3_4_speed` | 20 | |
| `bridge_speed` | 30 | |
| `enable_prime_tower` | 0 | |

Delta from the v5 hub preset: layer 0.15 → 0.10, top shells 5 → 7, top thickness 1 → 0.8, overhang 3/4 speed 25 → 20, build-plate-only 1 → 0. Validated 0 unknown keys / 0 type mismatches against a resolved X1C project config.

## Verify in preview

- A support ring between the flanges, standing on the bottom flange and reaching the lip underside.
- Support under the web and the centre pocket from the plate.
- **Nothing** in the nut slot, the screw hole or the drum hole.

Removal: break the ring in 2–3 places with flush cutters and peel it outward.

## Off-slicer

- Chamber door closed, bed 90–100 °C, glue stick.
- `filament_shrink` left at **100 %** (what v5 was printed and fitted with). Changing it now would change the bore fit.
- Support for PLA/PETG doesn't work under ABS, so keep it single-material.
