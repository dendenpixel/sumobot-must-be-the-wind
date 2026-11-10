> **Superseded 21 Sep 2026.** Hub v6.2 is on the bot (`docs/wheels/WHEEL_HUB_V6_CHANGE.md`), v5 printed in ABS at `filament_shrink` 100 % and fitted, but the tyre walked over its Ø40 flange and the heat-set insert pulled out. Kept for the reasoning/history.

# Wheel hub v5 — driver holes opened to Ø6.5, keyholed into the counterbore (15 Sep 2026)

Base file: `sumo_wheel_hub_v4.stl` (`WHEEL_V4_CHANGE.md`). Mesh-edited with manifold booleans, same method as v4 — not re-modelled. Output `sumo_wheel_hub_v5.stl`, watertight. 16.5 g.

**v5 supersedes v4.** v4 is the last hub that will fit through the old open-topped well procedure; v5 is the hub that goes with the v12 carriers, and it is the one to print. This change was made in the same pass as the v12 carriers — the carrier-side numbers and the assembly sequence are in `../chassis/v11/CARRIER_V12_CHANGE.md`, and the print preset is `../printing/PRESETS_v5hub_v12carriers.md`.

## Why

v4's Ø4.5 driver holes were sized against the Phillips heads measured on the fitted pair (~3.4–4.8 mm). The v11/v12 carrier faceplate is **countersunk**, so the screw that goes through the hub is an **M3 flat-head with a head Ø of 5.5–6 mm** — it does not pass a Ø4.5 hole. v4's own "not changed / still open" note called this out: *"If the real screws are standard 5.5 pan heads, go to Ø6."* This is that change, at Ø6.5.

The v4 note also flagged the consequence of opening the holes: at Ø6 there is only ~0.9 mm of material left between the hole and the Ø9.2 × 2.5 counterbore, and it suggested a relief instead. v5 takes the other option and **merges the two** rather than leaving a sliver that would print as a single unsupported wall.

## The change

| | v4 | v5 |
|---|---|---|
| Driver through-holes | 2 × **Ø4.5** axial, at r 8.5 on ±y (17.0 c-c), full length | 2 × **Ø6.5** axial, same centres, full length (cut at **6.71** with the 0.21 hole-shrink allowance) |
| Hole ↔ counterbore | ~0.5 mm sliver of material between them over the counterbore's 2.5 mm depth | **merged — keyholed into the Ø9.2 counterbore** over its full 2.5 depth, so there is no sliver |
| Bore Ø4.10 / flat 1.55, counterbore Ø9.2 × 2.5, grub channel, bead ribs, flanges Ø40.0, web | — | untouched |
| Overall length | 28.9 | 28.9 |
| Mass, PLA @ 1.24 | 17.0 g | **16.5 g** |

Hole centres are unchanged, so they still sit **90° from the D-flat** (clear of the grub-screw channel) and still inside the drum at r 8.5 + 3.25 = 11.75 < 15.1, so the tyre never sees them.

## What has to line up

The Ø6.5 holes are coaxial with the carrier's faceplate M3 holes at (5.5, 12.5) and (22.5, 12.5), and with the two new **Ø6.5 driver holes through the carrier's outer well wall**. Driver reach through the stack is 1.2 mm wall + 1.6 mm gap + 28.9 mm hub, so the driver needs **≥ 40 mm of shaft under Ø6**.

## Assembly order this enables

1. Heat-set insert into the hub grub channel (Ø4.1 × 6 pilot), M3 grub onto the shaft flat, hub ~0.5 mm off where the carrier wall will be. Tyre on.
2. Carrier upside down on the bench; drop the assembled motor + wheel in through the faceplate slot.
3. Rotate the wheel until a hub hole lines up with a faceplate hole. Long driver in through the outer-wall hole → through the hub → drive the M3 flat-head into the motor. Both sides.
4. Flip, lower onto the base, 4 carrier bolts. Tape over the two outer-wall holes.

## Print

ABS, `SumoBot Wheel Hub v5 ABS @BBL X1C`, as-is orientation, 0.15 mm layers, `support_on_build_plate_only = 1` so nothing lands in the tyre groove. Full analysis in `../printing/PRESETS_v5hub_v12carriers.md`.

## Not changed / still open

- **Motor tapped-hole axis vs the D-flat — now closed.** v5 assumed the two empty tapped M3 holes sit at 3 and 9 o'clock with the flat at 12. Confirmed on the part 17 Sep (`../hardware/MEASURED_PARTS.md` §2.1): **3/9 with the flat at 12, exactly as assumed — hub v5 needs no change.** Had it read 12/6, the hub holes would have had to move and the grub channel was in the way.
- **Bore fit — still open.** No coupon printed. The recommended path is unchanged: Ø3.95 / 4.05 / 4.15, and do not go past ~0.15 mm interference. The new motor pair measured shaft Ø**3.99** on 17 Sep, which makes **4.05** the leading candidate against the current 4.10.
- Screw: M3 flat-head, length = 1.2 mm faceplate + motor thread depth (≈ M3 × 6). Confirm head Ø ≤ 6 before printing a second hub.
