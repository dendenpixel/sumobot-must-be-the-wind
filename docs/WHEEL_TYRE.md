> **Superseded 21 Sep 2026.** The built wheel is hub v6.2 with a cast silicone tyre (`docs/wheels/README.md`), motors are the JGA25-371 130 rpm pair and the pack is the Ovonic 3S 2200 (`docs/hardware/MEASURED_PARTS.md`). Kept for the reasoning/history (tyre stiffness, μ and diameter trade study still hold).

# Wheels, tyres and motors (rev 4-5 Sep 2026)

Supersedes the tyre and motor rows in `DECISIONS.md` (2 Sep). Assumptions throughout:
850 g bot, plenum 0.031 m2, 2-wheel skid steer, planning mu = 0.70.

## 1. The finding that reorders everything

**The LEGO 62.4 x 20 balloon tyres make the downforce fan a net negative.**

Measured squat was 2-2.5 mm under +1.5 kg, i.e. a pair stiffness of **6.5 N/mm**. Brim
clearance is 1.0 mm, so the brim grounds at 6.5 N of tyre load — **at about 210 Pa**, below
any design point we had. Past that, a rigid PLA brim (~100x stiffer than a balloon tyre)
takes ALL further load, and it drags at mu ~0.3 instead of gripping at mu 0.70.

| Fan | N on tyres | N on brim | Net push |
|---|---|---|---|
| off | 8.3 | 0 | **+5.8 N** |
| 400 Pa | 6.5 | 14.2 | +0.3 N |
| 800 Pa | 6.5 | 26.6 | **-3.4 N** |

A solid cast-silicone tyre on a rigid hub is ~15x stiffer (20A silicone, 5 mm wall, 25-30 mm
wide -> ~96 N/mm pair):

| Fan | squat | N on tyres | Net push |
|---|---|---|---|
| 400 Pa | 0.22 mm | 20.7 | +14.5 N |
| 800 Pa | 0.35 mm | 33.1 | **+23.2 N** |

**The tyre swap is not an optimisation. It is what makes the fan work at all.**

## 2. mu correction

`DECISIONS.md` (2 Sep) says "target mu >= 1.0". **That target is wrong and is withdrawn.**

Measured mu on smooth board, the only real numbers that exist: Banebots rubber 0.55 |
FingerTech PU 0.70 | JSumo silicone 0.75 | 70A rubber on painted steel 0.743.

**Plan at mu 0.70. Check the push-out margin at mu 0.60.**

Shore target **A15-A25**. Softer than A15 picks up arena dust and mu collapses; harder than
A25 gives the rubber-compound numbers above, not the silicone ones.

Under high downforce mu falls with contact pressure (adhesion-limited rubber, roughly
mu ~ N^-1/3; literature brackets the exponent between -1/5 and -1/2). So **width is the
cheapest grip on the bot** — 30 mm wide at 45 N is ~30-40 kPa contact pressure against
~100 kPa at 20 mm. Do not narrow the tyre to save grams.

## 3. Wheel diameter

Crown = D + 6 mm. Ramp run 50 mm.

| D (mm) | Push ceiling 2T/r @ 6 kg.cm | 1 m @ 130 rpm loaded | Wheel pair mass |
|---|---|---|---|
| 62.4 | 37.7 N | 2.3 s | 73 g |
| 50 | 47.1 N | 2.9 s | 50 g |
| **45** | **52.3 N** | **3.3 s** | **41 g** |
| 40 | 58.8 N | 3.7 s | 34 g |

**Target 45-52 mm OD, 25-30 mm wide.** Against 62.4 mm that is ~+39 % push ceiling for free
and ~42 g off the rims. The lost speed costs nothing that matters: the tasks are pushing a
**passive** object out & the bracket. There is no timed sprint. Push force is the
quantity that counts.

Note the ramp angle is set by the 50 mm run, not by wheel diameter — every diameter in the
table gives an unclimbable single-slope ramp. Wheel diameter buys **torque multiplication**,
nothing else.

## 4. Motors are not the limit

Required per-motor torque T = mu x N x r / 2.

| Fan | Downforce | N_total | Grip @ mu 0.70 | T needed @ D45 |
|---|---|---|---|---|
| 400 Pa | 12.4 N | 20.7 N | 14.5 N | 1.67 kg.cm |
| 800 Pa | 24.8 N | 33.1 N | 23.2 N | 2.66 kg.cm |

25GA-370 family: 34:1 -> 4.5 kg.cm, 45:1 -> 6, 75:1 -> 9, all <= 3 A. At 45:1 and D45 the
push ceiling is 52 N against 23 N of grip — **2.3x margin**.

