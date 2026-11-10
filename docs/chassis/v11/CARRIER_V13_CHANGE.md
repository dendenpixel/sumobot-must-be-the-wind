# Carrier v13, open-bottom hoops, straight drop-in (21 Sep 2026)

Base files: `v12_carrier_L.stl`, `v12_carrier_R.stl`. Mesh-edited with manifold booleans, both watertight, single body, consistent winding. Outputs: `v13_carrier_L.stl`, `v13_carrier_R.stl` (**STL not in the repo**). R is the point-mirror of L (x→−x, y→−y), and every number below is L.

**This is the carrier on the bot** (both sides, PLA). Print settings: `../../printing/PRESETS_v13_carriers_PLA.md`. Supersedes `CARRIER_V12_CHANGE.md`. The v12 → v13 entry is in `CHANGELOG.md`.

## Why (root cause of the 30–45° wiggle and the snapped strips)

Measured on the v12 mesh, the three motor-cheek pairs (Y 27–39, 3–15, −31.3…−19.3) are full **U-saddles under the motor**, and at Z 0.5 the channel between them is only ~8 mm wide, so the motor body can only go in from the **top**. v12 slotted the faceplate **downward**, so the Ø7 collar can only go in from the **bottom**. The two contradict each other, the only way in was tilted, spreading the blades (1.5 thick, to Z 22), and the saddles were tied together only by **1.5 × 4 mm strips**, which snapped during assembly. It was a v12 design miss, not an assembly fault.

Also, with the measured motor (Ø24.78 × 58.84, tail at Y −21.04) the third cheek pair touched nothing.

## The change

| | v12 | v13 |
|---|---|---|
| Motor entry | body from top, collar from bottom (contradiction) | **everything from below**, carrier upside down, straight vertical |
| Under the motor | U-saddles, 8 mm opening | **nothing**, motor rests on the base roof as before |
| Retention over the top | friction blades to Z 22 | **2 hoops**: Y 27–37.8 (butts into the faceplate as a gusset) and Y 3–15 |
| Hoop section | — | walls x 0.1–1.35 and 26.65–28.0, cavity half-width / radius **12.65** (0.26 radial on Ø24.78), arc to the 45° tangent, 45° shoulders 1.7 thick, **flat bridge 9.98 wide at Z 25.40**, top Z 27.40 (carrier is 28.1) |
| Between hoops | 1.5 × 4 strips | link walls Z 0–12, same thickness, Y 15–27 |
| Lead-in | — | 0.5 × 45° chamfer at the mouth (bed side) |
| Third cheek pair (Y −31…−19) | present | **deleted** |
| Inner wall outer face | x 0 (touching the other carrier) | x 0.1 (0.2 total between carriers) |
| Faceplate, slot, Ø6.5 driver holes, wellcap bosses, mounts | — | **unchanged** |
| Volume | 15 795 mm³ | **13 988 mm³** (L), 13 982 (R) → 17.3 g solid PLA |

The v12 doc's "15.8 g" doesn't match 15 795 mm³ × 1.24 (= 19.6 g solid). Printed mass is unmeasured, weigh one.

## Verified (boolean intersection volume, both sides)

| Check | Result |
|---|---|
| Motor Ø24.78 × 58.84 seated | 0.000 mm³ |
| Motor swept vertically from Z −40 to seated | 0.000 mm³ |
| Wheel Ø46.8 × 28.9 swept into the well | 0.000 mm³ |
| Ø7 boss swept up the faceplate slot | 0.000 mm³ |
| Motor top 24.89 → bridge underside 25.40 | 0.51 clear |

## Assembly (replaces v12 steps 2–3)

1. Hub + tyre on the shaft (hub v6.2, captive nut, see `../../wheels/WHEEL_HUB_V6_CHANGE.md`).
2. Carrier upside down on the bench. Lower motor + wheel **straight in**: collar into the slot, wheel into the well, body between the hoop walls until it bottoms on the hoop bridges.
3. Long driver through the outer-wall hole, through the hub, 2 × M3 flat-head into the motor.
4. Flip, 4 carrier bolts, tape over the two outer-wall holes.

## Open / assumptions

- **New occupied volume:** Z 22 → 27.4 above each motor for Y 3–15 and 27–37.8. Assumed free (below the carrier top at 28.1). Check nothing on the lid or wiring sits there.
- **Motor Phillips heads (12/6 o'clock, r 8.54, head Ø ~4.5, height unmeasured):** the 6 o'clock one falls in the slot, the 12 o'clock one has no relief in the 1.2 faceplate and must be sitting against it. Not changed in v13 (a relief hole would leave a 1.7 mm ligament over the load-carrying bore top). Measure the head height before touching this.
- Faceplate is still 1.2 with knife-edge countersinks. Hoop 1 now braces it. Not thickened (the tail gap is 16.76, so inboard thickening is possible if needed, a v14 candidate).
- Wall clearance assumes OD 24.78 on both motors. If it binds, the fix is in the slicer (`xy_contour_compensation −0.05`), not a recut.
- Toe of each carrier on the printed base is unmeasured. The first drive's drift to the right lists it as a check.
