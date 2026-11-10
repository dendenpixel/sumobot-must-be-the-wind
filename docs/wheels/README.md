# Wheels

**On the bot now: hub v6.2 (ABS) + cast silicone tyre (Mold Star 15, v1 ring mould), measured OD 46.8.** Hub file `hardware/cad/v11/stl/sumo_wheel_hub_v6_2.stl`, mould `hardware/cad/v11/stl/tyre-ring-mould.stl`, preset `../printing/PRESETS_hub_v6_2_ABS.md`. Cast procedure: `../WHEEL_V1.md` (the mould and cast half is still current).

From v4 on each hub is a mesh edit of the one before it, all in the same frame (motor face at Z 0, axis vertical), so the numbers compare directly.

## Lineage

| Rev | Date | Flange Ø | Length | Bore / flat | Thread | What changed & why | Doc |
|---|---|---|---|---|---|---|---|
| v1 | 5 Sep | — | — | Ø4 D (drawn) | self-tap M3 × 8 | first hub, OpenSCAD, 12 axial ribs, ring stretched on | `../WHEEL_V1.md` |
| v2 | by 8 Sep | Ø39.0 (mesh) | 34.0 | Ø4 D, 3.5 across | radial pilot, Ø4.5 access hole | reprint of v1, measured bore undersize (3.77–3.81 on a 4.10 shaft) | `WHEEL_V1_SPEC.md` (as-measured) |
| v3 | 8 Sep | Ø39 | **29.0** | unchanged | unchanged | too long for the well: seat 30 → 27, flanges 2 → 1 thick, Ø9 × 2.5 counterbore swallows the motor boss | `WHEEL_V3_SPEC.md` |
| ~~v3 alt~~ | 14 Sep | Ø40 | 34 | — | — | **dead branch**, never in the robot | `WHEEL_V3_CHANGE.md` |
| v4 | 14 Sep | Ø40 | 28.9 | Ø4.10 / 1.55 | grub in channel | tyre bulging over the flange, rubbing the well wall, 2 × Ø4.5 driver holes so the faceplate M3s can be driven through the hub | `WHEEL_V4_CHANGE.md` |
| v5 | 15 Sep | Ø40 | 28.9 | Ø4.10 / 1.55 | heat-set insert | driver holes Ø6.5 for the M3 flat-heads in the countersunk v12 faceplate. Printed ABS, fitted, tyre walked over the flange | `WHEEL_HUB_V5_CHANGE.md` |
| v6 | 21 Sep | **Ø43** | 28.9 | Ø4.10 / 1.55 | heat-set insert | lip 1.0 → 2.5 above the ribs so the tyre stays on | `WHEEL_HUB_V6_CHANGE.md` |
| v6.1 | 21 Sep | Ø43 | 28.9 | Ø4.10 / **1.45** | **captive M3 nut**, M3 × 10 | rotational slop, insert pulling out, access hole Ø6 | `WHEEL_HUB_V6_CHANGE.md` |
| **v6.2** | 21 Sep | Ø43 | 28.9 | Ø4.10 / 1.45 | captive M3 nut, M3 × 10 | top lip drooped on print, pad raised, teardrop drum hole, support on the part. **On the bot** | `WHEEL_HUB_V6_CHANGE.md` |

v1's dimensions live in the OpenSCAD source, which isn't in the repo. v2's Ø39.0 is the vertex-exact mesh value (`WHEEL_V3_CHANGE.md`), `WHEEL_V3_SPEC.md` reads Ø38.4 off a section.

## Tyre

- Cast in Mold Star 15 SLOW (Shore 15A) in the printed v1 ring mould, procedure in `../WHEEL_V1.md`.
- Measured on the wheel: tyre ID 38.1 (seated on the ribs), **OD 46.8**, wall ≈ 4.35.
- Cast ring is 30 wide, trimmed to the 27 seat (`WHEEL_V3_SPEC.md` §3). Trimmed width is unmeasured.

## Open

- Hub bore coupon (Ø3.95 / 4.05 / 4.15 printed) against the new Ø3.99 shaft. The CAD bore is still 4.10.
- Wheel mass with tyre, unweighed.
