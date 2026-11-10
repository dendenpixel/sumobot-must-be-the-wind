> **Superseded 14 Sep 2026.** Dead branch, never in the robot, hub v4 was built from the 29-long v3 in `docs/wheels/WHEEL_V3_SPEC.md` and the current hub is v6.2 (`docs/wheels/WHEEL_HUB_V6_CHANGE.md`). Kept for the reasoning/history (the rib-height finding).

# Wheel hub v3 — flange OD change (14 Sep 2026)

Made by editing the `sumo_wheel_hub_v2.stl` mesh directly, not re-modelling. 4128 of 25980 vertices moved; the other 21852 are bit-identical to v2.

## The change

| | v2 | v3 |
|---|---|---|
| Flange OD (the lips) | Ø39.0 | **Ø40.0** |
| Lip height above the bed | 2.0 | **2.5** |
| Lip height above the 12 bead ribs | 0.46 | **0.96** |
| Tyre bed Ø | Ø35.0 | Ø35.0 |
| Bed width (between flanges) | 30.0 | 30.0 |
| Flange thickness (axial, each) | 2.0 | 2.0 |
| Bead ribs (12 off, every 30°) | Ø38.08 | Ø38.08 |
| Overall height | 34.0 | 34.0 |
| Bore, D-flat, grub screw, spokes | — | untouched |
| Volume / PLA mass | 15897.6 mm³ / 19.71 g | 16145.7 mm³ / **20.02 g** |

Mass penalty ×2 wheels = **+0.62 g** against the 990 g budget. Noise.

## Cross-check against v2

- Watertight: both true. Winding consistent: both true. Euler number unchanged at −4 (same topology, no holes opened).
- Triangle and vertex counts identical (8660 / 4326) — no remesh.
- Only vertices at exactly r = 19.500 moved, and only radially: max displacement 0.500 mm, z displacement 0.000.
- Moved vertices live only at z = 0, 2, 32, 34 — i.e. the two flange OD cylinders and the two outer face rings. Nothing else.
- Feature radii 17.5 / 15.1 / 8.0 / 2.05 / 1.55 / 19.0 / 19.041 present in identical counts in both files.

## As-measured geometry of v2 (recorded, since it wasn't written down)

Z=0 is the motor face. Profile, outer to inner:

```
z 0.0 – 2.0     r 19.5   bottom flange (2.0 thick)
z 2.0 – 32.0    r 17.5   tyre bed, 30.0 wide
                r 19.04  12 axial bead ribs, every 30°, z 2–32
z 32.0 – 34.0   r 19.5   top flange (2.0 thick)
z 15.5 – 18.5   r 8.0 – 15.1  spoke web
central         r 1.55 / 2.05 bore + D-flat, grub screw boss at z ≈ 6.8–11.4
```

This fills the **tyre width (silicone, axial)** blank in `WHEEL_V1_SPEC.md` from the CAD side: the channel is 30.0 wide. v1's measured tyre bed was 28.98.

## Open risk — the bead ribs, not the lips

The tyre's inner surface rides on the 12 ribs at Ø38.08, not on the Ø35 bed. So the wall the tyre actually has to climb over was only **0.46 mm** in v2, which is the real reason it walked off — not the 2.0 mm figure the bed suggests. v3 doubles that to 0.96 mm.

If v3 still peels, the fix is one of:

1. Cut the ribs back (Ø38.08 → Ø36.5) so the tyre seats deeper in the channel and the full lip does the work. Bigger effect than another 0.5 mm on the flange.
2. Keep going on flange OD — Ø41, Ø42. Cheap to test, but each step makes the tyre harder to stretch on.

Also note: the measured tyre ID is 38.1–38.68, so it now has to stretch over Ø40 lips instead of Ø39. Fitting will take more thumb. That extra tension is working in the right direction for retention, but check it doesn't deform the lip outward on a PLA print.
