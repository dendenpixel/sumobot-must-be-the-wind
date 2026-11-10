> **Superseded 15 Sep 2026.** Replaced by hub v5 and then v6.2 (`docs/wheels/WHEEL_HUB_V6_CHANGE.md`). Kept for the reasoning/history.

# Wheel hub v4 — driver holes, wider lip, trimmed face (14 Sep 2026)

Base file: `sumo_wheel_hub_v3.stl` — the **29-long** v3 from `WHEEL_V3_SPEC.md` (Ø39 flanges), NOT the Ø40 × 34 "v3" in `WHEEL_V3_CHANGE.md`. Two files carry the v3 name; this lineage is the one in the robot.

Mesh-edited (vertex moves + one manifold boolean), not re-modelled. Output `sumo_wheel_hub_v4.stl`, watertight.

## Why

1. Cast silicone ring runs slightly oversize → bulges over a Ø39 flange that only stands ~0.5 mm proud of the Ø38 bead ribs.
2. Wheel rubs the wheel-well side wall. Den asked for 0.1 narrower.
3. Assembly deadlock: closed wheel well means motor goes in from inside, wheel from outside, and then the grub screw is unreachable. Fix is to open the well to the top (soldering iron / heat gun), pre-assemble motor + wheel + grub on the bench, drop in as a unit — which then needs the faceplate M3 screws reachable *through* the wheel.

## The change

| | v3 (29-long) | v4 |
|---|---|---|
| Flange OD | Ø39.0 | **Ø40.0** (688 verts at r 19.5 → 20.0, radial only) |
| Lip above bead ribs | ~0.5 | **~1.0** |
| Overall length | 29.0 | **28.9** (outer face z 29 → 28.9; motor face untouched) |
| Outer flange thickness | 1.0 | 0.9 |
| Driver through-holes | none | **2 × Ø4.5 axial, at r 8.5 on ±y (17.0 c-c), full length** |
| Bore Ø4.10 / flat 1.55, counterbore Ø9.2 × 2.5, grub channel (+x, z≈9), ribs, web | — | untouched |
| Volume / PLA @1.24 | 13939 mm³ | 13735 mm³ / **17.0 g** |

Holes sit 90° from the D-flat so they clear the grub-screw channel, and inside the drum (r < 15.1) so the tyre never sees them. Wall between bore and hole ≈ 4.2 mm. Verified by point-containment along the hole axis at z 0.5–28: clear full length, solid either side.

Hole is Ø4.5 not Den's "M4 hole" because the screw **head** has to pass through the hub (hub face sits ~0.5 mm off the chassis wall). Measured heads on the fitted Phillips pair were ~3.4–4.8. If the real screws are standard 5.5 pan heads, go to Ø6 — that still leaves ~3.4 mm bore wall but only ~0.9 mm to the counterbore at z < 2.5; consider a shorter counterbore-side relief instead.

## Assembly order this enables

1. Grub screw onto the shaft flat on the bench, wheel ~0.5–1 mm off where the chassis wall will be.
2. Drop motor + wheel into the (now top-open) well.
3. Rotate wheel until the two holes line up with the faceplate tapped holes; long Phillips / 4 mm hex extension through the hub; drive both M3s.
4. Tape over the cut in the well.

**No spacer** between wheel and chassis wall — the grub screw sets axial position; the counterbore already swallows the motor boss. A spacer touching the wall would just be a rubbing face.

## Not changed / still open

- **Bore fit — open.** No fit report on the current bore yet. Coupon at Ø3.95 / 4.05 / 4.15 still the recommended path; do not go past ~0.15 interference on PLA.
- 0.1 mm off the length is within print noise. If it still rubs, the tyre (30 wide ring in a 27 seat) is the more likely culprit than the hub — check the ring isn't overhanging the flanges.
