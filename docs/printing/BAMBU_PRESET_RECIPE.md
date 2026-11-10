# Bambu Studio — Importable Preset Recipe (verified working)

Status: **confirmed working** — "There are 3 configs imported."
Bambu Studio build: **02.08.02.61**, X1C 0.4 nozzle.

This documents how to hand Bambu Studio a set of process presets as a file, so settings never have to be retyped. Two earlier attempts failed; the reasons are recorded at the bottom so they aren't repeated.

> **The printer json is in the repo** at `docs/printing/assets/X1C_printer_preset.json` (132 keys, `"from": "System"`, `version 2.8.0.6`). Copy it to `printer/Bambu Lab X1 Carbon 0.4 nozzle.json` when assembling a bundle, there's no need to re-export it.

---

## The container: `.bbscfg` (a plain zip)

A bare `.json` will NOT import. The importable unit is a `.bbscfg` zip with this layout — **no directory entries** in the archive (`zip -D`):

```
printer/Bambu Lab X1 Carbon 0.4 nozzle.json     <- docs/printing/assets/X1C_printer_preset.json
process/<Preset Name>.json                      <- one per preset
bundle_structure.json
```

### bundle_structure.json

```json
{
    "bundle_id": "<anything unique>",
    "bundle_type": "printer config bundle",
    "filament_config": [],
    "printer_config": ["printer/Bambu Lab X1 Carbon 0.4 nozzle.json"],
    "printer_preset_name": "Bambu Lab X1 Carbon 0.4 nozzle",
    "process_config": ["process/Name A.json", "process/Name B.json"],
    "version": "02.08.02.60"
}
```

Note the **long** version form here (`02.08.02.60`) — different from the process presets.

### Each process preset json

Required envelope — nothing more, nothing less:

```json
{
    "from": "User",
    "inherits": "0.20mm Standard @BBL X1C",
    "name": "<Preset Name>",
    "print_settings_id": "<same as name>",
    "print_extruder_id": ["1", "1"],
    "print_extruder_variant": ["Direct Drive Standard", "Direct Drive High Flow"],

    ... only the keys you are overriding ...

    "version": "2.8.0.6"
}
```

`version` here is the **short dotted** form `2.8.0.6`. This single field was the cause of both earlier rejections.

Do **NOT** include: `type`, `setting_id`, `instantiation`, `is_custom_defined`, `compatible_printers`. The user's own working export has none of them, and their presence appears to fail the compatibility check.

Values are strings. A handful of keys are **arrays of 2** — get the type right or the import silently drops the key:
`bridge_speed`, `outer_wall_speed`, `inner_wall_speed`, `initial_layer_speed`, `outer_wall_acceleration`, `initial_layer_acceleration`, `support_speed`, `support_interface_speed`, `enable_overhang_speed`,
`overhang_1_4_speed`, `overhang_2_4_speed`, `overhang_3_4_speed`, `overhang_4_4_speed`, `overhang_totally_speed`.

Import via **File → Import → Import Configs…**

---

## Reading a preset back

Bambu stores **only the diff** against the inherited profile. A re-exported preset is much shorter than what was sent — every key matching the base profile is dropped, not lost. `["nil", "10"]` in an array is Bambu's "this extruder variant isn't overridden" sentinel, not corruption.

To confirm what's actually in force, read `Metadata/project_settings.config` from a saved `.3mf` — that's the fully resolved config (581 keys).

If settings appear not to have taken, **check which preset is selected in the dropdown first.** A leading `*` means unsaved modifications to whatever profile is named — frequently not the one just imported.

---

## Getting the reference files

Two different schemas, don't confuse them:

| Source | Gives you | Doesn't give you |
|---|---|---|
| `.3mf` → `Metadata/project_settings.config` | correct **key names** and value types (581 keys, fully resolved) | the preset envelope |
| `.bbscfg` export | the correct **envelope** + a real `printer/` json to copy | only the keys the user overrode |

**You need both.** Ask for the `.bbscfg` first. (The printer json half is now cached — see the note at the top.)

To produce a `.bbscfg`: File → Export → Export Preset Bundle → *Printer preset bundle(.bbscfg)*.

⚠️ Export shows **nothing** until at least one user preset exists. If the dialog says *"Please select at least one printer or filament"*, the user has only a modified system profile (dropdown shows a leading `*`). They must click the 💾 icon beside the process dropdown once to create a user preset — then export works.

---

## Overhang speed band mapping (confirmed)

The five UI rows map to these keys, in order:

| UI row | Key |
|---|---|
| 10% | `overhang_1_4_speed` |
| 25% | `overhang_2_4_speed` |
| 50% | `overhang_3_4_speed` |
| 75% | `overhang_4_4_speed` |
| 100% | `overhang_totally_speed` |

