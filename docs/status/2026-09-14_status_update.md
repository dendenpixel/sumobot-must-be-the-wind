> **Superseded 23 Sep 2026.** This is a 14 Sep snapshot, current build state is in `README.md` & [`docs/status/2026-09-23_first_drive.md`](2026-09-23_first_drive.md). Kept for the reasoning/history.

# SumoBot chassis, status update 14 Sep 2026

Hello again, this is the state of the v11 chassis as of today, written so anyone in the group, or anyone reading the repo later, can follow what happened without digging through the CAD briefs.

## Where we were

v10 came out of Astra as a flat 240 mm octagon with the wheels hanging outboard and the electronics on a tray at Z 38, which was nothing like the sombrero we'd agreed on, so I binned the shape. The process bits stayed: the CadQuery build pipeline, provenance tags on every number, the 3D pressure flood test & the straight-slide battery. The v11 layout was approved on 12 Sep. It's a 249 x 249 superellipse base with a continuous 15° wedge, rim 0.5 mm off the floor, two wheels sealed inside the footprint with the motors staggered ±14 mm, the EDF straight through the roof at (57, 0) & the battery on the roof at the rear, sliding out through a slit in the lid. The T-Display S3 sits on the right wellcap because it turned out not to fit on the roof.

## What got built this round (12 to 14 Sep)

The biggest design change came from a print problem rather than a physics one. Astra found that printing the base roof-down would put the well walls and motor cheeks 28 mm below the bed, and the only way to make that work was a support forest under the whole wedge, which I wasn't going to accept after snapping ribs peeling PLA supports off last time. So the rule is now that the base carries nothing above Z 10.9. The well walls & cheeks became two bolt-on motor carriers, the battery rails became a separate frame, the fan seat got recessed into a boss under the roof & the collar was deleted, so the lid locates on its four M3 bolts instead. Nine printed parts instead of five, every one of them printing right way up with no support. Funnily enough the v10 handover had suggested a removable carrier, so it was right about that one thing.

Base stage (13 Sep): base, carrier L/R & battery frame built in CadQuery, 40 of 40 geometry gates passing, base at 116.8 g. The as-built numbers override the brief, faceplate outer face at |Y| 39, fan boss Ø58, frame bolts at (−78, ±61) & (−43, 0). The base is on the printer now. One thing to watch: the encoder tail gap on the new JGA25-371 motors is about 1.3 mm after the connector, so if it doesn't fit, only the carriers get reprinted, not the base.

Lid stage (13 Sep): lid, wellcap L/R & clamp ring built on the same code base, 60 of 61 gates passing. The one fail is lid mass at 128 g against a 110 g target, which I've accepted for now since the full structure is still around 259 g, under the old v5 figure. The ToF sensors changed the most here, the recessed facets in the brief clashed with the fan and the lug driver bores, so each sensor is now a small nose on the tower with its optical axis at Z 39.9, and the old Z 48 layout points are superseded. The battery slit went to full height at Y ±62, the button moved to (12, 22), and the cable gland & group-panel recess were deleted because neither prints on the bed face.

Lid print profile (13 Sep): PETG with Bambu's Support for PLA/PETG as the interface material, 0.16 layers, 4 walls, 25% infill. The whole lid only needs 572 mm² of support in four thin bands at Z 29.5, 38.7, 44.7 & 51.7, so the profile sets the support threshold at 35° to keep the 4,292 mm² skirt self-supporting, and "on build plate only" has to stay off or none of those bands get support at all.

Wheel hub v4 (14 Sep): the cast silicone ring was bulging over the Ø39 flange & the wheel was rubbing the well wall, but the real problem was assembly. With a closed well the motor goes in from inside, the wheel from outside, and then the grub screw can't be reached. The fix is to open the well to the top, pre-assemble motor + wheel + grub on the bench, & drop it in as a unit. That needs the faceplate M3s driven through the hub, so v4 has two Ø4.5 driver holes at 17 mm c-c, a Ø40 flange and 0.1 mm off the length. Bore fit is still untested, the coupon at Ø3.95 / 4.05 / 4.15 is the next thing to print.

Wellcap +2 mm (14 Sep): the tyre was rubbing the cap ceiling, so both caps got every vertex above z 1.25 shifted up 2 mm, same screws, same engagement. That puts the cap roof at Z 50, so the lid needs checking for at least Z 52 clearance over the wells before it prints.

Bambu presets (14 Sep): after two failed attempts I worked out that Bambu Studio only imports a `.bbscfg` zip with the right envelope (short `2.8.0.6` version string, no `type` or `setting_id` fields), and now four process presets import in one go: Lid PETG, PLA Parts Plate, Hub PLA & Hub ABS. No more retyping 30 settings per part.

Two different files are called wheel hub v3. v4 is derived from the 29-long one, the Ø40 x 34 one is a dead branch.

## Open items

Hubs & the bore coupon (me), encoder connector vs the 1.3 mm tail gap once the motors land, TTGO header pins, the lid-over-wellcap clearance check, and whether the lid's 18 g can come back with thinner walls, 2.0 down to 1.6, if we end up needing the mass.

All in all, the v11 architecture is holding, everything since the 12th has been fit & print fixes rather than shape changes, which is the first time that's been true since v5.
