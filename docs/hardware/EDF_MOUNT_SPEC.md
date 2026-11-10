> **Superseded 17 Sep 2026.** The fan mount as printed is clamp ring v2 with M3 × 8 button heads & a 3 mm EPDM gasket (ID 43.5 / OD 47) on the measured fan, see `../chassis/v11/CLAMP_RING_V2_CHANGE.md` and `MEASURED_PARTS.md` §2.10. Kept for the reasoning/history.

# SumoBot — EDF mount, rough spec + caliper list (11 Sep 2026)

**Chassis-agnostic on purpose.** Every dimension here is referenced to the *fan*, not to v8's
geometry, so it drops into v9 unchanged. Whoever does the v9 CAD only needs §5 — a space
reservation and a screw pattern.

Supersedes the Master Plan line *"XFly 40 mm EDF … no mounting flange → printed split clamp
ring"*: the listing drawing shows **two mounting ears moulded onto the housing**. It also gives
**49.0 mm overall height** against the brief's *"reserve 48 mm until calipered"* — 1 mm over.

**§1 is read off a seller drawing, not calipered.** The fan has since been measured — where the two disagree, `MEASURED_PARTS.md` §2.10 wins (flange OD **47.81** worst case × **3.31–3.50** thick, duct OD **42.87**, duct section **26.44** with the datum unstated, motor stack past the duct **27.5**; overall height still unmeasured).

**One fan, no spare (Den, 17 Sep): do not bench-test it loose.** Verify all wiring and code first, plug it in last, one shot.

---

## 1. What the drawing gives

| Dim | Value | Reading |
|---|---|---|
| Overall height | **49.0** | flange top face → bottom of motor bell |
| Housing/duct height | **28.0** | flange top → bottom of duct body |
| → motor protrusion | **21.0** | 49 − 28, derived |
| Housing OD | **43.0** | body only, ears excluded |
| Fan Ø | **Ø40.0** | nominal size; 43 OD matches the XFly 1413 |
| Ears | 2, opposite, one hole each | roughly mid-height |
| Blades | ~12 | matches the spec |

43.0 OD → duct bore **43.3 target printed** (+0.3 clearance), before printer shrinkage.

---

## 2. Load check — this is not a strength problem

| Source | Force |
|---|---|
| Pressure across the fan: 800 Pa × Ø43 (1 452 mm²) | 1.2 N |
| Fan thrust, ~300 g | 3.0 N |
| Impact shock: 40 g part at 20 g | 8.0 N |
| **Worst case** | **~12 N** |

One M3 in tension is good for several hundred newtons. Four is ~100× the load.

**So the mount is sized by vibration loosening and by holding the intake lip on its seat, not by
strength.** Consequences: threadlock on every screw, a compliant washer under anything the motor
can buzz against, a gasket at the lip. Not bigger screws, and not more of them.

---

## 3. The mount — option A: clamp ring (build this)

One extra printed part. Works whether or not the ears turn out usable, and survives a fan swap.

```
        ┌── Ø70 OD ──┐
    ○   │            │   ○      ring, 3.0 thick, PETG
        │  Ø44.5 ID  │           4 × M3 on a Ø60 PCD
    ○   │            │   ○       at 45/135/225/315°
        └────────────┘
```

| Feature | Value | Why |
|---|---|---|
| Ring OD | **Ø70** | PCD + 10; enough meat around each screw |
| Ring ID | **Ø44.5** | clears the 43.0 body, overlaps a ~47 flange by ~1.3 radial |
| Thickness | **3.0** PETG (4.0 if PLA) | 3 mm PETG won't creep under a clamped gasket; PLA will |
| Screw PCD | **Ø60** | clears the flange OD with ~6 mm of margin |
| Screw holes | 4 × **Ø3.4** (+ shrinkage), Ø7.0 × 1.5 counterbore | M3 button head sits flush |
| Screws | **M3 × 12** button head + threadlock | ring 3 + flange 3 + ~6 engagement |
| Anchors | 4 chassis posts, **Ø8.5**, Ø4.15 pilot 6.0 deep, slot-2 heat-set insert | the insert carries the thread, so screw tolerance stops mattering |
| Gasket | 1 mm silicone, **ID Ø44 / OD Ø52** | seals the lip *and* kills the motor buzz path |
| Ear relief | two arches in the ring, sized off §4 item 5 | so the ring seats flat if the ears are in the way |

