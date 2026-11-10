# Clamp ring v2 rev B — thicker ring, deeper relief, 3 mm gasket (17 Sep 2026)

Modelled from scratch in CadQuery (`build_clamp_ring_v2.py`), not mesh-edited. Four outputs, all
single watertight genus-5 solids: `clamp_ring_v2_{nominal,shrinkcomp}` and
`clamp_ring_v2_earslot_{nominal,shrinkcomp}`. **Print `clamp_ring_v2_shrinkcomp`** (on the bot in ABS, file `hardware/cad/v11/stl/clamp_ring_v2_shrinkcomp.stl`, the reserve ear-slot variant is `hardware/cad/v11/stl/clamp_ring_v2_earslot_shrinkcomp.stl`). The rev A
3.0 mm-thick files have been overwritten — nothing on disk is the old part.

## Why

1. **A 1 mm gasket cannot span the real tolerance band.** The seat floor is not a datum: a >55°
   down-facing annulus 2.05 mm wide printed 3 mm above the bed, plus elephant's foot on the roof
   face, plus a shrink figure extrapolated from a Ø4.15 coupon to a Ø47 feature. As-printed seat
   depth D is **2.8–3.4**, not 3.0. With `c = relief_depth + D − t` and t = 3.31–3.50, `D − t`
   swings 0.79 mm. Staying under 50 % squeeze needs relief depth **> 1.20**; staying in contact
   needs **< 0.91**. No number satisfies both. Verified independently — the premise holds.
   A 3 mm element opens a window of **2.20–2.91**.
2. **Rev A's Z features landed on half layers.** 1.1 was 5.50 L and 1.5 was 7.50 L at 0.20 mm, so
   slicer rounding moved the relief depth ±0.1 and swung the squeeze from 11 % to 50 %. Every rev
   B height is now a whole layer.
3. **Ø49.0 left too little roof land.** The seat is hand-reamed to 48.05–48.10 and will go oval by
   ±0.2; Ø49.0 gave the ring's bearing edge only ~0.45 mm to sit on. Ø50.0 gives **0.950**.

## The change

| | rev A | rev B |
|---|---|---|
| Thickness | 3.0 | **4.4** (22 L @ 0.20) |
| Underside relief | Ø49.0 × 1.1 | **Ø50.0 × 2.4** (12 L) |
| Web over relief | 1.9 | **2.0** (10 L) |
| Ear counterbore | Ø6.5 × 1.5 | **Ø6.5 × 1.6** (8 L) |
| Material under each head | 1.5 | **2.8** (14 L) |
| Bearing annulus | Ø49→Ø56, 3.5 wide | **Ø50→Ø56, 3.0 wide** |
| Compliant element | 1 mm silicone, ID 44.5 / OD 47.5 | **3 mm EPDM, ID 43.5 / OD 47.0** |
| Squeeze across the box | no valid window | **17.00 – 43.33 %**, 16/16 cells |
| Roof land (relief vs reamed Ø48.10) | ~0.45 | **0.950** |
| Relief vs flange Ø47.81 | 0.595 | **1.095** |
| Bore vs duct Ø42.87 | 0.815 | 0.815 (unchanged) |
| Screw | M3 × 6 | **M3 × 8**, 5.20 engaged (1.73 × D) |
| Volume / PETG @ 1.27 | 2777.6 mm³ / 3.53 g | 3685.1 mm³ / **4.68 g** (shrinkcomp **4.56 g**) |
| Bore Ø44.5, OD Ø56.0, ears 4 × Ø9.5 on Ø60 PCD at 45/135/225/315°, holes Ø3.4, 1.5 seam blend | — | untouched |

Gate 2 in the rev A brief asked for a 69.5 mm X/Y bbox. That is only reachable with ears at
0/90/180/270°; at 45° an ear reaches 25.96 along X, inside the Ø56 OD. **Bbox is 56.0 × 56.0 ×
4.4 and 69.5 is the across-ears diagonal** — both measured. Ear angles confirmed against the roof
insert pattern, so the angles stay and the gate was restated.

Shrink-comp convention unchanged: **+0.21 on internal diameters only** (44.5 → 44.71, 50.0 →
50.21, 3.4 → 3.61, 6.5 → 6.71). Depths, thicknesses and externals untouched, so the gasket box is
identical between the two. The slots are a generous clearance feature and are not compensated.

## Gates

**64 PASS, 6 FAIL** across four variants (`check_clamp_ring_v2.py`). All values probed out of the
solid — point-in-solid bisection, B-rep cylinder radii and plane heights, plus an STL mesh audit.
Full table in `clamp_ring_v2_GATES.md`. The six failures are two findings repeated:

- **11b (×4): the gasket ID is inboard of the bore.** ID Ø43.5 → r 21.750 against a web inner edge
  at r 22.250, so **0.500 mm of gasket width (28.6 %, 69 mm²) is never pressed**. Loaded area is
  **179.7 mm², not 248.8** — use the smaller figure for anything force-related. On shrinkcomp it
  is 0.605 mm / 34.6 % / 164.9 mm². The other half of the check passes: the gasket does sit wholly
  on the flange, +0.315 inboard and +0.355 outboard, still positive at 0.20 mm of seat float.
  **Leave it.** Moving the ID to Ø44.5 narrows the section to 1.25 mm and takes h/w from 1.71 to
  2.40, which will roll instead of compress; opening the bore to Ø43.5 fails the bore-to-duct gate.
- **14b (×2): the ear slot breaches the relief wall.** 4 mm deep from Ø44.5 lands at Ø52.5 against
  a Ø50.0 relief wall — past it by **1.25 mm**. Any slot deeper than 2.75 cannot pass that check.
  See the ear-slot section below.

