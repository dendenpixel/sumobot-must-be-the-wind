> **Superseded 12 Sep 2026.** The chassis is v11 (`docs/chassis/v11/START_HERE.md`). Kept for the reasoning/history.

# SumoBot Chassis — Clean-Slate Design Handover (v9)

**Date issued:** 11 September 2026
**From:** Den, group leader, university group project
**To:** a fresh design agent with no prior context on this project
**Deliverable wanted:** a printable **STL** (or a set of STLs) for the robot's chassis, plus the reasoning behind it.

---

## 0. Read this first — what I actually want from you

We have been through **eight chassis revisions** and we are still not meeting our own requirements. Each revision was built from a brief that turned out to be internally inconsistent, so the model was correct and the *brief* was wrong. I am handing the whole problem to you, fresh, because I think the accumulated assumptions are now part of the problem.

**What I want:**

1. A chassis you would design, given the rules, the parts, and the physics below.
2. Output as **STL files, printable on a Bambu Lab X1C** (256 × 256 bed), with a self-check that proves the geometry is what it claims to be.
3. Your reasoning, stated plainly — especially anywhere you disagree with us.

**What I am NOT asking for:** a faithful reproduction of our current design. Everything in §5 (Current Design and Why) is **context, not instruction**. If you look at it and think the architecture is wrong, say so and design what is right. The only things you cannot change are in §2 (Hard Constraints) — those are competition rules and physical parts we already own.

**If something in here is ambiguous, contradictory, or missing — ask me. Do not guess.** Guessing is precisely what produced eight revisions. I would much rather answer five questions than print another wrong part. I have calipers and a scale on the desk; most questions I can answer in 30 seconds.

### Provenance tags — read these literally

| Tag | Means |
|---|---|
| **MEASURED** | A literal caliper or scale reading on a physical part. No clearance added. |
| **CAD** | A design value we chose. It may never have been printed or verified. |
| **DERIVED** | Calculated from a measurement plus a policy (e.g. a panel cut-out sized from a body dimension). |
| **SELLER** | Read off a listing or a seller drawing. Never physically verified. **Treat as suspect.** |
| **UNKNOWN** | Nobody has established this. Do not invent a value — ask. |

I have gone through and re-tagged everything. Where an earlier document of ours claimed something was measured and it wasn't, the tag below is the correct one.

### Known conflicts I have NOT resolved

These are places where two of our own documents disagree and I want your read on which is right. They are flagged inline as ⚠ **UNRESOLVED** and collected in §10.3. Please do not silently pick one.

---

## 1. The problem in one paragraph

Build a 1 kg sumo robot chassis that (a) cannot be wedged under or flipped, (b) presses its tyres into the floor hard enough to out-push everyone else, and (c) contains a specific, already-purchased set of electronics. It must fit in a 250 × 250 × 250 mm box, weigh under 1000 g including everything, and be 3D printed on a consumer FDM printer. Front and rear are both pushing faces. The arena is a ~1 m black circle bounded by a white line; driving over the line loses the match.

---

## 2. HARD CONSTRAINTS — not negotiable

### 2.1 Competition rules (from the course project brief)

| Rule | Value |
|---|---|
| Max size | **250 × 250 × 250 mm** — "these will be checked" |
| Max weight | **1000 g** — checked |
| Arena | ~1 m diameter black circle, bounded by a white line. Drive outside the line = loss |
| Objective | Find the opponent and push them out or flip them over |
| Controller | **Must** use the provided TTGO ESP32 |
| Chassis | Must be built from scratch. **Cannot use published designs.** |
| Boards | No commercial boards except a motor controller |
| Opponent detection | Must be indicated on a display **or a dedicated LED** |
| Group number | Must be clearly shown on the robot |
| First drive (w/c 21 Sep) | Drive 1 m forward, stop, 1 m back, stop |
| Competition (w/c 12 Oct) | Push out a stationary passive object, then random-tournament competition |

**Suction / downforce fan is APPROVED.** Coordinator confirmed 8 Sep 2026. His caveat: the competition surface is a timber plate and is **not perfectly smooth** — expect side-leak losses. Design the seal for a floor that is not flat.

The coordinator's words on scope: *"out of scope"* means **destructive actions toward the opponent only** — no "robot war". He did not enumerate what is permitted. My reading is that pushing, wedging, lifting and carrying are all fine, but that is my inference, not his ruling.

### 2.2 Physical constraints we cannot change

| Constraint | Value | Provenance |
|---|---|---|
| Printer | **Bambu Lab X1C**, 0.4 nozzle, 0.2 mm layer | It's what we have |
| Usable bed | **256 × 256 mm**, no brim, no skirt | A 250 mm part has 3 mm of margin |
| Materials | PLA (primary), PETG (small/flexing parts), ABS if toughness demands it | On hand |
| Hole shrinkage | **Holes come out ~0.21 mm UNDER nominal** | ⚠ **DERIVED, not measured.** Two separately printed wheel bores came out 3.81 and 3.77 in a bore we *believe* was drawn at 4.00. Nobody has opened the CAD file to confirm the 4.00. See §10.1 item 4 — this is a 30-second check that turns a guess into a constant, and it applies to **every hole on the bot** |
| Printed mass | **0.82 × (STL volume × 1.24 g/cm³)** for PLA as we print it | MEASURED — calibrated against a chassis we weighed at 267 g whose STL volume was known |
| Support | Supports that anchor **to the bed** are acceptable. Supports that anchor **onto the part** are a defect — Den has snapped thin ribs peeling PLA support off | Practical experience |
| Max overhang | **55° from horizontal** with no support | Printer capability |

### 2.3 Parts we already own and must design around

Full detail in §4. Short version: we have the motors, wheels, battery, ESC, drivers, sensors, connectors and (probably) the controller. **You do not get to specify different parts.** You can tell me one is a bad choice and why, and I will listen, but the design has to work with what is in the box.

---

## 3. The physics — this is what actually drives the design

This is the reasoning layer. If you change the architecture, change it against these numbers, not against our conclusions.

### 3.1 Push force

```
Push = μ × N
```

- **μ** comes from the tyres. We cast our own silicone tyres (Mold Star 15), targeting **μ ≥ 1.0**.
- **N** = weight + downforce. Weight is capped by the rules at 1.000 kg = **9.81 N**. Our working target is 0.99 kg = **9.7 N**, and that is the figure used below.
- So at 0.99 kg and μ 1.0, a bot with no downforce gets **~10 N of push**. That is the entire game everyone else is playing.

### 3.2 Downforce

```
Downforce = ΔP × A
```

- **A** = sealed plenum area. This is free — it is a geometry decision, it costs grams of plastic only.
- **ΔP** = pressure differential from a 40 mm EDF pulling air out of a skirted plenum. Practical figure for a 40 mm 12-blade 3S EDF at stall: **800–1500 Pa**. We design to **800 Pa** as the conservative case.

Worked numbers on our footprint:

| Seal loop | Area (mm²) | N at 800 Pa |
|---|---|---|
| v5/v6 as built, nominal | 30,217 | 24.2 |
| v5/v6 as built, **actual** (wheel wells leak — see §6.1) | ~26,400 theoretical, **~0 real** | **~0** |
| Full-perimeter superellipse at **rim inset 18** | **43,168** | **34.5** |
| Same, with wheel wells sealed out of the plenum | ~39,600 | **~31.7** |

> ⚠ **UNRESOLVED (U1).** Those areas were computed at **rim inset 18**. The layout we actually built (§5.10) puts the seal loop at **rim inset 20**. Two extra millimetres of inset costs roughly 1,500 mm² ≈ **1.2 N**. So the "41 N" headline below is computed on a loop the current layout does not use — the real figure for the as-drawn v8 loop is closer to **40 N**. Not fatal, but it means the two numbers in our own documents were never reconciled. **If you re-derive the loop, state the inset you used and recompute.**

### 3.3 Where it lands

| State | Normal force N | Push (μ=1.0) |
|---|---|---|
| Today (suction effectively zero) | 9.7 N | **~10 N** |
| Wells sealed, old v5 loop | 30.8 N | ~31 N |
| Wells sealed + full-perimeter loop at inset 18 | 41.4 N | **~41 N** |
| Same at inset 20 (what we drew) | ~40 N | ~40 N |
| **Drivetrain ceiling** (2 × ~6 kg·cm on a 23.4 mm wheel radius) | — | **~50 N** |