Higher % = more overhanging = the band that protects flat ceilings. Stock is `0 / 50 / 30 / 10 / 10`.

---

## Other useful key names (X1C, this build)

`elefant_foot_compensation` (note the spelling), `xy_hole_compensation`, `xy_contour_compensation`, `precise_outer_wall`, `wall_generator` (`classic` | `arachne`), `support_interface_pattern` (`rectilinear_interlaced`), `support_bottom_interface_spacing`, `support_interface_not_for_body`, `support_object_first_layer_gap`, `support_remove_small_overhang`, `support_critical_regions_only`, `tree_support_wall_count` (this is the "Support wall loops" field), `flush_into_infill`, `flush_into_support`, `enable_prime_tower`, `brim_type` (`no_brim` | `outer_only` | `auto_brim`), `thick_bridges`, `skirt_loops`.

`support_filament` / `support_interface_filament`: `"0"` = Default (same as model), otherwise the **project filament slot index**. Slot numbering is per-project, so this field usually needs checking after loading a preset.

**`filament_shrink` is a FILAMENT key, not a process key** (`['100%','100%']`). Shrinkage compensation cannot be delivered in a `.bbscfg` process preset — it must be set by hand in the filament profile.

---

## Presets currently built

| Preset | For | Defining setting |
|---|---|---|
| `SumoBot Lid PETG SupIF @BBL X1C` | v11 lid, PETG + support interface | `support_on_build_plate_only = 0`, Z gaps `0`, interface spacing `0` |
| `SumoBot PLA Parts Plate @BBL X1C` | multi-part plates, single PLA | Z gaps `0.2`, no prime tower, brim on |
| `SumoBot Wheel Hub PLA @BBL X1C` | wheel hub v4 | `support_on_build_plate_only = 1` (keeps support out of the tyre groove), hole comp `0`, 40% infill |
| `SumoBot Wheel Hub ABS @BBL X1C` | wheel hub v4 in ABS | layer `0.15` (lands Z15.50 exactly), `precise_outer_wall 1`, brim `outer_only 8`, elephant foot `0.2` |
| `SumoBot Wheel Hub v5 ABS @BBL X1C` | wheel hub v5 (superseded) | layer `0.15`, `support_on_build_plate_only = 1` |
| `SumoBot v12 Carriers PLA @BBL X1C` | v12 carriers (superseded) | layer `0.2`, 4 walls, 40 % grid, hole comp `0.15` |
| `SumoBot Battery Frame v2 PLA @BBL X1C` | battery frame v2 | layer `0.16`, **3 walls** (sets the finger spring rate), no support |
| `SumoBot Clamp Ring v2 ABS @BBL X1C` | clamp ring v2 | layer `0.2`, print flipped top-face down, hole comp `0` |
| `SumoBot Wheel Hub v6 ABS @BBL X1C` / `v6.1` | hubs v6, v6.1 (superseded) | layer `0.10`, `support_on_build_plate_only = 1` (lip drooped) |
| `SumoBot Wheel Hub v6.2 ABS @BBL X1C` | **hub v6.2, current** | layer `0.10`, `support_on_build_plate_only = 0` |
| `SumoBot v13 Carriers PLA @BBL X1C` | **v13 carriers, current** | layer `0.2`, `bridge_no_support = 1` for the hoop bridges |

All inherit `0.20mm Standard @BBL X1C`. Bundles on hand are in `hardware/cad/v11/presets/` (index `hardware/cad/README.md`), and each part's analysis is in its own `PRESETS_*.md` here.

---

## Failure log

| Attempt | Result | Cause |
|---|---|---|
| v1 — bare `.json`, guessed schema | 0 imported | no `version` field; wrong container; invented fields |
| v2 — bare `.json`, keys validated against `project_settings.config` | 0 imported | key names were right, but envelope was wrong: `version` in long form, plus `type`/`setting_id`/`instantiation`/`is_custom_defined`/`compatible_printers` present and `print_settings_id`/extruder arrays absent |
| v3 — `.bbscfg` cloned from the user's own export | **3 imported** ✅ | — |

Lesson: ask for the user's `.bbscfg` export **first**. The preset envelope cannot be derived from a 3mf or from general knowledge, and guessing burns several rounds.

---

## Settings only live in the right place

- **Process preset** (`.bbscfg` / dropdown) — layer height, walls, infill, support settings, speeds.
- **Filament preset** — temperatures, cooling, `filament_shrink`.
- **`.3mf` project** — plate arrangement, per-object orientation, painted supports, per-object overrides. Save with File → Save Project As.

All three are needed to fully reproduce a plate.