Everything else measured exact: relief **2.4000**, web **2.0000**, under-counterbore **2.8000**,
holes **Ø3.4000 at r 30.0000** on 45.000/135.000/225.000/315.000°, bore **44.5000**, Euler **−8**
(genus 5 = bore + 4 bolt holes) on all four.

## Gasket compression box

3 mm EPDM, `c = 2.4 + D − t`. Cells are **c / squeeze %**.

| | t = 3.31 | t = 3.35 | t = 3.40 | t = 3.50 |
|---|---|---|---|---|
| **D = 2.8** | 1.89 / 37.00 | 1.85 / 38.33 | 1.80 / 40.00 | **1.70 / 43.33** |
| **D = 3.0** | 2.09 / 30.33 | 2.05 / 31.67 | 2.00 / 33.33 | 1.90 / 36.67 |
| **D = 3.2** | 2.29 / 23.67 | 2.25 / 25.00 | 2.20 / 26.67 | 2.10 / 30.00 |
| **D = 3.4** | **2.49 / 17.00** | 2.45 / 18.33 | 2.40 / 20.00 | 2.30 / 23.33 |

Range **17.00–43.33 %**, 16/16 cells inside (0, 50). The 17–43 estimate was right; the top cell is
43.33.

## Ear-slot variant

Two opposed 12 wide × 4 deep slots at 0°/180°, full ring height, outer corners radiused 1.5.
Clear of the ear pads by **10.83 mm** and of the ring OD by **1.75 mm**. Mass 4.32 g nominal /
**4.20 g** shrinkcomp.

It costs more than the brief assumes. Radial section at a slot drops from **18.70 to 7.70 mm²
(59 % removed)**, and because there is no web over a slot there is **no gasket compression across
two 30.8° arcs — 17.1 % of the circumference** — sitting exactly midway between screw pairs, which
is already the least stiff part of the ring.

`SLOT_WEB_ONLY = True` in the build script cuts the slot only through the web (Z ≥ 2.4) and leaves
the relief wall and bearing annulus continuous: **10.70 mm² retained instead of 7.70**, at the cost
of a stepped clearance envelope (Ø50.0 below Z 2.4, Ø52.5 above). The relief already gives Ø50.0
of clearance down there, so unless the duct ear is a straight boss needing the full 4 mm all the
way down, **this is the version to print.** One line to switch.

Print neither until a test fit says the ear actually fouls. If it does, rotate the fan onto one
slot and consider deleting the unused opposed slot rather than keeping both.

## Print settings

- PETG, Bambu X1C, 0.4 nozzle. **0.20 mm layers, 0.20 first layer** — every critical Z is a whole
  layer (22 / 12 / 10 / 8 / 14).
- **Top face down on the bed.** Underside-down turns the relief ceiling — the gasket contact face —
  into a 2.75 mm unsupported inward overhang. Top-down, the only overhang is the 1.55 mm annular
  counterbore floor under each screw head, which the screw flattens anyway.
- Walls 4, top/bottom 5, infill 100 %. No supports.

## Assembly

- **M3 × 8 button head.** 2.8 mm passes through the ring, **5.20 mm engages** the insert
  (1.73 × D) with 0.50 mm spare. **M3 × 6 gives 1.07 × D — too short. M3 × 10 bottoms in the
  insert by 1.50 mm** and would read as torqued while clamping nothing. Put this on the BOM.
- This is a **displacement-controlled** joint: the ring bottoms on the roof and the geometry sets
  the squeeze. Tighten in a diagonal cross pattern **until the ear undersides are hard down on the
  roof**, then stop. Expect **0.2 N·m**; allow up to **0.3**; never exceed 0.3. Required preload
  is 40 N per screw at the mild corner and up to ~296 N at the stiff one, against 333 N at
  0.2 N·m — the margin is thin, so seat by feel rather than by torque alone.
- **No threadlock on the first fit.** Expect to pull this apart.
- Head stands 0.05–0.15 mm proud of the top face (ISO 7380 M3 head is 1.65–1.75 in a 1.6 recess).

## Not changed / still open

- **Web creep is the real reservation.** The 2.0 web runs at 13.2 MPa bending at 43.3 % squeeze
  unconfined, and up to **26.3 MPa (SF 1.9)** if the gasket confines — which it probably does, it
  is captured by the duct lip 0.315 mm inboard and the seat wall 0.525 mm outboard and touches
  both by ~25–30 % squeeze. Rev A ran at SF 8.9. PETG creeps. **Re-check the clamp after a week of
  running.** If the roof can be controlled at all, favour the deep end of the seat band — D = 3.4
  gives 17 % squeeze and SF 13.9.
- **The relief is out of room.** Ø50.0 leaves 0.250 mm to the ear pad tips (0.145 on shrinkcomp).
  **Ø50.5 is the hard limit.** Gate 8 now probes the four pad tips at r 25.3 to catch it. A future
  revision cannot go wider without moving the ears.
- **Nothing centres the ring but the bolt holes.** Relief Ø50.0 is larger than the reamed seat, so
  it cannot pilot. Ring float 0.20 (0.305 on shrinkcomp) plus fan float in the seat 0.15–0.20 means
  the unsupported gasket lip varies **0.100–0.900 mm** around the circumference. A Ø47.9 spigot on
  the underside would fix it for nothing if it ever matters.
- **Gasket bulge at the stiff corner.** At 43.3 % the section goes 1.75 → 3.09 mm wide, which puts
  the inner edge **0.354 mm past the duct lip** and the outer edge past the flange OD into the
  seat gap. It sits over the duct wall, not in the airflow, so this is a note not a fault — but
  worth a look on the first test fit.
- Duct ear position along the duct still unmeasured. That is what the slot variant is for.