**The design target is grip ≈ 40 N against a drivetrain ceiling of ≈ 50 N.** That is the right place to stop. More suction past that point is wasted mass and current, because the motors run out first.

### 3.4 The real loss mode

At ~40 N of normal force, the force needed to **tip** this bot about its wheels is >120 N. Nothing in a 1 kg class generates that. So tipping is not the threat.

**The real way we lose is being wedged under and lifted.** That is a *geometry* problem (continuous unbroken rim, low leading lip) and a *downforce* problem — not a centre-of-gravity problem. Bottom-heaviness is worth having because it is nearly free, but do not spend design effort on it at the expense of the rim and the seal.

### 3.5 Corollaries that shaped everything

1. **Area is cheap, pressure is expensive.** Grow the sealed footprint before reaching for a bigger fan.
2. **A hole in the plenum is worth more than any other defect.** Our v5/v6 chassis has ~3,600 mm² of open hole inside the skirt loop — roughly 9× the entire design leak of 382 mm² — and that single fault makes the fan, the ESC, the battery upgrade and the whole suction argument produce nothing. See §6.1.
3. **The rim is the armour, the skirt is the seal, and they are different parts.** Hard PLA rim at the outside, **0.50 mm** off the floor, continuous 360°, is what stops an opponent's blade getting under us. The soft silicone skirt is tucked ~20 mm inboard under the wedge where nothing can hit it. Rubber at the leading edge would be *worse* — it is compliant, so a blade lifts it instead of being stopped.
4. **Ballast is the one mass on the bot that does useful work.** It is normal force, and push = μN. Everything else is overhead. Never save weight by deleting ballast.

---

## 4. THE PARTS — everything that must fit

