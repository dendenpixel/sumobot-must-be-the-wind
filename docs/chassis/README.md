# Chassis docs

Start at `v11/START_HERE.md`, which has the table of every printed part and the revision on the bot. v11 is the current chassis, and the CAD files are in `hardware/cad/v11/` (index `hardware/cad/README.md`).

| Folder / file | What |
|---|---|
| `v11/START_HERE.md` | Current state, printed-parts table, open measurements |
| `v11/CHANGELOG.md` | Every change since v10 and why (append-only) |
| `v11/CARRIER_V13_CHANGE.md` | Current carriers, open-bottom hoops, straight drop-in |
| `v11/BATTERY_FRAME_V2_CHANGE.md` | Current battery frame, rear snap fingers |
| `v11/CLAMP_RING_V2_CHANGE.md` | Current EDF clamp ring, 3 mm gasket |
| `v11/WELLCAP_PLUS2.md` | Current wellcaps, +2 mm ceiling |
| `v11/LAYOUT_PASS.md`, `v11/REPORT_base_stage.md`, `v11/REPORT_lid_stage.md` | The layout decisions and the two CAD build reports behind the v11 parts |
| `v11/CAD_BUILD_BRIEF.md` | The prompt the v11 CAD was built from (12 Sep), historical |
| `v10_POSTMORTEM_and_prompt_spec.md` | Why v10 came out wrong and the prompt rules that fixed it, plus the parts register at the time |
| `archive/` | v5–v9 postmortems and handovers. They contradict each other, read only for history |

Related: `../wheels/` (hub lineage v1 → v6.2, cast tyre, see its README), `../hardware/` (measured parts, mass budget, wiring), `../printing/` (one preset doc per part, Bambu recipe), `../status/` (dated status updates).

## What's superseded

Each of these carries a banner on its first line pointing at what replaced it.

| Doc | Replaced by | Why kept |
|---|---|---|
| `../GEOMETRY.md` | `v11/` (249 superellipse, no claw, no lidar) | the 4 Sep shape reasoning |
| `../WHEEL_TYRE.md` | `../wheels/README.md` for the hub, `../hardware/MEASURED_PARTS.md` for motors & pack | the tyre stiffness, μ and diameter trade study still holds |
| `../WHEEL_V1.md` (hub half) | `../wheels/WHEEL_HUB_V6_CHANGE.md` | the mould and cast procedure is still the current one |
| `../DOWNFORCE_FAN.md` (plenum geometry, skirt, test method) | `v11/` for the plenum, one-shot on-bot test | 3S derate, thermal rule, fan choice still current |
| `v11/CARRIER_V12_CHANGE.md` | `v11/CARRIER_V13_CHANGE.md` | driver-hole and down-slot reasoning carried into v13 |
| `../wheels/WHEEL_HUB_V5_CHANGE.md` | `../wheels/WHEEL_HUB_V6_CHANGE.md` | driver-hole sizing |
| `../wheels/WHEEL_V4_CHANGE.md`, `../wheels/WHEEL_V3_SPEC.md` | hub v6.2 | lineage |
| `../wheels/WHEEL_V3_CHANGE.md` | nothing, dead branch never in the robot | record of the rib-height finding |
| `../printing/PRESETS_v5hub_v12carriers.md` | `../printing/PRESETS_hub_v6_2_ABS.md`, `../printing/PRESETS_v13_carriers_PLA.md` | orientation analysis |
| `v11/CAD_BUILD_BRIEF.md` | as-built numbers in the REPORTs and CHANGELOG | the prompt as issued |
| `v10_POSTMORTEM_and_prompt_spec.md`, `archive/*` | `v11/` | history |
