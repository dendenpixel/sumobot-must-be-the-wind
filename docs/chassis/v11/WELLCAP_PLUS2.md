# Wellcap +2 mm ceiling (14 Sep 2026)

**On the bot (23 Sep).** Files: `hardware/cad/v11/stl/v11_wellcap_L_plus2.stl`, `hardware/cad/v11/stl/v11_wellcap_R_plus2.stl`, derived from `v11_wellcap_L/R.stl` by a vertex shift, no remesh. Both watertight.

**Why:** the silicone tyre was rubbing the cap ceiling. Den asked for +2 mm.

**As-built v11 cap (mesh coords, printed ceiling-down):** 1.2 plate at z 0–1.2 = the roof over the tyre; perimeter skirt and four screw bosses stand off it to z 8.7 and land on the well-wall tops. Bosses: Ø3.6 through, Ø6.5 × 2.1 head pocket on the outer face, boss body 6.6 long.

**Change:** every vertex above z 1.25 moved +2.0 in z. Skirt 7.5 → 9.5 tall, overall 8.7 → 10.7. Head pocket 2.1 → 4.1 deep; boss body still 6.6, so **same screws, same engagement**, head sits 2 mm deeper. Mass +0.5 g per cap. Roof in the robot rises Z 48 → 50 (underside); lid inner surface over the wells must still be ≥ Z 52 (I6 in the v6 prompt) — check the lid clears the new cap top at Z ~51.2.

The 0.45 mm pocket wall between plate top and old pocket floor is now 2.45 tall at the same thickness — cosmetic, but watch it on the first print.
