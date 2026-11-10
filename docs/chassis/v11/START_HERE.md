# SumoBot v11 — START HERE

Owner: Den. This folder is the single source of truth for the v11 chassis. Read this file, then `CHANGELOG.md`, then whatever the current task needs. Do not go looking for v5–v10 material; the lessons from it are already baked in here, and the old briefs contradict each other.

## What v11 is

A sombrero: 249 × 249 superellipse base (pressure vessel, 15.14° continuous wedge, rim 0.5 mm off the floor) + a leaning-tower lid with a flat top at Z 65.6. Two wheels in sealed wells inside the footprint, motors staggered ±14 mm, EDF straight through the roof at (57, 0), battery on the roof at the rear sliding out through a slit in the lid, electronics flat on the roof, LilyGO T-Display S3 (measured 62.3 × 25.65 × 6.88) planned for the right wellcap, 7 ToFs and the PCF8574 in the lid, one 4-wire plug between lid and base.

**v11.1 rule (12 Sep evening): the base carries nothing above Z 10.9.** Well walls + motor cheeks are two bolt-on carriers; rails + stop + XT60 bracket are one battery frame; the fan lip seat is recessed into a roof boss; no collar (the lid locates on its four M3 bolts). Nine printed parts: base, lid, carrier L, carrier R, battery frame, wellcap ×2, clamp ring, hub ×2.

## Printed parts: current revision

Everything below is the revision on the bot as of 23 Sep 2026. Files are under `hardware/cad/v11/` (see `hardware/cad/README.md`).

| Part | Rev | File in repo | Material | Preset | On bot |
|---|---|---|---|---|---|
| Base | v11 | `stl/v11_base.stl`, `step/v11_base.step` | PLA | `REPORT_base_stage.md` §5 | yes |
| Lid | v11 | `stl/v11_lid.stl`, `step/v11_lid.step` | PETG translucent | `SumoBot Lid PETG SupIF`, `../../printing/LID_PRINT_PROFILE.md` | yes |
| Carrier L / R | **v13** | STL not in the repo | PLA | `SumoBot v13 Carriers PLA`, `../../printing/PRESETS_v13_carriers_PLA.md` | yes |
| Wellcap L / R | **+2 mm** | `stl/v11_wellcap_L_plus2.stl`, `stl/v11_wellcap_R_plus2.stl` | PETG (as designed) | none (top face down, `REPORT_lid_stage.md`) | yes |
| Battery frame | **v2 (clip)** | `stl/v11_battery_frame_v2_clip.stl` | PLA | `SumoBot Battery Frame v2 PLA`, `../../printing/PRESETS_battery_frame_v2_PLA.md` | yes |
| Clamp ring | **v2 rev B** | `stl/clamp_ring_v2_shrinkcomp.stl` (+ `earslot` reserve) | ABS | `SumoBot Clamp Ring v2 ABS`, `../../printing/PRESETS_clamp_ring_v2_ABS.md` | yes, fan not mounted |
| Wheel hub ×2 | **v6.2** | `stl/sumo_wheel_hub_v6_2.stl` | ABS | `SumoBot Wheel Hub v6.2 ABS`, `../../printing/PRESETS_hub_v6_2_ABS.md` | yes |
| Tyre ×2 | cast | mould `stl/tyre-ring-mould.stl` | Mold Star 15 silicone (mould PLA) | cast procedure `../../WHEEL_V1.md` | yes, OD 46.8 |

Change records: `CARRIER_V13_CHANGE.md`, `WELLCAP_PLUS2.md`, `BATTERY_FRAME_V2_CHANGE.md`, `CLAMP_RING_V2_CHANGE.md`, `../../wheels/WHEEL_HUB_V6_CHANGE.md` (lineage in `../../wheels/README.md`).

## Files

