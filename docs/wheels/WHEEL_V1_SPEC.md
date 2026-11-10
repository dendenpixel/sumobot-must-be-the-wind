# Wheel — as-measured across two printed versions, and the bore diagnosis (11 Sep 2026)

Measured off physical printed wheels with silicone tyres fitted. Supersedes any bore figure in `WHEEL_V3_SPEC.md` until it's re-cut.

## Measured — two different printed rims

| Dimension | **v1** (older) | **newest rim** | Note |
|---|---|---|---|
| Internal rim / lip diameter | 30.04 | **29.93** | consistent |
| External rim OD (to the lips) | 38.68 | **38.1** | = tyre ID |
| **OD with silicone tyre** | 46.62 | **46.8** | tyre wall ≈ 4.0–4.35 |
| Rim width (tyre bed) | 28.98 | ☐ | |
| **Hub bore, round side** | **3.81** | **3.77** | **both undersize — see below** |
| **Hub bore, across the flat** | **3.44** | **3.45–3.46** | |
| Hub bore depth | ☐ | **~14 (estimated)** | deeper than the shaft's 12.36 stick-out, so no bottoming |
| Counterbore for the Ø7.05 × 2.36 collar | ☐ | recess present on the outer face, dims unclear | needs confirming |
| Tyre width (silicone, axial) | ☐ | ☐ | **blocks the flange design** |
| Mass with tyre | ☐ | ☐ | ×2 into the 990 g budget |

## FAULT 1 — the bore is undersize on BOTH wheels, and that's the diagnosis

| | Shaft (measured) | v1 bore | Newest bore |
|---|---|---|---|
| Round Ø | **4.10** | 3.81 | **3.77** |
| Across flat | **3.46** | 3.44 | **3.45** |

Two separately printed wheels landing at 3.81 and 3.77 is not a one-off bad print. It's **systematic hole shrinkage**: a nominal Ø4.0 hole printed in PLA comes out ~0.2–0.25 mm under, because internal perimeters over-extrude slightly into the hole. Every printer does this; the amount is a property of this printer + filament + profile.

So there are **two stacked errors**, and the design only ever accounted for zero of them:

1. The shaft is **4.10**, not the 4.00 the wheel was drawn around.
2. The printer delivers **~0.21 mm less** than whatever the CAD says.

Combined, the hole is ~0.3 mm too small, which is exactly the interference measured.

**To confirm the shrinkage number, one question: what is the bore dimension in the CAD file?** If it says 4.00, then shrinkage = 4.00 − 3.79 = **0.21 mm**, and the compensation is arithmetic from there:

```
target printed bore = 4.20          // shaft 4.10 + 0.10 slip fit
CAD bore            = 4.20 + 0.21 = 4.41
CAD flat            = 3.56 + 0.21 = 3.77
hub_bore_depth      = 9.0            // only 8.0 of usable D-flat on the shaft
hub_counterbore     = Ø9.0 × 3.0     // clears the Ø7.05 × 2.36 collar
```

**The coupon is now doing two jobs** — finding the fit AND measuring this printer's hole shrinkage. Print three bores at CAD **4.35 / 4.41 / 4.47**, caliper each hole after printing, then try the shaft. Whatever offset comes out applies to *every* hole on this bot, not just the wheel: insert pilots, M3 clearance holes, the XT60 slot.

Note: forcing the wheel onto a 0.3 mm interference splits the hub along a layer line or swells it permanently, and once swollen the D-flat stops locating and the wheel slips under torque. "Hammer it on" was never the design working — a correct hub slides on by hand with the flats aligned and the grub screw does the holding.

## FAULT 2 — the tyre isn't retained; a wider rim alone won't fix it

The tyre is wider than the bed, so it overhangs and peels.

Widening the bed makes it *sit* better but doesn't **hold** it — nothing stops it walking sideways under side-load, which in sumo is the normal state. What holds it is a **raised flange at each edge**:

```
bed_od   = 38.1       // unchanged — changing it orphans every tyre already cast
bed_w    = tyre width + 0.3
flange_h = 2.0        // above the bed, per side
flange_w = 1.5
```

The tyre drops into a channel and is captured axially.

## Knock-on: 46.8 is the real wheel diameter

Use **46.8**, not the bare rim's 38.1:

- **Ride height / ground clearance** comes off this.
- **Top speed** at the new motors' 130 rpm: π × 0.0468 × 130/60 ≈ **0.32 m/s**. Fine for sumo, worth knowing before anyone expects more.

## Still needed

- **The CAD bore value** — turns the shrinkage estimate into a measured constant.
- **Tyre width** (silicone alone, axial) — blocks the flange design.
- Confirm the outer-face recess is a collar counterbore, and its Ø + depth.
- Wheel mass with tyre.
