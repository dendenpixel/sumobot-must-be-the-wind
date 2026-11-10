# Print preset, v13 carriers (PLA)

Built 21 Sep 2026. Preset **`SumoBot v13 Carriers PLA @BBL X1C`** (bundle `SumoBot_v13_Carriers_PLA.bbscfg`), inherits `0.20mm Standard @BBL X1C`. Files: `v13_carrier_L.stl` + `v13_carrier_R.stl`, both on one plate. Supersedes `SumoBot v12 Carriers PLA @BBL X1C` for these parts.

The v13 STLs and the `.bbscfg` aren't in the repo, so the full settings delta is below and the preset can be rebuilt by hand from it (or from the v12 bundle in `hardware/cad/v11/presets/`, changing the keys marked). Design record: `../chassis/v11/CARRIER_V13_CHANGE.md`. Envelope rules: `BAMBU_PRESET_RECIPE.md`.

## Measured geometry

| | L | R |
|---|---|---|
| bbox | 77.0 × 76.45 × 28.1 | 70.0 × 79.5 × 28.1 |
| facets | 10 870 | 10 674 |
| as-is: bed / needs support | 1133.0 / 241.2 mm² | 1129.3 / 241.2 mm² |
| flipped 180° X | 355.2 / 1026.7 | 354.7 / 1023.0 |
| on side 90° X | 138.0 / 3069.8 | 8.3 / 3044.0 |

As-is (feet down) wins on both. Slope bins (L): 0–5° 229.5 · 5–30° 11.7 · 30–44.9° 6.7 · **44.9–55° 442.1 (hoop shoulders, exactly 45°, self-supporting)** · 55–90° 386.6.

## Critical Z bands

| Z | Area | Feature | Raycast below | Verdict |
|---|---|---|---|---|
| 15.85 | 1.0 mm² | sliver (carried over from v12) | — | ignored (`support_remove_small_overhang`) |
| **25.40** | **227.5 mm²** | the two hoop bridges, 9.98 wide × 10.8 and × 12.0 long | empty at centre, both edges, both ends of both hoops, L and R (30 probes each). From above: bridge solid 25.40–27.40, shoulders solid 24.79–27.19 at x = 14 ± 5.6 | **true bridge, anchored both sides, 9.98 span, bridge it with no support** |

The v12 Z 19.10 ledge is gone (it was on the saddles).

**`support_on_build_plate_only = 1`**, since the only band is over open plate and nothing sits over part material.

**`bridge_no_support = 1`**. The 9.98 mm span is over the usual 5 mm rule of thumb, but it's anchored both sides, it's PLA, the 0.51 mm clearance to the motor absorbs sag, and the v11 battery frame's 15.9 mm XT60 bridge already printed unsupported. A 10 × 11 mm support tower 25 mm tall is the likelier failure. To get the column instead, set `bridge_no_support = 0` (it stands on the bed inside the hoop and pulls out of the open tunnel).

**Layer height 0.20**, since (25.40 − 0.2) / 0.2 = 126 exactly. 0.16 lands 0.08 off. 0.15 is exact too but costs ~33 % more time for nothing.

## Settings delta vs `0.20mm Standard @BBL X1C`

| Key | Value | Why |
|---|---|---|
| `layer_height` | 0.2 | Z 25.40 lands exact |
| `wall_loops` / top / bottom | 4 / 5 / 5 | drivetrain carrier, load-bearing |
| `sparse_infill_density` / pattern | 40 % / grid | same |
| `wall_generator` | arachne | 1.25 walls resolve as 3 lines |
| `precise_outer_wall` | 1, outer wall 60 mm/s, 2000 accel | motor clearance is 0.26 |
| `xy_hole_compensation` | 0.15 | clearance holes (assumed, 0 if any seat is a press fit) |
| `elefant_foot_compensation` | 0.15 | PLA, keeps the lead-in mouth open |
| `brim_type` / `brim_width` | outer_only / 5 | thin 36 mm walls want the grip |
| `enable_support` | 1, normal(auto), snug, threshold 30 | safety net only, 45° shoulders stay bare |
| `support_on_build_plate_only` | 1 | band is over open plate |
| `bridge_no_support` | 1 | see above |
| `support_remove_small_overhang` | 1 | kills the 1 mm² sliver |
| Z gaps / XY / interface | 0.2 / 0.2 / 0.35 / 2+2 layers, spacing 0.2 | PLA single-material |
| `bridge_speed` | 40 | PLA |
| `thick_bridges` | 0 | cleaner bridge underside |
| `enable_prime_tower` | 0 | single material |

Validated against a resolved X1C project config (582 keys): 0 unknown keys, 0 type mismatches. Envelope self-check passed, printer JSON byte-identical to `assets/X1C_printer_preset.json`.

## Verify in preview

- Z 25.40 (layer 127): both hoops show **bridge** lines running across X (the 10 mm way), no support underneath.
- No support anywhere on the 45° shoulders (Z 18.8 → 25.4).
- Link walls and hoop walls slice as 3 continuous lines, no gap-fill confetti.

## Off-slicer

- PLA, nothing special, door any position, both carriers on one plate.
- After printing, run a blade along the chamfered mouth to clear brim flash before dropping the motor in.
- If the motor binds between the walls, set `xy_contour_compensation −0.05` and reprint. Don't sand the 1.25 walls.

Import: File → Import → Import Configs…, which should report **1 config imported**.