**How it loads:** the fan drops into the bore from above, flange lands on a shoulder in the duct,
the ring goes over the top and pulls the flange onto the gasket. Four bolts, lid off, no
disassembly. The screws only resist lift — the bore locates it radially.

## 4. The mount — option B: use the ears

Cheaper, two screws, but only if they measure out.

- Two posts, Ø8.5, rising to the ear underside height, at the ear hole centres.
- Ear hole ≥3.2 → M3 clearance + slot-2 insert. ≤2.6 → Ø2.1 pilot + M2.5 self-tapper, no insert.
- M3 × 10 button head, threadlock, **1 mm silicone washer under each ear**.
- Still needs the lip gasket. The ears stop it lifting; they don't seal anything.

**Two ears on opposite sides resist lift but not rotation about the axis between them** — the
fan can rock. Fine at 12 N, but it's why option A is the pick if you only build one.

---

## 5. What v9 CAD actually needs to reserve

This is the whole handoff. Nothing else in this file constrains the chassis.

| Reserve | Value |
|---|---|
| Duct bore | **Ø43.3** + printer shrinkage, through the roof and pan |
| Lip seat | shoulder at the bore bottom, **Ø47.6 above / Ø43.5 below**, so the fan loads from the top |
| Clear cylinder above the seat | **Ø72 × 50 tall** — the fan is 49, plus the ring |
| Screw pattern | **4 × M3 inserts on a Ø60 PCD at 45/135/225/315°**, post tops flush with the seat plane |
| Exhaust | Ø48 grille above, ≥65 % open, ≥2 mm clear over the motor |
| Air | do **not** fully enclose the motor — it's air-cooled |

The Ø60 PCD is the only number that has to agree between the ring and the chassis. Everything
else is local to one part or the other.

---

## 6. Caliper list — ten readings, blocks the ring

Digital calipers, each taken twice at different clock positions (moulded ducts are oval).

| # | Measure | What it locks |
|---|---|---|
| 1 | **Flange OD and thickness** | Ring ID and the Ø60 PCD. **The single most important pair** |
| 2 | **Housing OD at 3 clock positions** | Confirms 43.0 and how oval; sets bore clearance |
| 3 | **Ear hole centre-to-centre** | Option B post positions |
| 4 | **Ear hole Ø** | M2.5 self-tapper vs M3 insert |
| 5 | **Ear thickness, tangential width, radial stick-out** | Ring relief arches; post pads |
| 6 | **Ear underside height above the flange** | Option B post height |
| 7 | **Motor bell OD and protrusion** (expect 21.0) | The Ø72 × 50 reservation |
| 8 | **Which end is the intake** (the radiused side) | Orientation. Gets this backwards and the bot blows instead of sucks |
| 9 | **Overall height** (expect 49.0) | Confirms the 50 mm reservation |
| 10 | **Mass** on the kitchen scale | Budget says 40 g; nothing on this bot has been weighed |

Grab while it's in hand: blade count, KV/cell rating on the label, stated current.

---

## 7. Open question — is this the right fan at all

The source page says **"rotate the knob to control speed."** An EDF has no knob; it takes a
BLHeli_S ESC on a 3-wire servo signal. If this is a 12 V vented cabinet fan rather than a ducted
EDF, its stall pressure is 10–40 Pa, not 800–1500, and it gives roughly **50 g** of downforce
instead of 1.5–2.5 kg — `SumoBot_Downforce_Fan.md` §Fan type rejects exactly that part.

**Brushless + 3-wire ESC lead = EDF. Two-wire brushed + speed knob = wrong part.** Confirm before
ordering or cutting a duct.
