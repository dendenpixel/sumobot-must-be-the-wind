> **Superseded 21 Sep 2026 for the hub.** The hub on the bot is v6.2 (`docs/wheels/WHEEL_HUB_V6_CHANGE.md`), the mould and cast procedure below is still the current one and the tyres on the bot were cast with it. Kept for the reasoning/history.

# Wheel v1 — cast silicone ring on a printed hub (5 Sep 2026)

Build procedure for the in-house wheel decided in `WHEEL_TYRE.md` section 5.

## Files

| File | What | Print |
|---|---|---|
| `hardware/cad/wheel_v1.scad` | parametric source (OpenSCAD). Change the numbers at the top, F6, export STL | — |
| `hardware/cad/hub_v1.stl` | HUB | ABS or PETG, 1 per wheel (2 total) |
| `hardware/cad/mould_v1.stl` | MOULD | PLA, 1 total, reused |
| `hardware/cad/ring_v1.stl` | the cast ring, reference geometry only | **do not print** |

> Updated 23 Sep: the mould is in the repo as `hardware/cad/v11/stl/tyre-ring-mould.stl`. The v1 hub, the ring
> reference and the OpenSCAD source aren't in the repo, the current hub is `hardware/cad/v11/stl/sumo_wheel_hub_v6_2.stl`.

## Print — HUB (ABS / PETG)

- Orientation: **as exported** (wheel axis vertical, motor face on the bed). Do not rotate.
  Coin orientation puts drive torque into in-plane shear; standing splits on a layer line.
- 0.16 mm layers, 5 walls, 40 % gyroid, 250-255 C, part cooling <= 40 %.
- Supports ON (normal or tree). They only touch the 2 mm ledge under the top flange.
- Z-seam painted onto the outer drum, away from the D-flat side.
- **Before printing the hub:** print a bore coupon at 4.00 / 4.10 / 4.20 and test it on the
  actual motor shaft. Set `shaft_d` to the one that slides on snug. Default 4.10.

## Print — MOULD (PLA)

Orientation as exported (base on bed, open trough up). 0.2 mm, 3 walls, 20 %, no supports.

## Cast — Mold Star 15 SLOW, 1:1

1. Masking tape over the two push-out holes on the underside of the mould.
2. Thin smear of Vaseline on the sleeve inner wall, the core outer wall and ribs, and the
   trough floor.
3. 12 mL Part A + 12 mL Part B per ring (24 mL; a pair is 48 mL, so mix 50). Stir 3 min
   scraping sides and bottom, pour into a second cup, stir 1 min more.
4. Pour a thin stream from ~30 cm into ONE spot until level with the SLEEVE top. The core
   stands 2 mm higher, so you cannot spill into it.
5. Tap the mould on the bench for 2 min. Leave 4 h (longer is fine).
6. Peel the ring's outer edge inward off the sleeve wall, then lift straight up. The ribs are
   axial so it lifts free. Use a dowel through the push holes if it fights you.
7. Trim flash off the top face with a razor. Wipe with IPA.

## Fit

- Ring as cast: ID 33, OD 43. Stretches onto the 35 mm hub -> **~45 mm installed** (predicted). Measured on the bot
  the tyre OD is **46.8** (`docs/wheels/WHEEL_V1_SPEC.md`), which is the number to use.
- Line the 12 grooves inside the ring up with the 12 ribs on the hub and work it on like a
  bicycle tyre. It sits between the two flanges.
- Set screw (v1 hub only, v6.2 uses a captive nut and M3 × 10, see `docs/wheels/WHEEL_HUB_V6_CHANGE.md`): M3 x 8 into the radial hole on the flat side of the boss. It self-taps the
  2.5 mm hole in ABS/PETG. Tighten onto the shaft FLAT.

## Verified numbers

| | Volume | Mass |
|---|---|---|
| hub | 15.9 mL | 16.6 g ABS |
| mould | 26.9 mL | 33 g PLA |
| ring | 17.9 mL | ~20.6 g silicone |
| **wheel** | | **~37 g each, ~74 g the pair** |

12 ribs x 1.5 x 30 mm give a torque capacity above 4 N.m against 0.4 N.m required — 10x.

## Materials

| Product | Shore A | Pot life | Kit | AUD | Perth |
|---|---|---|---|---|---|
| **Mold Star 15 SLOW** (Smooth-On) | 15 | **50 min** | 900 g | **52.00** | **U Resin, Maddington — pickup, in stock** |
| U Resin Slow Set Silicone | 20 | ~30 min | 2 kg | 115.00 | U Resin, Maddington |
| Mold Star 22T | 20 | 6 min | 900 g | 72.00 | U Resin — pot life too short |
| PinkySil Fast Set | 20 | 6 min | 500 g | 45.00 | Composites Warehouse, O'Connor — pot life too short |

Mold Star 15 SLOW is the only product that is soft enough, has a usable pot life for a first
attempt, and can be picked up in Perth. **A 6 min pot life is not enough for a first cast.**

- **U Resin**, Maddington 6109, by appointment.
- **Composites Warehouse**, O'Connor 6163 — (08) 9331 5513, Mon-Fri 09:00-16:30.

PLA does not inhibit platinum-cure silicone, so casting in the printed mould is fine.
(SLA resin does inhibit it — do not use a resin-printed mould.)

## Dead ends — do not re-investigate

- **Oogoo / caulk tyres.** One-part sealants only cure a few mm deep, so a 20-25 mm solid
  ring will never cure through. Selleys Roof & Gutter is neutral-cure, which is the wrong
  chemistry for the cornstarch trick, and cures to A32 before filler — expect mu 0.45-0.60,
  worse than a rubber band. Buy Selleys **Glass** Silicone (acetoxy) and use it for the
  **skirt**, not for tyres.
- **Perth retail** (Bunnings, Repco, Supercheap, Spotlight, Clark Rubber): nothing usable.
  Plasti Dip is 0.1-0.2 mm per coat, ~50 coats. Nitrile O-ring cord is ~70A, too hard.
  Silicone baking mats are fibre-reinforced.
- **AliExpress bare competition tyres:** three independent search passes in Chinese and
  English, all nothing. AliExpress semantically remaps the queries. Do not re-run it.

## Interim tyre for the early drive tests (not used, the cast tyres were ready for the 23 Sep first drive)

Rubber bands No. 64, 4 stacked per wheel for ~24 mm width, ~AU$7 from Officeworks.
Claimed mu 0.6-0.8, never measured by us. Good enough for a first drive, which
needs nothing that is still shipping.
