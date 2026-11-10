> **Superseded 21 Sep 2026.** Replaced by `docs/printing/PRESETS_hub_v6_2_ABS.md` and `docs/printing/PRESETS_v13_carriers_PLA.md`, and the build-plate-only call below doesn't hold for the Ø43 hub lip. Kept for the reasoning/history.

# Print presets — wheel hub v5 (ABS) + v12 carriers (PLA)

Built 15 Sep 2026. Two separate `.bbscfg` bundles because the materials differ.
Both inherit `0.20mm Standard @BBL X1C`. Envelope per `BAMBU_PRESET_RECIPE.md`.

Design records for the parts: `../wheels/WHEEL_HUB_V5_CHANGE.md` and `../chassis/v11/CARRIER_V12_CHANGE.md`.

| Bundle | Preset name | For |
|---|---|---|
| `SumoBot_WheelHub_v5_ABS.bbscfg` | `SumoBot Wheel Hub v5 ABS @BBL X1C` | `sumo_wheel_hub_v5.stl`, ABS, one part |
| `SumoBot_v12_Carriers_PLA.bbscfg` | `SumoBot v12 Carriers PLA @BBL X1C` | `v12_carrier_L.stl` + `v12_carrier_R.stl`, PLA, both on one plate |

## Measured geometry

**Wheel hub v5** — bbox 40 × 40 × 28.9, 9452 facets. Unchanged support topology from v4.

| Orientation | Bed contact | Support needed |
|---|---|---|
| as-is | 639.0 mm² | 798.6 mm² |
| flipped 180° X | 540.1 mm² | 896.1 mm² |
| on side 90° X | 8.0 mm² | 1255.7 mm² |

as-is wins. Critical bands:

| Z | Area | Feature | Below it | Verdict |
|---|---|---|---|---|
| 2.50 | 42.2 mm² | central pocket ceiling | open plate (raycast: no solid) | support from bed |
| 3.00 | 23.4 mm² | pocket shoulder | open plate | support from bed |
| 10.11–10.25, 11.24 | ~9 mm² total | 1.1 mm² slivers | — | ignored via `support_remove_small_overhang` |
| **15.50** | **470.1 mm²** | flange underside, r ≤ 14 | open plate | support from bed |
| **28.00** | **248.9 mm²** | tyre-groove upper lip, r 17→19.3 | groove floor at r≈17 | must NOT be supported |

Groove confirmed by cross-section: walls at r = 15, 17, 17.5, 18, 18.5, 19 from Z 20 to Z 27.9; at Z 28.2+ only r = 15 and 19.5.

**`support_on_build_plate_only = 1`** — same call as v4. The 470 mm² flange stands on open plate so it still gets supported; the Z 28.00 lip's only foundation is the groove floor, and a column in a 2.5 mm annular groove is unremovable.

**Layer height 0.15** — lands Z 15.50 exactly ((15.50 − 0.2)/0.15 = 102). Z 28.00 lands 0.05 mm off. 0.20 would land Z 28.00 exact but Z 15.50 off by 0.10 mm; 15.50 is the larger band (470 vs 249 mm²).

**Carriers L + R** — 77 × 110.75 × 28.1 and 70 × 113.8 × 28.1, mirrored.

| Orientation | Bed contact | Support needed |
|---|---|---|
| as-is | ~1938 mm² | 27.9 mm² |
| flipped 180° X | ~355 mm² | ~1262 mm² |
| on side 90° X | 8–127 mm² | ~3207 mm² |

as-is by a mile. Only two bands, both self-supporting:
- Z 15.85, 1.0 mm² — sliver.
- Z 19.10, 14.2 mm² — a 1.6 mm wide × 27 mm long ledge. Raycast at three points along it: solid below at both ends (to Z 3.46 and Z 16.1), open in the middle. A 1.6 mm bridge — self-supports.

The 77.7 mm² at 40–45° is a chamfer. Threshold stays at 30 so it is not wrapped.

Support is left enabled with `support_remove_small_overhang = 1` so it generates ~nothing but still catches anything unexpected. Layer height 0.20 — no band needs exact landing, and these are two 110 mm parts.

## Settings delta (vs `0.20mm Standard @BBL X1C`)

| Key | Hub ABS | Carriers PLA | Why |
|---|---|---|---|
| `layer_height` | 0.15 | 0.2 | Z 15.50 exact landing / no critical band |
| `wall_loops` / shells | 4 / 5 / 5 | 4 / 5 / 5 | drive parts |
| `sparse_infill_density` | 40% grid | 40% grid | load-bearing |
| `support_on_build_plate_only` | **1** | 1 | keeps support out of tyre groove / all bands over plate |
| `support_threshold_angle` | 30 | 30 | keeps the 40–45° chamfer unsupported |
| `support_top/bottom_z_distance` | 0.2 | 0.2 | single-material |
| `support_object_xy_distance` | 0.40 | 0.35 | ABS / PLA |
| `support_remove_small_overhang` | 1 | 1 | kills the 1 mm² slivers |
| `elefant_foot_compensation` | 0.2 | 0.15 | ABS squish |
| `brim_type` / `brim_width` | outer_only / 8 | outer_only / 5 | ABS on 40 mm × 28.9 tall needs it |
| `xy_hole_compensation` | 0 | 0.15 | ABS uses `filament_shrink` instead; never both |
| `precise_outer_wall` | 1 | 1 | tolerances |
| `bridge_speed` | 30 | 40 | material |
| `enable_prime_tower` | 0 | 0 | single material each |
| `thick_bridges` | 0 | 0 | cleaner undersides |

## Off-slicer

- **ABS hub**: chamber door CLOSED, bed 90–100 °C, glue stick. Set **Filament settings → Advanced → Shrinkage compensation = 100.5%**, print ONE hub, measure the 40 mm OD, then `filament_shrink = 100 × 40 ÷ measured`. `filament_shrink` is a filament key — it cannot live in the `.bbscfg`.
- **PLA carriers**: nothing special. Both on one plate.
- Carriers `xy_hole_compensation = 0.15` assumes clearance holes. If any seat is a press fit (bearing, motor boss), set it to 0.

## Verify in preview

- Hub Z 15.50 — support present, standing on the plate.
- Hub Z 28.00 — **no support inside the tyre groove**. If any appears, `support_on_build_plate_only` did not take.
- Hub Z 2.50/3.00 — support present from the plate.
- Carriers Z 19.10 — should show a bridge, not a support wall.

Import: File → Import → Import Configs… — each bundle should report **1 config imported**.