Break-even fan pressure (the pressure at which torque finally becomes the limit) is
1096 Pa at 34:1 / D45 and 1490 Pa at 45:1 / D45 — both above anything the fan can hold.

**Grip is the limit, not torque, at any ratio >= ~34:1.** The 2 Sep "buy a 1:78 pair if the
on-hand motors are fast" trigger stands, but the urgency is gone: characterise the on-hand
pair first (`RISK_REGISTER.md` row 13). If they are >= 4.5 kg.cm, keep them and buy nothing.

## 5. Wheel build — IN HOUSE

**Decision (5 Sep): we print our own hubs and cast our own silicone tyres. Buying tyres or
mounting hubs is dropped entirely — do not re-cost it.**

Rationale, briefly, since it was researched: no bare competition tyre exists on AliExpress
in any vocabulary (three independent search passes, all nothing — do not re-run that
search). The only bare-tyre supplier in the size window is JSumo in Turkey, at AU$38-73
landed depending on whether you gamble on registered air arriving before 12 Oct, with an
**unpublished inner bead diameter** — meaning you print a hub to an unknown number anyway.
Casting removes the shipping gamble and the bead unknown at similar cost, and it is the
approach the same research found Polish minisumo teams reaching independently.

Build procedure: **`WHEEL_V1.md`**.

Architecture rules that survive from the trade study, whichever way the wheel is made:

- **Plastic must never touch the shaft.** Direct D-flat drive in plastic puts ~230 N on two
  sharp bore corners. Bolted to a metal hub on a 12.7 mm bolt circle it is 15.4 N per M3 —
  **15x less stress**. Use the brass couplers already on hand: print a pocket around the
  coupler and replace its grub screws with longer M3 SHCS through 3.2 mm clearance holes, so
  the screw shanks act as shear dowels in double shear.
- **PETG or ABS, not PLA.** Izod 8-12 vs 2-4 kJ/m2, Tg 80 vs 60 C — the shaft conducts motor
  heat into the hub. Reject CF grades: the bore needs ductility, not modulus.
- **Print coin orientation** (wheel axis vertical, flat on bed). Torque is then in-plane
  shear within a layer. Standing orientation puts it on interlayer shear and the hub splits
  along a layer line on first impact.
- **Bore 4.10 mm, D-flat 3.60 mm — clearance, not press.** A press fit in plastic creeps.
  Print a 4.00 / 4.10 / 4.20 coupon and test on the actual shaft before committing.
- **Silicone will not bond to PETG.** No datasheet supports a reliable cured-silicone-to-
  thermoplastic shear bond. Retention is **mechanical only**: 10-12 radial 3.5 mm
  through-holes with an inside counterbore so the silicone forms mushroom rivets, plus
  1.5-2 mm side flanges.

## 6. Weight

| Change | delta |
|---|---|
| 62.4 LEGO + hub -> 45-52 mm cast silicone + printed rim | -31 g |
| Crown wall 68.4 -> 51.0 mm | -11 g |
| **Net** | **-42 g** |

This is not a saving. The limit is 1 kg and we are at ~850 g. It is 42 g moved **off the
rims** — the worst place for it, rotational inertia and unsprung — and available as low
ballast between the axles. **Ballast to 985-995 g.** That is 1.4 N of normal force that does
not depend on the fan, the skirt, or a rules ruling.

Watch: one Ovonic 3S 1500 is ~150-160 g against the old 850 mAh's ~75 g. **Run one pack on
the bot**, not two. Better still, one pack for the fan and one for drive + logic — that
decouples a 5-10 Hz sag limit cycle, since fan pressure goes as V^2 and a 15 % sag is a
28 % pressure loss, arriving exactly at contact.

## 7. Measurements to take

1. **Characterise the on-hand motors** (30 min). No-load rpm at 12 V gives the ratio
   (130 -> 45:1, 175 -> 34:1, 80 -> 75:1). Then a 100 mm lever arm on a kitchen scale,
   powered: T[kg.cm] = mass[kg] x 10. If >= 4.5 kg.cm, keep them.
2. **Push force vs fan throttle, 0 / 50 / 100 %.** Spring scale, pull until the wheels spin.
   If push does not rise monotonically with throttle, the brim is grounding — section 1.
3. **Straightedge and feeler gauges on the actual arena.** A 1 m MDF board bows 1-3 mm. A
   1 mm rigid brim has no margin for a bowed board or a taped seam.
4. **Yaw check under clamp.** M_avail/M_req is identical to the straight-line ratio and
   track width cancels, so 2.3x at 45:1 / D45 / 800 Pa. But a skid-steer pivot under clamp
   is slip-governed and **encoder counts do not measure heading** — see `DECISIONS.md`.
