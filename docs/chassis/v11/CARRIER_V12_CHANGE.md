> **Superseded 21 Sep 2026.** Carrier v13 is on the bot (`docs/chassis/v11/CARRIER_V13_CHANGE.md`), v12 couldn't be assembled straight (saddles and down-slot contradict) and its tie strips snapped. Kept for the reasoning/history.

# Carrier v12 + wheel hub v5 — drop-in motor/wheel unit (15 Sep 2026)

Base files: `v11_carrier_L.stl`, `v11_carrier_R.stl` (Astra base stage, 13 Sep), `sumo_wheel_hub_v4.stl`. Mesh-edited with manifold booleans (same method as hub v4), all three watertight. Outputs: `v12_carrier_L.stl`, `v12_carrier_R.stl`, `sumo_wheel_hub_v5.stl`. R is the point-mirror of L (x→−x, y→−y); every number below is L, negate x and y for R.

Hub v5 has its own change record in `../../wheels/WHEEL_HUB_V5_CHANGE.md`. Print settings for both parts: `../../printing/PRESETS_v5hub_v12carriers.md`.

## Why

Sealed well + closed faceplate = the motor goes in from the bay, the wheel from below, and the grub is unreachable. Hub v4 already added driver holes through the hub so the faceplate screws can be driven with the wheel on; this pass makes the carrier accept a **pre-assembled motor + hub + tyre** and gives the driver a way in.

## Measured before cutting (v11 carrier L)

| Feature | Value |
|---|---|
| Faceplate wall | 1.2 (Y 37.8–39.0), Z 0–28.1, X −13.1…41.1 |
| Bore | Ø8.2 at (14, 12.5) |
| Faceplate M3 holes | (5.5, 12.5) and (22.5, 12.5), 17.0 c-c, 90° countersink opening on the well side, no pads |
| Outer well wall | 1.2 (Y 70–71.2). Hub outer face at Y ≈ 68.4 → 1.6 gap |
| Wellcap insert bosses | Ø8.5 full height, pilots Ø4.36 at (−5, 74.44), (20, 74.46), (44.14, 44), (44.14, 58) |
| Floor | none under the well or the motor bay — base roof closes it |

## The change

| | v11 | v12 |
|---|---|---|
| Faceplate slot | — | **8.2 wide from bore centre down through Z 0** (box 8.2 × 14.5 at x 14). Bore top intact. 21.8 of wall each side, 2.7 between each M3 hole and the slot edge |
| Outer-wall driver holes | — | **2 × Ø6.5 (cut 6.71 with hole shrink) at (5.5, 12.5) and (22.5, 12.5)**, coaxial with the faceplate holes and the hub holes |
| Boss at (20, 74.46) | full-height column | **undercut**: solid from Z 16.5 at the wall face rising at 45° outward (Z 24 at the far edge). Pilot Ø4.36 × 6 untouched (still reads 15.75–24.25 in x at Z 25). Prints without support. Wellcap unchanged, 4 screws kept |
| Mass | 17.8 g | 19.6 g solid est. (15 795 mm³ × 1.24), printed mass unmeasured |

Hub v5: driver holes **Ø4.5 → Ø6.5** (cut 6.71) at r 8.5 on ±y, merged into the Ø9.2 counterbore over its 2.5 depth (keyhole) so there's no 0.5 mm sliver between hole and counterbore. Bore, flat, grub channel, ribs untouched. 16.5 g.

Why the slot goes **down**, not up (the original sketch had it up): the carrier is bolt-on and open underneath, so the unit goes in with the carrier upside down on the bench and the base roof closes the slot when bolted. Ground reaction pushes the wheel up into the intact bore top — the collar carries it, not two M3s in shear in a 1.2 wall. Nothing to seal.

Why Ø6.5: the faceplate is countersunk, so the screw is an M3 flat-head (head Ø5.5–6). Hub v4's Ø4.5 wouldn't pass the head. Driver needs ≥ 40 mm of shaft under Ø6 (reach = 1.2 wall + 1.6 gap + 28.9 hub).

## Assembly order

1. Slot-2 insert into the hub grub channel (Ø4.1 × 6 measured — standard pilot), M3 grub onto the shaft flat, hub ~0.5 off where the wall will be. Tyre on.
2. Carrier upside down on the bench. Drop motor + wheel in: collar into the slot, wheel into the well, motor onto the cheeks.
3. Rotate the wheel until the faceplate hole shows through a hub hole. Long driver through the outer-wall hole → hub → drive M3 flat-head into the motor. Both sides.
4. Flip, lower onto the base (wheel through the roof cut-out), 4 carrier bolts.
5. Electrical tape over the two outer-wall holes. Well and bay are both at ambient (well is outside the plenum) so this costs no downforce — it only keeps arena grit out of the bay.

## Open

- **Motor tapped-hole axis vs D-flat** — hub holes are 90° from the flat. Flat facing up: empty tapped holes at 3/9 o'clock = fine; 12/6 = hub holes must move and the grub channel is in the way. Not checked yet. Hub v5 assumes 3/9.
- Screw: M3 flat-head, length = 1.2 + motor thread depth (~M3 × 6). Confirm head Ø ≤ 6.
- Bore fit coupon still not printed.
- The old motor pair (bench spares) has the same faceplate interface, so this works for them too.

---

**Update 17 Sep 2026 — two of the open items above are now closed by measurement.** Per `../../hardware/MEASURED_PARTS.md` §2.1: the new JGA25-371 pair has its **tapped-hole axis at 3 and 9 o'clock with the D-flat at 12**, which is exactly what hub v5 assumes — no hub change. Measured body length is **58.84 mm** (not 65), giving a tail gap of 16.76 mm, so the **v12 carriers need no reprint**. Still open: bore-fit coupon, Phillips head height against the carrier faceplate seat, and the hub bore 4.10 → 4.05 candidate on a Ø3.99 shaft.
