# CAD, the v11 chassis family

Everything needed to reprint the bot as it stands on 23 Sep 2026. STL and STEP files go through Git LFS (see `.gitattributes`), so clone with LFS installed or you'll get pointer files.

Frame for every file: mm, **+X front, +Y left, Z 0 = arena floor** (assembly and layout). Single-part STLs are exported in print orientation. Design history and every number behind these parts: `docs/chassis/v11/START_HERE.md` and `docs/chassis/v11/CHANGELOG.md`.

## `v11/stl/`, printable parts

| File | Part | Rev | Material | Qty | Preset | On the bot |
|---|---|---|---|---|---|---|
| `v11_base.stl` | base (pressure vessel, wedge, wells, fan seat) | v11 | PLA | 1 | settings in `docs/chassis/v11/REPORT_base_stage.md` §5 | yes |
| `v11_lid.stl` | lid (tower, ToF noses, grille, battery slit) | v11 | PETG translucent + support interface | 1 | `presets/SumoBot_Lid_PETG_SupIF.json`, `docs/printing/LID_PRINT_PROFILE.md` | yes |
| `v11_wellcap_L_plus2.stl` / `v11_wellcap_R_plus2.stl` | wheel-well caps, +2 mm ceiling | v11 +2 | PETG (as designed) | 1 + 1 | none, top face down, see `docs/chassis/v11/REPORT_lid_stage.md` | yes |
| `v11_battery_frame_v2_clip.stl` | battery rails, stop, XT60 bracket, rear snap fingers | v2 | PLA | 1 | `presets/SumoBot_BatteryFrame_v2_PLA.bbscfg` | yes |
| `clamp_ring_v2_shrinkcomp.stl` | EDF clamp ring | v2 rev B | ABS | 1 | `presets/SumoBot_ClampRing_v2_ABS.bbscfg` | yes (fitted, fan not mounted yet) |
| `clamp_ring_v2_earslot_shrinkcomp.stl` | clamp ring with two web-only ear slots | v2 rev B, reserve | ABS | 0 | same as above | no, print only if the fan's duct ear fouls the ring |
| `sumo_wheel_hub_v6_2.stl` | wheel hub, captive M3 nut | v6.2 | ABS | 2 | `presets/SumoBot_WheelHub_v6_2_ABS.bbscfg` | yes |
| `tyre-ring-mould.stl` | casting mould for the silicone tyre ring | v1 | PLA | 1, reused | 0.2 mm, 3 walls, 20 %, no support (`docs/WHEEL_V1.md`) | tool, not on the bot |
| `v13_carrier_L.stl` / `v13_carrier_R.stl` | motor + wheel-well carriers | v13 | PLA | 1 + 1 | `docs/printing/PRESETS_v13_carriers_PLA.md` | yes. **STL not in the repo** |

## `v11/step/`, B-rep for editing and renders

| File | What |
|---|---|
| `v11_assembly_full.step` | base-stage and lid-stage parts assembled with hardware envelopes, exported 13 Sep, so it predates the carrier v12/v13 and hub v5/v6 mesh edits |
| `v11_base.step` | base, v11 (exported 12 Sep) |
| `v11_lid.step` | lid, v11 (exported 13 Sep) |

The carriers, battery frame v2, wellcap +2 and hubs from v4 on were mesh edits of STLs, so they have no STEP.

## `v11/presets/`, Bambu Studio X1C (0.4 nozzle) process presets

Import with File → Import → Import Configs…. How the bundles are built: `docs/printing/BAMBU_PRESET_RECIPE.md`.

| File | Preset name | For | Status |
|---|---|---|---|
| `SumoBot_BatteryFrame_v2_PLA.bbscfg` | SumoBot Battery Frame v2 PLA @BBL X1C | battery frame v2 | current |
| `SumoBot_ClampRing_v2_ABS.bbscfg` | SumoBot Clamp Ring v2 ABS @BBL X1C | clamp ring v2 | current |
| `SumoBot_WheelHub_v6_2_ABS.bbscfg` | SumoBot Wheel Hub v6.2 ABS @BBL X1C | hub v6.2 | current |
| `SumoBot_Lid_PETG_SupIF.json` | SumoBot Lid PETG SupIF @BBL X1C | lid | current. A bare process json, which Bambu won't import on its own. Wrap it in a `.bbscfg` per the recipe, or set it by hand from `LID_PRINT_PROFILE.md` |
| `SumoBot_v12_Carriers_PLA.bbscfg` | SumoBot v12 Carriers PLA @BBL X1C | v12 carriers | **superseded** by the v13 preset. Rebuild v13 from this one using the delta in `PRESETS_v13_carriers_PLA.md` (the v13 bundle isn't in the repo) |

## `v11/layout/`, the envelope model (v11.2, 22 Sep)

| File | What |
|---|---|
| `layout.py` | envelope model for the whole bot, regenerates `interfaces.json`, `plan.png`, `zstack.png` and `checks.json`, the last isn't committed (`python3 layout.py`, needs `shapely`, `matplotlib`, `numpy`) |
| `interfaces.json` | every frozen number: Z levels, insets, wheel, well, duct, battery, ToF and fixing positions, carrier and frame bosses |
| `plan.png` | plan view, base / hardware / lid |
| `zstack.png` | side view, Z stack |

v11.2 note: motor envelopes stay at the 69.3 mm worst case because the carriers were already printed. The published `layout.py` writes its outputs into whatever folder you run it from, and `plan.png` / `zstack.png` here are regenerated from it (2 Nov 2026).

## Not in this repo

- v13 carrier STLs and the v13 `.bbscfg`.
- The CadQuery build code for the base, lid and clamp ring (`build.py` and modules, `parameters.json`, gate JSONs).