Clearance policy: bores for shafts/bosses **+0.2–0.25 on Ø** · pockets for boards/modules **+0.5 per side** · M3 clearance Ø3.4 · stacking dimensions +1–2 end clearance · **and on top of all of that, +0.21 mm on every hole for printer shrinkage** (subject to §2.2's caveat).

### 4.1 Drive

**Motors — old pair. ON HAND.** Currently the bench spares / first-drive motors.

| | Value | Provenance |
|---|---|---|
| Body length (faceplate → back of housing) | **39.29** | MEASURED |
| Gearbox length / can length | 21.00 / 17.53 | MEASURED |
| Faceplate boss | **Ø7.05, 2.36 proud** | MEASURED |
| Shaft | **Ø4.10 round, 3.46 across flat**, 10.0 long from collar top, 8.0 of it flat | MEASURED |
| Total shaft stick-out from faceplate | 12.36 | MEASURED |
| Mounting holes | **17.00 c-c nominal, tapped M3** | DERIVED — two rounds read 16.90 and 16.88; 17.00 is the inferred nominal |
| Encoder | 6-pin at the back of the can | MEASURED |

**These are NOT 371s.** A 370 can is ~30 mm; this is 17.53, i.e. 310-class. Lower power than assumed and the 12 V rating is unconfirmed.

**Motors — new pair. ORDERED, NOT ARRIVED. EVERY FIGURE IS SELLER.** BRINGSMART JGA25-371, 12 V, "130 rpm", Hall encoder, AU$12.79 ea.

| | SELLER |
|---|---|
| Gearbox Ø / can Ø | 25.0 / 24.4 |
| Body length | **61–69 (seller drawings disagree; we assumed 65)** |
| Shaft | Ø4 × 12, D-flat 3.5 across × 8 long |
| Faceplate | 2 × M3 tapped, 17 mm c-c, Ø7 boss |
| Encoder cable | 2.54 mm 6-pin, 200 mm |
| Mass | ~95 g each — **never weighed** |

> **This is the single biggest unknown on the bot.** 190 g of a 967 g budget rests on a seller estimate, and an entire geometric feature of the current design (a ±14 mm motor stagger in X) exists *only* because they are assumed to be 65 mm long. If they turn out short like the old pair, the stagger is unnecessary and the duct can move back toward the centre.
>
> **Design the motor mount so it tolerates a body length anywhere from 39 to 69 mm.** Our current approach: cradle cheeks in three 12 mm segments so any length lands on at least two of them.

**Wheels — printed hub + cast silicone tyre. ON HAND.**

| | Value | Provenance |
|---|---|---|
| **OD with silicone tyre fitted** | **46.80** | MEASURED |
| Rim OD (tyre bed) | 38.10 | MEASURED |
| Hub bore as printed | 3.77–3.81 round / 3.45 across flat | MEASURED — **currently ~0.3 mm too tight for the 4.10 shaft; do not fit yet** |
| Hub v3 overall length | 29.0 (1.0 flange + 27.0 ring seat + 1.0 flange) | **CAD** — the v3 hub design, not a printed part |
| Counterbore in motor face | Ø9.0 × 2.5 deep | **CAD** ⚠ see U2 |
| Drive | Radial M3 set screw at Z 9.0 onto the shaft D-flat | CAD |
| **Tyre width currently assumed** | **30.0** | ⚠ see U3 — this is the untrimmed cast ring |

> ⚠ **UNRESOLVED (U2).** Two of our documents give the hub's motor-face counterbore as **Ø9.0 × 2.5 deep** and one gives **Ø9.0 × 3.0 deep**. The depth must exceed the motor boss protrusion (Ø7.05, 2.36 proud on the old pair) by ~0.5. Caliper the new motors' boss when they land and set it from that.
>
> ⚠ **UNRESOLVED (U3) — and it propagates.** The wheel-well depth in §5.10 is `tyre_width + 4 = 34.0`, i.e. built on **tyre_w = 30.0**. But our wheel v3 spec trims the cast rings from 30 → **27.0** to fit the well, and the parts register agrees. So either the well is 3 mm oversized or the trim hasn't happened. **Nobody has calipered the actual ring on the actual wheel.** I can do it today — ask me.

**`axle_z = wheel_od / 2 = 23.40`. Make this an assertion in your model.** Our v5 build violated it and the tyres sat 2.45 mm off the ground — the bot rode on its own rim. See §6.2.

Top speed at 130 rpm on a 46.8 wheel ≈ **0.32 m/s**. This is a tank, not a sprinter. That is deliberate.

### 4.2 Power

**Battery — Ovonic AIR 3S 2200 mAh 120C, XT60. ON HAND. ×2 owned, ONE goes on the bot.**

| | Value | Provenance |
|---|---|---|
| Body | **106.29 × 34.39 × 21.46** | MEASURED |
| Mass | **151.2 g** | WEIGHED |
| Connector | **XT60** | MEASURED (supplier substituted up from an ordered 1500 mAh 45C XT30) |
| Balance/charge lead | ~75 mm | MEASURED |
| Discharge lead | ~132 mm | MEASURED |
| **Bay to design for** | **110 × 38 × 24** | **DERIVED** — puff allowance, NOT the +0.5/side pocket policy |

> LiPos swell with age, heat and depth of discharge. A pack clamped in a tight pocket has nowhere to go. **Retain it with a strap, never by pinching it between walls.**
>
> **One pack on the bot.** Series (6S) would destroy the 12 V motors and the 3S fan. Parallel costs 151 g against ~23 g of headroom for runtime nobody needs — 2200 mAh already covers two 3-minute bouts.
>
> **Den wants the battery swappable mid-tournament without removing the lid.** Our current answer (numbers in §5.11) is an open rectangular aperture in the rear of the lid with the pack lifting clear of a low-walled sunk tub and drawing straight out. If you have a better idea, take it — but the swap must not require unbolting the lid.

**ESC — LittleBee Spring 30 A BLHeli_S. ON HAND. ×2 owned, one used.**

| | Value | Provenance |
|---|---|---|
| Board | 35.1 × 18.16 | MEASURED |
| **Heatshrink envelope (what must fit)** | **41.82 × 18.16** | MEASURED |
| Thickness | 5.55 fattest | MEASURED |
| **Power wires** | **~80 mm only** | MEASURED — this caps where it can live |
| Signal lead | ~152 mm | MEASURED |
| Mounting holes | **none** | MEASURED — it has to be strapped or pocketed |

> **Where it lives:** in the current layout it sits on **Board A** (the power board zone) with zip ties. There is no separate printed ESC saddle. Two traps: (1) 80 mm of lead minus routing leaves ~60 mm of usable reach to the power bus — verify before committing its position, or you are adding a solder joint to the highest-current wire on the bot. (2) **Do not fully enclose it in PLA.** Continuous EDF draw in a sealed pocket has nowhere to dump heat.

**XT60 + loop key (arming disconnect). ON HAND. ×5 pairs.**

| | Value | Provenance |
|---|---|---|
| Yellow panel socket body | 15.56 L × **8.13** W | MEASURED |
| **Over the side ridge** | **9.15** ← the retention feature | MEASURED |
| Socket overall height (tab tips → top) | 20.31 | MEASURED |
| Black key external | 16.47 × 9.23, protrudes **10.6** | MEASURED |
| **Panel cut-out** | **15.9 × 8.4** | **DERIVED** — sized from the 8.13 body, deliberately NOT the 9.15 ridge |

> The connector pushes in from **inside** until the 9.15 ridge bottoms on the inner wall face, so it cannot pull through when the key is yanked mid-match. Cut the slot at 9.7 to clear the ridge and the whole connector exits the first time someone pulls the key.
>
> The key protrudes 10.6 mm past the panel. That is a lever arm for an opponent — recess it into a shallow well.

**Power / start button — snap-fit, 3 pins. ON HAND.**

| | Value | Provenance |
|---|---|---|
| **Body Ø** | **18.51** (19.28 at widest) → hole **Ø18.70** | MEASURED → DERIVED |
| Overall height, pin tips → cap | 29.33 | MEASURED |
| **Panel thickness the clips grip** | **UNKNOWN — BLOCKING** | — |

> A snap-fit panel part only latches if the panel it grips is inside the clips' grip range (typically 1.0–2.5 mm). **If the wall is thicker than that range, the button never latches and no hole-diameter tuning fixes it.** Our current answer is a local circular pad of exactly the right thickness (Ø26, blended into the shell over a 6 mm annulus). A counterbore into a 1.6 mm skin is impossible — we tried to spec that and it was rejected, correctly.
>
> This button is **signal only**. It must never carry motor or EDF current. The XT60 loop key is the real disconnect. Its three pins are also unidentified — probably COM/NO/NC, and wiring an NC contact into a start path gives a bot that runs until you press the button.

**LiPo voltage alarm / buzzer. ON HAND.**

| | Value | Provenance |
|---|---|---|
| Body | **33.22 × 25.72 × 12.21** | MEASURED |
| Overall incl. pins | 38.67 (pins ~5.4 proud) | MEASURED |
| **Buzzer domes** | c-c **12.2**, ~4.7 wide each | MEASURED |
| Mounting holes | **none** | MEASURED |

> Needs: a pocket ~34 × 27 × 13 lying flat · **vents directly over both buzzer domes at 12.2 c-c or it is inaudible and pointless** · display readable and button reachable without disassembly · ~6 mm clear off the pin edge for the balance plug · friction fit + strap, not glue (it comes off with the battery).

### 4.3 The downforce fan

**XFly 1413 40 mm EDF, 12-blade, ~KV5000, 3S. ORDERED, NOT ARRIVED. ALL FIGURES SELLER.**

| | SELLER |
|---|---|
| Overall height | **49.0** (flange top → bottom of motor bell) |
| Duct/housing section height | 28.0 → motor protrudes 21.0 below |
| Housing OD | **43.0** (ears excluded) → bore **Ø43.3** target printed + shrinkage |
| Fan Ø | 40.0 |
| Intake lip | ~Ø47 |
| Mounting | **two small moulded ears on opposite sides, one hole each, roughly mid-height. Dimensions UNKNOWN** |
| Mass | 40 g claimed, never weighed |
| Leads | 3.5 mm bullets, 270 mm |

**What the chassis must reserve:**

| Reserve | Value |
|---|---|
| Duct bore | **Ø43.3** + printer shrinkage, through roof and pan |
| Bellmouth | R5 on the plenum side — worth 10–20 %, a sharp hole stalls the rotor |
| Lip seat | a shoulder the flange lands on, **Ø47.4–47.6 above / Ø43.5 below**, so the fan loads from the top |
| **Seat plane height** | **Z ≈ 13.0** in the current layout ⚠ see U4 |
| Clear space above the seat | **Ø72 for the first ~6 mm** (the clamp ring), then **Ø50 up to Z ≈ 63** (the fan body and motor bell) |
| Screw pattern | **4 × M3 inserts at 45/135/225/315° on a Ø60 PCD** ⚠ see U5 |
| Exhaust | Ø48 grille above, ≥65 % open, grille inner surface at **Z ≥ 64.0** |
| Air | **Do not fully enclose the motor — it is air-cooled** |

The mount is a separate printed clamp ring (Ø70 OD, Ø44.5 ID, 3 mm PETG) that pulls the fan's flange down onto a 1 mm silicone gasket (ID Ø44 / OD Ø52).

Load check: worst-case combined load on the mount is **~12 N** (pressure 1.2 N + thrust 3.0 N + 8 N impact shock). One M3 in tension handles several hundred. **The mount is sized by vibration loosening and by holding the intake lip on its seat, not by strength.** Threadlock everything, compliant washer anywhere the motor can buzz, gasket at the lip.

> ⚠ **UNRESOLVED (U4) — and it sets the total height of the robot.** Our EDF mount document says the fan's lip seat is *"at the bore bottom"* (i.e. at the pan underside, Z 1.5), which would put the fan top at Z ~50. Our v8 chassis prompt puts the counterbore *"measured down from the collar top"* at **Z 14.0**, which puts the fan top at **Z 62.0** — and the lid's flat top at Z 65.6 was derived from exactly that (62.0 + 2.0 clearance + 1.6 shell = 65.6, grille inner 64.00). **The two documents are ~12 mm apart and the lid was sized to the second one.** Pick one, say which, and derive the lid height from it.
>
> ⚠ **UNRESOLVED (U5).** The clamp ring is drawn for a **Ø60** screw PCD; the v8 chassis was drawn with pilots on a **Ø62** circle. That is the one number the two parts must share and they currently don't.
>
> ⚠ **OPEN RISK (U6).** The source listing says *"rotate the knob to control speed."* An EDF has no knob — it takes a BLHeli_S ESC on a 3-wire servo signal. If this is a 12 V vented cabinet fan rather than a real ducted EDF, its stall pressure is 10–40 Pa, not 800, and it produces ~50 g of downforce instead of 1.5–2.5 kg. **Brushless + 3-wire ESC lead = EDF. Two-wire brushed + speed knob = wrong part.** Unconfirmed until it lands.
>
> **Design consequence of U6:** the chassis should still be a competitive pusher if the fan turns out to be useless. Do not design something that is only viable with suction working.

### 4.4 Sensors

**VL53L0X time-of-flight (opponent detection). ON HAND.**

| | Value | Provenance |
|---|---|---|
| PCB | **24.78 × 10.32 × 3.18** | MEASURED |
| **Mounting hole c-c** | **19.79** | MEASURED |
| **Hole Ø** | **2.94** → M2.5 clearance, so pilots want **Ø2.1** for M2.5 self-tappers (NOT M2) | MEASURED → DERIVED |
| Field of view | **25°** | SELLER/datasheet |
| Header | 6-pin 2.54: VIN GND SCL SDA GPIO1 XSHUT | MEASURED |
| Pocket that fits | 26 × 12 × 4 | **CAD** |
| **Quantity on hand** | **5** ⚠ see U7 | MEASURED (counted) |

> **Pocket orientation matters and it cost us a revision.** On a curved, leaning tower wall a 26 mm *horizontal* opening drops 3.69 mm across its width, which shortened the effective pilot spacing to 17.79 instead of 19.79. The fix: rotate the pocket so the board's **long axis is vertical** — 12.0 horizontal × 26.0 vertical × 4.0 deep, pilots 19.79 c-c measured **vertically**. Plus a local flat seat (up to 1.5 mm of wall removed so the seat is planar across the full 12 mm) and a 5° wedge in the pocket floor so a board seated flat has a horizontal optical axis despite the wall lean.
>
> On a flat vertical wall none of that is needed. This is only a problem if you build a leaning tower.

> ⚠ **UNRESOLVED (U7).** The current layout uses **six** ToF sensors at yaws [0, +25, −25, +90, −90, 180] — adjacent 25° cones giving a seamless −37.5°…+37.5° front arc plus flanks and rear, 150° of coverage out of 360°. But: **we only have five on hand** (the count is disputed — 3 old + 5 new should be 8), and the wiring topology and PCF8574 pin budget in our own docs are written for **three**. Six sensors = 6 XSHUT + LED + buzzer = exactly 8 expander pins, one chip completely full.
>
> An alternative arrangement [0, +25, −25, +50, −50, 180] gives a continuous −62.5°…+62.5° front arc at the cost of flank awareness. **This is a genuinely open trade — tell me how many you'd use, where, and why.**

**TCRT5000 + LM393 line sensors (white-line edge detection). ON HAND. 5 on hand, 4 used.**

| | Value | Provenance |
|---|---|---|
| Module | ~32 × 14 × 10 | SELLER |
| **Bare sensor body (desoldered)** | 10.2 × 5.8 × 7.0 | SELLER — **NOT MEASURED, BLOCKING** |
| Pins | 4: VCC GND D0 A0 | MEASURED |

> **Decision already made and I'd like to keep it unless you have a better answer:** desolder the bare TCRT5000 off the module and fly 4 wires to the LM393 board sitting inboard, because the whole module needs ~16.4 mm of radial depth and the band available on our current geometry is 11.0 mm. The bare sensor fits; the module does not.
>
> Requirements: **optical face ≤5 mm off the floor**, pocket **open only downward**, IR-opaque walls (black PLA), no plenum leak, no crosstalk. At 0.32 m/s, 17 mm of detection lag is ~53 ms, which a fast control loop absorbs easily.
>
> Wire routing trap we hit: the wire hole must go **radially inward under the wedge skin** and pass through the roof plate *inboard of the knee*. Putting it in the pocket ceiling is wrong — outboard of the knee that ceiling faces atmosphere, not the bay.
>
> Run them off **3V3, not 5 V** — D0 goes straight into ESP32 GPIO 36–39 and the ESP32 is not 5 V tolerant.

### 4.5 Control and PCB

**TTGO T-Display (ESP32) — the required controller.**

| | SELLER |
|---|---|
| Outline | 51.5 × 25.5 |
| Headers | 2 × 12-pin |
| USB-C | on one short end |

> ⚠ **Unconfirmed at the time of writing (flagged since 2 Sep).** It is not in the carried-over inventory. Both wiring paths and the entire PCB hang off it. (Resolved 12 Sep: the board is a LilyGO T-Display S3, measured 62.3 × 25.65 × 6.88.)
>
> Current plan: TTGO lies **flat on the logic board with its display facing up**, visible through a window in the lid. There is no USB port in the shell — reprogramming is lid-off (four bolts, one plug) or over-the-air.

**Expansion PCB modules. ON HAND, MEASURED.**

| Module | Qty | Measured (L × W × H) | CAD box |
|---|---|---|---|
| DRV8871 motor driver | 4 (2 used) | 25.17 × 21.63 × 9.6 | 26.0 × 22.5 × 10.5 |
| MP1584EN 5 V buck | 4 | 13.86 × 9.95 × 7.84 | 15.0 × 11.0 × 8.5 |
| PCF8574 I/O expander (HW-171) | 4 | 54.64 × 15.62 × 11.29 | 56.0 × 16.6 × 12.0 |
| 1000 µF 25 V electrolytic | ~10 | can Ø10.38 × 16.99, ~18 mm standing | — |
| Protoboard (stripboard) | 1 | 160 × 63.8 × 2.74 | cut to size |

> ⚠ **UNRESOLVED (U8) AND IT AFFECTS YOUR LAYOUT.** The original brief reserved 70 × 50 = 3,500 mm² for the expansion PCB. The modules measure **~6,700 mm²** — the four PCF8574s alone are 3,720 mm², exceeding the entire reserved envelope before a single trace is routed.
>
> The three-ToF pin map only needed **one** PCF8574. The six-ToF arrangement (U7) needs one completely full. Either way it is not four. This is being settled with our electrical guy.
>
> **Tell me how much board area your layout can offer and I will size the board to it**, rather than the other way round — that is the more useful direction. The current layout offers two flat zones totalling ~3,400 mm² (Board A 2,280 mm² for power, Board B 1,130 mm² for logic), with M3 nylon standoffs and **no printed standoffs** — nothing stands proud of the roof. Stack height above the roof is ~20 mm (top at Z 31).
>
> There is also a **second PCF8574 inside the lid** in the current design, fed by one 4-way JST-XH through a Ø10 gland, driving all the ToF XSHUT lines, the opponent LED and the button locally — so the lid comes off as one plug and four bolts. Keep that pattern or replace it, but the lid needs *some* answer for its own wiring.

**M3 heat-set inserts — the only fastener on the bot.**

| | Value | Provenance |
|---|---|---|
| Insert used | 4.96 long × Ø4.48 knurl (one size, everywhere) | MEASURED |
| **Pilot** | **Ø4.15 × 6.0 deep**, boss Ø8.5, 0.5 chamfer | **CAD target** — this is the middle value of a coupon (4.00/4.15/4.30) that has not been printed yet |
| Rule | Never lubricate — brass must bond to melted PLA. Seat 0.1–0.2 below flush | — |

> **Policy: the person building this must never have to choose a part variant.** One insert size everywhere, one pilot everywhere. Variation is absorbed in CAD, not at the bench.

### 4.6 Consumables

| Item | Spec | Use |
|---|---|---|
| Silicone sheet | 1 mm × 250 × 250 | The skirt — cut into strips, bonded into a groove |
| Feeler gauge | 0.30 mm blade, 100 × 12.7 | Optional scraper lip at the leading edge |
| Silicone (Mold Star 15) | — | Cast tyres |
| Ballast | 20c coins 11.3 g, 50c 15.55 g | Trim to just under 1000 g |

---

## 5. CURRENT DESIGN AND WHY — context, not instruction

This is what we have now (v8), and the reasoning behind each choice. **Read it to understand the problem, not to copy the answer.**

### 5.1 Overall architecture

**Four printed parts:**

| Part | Qty | What it is |
|---|---|---|
| **BASE** | 1 | The wedge, the rim, the plenum, the seal loop, the wheel-well walls, the motor cradles, the battery tub, the board zones, the duct. The pressure vessel. |
| **LID** | 1 | Skirt, tower, flat top, all the sensor and access openings. |
| **WELLCAP** | 2 | A small open-bottom box that caps each wheel well from above, sealing on 3 mm EPDM foam. |

Plus PETG small parts: the EDF clamp ring, motor cap straps, skirt clamp strips.

The split is at the **knee** — a curve 34 mm inboard of the rim, at **Z 10.90**. Outboard of the knee and below Z 10.90 is BASE; above Z 10.90 and inboard of the knee is LID. (The base does have features standing above Z 10.90 *inboard* of the knee — tub walls, duct collar, motor cheeks, well walls. The knee is a plan-view boundary, not a height boundary.)

**Why the base is not split:** it is the pressure vessel. A glued seam in the plenum wall is a leak. 250 × 250 fits on a 256 bed with 3 mm to spare — a verified requirement, not an assumption.

### 5.2 The "sombrero" outer shape

A continuous ramp rising from a very low rim all the way round to a high centre.

**Reasoning:** an opponent's wedge that gets under you wins. A ramp that starts at 0.5 mm off the floor and rises means there is nothing to get under — they ride up instead. The sides are deliberately **climb ramps, not deflectors**: the intent is that a side attacker climbs onto our roof, at which point we yaw under software control and they slide off. We considered spraying a grip coating on the upper surface so a lifted opponent's wheels grab on and get carried off the arena.

**Outer curve:** a **superellipse** `|x/125|⁴ + |y/125|⁴ = 1` — 250 × 250 bounding box, r = 125.00 on the axes, r = 148.65 on the diagonals.

**Why a superellipse and not a circle:** it fills the corners of the legal box. A plain circle of Ø250 has 49,087 mm² of plan area; this superellipse has ~57,900. Since downforce = ΔP × A and area is free, that matters. It also gives four diagonal "corners" with useful depth for line-sensor pockets.

**Why not a square:** rim flatness on a printed 250 mm square, and print warping.

**Wedge angle:** currently a straight **15.14°** ramp from the rim (Z 1.70 at the top edge of the rim lip) to the knee (Z 10.90) — a 34.0 mm run and a 9.20 mm rise, identical at every bearing. Earlier versions used a two-slope profile (shallow then steep) and it was dropped for simplicity.

### 5.3 The rim

A continuous 1.2 mm-thick lip, underside **0.50 mm** off the floor, unbroken for the full 360°.

**This is the single most important defensive feature on the bot** and it is the thing our earlier revisions got wrong. v5 had *no rim at all* for 164° of the perimeter (the two claw sectors), so at the front and rear the only thing between an opponent's blade and our skirt was a bolted-on cover horn.

0.3 mm was the as-built value and it scrapes under load; **0.50 mm at rest with light contact under suction was chosen deliberately** so that scraping is a decision rather than an accident.

### 5.4 The plenum and the seal

| Level | Z |
|---|---|
| Rim lip underside | **0.50** |
| Rim lip top edge | 1.70 |
| Pan underside | **1.50** |
| Plenum cavity | **1.50 → 9.70** (8.2 mm deep) |
| Roof plate | 9.70 → 10.90 |
| **Roof top = knee height** | **10.90** |

**Main seal loop:** one closed wall, 3.0 mm thick, outer face at rim inset 20.0 and inner face at rim inset 23.0, running from the pan underside up to the wedge skin and fused to it. **A plain smooth offset — no detours, no boxes, nothing on it.** Every detour costs area and adds leak path.

**Skirt groove:** 1.3 mm wide × 2.0 mm deep, cut upward from the wall underside (open at Z 1.50, floor at Z 3.50), centred in the 3.0 mm wall, continuous through corners, with a 45° chamfer ~0.4 mm each side on the mouth so print support releases. 1 mm silicone sheet strips bond in with acetoxy adhesive, standing ~2 mm proud, touching the floor with ~0.5 mm interference.

**Ribs:** 8 radial, 2.0 mm wide with R1.5 root fillets, from r 30 outward to the main loop, skipping the duct, both well loops, the tub, the board zones and the sensor pods by ≥3 mm.

> ⚠ **UNRESOLVED (U9).** Our fan brief says the plenum wants **9–10 mm** of flow depth and explicitly rejected 7.0 mm on that basis. The built plenum is **8.2 mm**. Nobody reconciled that. It is probably fine — this is a static-pressure volume with very little flow — but if you change plenum depth, that's the reasoning chain you're arguing with, and it trades directly against axle height (§5.6).

**Bleed:** two Ø12 knock-outs in the roof, **sealed by default** with 0.6 mm membranes and a 0.4 mm annular score on the bay side, drilled out only if tuning shows we need bleed. A slight leak is actually a feature — the EDF motor is air-cooled and a dead-sealed plenum cooks it in 2–3 minutes.

**Straight-through duct:** plenum below → EDF pulling down → exhaust straight up through the top. Stationary gas means uniform pressure, so there is nothing to gain from channels, venturis or clever routing. Every bend is a loss.

### 5.5 The wheel wells — the thing we got badly wrong

**Current design:** each wheel sits in its own sealed well that is *outside* the plenum, with its own closed 3.0 mm seal wall carried down to the pan underside and its own skirt groove, so the wheel can touch the floor without opening a hole into the pressure vessel. The well is open to the arena below and capped above by a printed **wellcap**.

**Why:** see §6.1. Our earlier build put the wells *inside* the skirt loop, which meant ~3,600 mm² of clear shaft straight to the arena floor sitting inside the pressure vessel — roughly 9× the entire design leak — and that made the suction system produce approximately nothing.

**Cost of the fix:** −3,600 mm² of ceiling area and +~376 mm of skirt loop. **Worth it.** An alternative — sealing the well with a silicone flap rubbing on the tyre — was rejected: it rubs, it leaks anyway, and it makes the seal depend on tyre height.

**Track:** wheel centres at (14, 55) and (−14, −55) — 110 mm track, point-symmetric with a ±14 mm stagger in X. The stagger exists **only because the new motors are assumed 65 mm long** and two of them on one axle line would collide at the centre. Confirm the motor length and this may vanish, which would let the duct move back toward the centre and remove an asymmetry we don't want.

> **Geometry trap that cost us a revision:** a wheel mounted on a Y-axis presents its **diameter in X** and its **width in Y**. We had the well dimensions on the wrong axes for a full revision. Well interior is `wheel_od + 6` in X (= 52.8) and `tyre_width + 4` in Y (= 34.0, built on the assumed 30 mm ring — see U3).

### 5.6 Drive mounting

The motor rests **directly on the roof plate with no floor under it** — two side cheeks only, half-round Ø25.3, open at the top, with a cap strap. This was a deliberate change: a 1.2 mm pod floor under the motor pushes the axle 1.2 mm higher, and we didn't have 1.2 mm to give.

The **faceplate is the well's inner wall** — a 1.2 mm wall with a Ø8 shaft hole at axle height and two Ø3.2 holes at 17.00 c-c on the horizontal through the shaft centre.

**Constraint chain, and it is tight:**
```
roof top      = 10.90
motor bottom  ≥ roof top             = 10.90
motor axis    = motor bottom + 12.5  = 23.40 minimum
axle_z        = wheel_od / 2         = 23.40   ← with a 46.8 wheel this is EXACTLY on the limit
```
There is **zero margin**. A thicker roof, a deeper plenum, a pod floor, or a smaller wheel all break it. This is the constraint that most tightly couples the plenum to the drivetrain, and if you want to relax it, the levers are a bigger wheel (needs a new tyre mould) or a shallower plenum (argues with U9).

### 5.7 The claw

Front and rear both have an **80° arc scalloped into the wedge face**, horns at ±40°, recessed ~12 mm in plan, with the blade rising from the rim to ~35 mm at the core wall.

**Intent:** trap an opponent in the cavity so they can be carried, not just pushed. Front and rear are symmetric because in a sumo match you will end up facing the wrong way and there is no time to turn around.

**Hard rule learned the hard way: the rim line passes underneath the claw unbroken.** Earlier versions cut the claw *through* the perimeter, which destroyed both the rim armour and the seal loop in the same stroke.

**Candour:** this is the least-validated feature on the bot. In the v8 base the claw was actually dropped in favour of a plain continuous wedge with four small corner pods, and nobody has tested whether the claw earns its complexity. If you think a symmetric 80° scallop is the wrong way to trap an opponent, say so.

### 5.8 The lid

- **Skirt:** a prismatic section (outer at rim inset 36.4, inner at 38.4, so 2.0 thick) that drops *inside* a collar on the base, 0.4 mm radial clearance, from **Z 10.90 to Z 20.90**. **HARD RULE: no lid surface is ever radially proud of the base.** Anything proud is something an opponent's blade can catch.
- **Tower:** above Z 20.90 the outer face leans inward **5° from vertical**, measured **from the skirt top as the datum** — outer face at height Z is rim inset (36.4 + (Z − 20.90)·tan 5°). Shell 1.6 mm.
- **Flat top** at **Z 65.6**, inner face at 64.00 (which is exactly the EDF grille-inner requirement).
- **Anti-climb lip:** 6 mm proud of the tower, widest at Z 53.0, with a **flat horizontal underside** at Z 53.0 and a 45° upper face running back into the tower at Z 59.0 — so something climbing us hits a square catch edge. Its widest point must still be inboard of the base collar.
- **Fixings:** **4 × M3**, at (±74, ±74), through 16 × 16 × 3.0 pads on the skirt's inner face into heat-set inserts in the base. Countersunk, nothing proud.

> **The tower-lean datum is the single number that cost us most on the lid.** Measuring the lean from Z 10.90 instead of the skirt top at Z 20.90 produced a 1.763 mm up-facing ledge right where the lid meets the base — a perfect ramp for an opponent's blade. Whatever shape you build, **state your lean datum explicitly and check the radial step at the transition is 0.00.**

> **Two lid fixings were deleted** (they were at (0, ±82)) because their 16 × 16 pads reached to Y 72, which is inside the wheel-well rectangle. That single mistake produced every clearance failure on that revision. Four M3 on a 148 mm diagonal square is ample: the register collar carries lateral load, the bolts only resist lift.

**Why the top is flat, and this one is near-non-negotiable:** the lid prints **upside down, flat top on the bed**. A domed top printed that way needs multi-stage support; a flat top printed skirt-down would be a 158 mm unsupported bridge. Flat top, printed top-down, tower flaring outward as it grows = self-supporting everywhere, zero supports. If you can find a shape that prints with no supports *and* isn't flat, I'm interested — but the print constraint outranks the aesthetics.

We **dropped the lidar entirely** (it was going to sit on the crown) to keep this simple.

### 5.9 Bottom-heaviness

Computed CG heights on the real meshes:

| Layout | CG height |
|---|---|
| Battery on the roof, PCB on 40 mm posts | **24.78 mm** |
| Battery in a sunk tub, PCB flat on the roof, smaller lid | **21.18 mm** |

−3.6 mm at identical mass. Contributions, biggest first (these overlap and do not sum exactly to the total):

| Move | CG effect |
|---|---|
| **PCB off tall posts onto the roof** | **−1.84 mm** ← biggest single win, and it's free |
| Battery into a sunk tub | −1.07 mm |
| Axle drop 26 → 23.4 | −0.50 mm |
| Lid shrinks | −0.46 mm |
| Ballast into plenum-side pockets | −0.17 mm |

**The PCB was the problem, not the battery.** 65 g on posts at Z 40 cost more CG than the 151 g battery did.

**The sunk battery tub costs zero downforce** — the tub's underside is still plenum ceiling, so the projected low-pressure area is identical. It only costs local flow depth, and the plenum is a static-pressure volume with almost no flow, so routing air around a 38 mm island is a non-issue.

But see §3.4 — this is worth having because it's nearly free, not because it's what saves us.

### 5.10 Current verified plan layout (v8)

If you want a starting point rather than a blank sheet, this is the layout we solved numerically — 28 envelopes rasterised at 0.5 mm, all 378 pairs tested, zero overlaps outside six declared fusions.

"RIM INSET d" = the superellipse offset d inward along its local **normal** (not a radial scale — on the diagonals a normal offset differs from a radial one).

| Curve | RIM INSET | r on the axes | r on the 45° diagonals |
|---|---|---|---|
| RIM | 0 | 125.00 | 148.65 |
| Seal loop outer face | 20.0 | 105.00 | 128.65 |
| Seal loop inner face | 23.0 | 102.00 | 125.65 |
| **KNEE** = base collar outer | 34.0 | 91.00 | 114.65 |
| Base collar inner | 36.0 | 89.00 | 112.65 |
| Lid skirt outer | 36.4 | 88.60 | 112.25 |
| Lid skirt inner | 38.4 | 86.60 | 110.25 |

| Envelope | Plan extent |
|---|---|
| Wheel, +Y side (diameter in X, width in Y) | X −9.4…37.4, Y 40…70 |
| Well interior, +Y (52.8 × 34.0) | X −12.4…40.4, Y 38.0…72.0 |
| Well seal wall outer (1.2 wall + 3.0 seal) | X −16.6…44.6, Y 33.8…76.2 |
| Motor cheeks (both cradles, one shared spine) | \|X\| ≤ 28.355, \|Y\| ≤ 33.8 |
| Duct collar Ø58 at (52, 0) | X 23.0…81.0, Y ±29.0 |
| Battery tub outer (rear corners chamfered 2×2) | X −85.0…−46.6, Y ±55.45 |
| Battery itself | X −83.8…−47.8, Y ±53.15 |
| Corner sensor pods ×4, centre r 120.15 on each diagonal | 13.8 tangential × 8.6 radial |
| Board A (power + ESC) | X 20…77, Y −76…−36 (2,280 mm²) |
| Board B (logic + TTGO) | X 46.6…78, Y 32…68 (1,130 mm²) |
| Lid fixings ×4 | (±74, ±74) |

**Declared fusions** (allowed, named, not conflicts): motor cheeks ↔ well seal walls (the faceplate *is* the well's inner wall) · cheeks ↔ duct collar (they merge below Z 14) · the two cradles share one central spine · collar band ↔ seal loop wall.

**The diagonal band available for a corner sensor pod is exactly 11.00 mm.** That is why it carries a bare desoldered TCRT5000 rather than the whole module.

### 5.11 Vertical stack — every Z level in the current design

This is the table whose absence caused most of our lid failures.

| Z | Feature |
|---|---|
| 0.50 | Rim lip underside |
| 1.50 | Pan underside; plenum floor; skirt groove mouth |
| 1.70 | Rim lip top edge |
| 2.70 | Battery tub outer floor |
| 3.50 | Skirt groove floor (2.0 deep) |
| 3.90 | Battery tub inner floor |
| 9.70 | Plenum ceiling / roof plate underside |
| **10.90** | **Roof top = knee = base/lid datum.** Lid skirt bottom sits here |
| 13.00 | Battery tub wall tops |
| 14.00 | Duct collar top; cheek↔collar fusion ends here |
| ~13.0 | EDF lip seat plane ⚠ U4 |
| 16.90 | Base collar top |
| 20.90 | **Lid skirt top — the tower-lean datum** |
| 22.00 | Battery aperture sill (1.10 mm above the skirt top, skirt unbroken) |
| 25.36 | Battery top surface |
| 31.00 | Board A / Board B stack top |
| 33.00 | Motor cheek tops |
| 39.00 | Well wall tops + their four M3 insert bosses |
| 46.00 | Battery aperture head |
| 48.00 | Wellcap ceiling underside (1.20 clear over a 46.8 wheel); ToF slot centres |
| 49.20 | Wellcap top |
| 51.00 | Rear ToF slot centre (raised to clear the battery aperture) |
| 53.00 | Anti-climb lip widest point, flat underside |
| 59.00 | Anti-climb lip 45° face meets the tower |
| **62.00** | **EDF top** ⚠ U4 |
| 64.00 | Flat-top inner face = grille inner requirement |
| **65.60** | **Flat top — highest point on the robot** |

**Required lid-inner clearances** (measure the lid's inner surface Z over each rectangle; any miss is a failure, and the fix is never to shrink the pocket):

| Over | Lid inner must be ≥ |
|---|---|
| Wellcap rectangles | **52.0** |
| Board A | 34.0 |
| Board B | 34.0 |
| Battery | 28.0 |
| EDF grille | 64.0 |
| Motor cheeks | 36.0 |
| Well walls and their bosses | 42.0 |

**Battery access aperture** (current answer to swap-without-lid-removal): one open rectangle through the rear tower, centred on the −X axis, **sill Z 22.00, head Z 46.00 (24.0 tall), 112.0 mm wide** along the tower surface, edges filleted R1.5. No cover, no latch. Clear opening must be ≥110 × ≥23 so a 106.29 × 21.46 pack passes. It costs **zero downforce** — the plenum is sealed below the roof plate and the bay above it is already at ambient. The sill is 1.10 mm above the skirt top so the skirt stays unbroken.

**Other lid openings** (all on the flat top unless noted): EDF grille Ø48 at (52, 0) · TTGO window 34 × 22 at (62, 50) with a 1 mm ledge for acetate · LiPo alarm pocket 34 × 27 × 13 hanging down at (−20, −45) with a 30 × 20 display window, two Ø4 vents at 12.20 c-c and a Ø8 finger hole · button pad Ø26 at (10, 40) · group-number recess 60 × 25 × 0.6 at (0, 70) · opponent LED Ø5.2 at (0, −70) · harness gland Ø10 at (−20, 20). **These must not overlap each other** — a previous revision put the group panel 18.5 mm into the fan grille.

---

## 6. KNOWN DEFECTS — please do not reinvent these

Every one of these cost us at least one print cycle or one full revision.

### 6.1 The wheel wells were open holes in the pressure vessel ⚠ WORST ONE

Flood-filled the plenum at Z = 7 on the real mesh and tested every cell for material at any Z:

| | mm² |
|---|---|
| Plenum area flooded | 30,217 |
| **Of which open floor-to-sky** | **~3,800** |
| — +Y wheel well | 1,769 |
| — −Y wheel well | 1,830 |
| — two Ø12 bleed holes (intentional, tape-closed) | 226 |
| Design skirt leak (764 mm loop × 0.5 mm) | 382 |

The well walls existed only from the roof upward. Below the roof there was nothing — a clear shaft to the arena floor, *inside* the skirt loop. A tyre blocks only its contact patch (~290 mm² each), so ~3,000 mm² stayed open, roughly **8× the entire design leak**. At a plausible ~8 L/s through that area, orifice velocity is ~2 m/s and ΔP is single-digit pascals. **The suction system produced effectively zero downforce regardless of how good the skirt was.**

**Whatever architecture you choose: run a flood-fill / ray-cast test that proves the plenum is closed.** Our acceptance criterion is **≤60 mm² of total open area** from the arena floor into the bay (that budget is four sensor wire holes at Ø4.21), excluding the duct bore which the fan fills.

### 6.2 The wheels did not reach the ground

Saddle floor at Z 13.35 + Ø25 motor can → axle held at Z 25.85. Measured wheel OD 46.8 → radius 23.4. Wheel bottom = **Z +2.45**. The bot sat on its rim and skirt with the tyres in the air.

Root cause: the chassis was built to a brief that had chosen **wheel OD 52** so the motor would clear the plenum roof. The wheels that actually exist are 46.8. Nobody re-derived the axle height when the wheel changed.

**`axle_z = wheel_od / 2` must be an assertion that fails the build.**

### 6.3 The battery bay was sized to the wrong battery

Brief reserved 75 × 40 × 30. The pack that arrived is **106.29 × 34.39 × 21.46** — 33 mm longer. It did not fit in the core at all.

### 6.4 Cover horns landed on base sensor boxes

The cover's claw horns came down onto the line-sensor boxes the base had put on the diagonals, so the cover perched ~14 mm high and would not seat. The base prompt promised "nothing outside r 96 in the sectors" while a different section of the *same* prompt put a 37.5 mm box on the diagonal. **No self-check tested it.**

### 6.5 v7: 38 envelope overlap pairs

The model built cleanly and the parts overlapped each other, because the brief was self-inconsistent. Root cause included the wheel-well axis swap (§5.5).

**The fix we adopted, and I'd like you to keep it:** solve and verify the layout **numerically first** — rasterise every envelope and test all pairs for overlap — and only then generate geometry. Declare any intentional fusions by name.

### 6.6 v8 lid: 23 failures, 9 of which were contradictions in our own brief

All the same class of error:

- Tower lean measured from the wrong datum → a 1.763 mm up-facing ledge where the skirt met the tower
- Flat-top Z derived from a shell thickness that contradicted the stated shell thickness
- ToF pockets specified with a horizontal long axis on a curved, leaning wall — the wall fell 3.69 mm across a 26 mm opening, so pilot spacing came out 17.79 instead of 19.79
- A battery hatch whose aperture cut through the skirt
- Lid fixing pads reaching into the wheel-well rectangles — this produced *every* clearance failure on that revision
- A Ø24 counterbore specified into a 1.6 mm skin (impossible)
- Two "separate" TTGO openings that overlapped by 7 mm in Z
- A flat pocket specified on a curved tower wall with no flat seat
- A group-number panel overlapping the fan grille by 18.5 mm

**The lesson: when a brief and geometry disagree, the brief is usually wrong. Name the contradiction, don't silently move geometry to resolve it.** That is exactly what I want you to do with *this* document too — I have flagged the conflicts I found, and there are probably more.

### 6.7 Small ones

| Item | Was specified | Reality |
|---|---|---|
| Power button hole | Ø12 | body is Ø18.51 — someone specced a different button |
| Buzzer pocket | 32 × 14 × 10 | alarm is 33.2 × 25.7 × 12.2 — nearly 2× the width and too shallow in every orientation |
| ToF pilots | Ø1.8 for M2 | holes are Ø2.94, M2.5-clearance → Ø2.1 pilots |
| M3 insert pilot | Ø4.0 × 5.7 | Ø4.15 × 6.0 (still a coupon target, not yet verified) |
| Every hole on the bot | nominal | +~0.21 mm printer shrinkage |
| Chassis mass estimate | ~220 g | **267 g weighed** — ate 57 g of ballast headroom |

---

## 7. MASS BUDGET — you have roughly 23 g of slack

Limit **1000 g**. Working target **985–995 g** (ballast right up to the line, because ballast is normal force and normal force is push).

| Item | Qty | g each | Total | Confidence |
|---|---|---|---|---|
| **Chassis, printed** | 1 set | — | **267** | **WEIGHED** — but see the note below |
| PETG small parts (clamp ring, cap straps, skirt strips) | — | — | 45 | estimate |
| Skirt silicone + adhesive | — | — | 20 | estimate |
| M3 inserts + fasteners | ~25 | — | 30 | estimate |
| **Structure subtotal** | | | **362** | |
| Motors | 2 | 95 | 190 | ⚠ **SELLER, never weighed** |
| Wheels with tyres | 2 | 37 | 74 | ⚠ never weighed |
| Battery | 1 | **151.2** | **151.2** | **WEIGHED** |
| EDF | 1 | 40 | 40 | SELLER |
| ESC | 1 | 25 | 25 | never weighed |
| Expansion PCB + modules | 1 | 65 | 65 | estimate |
| Alarm, button, XT60, wiring | — | — | 60 | estimate |
| **TOTAL** | | | **≈ 967 g** | |
| **Ballast headroom to 990** | | | **≈ 23 g** | |

> ⚠ **Three caveats on that 267 g, and together they are worth ~100 g:**
>
> 1. **It is the v5 housing + v5 cover** (153 g + 113 g), weighed on the scale. That architecture is retired. The v8 base's computed mass is ~154 g and the v8 lid target is ≤110 g, i.e. ~264 g — no regression, but it is a computed figure, not a weighed one.
> 2. **We do not know whether the 267 g included the PETG small parts or just the two big prints.** If it already included them, the structure subtotal drops to ~317 g and total to ~922 g, giving **~68 g of ballast instead of 23 g.** That is the difference between comfortable and almost none, and it is one trip to the scale away. It has not been done.
> 3. **The two current mass targets (base ≤175 g, lid ≤110 g) total 285 g**, which is 18 g *above* the 267 g the budget line uses. Hitting both targets and no better would consume most of the remaining ballast.

**Structure is the lever you control.** If your design is lighter, that is directly more ballast, which is directly more push. **Beating base 175 g / lid 110 g is valuable.**

Levers if it goes over, cheapest first: shell 2.0 → 1.6 mm with ribs (−25 g) · pan 6 → 4 perimeters (−10 g) · infill → 15 % gyroid (−8 g). *(An older list also suggested deleting a crown dome — the current lid has a flat top and no dome, so that lever no longer exists.)*

---

## 8. WHAT I WANT YOU TO DELIVER

### 8.1 The output

1. **STL file(s)**, binary, millimetres, ready to slice on a Bambu Lab X1C. Name them clearly.
2. Generate the mesh **analytically** where possible. Any skin thinner than ~1.6 mm built from a voxel/marching-cubes approach comes out terraced.
3. A **self-check panel that measures the exported mesh**, not the design intent. Several of our failures were caught only because the check measured the actual vertices.
4. A **written rationale** — what you changed from our approach and why.

### 8.2 Self-checks I want to see, whatever architecture you pick

| Check | Criterion |
|---|---|
| **Plan-overlap map** | Every envelope pair tested, zero overlaps outside explicitly declared fusions |
| **Plenum closure** | Flood-fill + vertical ray-cast: total area open from arena floor to bay **≤ 60 mm²**, itemised, with knock-outs reading CLOSED |
| **Skirt groove continuity** | Every loop continuous, no interruption, minimum depth held, lengths reported |
| **Wheel fit** | Clearance from the wheel envelope to the well interior on **all four sides** of **both** wheels, all positive. *This is the check that did not exist in v7 and it is the one that killed it.* |
| **Axle identity** | `axle_z = wheel_od / 2`, exactly |
| **Motor clearance** | Motor bottom ≥ roof top |
| **Interior clearance envelope** | Lid inner surface Z over every roof feature, measured, against the required values in §5.11, pass/fail per rectangle |
| **Radial step at the base/lid transition** | 0.00 (this is the ledge that cost us a revision) |
| **Nothing proud** | No lid surface radially outboard of the base, at any height, at 36 bearings |
| **Steepest overhang** | ≤ 55° from horizontal in the stated print orientation, worst location named |
| **Bounding box** | ≤ 250 × 250 × 250 |
| **Mass** | Volume, and mass at both 1.24 and 1.017 g/cm³ (the 0.82 real-print figure) |
| **Watertight** | Open-edge and non-manifold-edge count = 0 |
| **Holes** | Every hole/bore/pilot includes the shrinkage offset |

**When a check fails: fail the build, print the constraint, the measured value and the required value. Never silently move geometry to make something fit.** If two requirements genuinely conflict, name the pair and stop — that means my brief is wrong and I need to fix it, not you.

### 8.3 Print notes I need from you

Orientation per part · material · layer height · wall count · infill · **exactly where support is needed and where it anchors** · any coupons to print first.

Support that anchors to the bed only is fine. Support that anchors onto the part is a problem — I have snapped thin ribs peeling PLA support off before.

Coupons we already know we need, shrinkage first because its result changes the others: **hole shrinkage (4.00 / 4.15 / 4.30)** · motor cheek bore (25.1 / 25.3 / 25.5) · skirt groove (1.25 / 1.30 / 1.35).

---

## 9. WHERE YOU HAVE FREEDOM — please use it

**Genuinely open. Change these if you can justify it:**

- The **overall shape**. Superellipse, circle, something else. We chose a superellipse to fill the legal box and maximise sealed area; if you have a better answer, take it.
- **How the parts split.** Base + lid + 2 wellcaps is where we landed for print-orientation reasons, not from first principles.
- **The wedge profile** — single slope, two slope, curved. Currently a straight 15.14°.
- **The claw.** Least-validated feature on the bot, and the current base doesn't even have one.
- **Where the fan duct goes.** It's at (52, 0) rather than the centre *only* because two assumed-65 mm motors occupy the middle. That off-centre duct puts the pressure centre 50 mm ahead of the axle, loading the front lip harder — an asymmetry we accepted rather than chose.
- **Motor mounting approach**, as long as the axle-height chain in §5.6 closes.
- **How the wheel wells are sealed**, as long as you can prove the plenum is closed.
- **Where the electronics go**, as long as the battery is swappable without lid removal and the CG stays low.
- **ToF count and angles** — see U7, this is genuinely unresolved.
- **Board area** — tell me what you can offer and we'll size the PCB to it.
- **Everything about the lid** other than needing to print without supports.
- **Anything I've got wrong.** Especially the physics — if my downforce numbers are optimistic or my push-force model is naive, tell me.

**Not open** (rules or physics, not preference):

- 250 × 250 × 250 box, 1000 g, TTGO controller, opponent-detection indicator, visible group number
- 256 × 256 print bed, no support anchored onto the part
- Continuous unbroken rim — see §3.4 and §5.3
- No lid surface radially proud of the base
- The parts list in §4 — we own these
- `axle_z = wheel_od / 2`
- The plenum must actually be sealed, and you must prove it

---

## 10. OPEN ITEMS

### 10.1 Unknowns I can resolve today — just ask

| # | Unknown | Why it matters |
|---|---|---|
| 1 | **Actual tyre width** on the fitted wheel (30 or trimmed to 27?) | Sets the wheel-well depth in Y. See U3 |
| 2 | **Bare TCRT5000 body dimensions** | Sets a pocket cut into the shell |
| 3 | **Button panel grip thickness** (flange underside → top of clip barbs) | If the wall is outside the clips' range the button never latches |
| 4 | **The CAD bore value used on the wheel hub** | Turns the 0.21 mm shrinkage figure from a guess into a constant. Applies to every hole on the bot |
| 5 | **Screw head height** above the old motor faceplate | Sets relief pockets in the well |
| 6 | **Re-weigh the chassis with every printed part on the scale at once** | Settles a 45 g swing in ballast headroom. See §7 |
| 7 | **Weigh the motors, one wheel, the ESC** | ~330 g of a 967 g budget is estimates; 190 g of it is the motors |
| 8 | **Recount the ToF sensors** | 5 or 8? Determines whether the six-sensor layout is even possible |

### 10.2 Waiting on parcels or people

| # | Unknown | Status |
|---|---|---|
| 9 | **New motor pair — length, diameter, mass, everything** | Not arrived. Assume 65 mm; design to tolerate 39–69 |
| 10 | **EDF — flange OD and thickness, ear dimensions, ear hole Ø and c-c, which end is the intake, mass** | Not arrived. Ten caliper readings the moment it lands |
| 11 | **TTGO T-Display — does it physically exist** | Flagged since 2 Sep, never confirmed |
| 12 | **PCF8574 count** | Halves or doubles the required board area |
| 13 | Whether a BLHeli_S ESC counts as an allowed "motor controller"; whether pre-start fan spool-up is allowed | With staff |

### 10.3 Conflicts between our own documents — I want your read

| # | Conflict |
|---|---|
| **U1** | Seal loop at **rim inset 18** (physics, §3.2) vs **rim inset 20** (built layout, §5.10). Worth ~1,500 mm² / ~1.2 N |
| **U2** | Wheel hub motor-face counterbore **Ø9.0 × 2.5** vs **Ø9.0 × 3.0** deep |
| **U3** | Tyre width **30.0** (used to derive the 34.0 well depth) vs **27.0** (the trimmed ring our wheel spec calls for) |
| **U4** | EDF lip seat at the **bore bottom (Z 1.5, fan top ~Z 50)** vs at the **duct collar (Z ~13, fan top Z 62)**. The lid's 65.6 flat top was derived from the second. **This sets the height of the entire robot** |
| **U5** | EDF clamp-ring screw PCD **Ø60** (ring drawing) vs **Ø62** (chassis pilots). The one number that must match |
| **U9** | Plenum flow depth: fan brief wants **9–10 mm**, built plenum is **8.2 mm**. Trades directly against axle height |

---

## 11. TIMELINE

Today is **11 September 2026**.

| When | What |
|---|---|
| **w/c 21 Sep** | First drive — 1 m forward, stop, 1 m back, stop. Needs a rolling platform driven by the ESP32 |
| **w/c 12 Oct** | Competition + push-out demo |

A chassis print is roughly a working day. **The first drive can run on a rolling test platform if it has to** — it's drive-only, no fan, no sensors. So the real deadline for a competition-ready chassis is early October, with at least one iteration cycle before it.

---

## 12. TL;DR for the impatient

Build a 250 × 250 × ~66 mm 3D-printed sumo robot chassis, under 1 kg all up, that:

1. Has a **continuous unbroken low rim** (0.50 mm off the floor) all the way round so nothing can get under it, with no part of the lid ever radially proud of the base.
2. Contains a **sealed plenum** big enough that a 40 mm EDF at 800 Pa gives ~30–35 N of downforce — and **prove the seal is closed** to ≤60 mm² of open area, because our last one leaked ~3,000 mm² and produced nothing.
3. Holds two gearmotors with the axle at exactly **half the 46.8 mm wheel diameter** (Z 23.40, zero margin), with the wheels in sealed wells **outside** the plenum.
4. Fits a 106 × 34 × 21 mm battery low down and swappable without removing the lid, plus ~3,400 mm² of board area, a 30 A ESC, five-or-six ToF sensors, four downward line sensors ≤5 mm off the floor, an arming connector, an alarm, a button, an LED and a group number.
5. Prints on a 256 mm bed as a base + lid (+2 well caps) with **no support anchored to the part**.
6. Comes in under ~265 g of printed structure so there's ballast headroom left.

**Then tell me what I got wrong.**

---

*Reference documents in the project knowledge base, if the handover recipient has access: `SumoBot_Hardware_Spec_Sheet.md` (authoritative measured dimensions) · `SumoBot_v6_Chassis_Review.md` (mesh-measured defect analysis) · `SumoBot_v8_Prompts.md` (current verified layout) · `SumoBot_v8_Lid_Mod.md` (lid corrections) · `SumoBot_EDF_Mount_Spec.md` · `SumoBot_Parts_And_Wiring.md` · `SumoBot_Mass_Budget.md` · `SumoBot_Downforce_Fan.md` · `SumoBot_Decisions.md`.*
