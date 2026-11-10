> **Superseded 14 Sep 2026.** The current hub is v6.2 (`docs/wheels/WHEEL_HUB_V6_CHANGE.md`, lineage in `docs/wheels/README.md`), the tyre trim procedure in §3 still applies. Kept for the reasoning/history.

# SumoBot wheel v3 (8 Sep 2026) — shorter hub, trimmed ring. Base unchanged.

Problem (Den, 8 Sep, photo 5): the assembled wheel is too long axially for the wheel well. Diameter is
fine. He measures the wheel at ~33 across and the well opening at ~31 and wants real clearance; the
silicone ring "could lose a mil or two".

## 1. Numbers, measured

| Item | Source | Value |
|---|---|---|
| Hub v2 overall length | `sumo_wheel_hub_v2.stl`, sectioned | **34.0** = 2.0 flange + 30.0 ring seat + 2.0 flange |
| Hub v2 drum / ribs / flanges | same | drum ≈ Ø34.6 with 12 axial ribs to Ø38, end flanges Ø38.4 × 2.0 wide (section reading, the vertex-exact mesh value is Ø39.0 per `WHEEL_V3_CHANGE.md`) |
| Hub v2 core | same | Ø16 × 20 long; Ø4 D-bore (flat at 1.75 from centre = 3.5 across), bore full depth 20; 3 mm web Z 15.5–18.5 |
| Hub v2 set screw | same | radial pilot at Z 9.0 from the motor face, on the D-flat side, reached through a Ø4.5 access hole in the drum |
| Ring as cast (v1 mould) | `../WHEEL_V1.md` | 30 wide, ID 33 / OD 43 → stretches to ~Ø45 on the hub |
| Wheel-well slot, as modelled (v5 housing) | housing mesh, X = 14 section | faceplate inner face Y 39.5 → outer-wall inner face Y 71.4 = **31.9** (Den eyeballs the print at ~31) |
| Motor boss through the Ø8 faceplate hole | JGA25-371 drawing, Ø7 boss | protrudes ≈ 2 mm past the faceplate — **caliper this one number before printing** |

So a flat-faced 34 mm hub needs 36 mm of slot and has 31.9. Two things fix it: shorten the hub, and swallow
the motor boss inside the hub instead of standing off it.

## 2. Wheel v3

| Parameter | v2 | **v3** | Why |
|---|---|---|---|
| Overall hub length | 34.0 | **29.0** | 31.9 − 29.0 = 2.9 mm total → ~1.4 mm per side nominal, ~1 mm per side if the slot really printed at 31 |
| Ring seat (between flanges) | 30.0 | **27.0** | ring loses 1.5 mm per face — Den's "a mil or two". Grip is μ·N; a 10 % narrower patch changes nothing |
| Flanges | 2.0 wide × Ø38.4 | **1.0 wide × Ø38.4** | still a positive stop; the ring is stretched on (ID 33 on Ø35), it isn't walking anywhere |
| Motor-face counterbore | none | **Ø9.0 × 2.5 deep**, concentric with the bore | motor's Ø7 boss disappears inside; hub face can sit ~0.5 mm off the faceplate. If the boss calipers > 2.5, deepen the counterbore — do NOT lengthen the hub |
| Bore | Ø4 D, 20 deep | unchanged | shaft is 12 long; engagement Z 2.5–12 |
| Set screw | Z 9.0 | unchanged | shaft D-flat runs Z 4–12 from the faceplate → screw still lands on the flat |
| Drum, ribs, web, access hole | as v2 | unchanged | |
| Track (ring centre-plane) | — | moves inboard 1.5 mm per side (Y ≈ ±55.5 → ±54) | irrelevant to handling |

Fit budget, per side, nominal slot 31.9: faceplate gap 0.5 (with the counterbore) + hub 29.0 + outer-wall
gap 2.4 → the wheel can float ±1 mm axially. Good — the set screw sets the position, not the walls.

## 3. Tyre — trim, don't recast (Den: "you choose")

Trim the existing 30 mm cast rings to **27.0**: 1.5 mm off **each** face, not 3 off one (keeps the ring
centred on the ribs).

1. Mark 1.5 mm in from each face with a fine marker at 4 points; join with a strip of masking tape as a fence.
2. Fresh snap-off / scalpel blade, ring lying flat on a cutting mat, blade vertical against a steel rule.
   Light passes, let the blade do the work — silicone tears if you push. Rotate the ring, don't drag the rule.
3. IPA wipe. A slightly wavy face is fine; it's the outboard edge, not the contact patch.

Plan B (recast, only if the cut is ragged): same v1 mould, **no new print** — the ring height is set by the
pour level. Put a tape line inside the sleeve 3 mm below its top, pour to the line: ≈ 21.6 mL per ring
(10.8 A + 10.8 B) instead of 24. Everything else in the v1 cast procedure unchanged.

## 4. Change list for the v3 hub

Same coordinate frame as v2 (motor face on Z = 0, axis vertical); everything not listed here is unchanged.

```

1. Overall length 34.0 → 29.0. The ring seat between the two flanges is now 27.0 (was 30.0);
   each flange is 1.0 wide (was 2.0), same Ø38.4. So: flange Z 0..1.0, ring seat Z 1.0..28.0,
   flange Z 28.0..29.0. The 12 axial ribs shorten with the seat (27.0 long).
2. Add a counterbore in the motor face: Ø9.0 × 2.5 deep, concentric with the shaft bore, open at
   Z = 0. Parameter motor_boss_depth = 2.5 (caliper the motor's Ø7 boss protrusion through the
   faceplate and set this ≥ that + 0.5).
3. Everything else unchanged: core Ø16 × 20, Ø4 D-bore (3.5 across the flat) 20 deep, 3 mm web,
   radial M3 set-screw pilot at Z 9.0 on the D-flat side with its Ø4.5 access hole through the drum.
   CONSTRAINT: set-screw centre Z must lie within the shaft's D-flat range Z 4.0..12.0 measured from
   the hub's motor face INCLUDING the counterbore (i.e. from Z 0) — report it.
4. SELF-CHECK lines: overall length (expect 29.00) · seat width (27.00) · flange width ×2 (1.00) ·
   flange OD (38.4) · counterbore Ø and depth (9.0 / 2.5) · bore Ø and across-flat (4.0 / 3.5) ·
   set-screw Z (9.0) · rib count (12) and rib length (27.0) · volume and mass at 1.27 g/cm³ PETG ·
   open-edge count (0).
5. Print notes unchanged from v2 (PETG/ABS, axis vertical, motor face on the bed, 0.16 layers,
   5 walls, 40 % gyroid, supports only under the top flange). Print a bore coupon first if the
   shaft_d changed since v2.
```

## 5. Check before it goes to the printer

Drop the v3 STL in chat and it gets sectioned the same way as v2: total 29.0, seat 27.0, counterbore
Ø9 × 2.5, set screw at Z 9. Then on the bench: hub on the shaft with the ring trimmed, into the well —
expect ~1 mm daylight each side.