| File | What | Status |
|---|---|---|
| `CAD_BUILD_BRIEF.md` | The CAD build prompt (v11.1), as issued 12 Sep | historical, as-built numbers in the REPORTs override it |
| `hardware/cad/v11/layout/interfaces.json` | Every frozen number: Z levels, insets, wheel/well/duct/battery/ToF/fixing positions, carrier/frame bosses | **v11.2, 22 Sep** |
| `hardware/cad/v11/layout/layout.py` | The envelope model that generates `interfaces.json`, `plan.png`, `zstack.png`, `checks.json`. `python3 layout.py` regenerates all of them; needs `shapely`, `matplotlib`, `numpy` | v11.2, 0 overlaps |
| `LAYOUT_PASS.md` | The decisions and the number behind each, wiring tree, measurement list | 12 Sep |
| `REPORT_base_stage.md` | **Base-stage build report**: the 10 deviations from the brief and why, §4 decisions, 40-gate table, masses, print settings, open questions | 12 Sep |
| `REPORT_lid_stage.md` | Lid, wellcaps, clamp ring rev A build report, 60/61 gates | 13 Sep |
| `CHANGELOG.md` | What each version changed and why; Den's verdicts | append, never rewrite |
| `hardware/cad/v11/` | STL per part in print orientation, STEP for base, lid and assembly, presets, layout | see `hardware/cad/README.md`. CadQuery build code not included |
| `../v10_POSTMORTEM_and_prompt_spec.md` | Why v10 failed, prompt-writing rules, parts register at the time | historical |

## Status (23 Sep 2026)

- Layout: approved. Re-run as **v11.2** on 22 Sep for the first-drive wiring, against the printed base, zero new overlaps.
- **All printed parts on the bot are the latest revisions** (table above): v11 base, v11 lid in PETG translucent, v13 carriers, wellcaps +2, battery frame v2, clamp ring v2, hub v6.2 with cast tyres.
- **Parts: everything ordered has arrived.** The JGA25-371 130 rpm motor pair and the XFly 1413 EDF were measured 17 Sep, the T-Display S3 on 12 Sep, everything else 11–12 Sep. Register: `../../hardware/MEASURED_PARTS.md`.
- **First drive build (drive only, 23 Sep):** JGA25-371 pair in the v13 carriers, hub v6.2 wheels, DRV8871 drivers, Brain on a breadboard on top of the bot for now (it moves to the protoboard next). The 23 Sep weigh-in photo shows the lid on, but no ToFs, line sensors or fan are fitted yet. Motors and encoders were both confirmed working after the 23 Sep rework. The bot runs 1 m forward and back on the timed build and drifts right. Mass 765 g on 23 Sep before sensors.
- Base + carrier L/R + battery frame BUILT in CAD 13 Sep, 40/40 gates PASS, base 116.8 g. As-built numbers in `REPORT_base_stage.md` §1 override the brief.
- Lid + wellcap L/R + clamp ring BUILT in CAD 13 Sep, 60/61 gates PASS, the one FAIL is lid mass 128 g vs ≤ 110 target (accepted). ToF geometry changed to "noses" at optical axis Z 39.9, the Z 48 layout points are superseded. See `REPORT_lid_stage.md`.
- Wellcaps: the **+2 mm** caps are on the bot, top ~Z 51.2. Lid fits over the +2 caps as assembled 23 Sep, measured clearance still to record. Caps have plain tops, no Brain pocket.
- Wheel hub: **v6.2** (supersedes v5). Captive M3 nut + M3 × 10 grub, Ø43 flanges. Round bore still Ø4.10 in CAD, the 4.05 coupon against the Ø3.99 shaft is open.
- Carriers: **v13** (supersedes v12, which couldn't be assembled straight and snapped its tie strips). v13 STLs aren't in the repo.
- Print profiles: `../../printing/` (one preset doc per part, `.bbscfg` recipe) and the bundles in `hardware/cad/v11/presets/`.
- Not built yet: coupons, final assembly gates.
- Closed 17 Sep: new-motor encoder connector exits radially, tail gap is 16.76. New-motor mass 96.2 g each incl. loom.
- Open measurements: **EDF overall height** (one bench-to-nub-tip reading, it gates whether the fan seat gets reamed at all), mass, intake end, ear dimensions and position. **Motors:** boss height above the faceplate, D-flat length from the shaft tip, Phillips head height, encoder connector pitch and cable length, label text, encoder cap Ø. **Also:** button panel grip thickness, hole-shrink coupon (assumed +0.21), carrier toe on the base.
- Fan: one EDF, no spare, tested on the finished bot only, fan mated last. See `../../DOWNFORCE_FAN.md`.
- Pins: `docs/PIN_MAP.md` is for the T-Display S3 (17 Sep).

## Working rule

A CHANGELOG entry goes in *before* anything changes, the layout model is re-run if the layout moves, and only then do the solids get touched. Rule from the postmortem: **patch, never rewrite.** A fresh build only when the architecture changes.
