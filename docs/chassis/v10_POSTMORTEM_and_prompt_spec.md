> **Superseded 12 Sep 2026.** The chassis is v11 (`docs/chassis/v11/START_HERE.md`) and the parts register below is replaced by `docs/hardware/MEASURED_PARTS.md`. Kept for the reasoning/history.

# SumoBot — Astra v10 postmortem and prompt spec

Prepared 12 Sep 2026. Sources: the full Astra v10 package (README, PRINT_LIST, VERIFICATION_REPORT, build.py, parameters.json, interfaces.json, checks JSON, 5 renders), the 4 handover docs Astra was given, and 22 project docs (measured parts, wiring, specs, v5→v9 prompts, decisions, postmortem, competition brief). Four AI subagents did the reading; this is the triage.

Frame throughout: mm, Z = 0 arena floor, +X front, +Y left.

---

## 0. TL;DR

Astra did what it was told. The prompt it was given (`SumoBot_Astra_Build_Handover.md`) is a **reviewer's audit**, not a design brief. It ranks "proposed dimensions and styling inherited from earlier versions" **fifth of five** priorities, opens with "Create an **original**… chassis", attaches four docs each labelled as unreliable or contradictory (30 "do not"s in 3,900 words), and contains no shape specification of its own. The shape *is* written down in the v9 master brief (§3 "FROZEN ARCHITECTURE") and the v9 handover (§5 "sombrero") — but the handover demotes its own §5 to "context, not instruction", and the Astra prompt says "do not simply reproduce v9". So Astra threw the shape away, kept a handful of inherited numbers without their reasons, and optimised for the one thing the prompt rewarded: a defensible verification report.

Fix: write the shape first (silhouette, five sentences and a reference image), freeze the layout in one file, rank layout above originality, and run it in two shots (layout → approve → solids), not one.

---

## 1. What went well (keep these)

| Thing | Why it's good |
|---|---|
| Real CAD kernel (CadQuery/OCCT), parametric `build.py`, `parameters.json` with provenance tags, `interfaces.json` for shared coordinates | This is the pipeline the postmortem §17 asked for and never got. **Reuse the pipeline, replace the design.** |
| 53/53 meshes watertight, STEP re-import valid, zero unintended solid overlaps | First build in the project with a clean mesh *and* a clean overlap check |
| Pressure isolation actually tested (3D flood fill at 0.8 mm + negative control) | Not a "panel of numbers" — a real connectivity test |
| Wheel wells sealed **out** of the plenum with their own skirt loops | The v5/v6 lesson (3,599 mm² of open well) correctly applied |
| `axle_z = wheel_od/2 = 23.40`, wheels touch the floor, motor bottom 1.1 mm above deck | The v5 "tyres in the air" bug did not recur |
| Battery: straight rear extraction, no lift over a sill, swept-volume checked | **This is DEC-13 — the blocker v7/v8/v9 never solved.** Astra solved it |
| Blind sealed insert bosses (no pilots through the 1.2 roof), 4 lid fixings, XT60 disconnect reinstated, open alarm window, button keep-out column | All lessons from the failure register, applied |
| Honest MEASURED / SELLER / PROPOSED / UNKNOWN tagging; fit coupons before the big print | Good discipline — keep it |
| Mass 951 g nominal, with a sensitivity case that *fails* (1016 g) flagged rather than hidden | Honest |

---

## 2. What went off the rails

### 2.1 The shape (the thing you actually care about)

| You wanted (v5→v9 docs, every version) | Astra built |
|---|---|
| **Sombrero**: superellipse 250×250, continuous 360° ramp at **15.13°** from a rim **0.50 mm** off the floor up to Z 10.9, then a leaning tower with an anti-climb lip, flat top Z 65.6 | **Octagon slab** 240×240, rim **2.2 mm** off the floor, 3 mm vertical band, then a **10.9° ramp only 4.6 mm tall**, then a **vertical-walled rectangular box lid** (201×156) with 0.8 mm skin |
| "An opponent's wedge that gets under you wins. A ramp from 0.5 mm means there is nothing to get under" | Attack profile front-to-back: skirt (Z −0.5) → **vertical 3 mm band Z 2.2–5.2** (a blade goes under it) → 10.9° ramp for 24 mm → **vertical lid wall Z 9.8–65.6**. The ramp only catches tips between Z 5.2 and 9.8 |
| "No lid surface ever radially proud of the base" | Lid box starts at Z 9.8 but the deck only reaches 96 mm half-width → **1.6–1.7 mm open slot under the whole 156 mm front wall** (only the two Ø10 lid-mount lands touch) |
| Anti-climb lip 6 mm proud, flat underside | 4 mm lip, on a box |
| Rim = hard PLA armour, continuous | Rim at Z 2.2 — a blade goes straight under it |

### 2.2 Layout choices Astra made on its own

| Choice | Where it came from | Problem |
|---|---|---|
| **Motor stagger ±14 mm** → wheel axles 28 mm apart, 8.6° contact-patch skew | `motor_x_offset = 14` is in your v9 brief — but the v9 handover says "**an asymmetry we don't want**… exists only because the new motors are assumed 65 mm long". Astra kept it, set `motor_length = 69` (worst case), and kept the stagger even though at its own track (184 mm) the motor **bodies** don't collide — only a PROPOSED 16×12 encoder-tail box does | Forced tyre scrub on every turn; the whole bot became point-symmetric, not mirror-symmetric |
| **Fan at X +64** | "Clearance from staggered motors" — a direct consequence of the stagger | Pressure centroid stays at (0,0), fan mass and grille are 64 mm forward |
| **Wheels outboard at Y ±92 in taped-on 1 mm box guards** | Nothing in your docs — your docs have wheels at Y ±55 in sealed wells inside the footprint | 112 mm lever arms, 1.0 mm clearance to an unmeasured tyre, retained by cloth tape |
| **Electronics on a tray at Z 38–62** | Nothing in your docs — the v9 master brief (§14.4) says "getting the PCB **off** the Z 40 posts was the single biggest CG win… 65 g on posts at Z 40 cost more CG than the 151 g battery" | Put the CG back up |
| **ToF carriers bolted on the *outside* of the front/rear faces**, PCBs 6–9 mm proud, six 34×18 holes in the walls | Nothing in your docs — you had them in 12×26 pockets flush in the tower | 5 exposed PCBs on the two impact faces |
| **Both pitch skids at Y = +60** | Loop bug (`sy=60` never varies) | No anti-tip contact on the right half at all |
| **41 printed pieces (21 distinct designs) + 2 alternatives + 10 coupons = 53 STLs**, brackets/guards/shelves/rails all separate, retained by tape and straps | The prompt's "a removable motor/well upper carrier is worth evaluating" + "use replaceable adapters to keep unmeasured parts from forcing reprints" | Everything became an adapter. The base is a flat plate with holes. Your design is 5 parts |
| **21 of 31 top-level parameters are PROPOSED**, 6 SELLER, 2 UNKNOWN (only `wheel_od` and `battery_mass_g` MEASURED) | The prompt said measured > seller > proposed, but gave it almost no measured layout numbers to use | Astra invented the layout because nobody handed it one |
| Comparator shelves at X −66 / +64 | Typo-class asymmetry | Nobody looked |

### 2.3 What the deliverable optimised for

Count across the package: "provisional" ×32 (12 of them in the print list alone), "NOT VERIFIED" ×8, and 21 of 31 tagged parameters PROPOSED. The prompt's §8 and §9 asked for exactly this — PASS/FAIL/NOT VERIFIED on every gate, "do not claim", "honest completion". Astra delivered a very honest report about a robot you don't want. There was no gate for "does it look like the robot Den described" because no such description existed.

---

## 3. Why — the prompt, line by line

These are the specific lines in `SumoBot_Astra_Build_Handover.md` that caused the outcome.

| Prompt text | Effect |
|---|---|
| "Create an **original**, low, robust 2WD sumo chassis…" | Licence to discard the sombrero. "Low" and "robust" are the only shape words in the whole prompt |
| Priorities list: 1 rules, 2 measured hardware, 3 function, 4 manufacturability, **5 "Proposed dimensions and styling inherited from earlier versions"** | You told it shape is the *least* important thing |
| "Do not simply reproduce v9's contradictory numerical specification" / MB is "internally inconsistent, not a buildable contract" / HO "explicitly permits design changes" / postmortem "its own recommendations also require checking" | Every attached source was pre-discredited. A model told its inputs are unreliable stops using them |
| "Resolve reversible geometry choices explicitly and continue… Do not ask permission for routine reversible design choices already authorized by this prompt" | Every layout decision became "reversible" and therefore Astra's to make |
| "Recommended first trial is the already-mentioned 240 mm footprint… re-solve component fit" | It did — as an octagon, because no shape was specified and 240 mm was framed as a *fit* problem |
| "A removable motor/well upper carrier is worth evaluating" | Became: everything above the deck is a separate part |
| "Use replaceable fan and sensor adapters to keep unmeasured parts from forcing reprints of the large base" | Became: 21 adapters |
| "Den reports that the v5.3 housing and v5 cover printed reasonably well… Preserve their useful physical fit and **manufacturing lessons**" / "`sumo_v5.3_housing.stl`, `sumo_v5_cover.3mf`: physical-print references **preferred by Den**" | The strongest shape signal in the whole prompt, and it's framed as a *printability* reference, not a silhouette to match. The v9 docs record *only* v5's failures. **Nowhere is "match the v5 silhouette" written** |
| "Do not ask permission for routine reversible design choices already authorized by this prompt" — vs the v9 handover §0: "If something in here is ambiguous, contradictory, or missing — **ask me. Do not guess.** I would much rather answer five questions than print another wrong part" | Fourth authority conflict, and the one that killed the visual check-in. Astra obeyed the newer instruction |
| §8 verification gates: 14 bullets, PASS/FAIL/NOT VERIFIED each | This is what it built the deliverable around |
| Doc-authority conflict: MB §3 "FROZEN ARCHITECTURE — do not re-open any of these" vs HO §0 "everything in §5 is context, not instruction… design what is right" vs this prompt "submission of this build prompt authorizes the functional approach above" | Three levels of authority, mutually contradictory. Astra picked the newest (this prompt) and the most permissive (HO) |

The v5 version worked because the v5 prompt (`SumoBot_v5_Prompts.md`) was the opposite kind of document: a positive geometry spec (rim Z, ramp angle, register OD, saddle position, every pocket with coordinates) with no "be original" and no discrediting of its own inputs. v6–v9 got worse each time because each brief grew by appending failure registers and contradictions instead of restating the geometry (the postmortem's own diagnosis: "the design had no representation other than English prose").

---

## 4. How to prompt Astra next time

### 4.1 Structure of the brief (order matters)

1. **THE PICTURE** — first, before any number. Five sentences plus a reference. Example:
   > This is a 250×250 sombrero. A continuous 360° ramp at 15° rises from a hard rim 0.5 mm off the floor to a flat roof at Z 10.9. Inside that, a superellipse tower leans in 5–10° to a flat top at Z 65.6 with a 6 mm anti-climb lip at Z 53. Two wheels on one collinear axle at mid-length, tucked in sealed wells inside the footprint. Battery low at the rear, fan straight through, electronics flat on the roof. Match the attached v5 renders/STL for silhouette; match nothing else from v5.
   Attach `views/01_assembly.png` from v10 labelled **"NOT THIS"** and a v5 render labelled **"THIS SILHOUETTE"**. Models follow pictures better than paragraphs.
2. **FROZEN** — a short list of things that may not change: footprint and profile, wheel position and collinear axle, Z levels (0.5 / 1.5 / 10.9 / 20.9 / 53 / 65.6), lid/base split at the knee, part count (base + lid + 2 wellcaps + clamp ring + hub), print orientation, no supports on the part, rules.
3. **PLACED** — per component: position, reason, what tolerance it has (§7 below). Numbers with "±" or "anywhere inside X" where you don't care.
4. **SOLVE** — the things Astra *is* allowed to invent: rib layout, boss positions, pocket details, gussets, fillets, exact groove path.
5. **ASK ME** — things it must stop and ask about, listed by name (motor length if measured > N, PCD 60/62, ToF count).
6. **CHECKS** — the gate list, kept, but *after* the geometry, and with one new gate at the top: "Render 6 views and 4 sections; **stop and show Den before exporting STLs**."
7. **DELIVERABLES** — capped. "5 printed parts. No coupons unless I ask. No alternatives. One STL per part."

### 4.2 Rules for writing it

| Rule | Why |
|---|---|
| **Delete "original", "clean slate", "design what is right", "may vanish", "worth evaluating"** | Each one is a licence. Astra took every one |
| **One document. One authority.** Don't attach four docs with a paragraph saying which parts of each are wrong | A discredited input gets discarded wholesale. Merge first (this doc is the start) |
| **Rank layout second, straight after rules.** Manufacturability and verification come *after* the shape | Priority order is read literally |
| **Positive statements, not prohibitions.** "Wheels at (0, ±55), one axle" beats "do not stagger unless…" | Prohibitions constrain one thing; the model invents around them. Positives fix the thing |
| **Give reasons with numbers** ("rim 0.5 mm because a blade must not get under") | With the reason, the model preserves the *intent* when it has to move something; without it, it keeps the number in the wrong place or drops it (the stagger is the proof) |
| **Never hand over a number you don't want kept.** The stagger, the 69 mm motor, the six ToFs all came from your docs | Every number in the brief is treated as a requirement |
| **Two shots, not one.** Shot 1 = 2D occupancy map + 4 views + `interfaces.json`, then you say yes. Shot 2 = solids | Every version v6–v10 failed at layout, not at CAD. Approve the layout while it's cheap |
| **Cap the part count and the report length** | Otherwise "replaceable adapter" becomes the design pattern and the report becomes the product |
| **Say what "done" looks like in a picture** — "Done when Den has seen 6 renders and 4 sections and said yes" (postmortem §17.7) | Astra had no visual acceptance gate, so it never asked |
| Keep the process rules you already had that worked: provenance tags, coupons-first for holes, PASS/FAIL gates, `interfaces.json` | They're the good part of v10 |

### 4.3 Split agents or one prompt?

**Split by phase, not by part or subsystem.**

- **Don't** split "sensors agent / fan agent / battery agent" — they compete for the same 250×250×66 volume, and the postmortem's overlap register (v7: 38 overlapping pairs) is exactly what happens when nobody owns the whole plan view.
- **Don't** split "base agent / lid agent" *cold* — postmortem C3: "base and lid were designed by two independent sessions with no shared interface document", and §1.1: "there is no base/lid pair that has ever been built against the same interface contract." That's the v7-lid-on-v8-base failure.
- **Do** run it as a pipeline:
  1. **Layout agent** (or you + me): produces the 2D occupancy map, the Z-stack, and a frozen `interfaces.json` (knee inset, collar radii, pilot coordinates, well rectangles, duct centre/PCD, Z levels). Renders 4 views. **You approve.**
  2. **Base agent** and **lid agent** in parallel, each given the *same* frozen `interfaces.json` and told "you may not change a number in this file — if you need to, stop and say which one". This is how the v8 prompts already worked, and Astra's `build.py` already reads `interfaces.json`, so the mechanism exists.
  3. **Independent checker agent** that never saw the briefs: imports both STEPs, runs overlap/flood/overhang/section cuts, renders 6 views. Postmortem C8: "the author was both writer and checker."
- A single one-shot with perfect restrictions would *probably* work for the base alone now, but the layout approval step is worth more than any amount of restriction text, because it catches "that's not the shape" at the 5-minute mark instead of after 53 STLs.

---

## 5. Parts register (what we actually have)

Provenance: **M** measured/weighed · **S** seller · **N** nominal/datasheet · **D** derived · **U** unknown.

| Part | Own / fit | Dimensions (mm) | Mass (g) | Mounting / leads |
|---|---|---|---|---|
| **Motor, new** — BRINGSMART JGA25-371, 12 V, ~130 rpm, Hall encoder | 2 / 2 | Gearbox Ø25.0 S, can Ø24.4 S, body **61–69 S** (design 65), shaft Ø4 × 12 D-flat 3.5 × 8 S, boss Ø7 S | ~95 ea S, **never weighed** | 2 × M3 tapped, **17.00 c-c** (confirmed on old pair); encoder 6-pin 2.54, cable 200 |
| **Motor, old** (bench / first-drive) | 2 / 0 | Body 39.29 M, gearbox 21.00 M, can Ø17.53 M, boss Ø7.05 × 2.36 M, shaft Ø4.10 M / 3.46 flat, 8.0 flat length | ☐ | M3 at 16.9 → 17.00; Phillips screw heads Ø3.4, **height ☐** |
| **Wheel** — PETG hub v3 + cast Mold Star 15 tyre | 2 / 2 | **OD with tyre 46.80 M**, rim OD 38.10 M, hub width 29.0 (1+27+1), bore CAD 4.41 / flat 3.77 (target printed 4.20 / 3.56), counterbore Ø9 × 2.5-or-3.0 | ~37 ea est | Radial M3 grub onto the D-flat. **Current printed bore 3.77 is too tight for a 4.10 shaft** |
| **Tyre ring** | 2 / 2 | Cast 30 wide, ID 33 / OD 43, stretched onto 38.1 bed; **trim to 27.0** | incl. | Stretch fit; fitted axial width **☐** |
| **Battery** — Ovonic AIR 3S 2200 mAh 120C XT60 | 2 / 1 | **106.29 × 34.39 × 21.46 M** | **151.2 M** | XT60 lead ~132 M; balance JST-XH ~75 M. Bay **110 × 38 × 24** (puff allowance), strap not clamp |
| **ESC** — LittleBee Spring 30 A BLHeli_S | 2 / 1 | Board 35.1 × 18.16 M; **with heatshrink 41.82 × 18.16 × 5.55 M** | 9 or 25 est, **never weighed** | No holes — strap/pocket. Power leads **~80 M → ~60 usable**. BEC red cut |
| **EDF** — XFly 1413 40 mm, 12-blade, ~KV5000 | 1 or 2 ordered / 1 | Housing Ø43 S, rotor Ø40 S, lip ~Ø47 S/U, duct section 28 S, overall **49 S** | ~40 S | Two ears, **all ear dims ☐**. Leads 270, 3.5 mm bullets. **Not arrived** |
| **EDF clamp ring** (print, PETG) | make 1 | OD Ø70, ID Ø44.5, 3.0 thick | ~10 | 4 × Ø3.4 on **PCD Ø60 or Ø62 (conflict)** at 45°; gasket 1 mm silicone ID 44 / OD 52 |
| **DRV8871** | 4 / 2 | **25.17 × 21.63 × 9.6 M** → box 26 × 22.5 × 10.5 | ☐ | Hole Ø/c-c ☐, terminal orientation ☐ |
| **MP1584EN buck** | 4 / 1 | **13.86 × 9.95 × 7.84 M** → box 15 × 11 × 8.5 | ☐ | Set 5.00 V before connecting anything |
| **PCF8574 HW-171** | 4 / 1 (+1 optional in lid) | **54.64 × 15.62 × 11.29 M** → box 56 × 16.6 × 12 | ☐ | Tallest module. 6 XSHUT + LED + button = all 8 pins |
| **TTGO T-Display** | 1 claimed, **never physically confirmed** / 1 | 51.5 × 25.5 S, thickness ☐ | ☐ | 2 × 12-pin headers, USB-C on a short end. Display up |
| **VL53L0X ToF** | **5 (should be 8 — recount)** / 3–6 | PCB **24.78 × 10.32 × 3.18 M**, holes Ø2.94 M at **19.79 c-c M** | ~1 | Pocket 26 × 12 × 4; pilots Ø2.10 for M2.5 self-tappers. FoV 25° N |
| **TCRT5000 + LM393 module** | 5 / 4 | Module ~31 × 14 × 10 S; **bare sensor 10.2 × 5.8 × 7.0 N — unmeasured** | ☐ | Bare sensor desoldered, flown on 4 wires ~40 mm to the LM393 board inboard. 3V3 only |
| **XT60 panel socket + loop key** | 5 pairs / 1 | Body **15.56 × 8.13 M**, ridge 9.15 M, height 20.31 M; key 16.47 × 9.23 × 10.6 M | 7.7 / pair | Cut-out **15.9 × 8.4** (body, not ridge). 21 mm behind, ~11 mm outside. Recess it |
| **LiPo alarm** | 1 / 1 | **33.22 × 25.72 × 12.21 M**, 38.67 with pins M, buzzer domes 12.2 c-c | ☐ | No holes. Pocket 34 × 27 × 13 lying flat, vents over both domes, display + button reachable, ≤ 75 mm from the pack |
| **Start button, snap-fit** | 1 / 1 | Body Ø18.51 M, widest 19.28 M, height 29.33 M; **panel grip thickness ☐ BLOCKING** | ☐ | Hole Ø18.70 D. Needs ~25–27 mm clear column below. Signal only |
| **Protoboard** | 1 / 1 cut | **160 × 63.8 × 2.74 M** | ☐ | Score and snap |
| **1000 µF 25 V caps** | ~10 / 1 + 2×220 µF | Can **Ø10.38 × 16.99 M**, ~18 standing; **lead pitch ☐** | ☐ | Bulk cap < 20 mm from ESC input |
| **M3 heat-set inserts** | kit / ~25 | **Slot 2 only: 4.96 long × Ø4.48 M**; pilot Ø4.15 × 6.0, boss Ø8.5 | ~30 with screws | Vertical into a boss with a flat land only. Never radial into a thin wall |
| **Silicone skirt sheet** | 1 / 1 | 250 × 250 × 1.0 S (thickness unverified) | ~20 | Strips, glued (acetoxy). Groove 1.3 wide |
| **Scraper feeler blade** | set / 1 | **0.30 × 100 × 12.7 S** | ~3 | Can't make a 175 mm blade from it |
| **Brass 4 mm couplers** | 3 / 0 | ☐ | ☐ | Fallback only |
| **EPDM foam tape** | — | 3 mm, compresses to 1.5 | ~2 | Wellcap seat |
| **Ballast** | — | 20c = 11.3 g, 50c = 15.55 g | ~23 g headroom | Stick-on at weigh-in |
| Retired — do not reserve | | CO₂ flipper, LEGO balloon tyres, MX1508, LM7805, 850 mAh pack, latching switch, lidar, XT30 | | |

Printed chassis so far: v5 pair **267 g weighed** (housing 153 + cover 113); v8 base **154 g weighed**. Printed mass ≈ 0.82 × (volume × 1.24).

---

## 6. Things we're unsure of (measure or decide before the next prompt)

Ranked by how much geometry each one moves.

| # | Unknown | Competing values | What it moves |
|---|---|---|---|
| 1 | **New motor body length** | 61 / 65 / 69 S; old pair 39.29 M | **Whether the stagger exists at all.** Also cheek length, duct position |
| 2 | **New motor mass** ×2 | ~95 ea S | 190 g of a 967 g budget on a guess, against 23 g headroom |
| 3 | **Fitted tyre width** | 30 assumed / 27 trimmed / 28.98 rim bed | `well_y`, wellcap, check D5 |
| 4 | **EDF lip-seat plane** | bore bottom (fan top ~Z 50) vs collar top (fan top Z 62) | **Robot height**; lid Z 65.6 was derived from the second |
| 5 | **EDF clamp PCD** | Ø60 vs Ø62 | The one number ring and base must share |
| 6 | **EDF ears** (width, thickness, hole, position) | all ☐ — not arrived | Clamp ring relief arches |
| 7 | **Is the EDF brushless?** | listing says "rotate the knob" | 800 Pa vs ~30 Pa. Whole suction concept |
| 8 | **Button panel grip thickness** | ☐ (placeholder 2.0) | Button mount — no hole tuning fixes a wrong thickness |
| 9 | **Bare TCRT5000 body** | 10.2 × 5.8 × 7.0 N | Corner pocket has 0.10 mm margin at 7.0 |
| 10 | **`hole_shrink`** | 0.21 D (from 4.00 − 3.79) — nobody opened the hub CAD to confirm 4.00 | Every hole on the bot. Astra used **0.0** |
| 11 | **ToF count** | 5 on hand / 8 expected / 3, 5 or 6 designed | Lid slots, PCF8574 pins |
| 12 | **TTGO exists?** | flagged since 2 Sep, never ticked | Board B, window |
| 13 | **PCF8574 count** | 1 needed / 4 owned | 3,720 mm² vs a 3,410 mm² board reserve |
| 14 | **Hub counterbore depth** | 2.5 vs 3.0 | Must clear the Ø7.05 × 2.36 boss |
| 15 | **Battery bay** | 36 × 108.5 (v8 tub) vs 110 × 38 × 24 (puff policy) | Tub is 2.0 short in X, 1.5 in Y |
| 16 | **ESC mass** | 9 vs 25 | 16 g of headroom |
| 17 | **Phillips head height** (old motors) / **1000 µF lead pitch** | ☐ / ☐ (expect 5.0) | Faceplate relief pocket / PCB footprint |
| 18 | **250.00 mm rim** | 250.00 exact vs a checked limit vs older "243 max" | Zero margin. Fallback 125 → 120 re-derives every inset |
| 19 | **Seal loop inset** | 18 vs 20 | ~1,500 mm² ≈ 1.2 N |
| 20 | **Does 267 g include the PETG parts?** | ☐ | 45 g swing in ballast headroom |

Caliper/scale session covering 1, 2, 3, 8, 9, 10, 17 is under an hour and unblocks most of this.

---

## 7. Placement — where each part goes, why, and what's negotiable

This is the section Astra never had. Every row: **where** (as your docs specify it), **why**, and **FROZEN / FREE / ASK** so the agent knows what it may touch. Coordinates are the v9 numbers; where v9 was internally inconsistent I've said so instead of picking.

### 7.1 Hull

| Item | Where | Why | Status |
|---|---|---|---|
| **Footprint** | Superellipse `\|x/125\|⁴ + \|y/125\|⁴ = 1` → 250 × 250, r 125 on axes, 148.65 on diagonals | Fills the legal box: ~57,900 mm² vs 49,087 for a Ø250 circle. Downforce = ΔP × A, area is free. Diagonals give depth for corner sensors | FROZEN as shape. **ASK**: 250.00 vs 240 (bed margin + rule margin). If 240, it's `125 → 120`, everything re-derives, still a superellipse — **not an octagon** |
| **Rim** | Hard PLA lip 1.2 thick, underside **Z 0.50**, continuous 360°, top edge Z 1.70 | "The single most important defensive feature." 0.3 as-built scraped; 0.5 = light contact under suction by decision. A blade can't get under 0.5 mm. v5 had no rim for 164° and that was the failure | FROZEN |
| **Wedge** | Straight ramp **15.13°** along the local normal, run 34, rise 9.2, rim Z 1.70 → knee Z 10.90, identical at every bearing. 1.2 skin over 8 radial ribs 2.0 wide, R1.5 fillets | Continuous so there's no sector to get under; sides are climb ramps by intent (opponent rides up, we yaw them off). 8 × 2.0 ribs because 12 × 1.2 snapped on support removal | FROZEN angle/levels. FREE: rib positions (must skip the tub, wells, duct boss, board zones by ≥ 3). ASK: single vs two-slope profile |
| **Knee / lid-base split** | RIM INSET 34.0 at Z 10.90. Base collar outer inset 34 / inner 36, Z 10.9–16.9. Lid skirt inside it, outer 36.4 / inner 38.4, **0.40 radial clearance** | Plan-view boundary: outboard = base, its underside is atmosphere; inboard = bay, at ambient. 0.4 because "a Ø172 PLA ring will not stay round" at 0.2 | FROZEN |
| **Plenum** | Pan underside Z 1.50, cavity Z 1.50–9.70 (8.2 deep), roof plate 9.70–10.90 | Base is the pressure vessel; everything above Z 10.9 is ambient. Nothing rigid below Z 1.50 except the rim lip within 12 mm of the rim | FROZEN levels. ASK: 8.2 vs 9–10 deep (fan brief) — trades directly against axle height which has **zero** margin |
| **Main seal loop** | One closed 3.0 wall, outer inset 20.0 / inner 23.0, Z 1.50 up to the wedge skin, "a plain smooth offset — no detours, no corners, no boxes" | Every detour costs area and adds leak path | FROZEN. ASK: inset 18 vs 20 |
| **Skirt** | 1 mm silicone strips **6 tall**, in a 1.3 × 2.0 groove opening downward (Z 1.50 → 3.50), 45° mouth chamfers, continuous through corners, glued. Bottom edge Z −0.5 at rest. Three loops: main + one per wheel well | Vertical curtain follows any plan curve with ~12 butt joints. Glue only — the 16 M2 pilots were deleted at v5. "A stiff skirt is a load path — don't stiffen it." Rim is armour, skirt is seal, different parts, ~20 mm apart | FROZEN. **Fix the arithmetic first**: 6 tall with 2 in a 2-deep groove = 4 proud, not 2. Choose strip height 4.5 (2 in, 2.5 proud) or accept 4 proud |
| **Ribs** | 8 radial, Z 5.5 to the ceiling, r 30 out to the main loop | See wedge | FREE within the skip rules |
| **Knock-outs / bleed** | 2 × Ø12, 0.6 membranes, sealed by default. v9 says **(52, ±35)**; postmortem failure 41 says move to **±36** because at ±35 the Ø12 is exactly tangent to the Ø58 boss | Tuneable bleed you told the coordinator about; the EDF's only thermal path | FROZEN existence; use ±36 (or duct_x, ±36 if the duct moves) |
| **Print** | Base upside-down, roof face on bed, PLA 0.2, 4–6 walls, 15–20 % gyroid. Support only in the wedge annulus (bed-anchored) + groove mouths. **One piece, never split.** Bambu X1C, 256 bed, 0.4 nozzle, `hole_shrink` +0.21 on every hole | You snapped rib legs peeling support. The base is the pressure vessel | FROZEN |

### 7.2 Drive

| Item | Where | Why | Status |
|---|---|---|---|
| **Wheels** | v9 as written: centres **(+14, +55)** and **(−14, −55)**, track 110. Intent (per the v9 handover): **X = 0 both, collinear**. **Axle Z 23.40 = 46.8/2**, wheel top Z 46.8 | `axle_z = wheel_od/2` is an identity — assert it. Mid-length so the CG lands near the axle and the bot pivots about its centre | FROZEN Z and collinear intent. **ASK**: track 110 (wheels inside the footprint in wells) vs wider (Astra used ±92 outboard) — a real decision, see the Stagger row |
| **Motors** | Axis along Y at Z 23.40, resting **directly on the roof (no floor under it)**, in two side cheeks Ø25.3+shrink, Z 10.9–33, open at the top, faceplate = the well's inner wall at \|Y\| 38 (1.2 thick), Ø8 shaft hole, 2 × Ø3.2 at 17.0 c-c | Roof 10.9 + motor radius 12.5 = 23.40 exactly — a 1.2 floor would lift the wheels off the ground (v5 did exactly that, +2.45). Drop in from above; nothing printed over the saddle | FROZEN Z chain. Cheeks must tolerate `motor_len` 39–69 |
| **Stagger** | v9: ±14 in X, point-symmetric. **Intent: none.** "Exists only because the motors are assumed 65 long… an asymmetry we don't want" | Two 65 mm motors on one axle at track 110 overlap ~10 mm at the centre | **ASK — resolve before the prompt.** Options: (a) measure the motors; if ≤ 55 the stagger dies; (b) widen the track to ≥ 2×(motor_len + faceplate + margin) and go collinear; (c) keep ±14 and accept the scrub. Do **not** hand Astra `motor_x_offset = 14` again without one of these |
| **Wheel wells** | Interior `well_x = wheel_od + 6 = 52.8` (X), `well_y = tyre_w + 4 = 34.0` (Y); +Y well X −12.4…40.4, Y 38…72 (with stagger); own closed 3.0 seal wall +4.2 all round down to Z 1.5, own skirt groove, **outside the plenum**, open to the arena below, walls 1.2 to Z 39 | Wells inside the loop = 3,599 mm² of leak = zero downforce. Diameter lies in X, width in Y (the axis trap that killed v7) | FROZEN principle. Numbers follow the wheel decision |
| **Wellcaps** | Open-bottom box over each well, ceiling Z 48.0, top 49.2, laps outside the walls, inward 3.0 ledge on 3 mm EPDM, 4 × M3 into wall-top pads. **No outward flange.** Light items only on top | Caps the well from the bay side; wheel needs 1.2 mm over Z 46.8 | FROZEN. Note postmortem failure 38: the Ø8.5 bosses can't sit on a 1.2 wall — use a local pad that *is* the boss |
| **Hub** | PETG, coin orientation, 0.16 layers, D-bore onto the shaft flat, radial M3 grub | Standing orientation splits on impact. Bore must be reprinted — 3.77 vs a 4.10 shaft | FROZEN. Bore coupon first |

### 7.3 Downforce

| Item | Where | Why | Status |
|---|---|---|---|
| **EDF duct** | Vertical, straight through pan and roof, intake **down**, exhaust **up** through the lid grille. v9 position **(52, 0)**. Bore Ø43.3+shrink, **R5 bellmouth mandatory** in a Ø58 boss to Z 4.5, Ø47.4 × 3.0 lip seat, Ø58 collar to Z 14, 4 pilots on PCD 60/62 in Ø8.5 bosses Z 1.5–14 | "Stationary gas ⇒ uniform pressure; every bend is a loss." Sharp entry stalls the rotor (10–20 %). Off-centre **only** because the staggered motors occupy the middle — "an asymmetry we accepted rather than chose." Pressure centroid does not move with the fan | FROZEN: vertical, straight-through, bellmouth. **ASK**: X position — if the stagger dies, **put it at (0,0)**. Lip seat plane (U4) and PCD (U5) must be decided first |
| **EDF body** | Top Z 62.0 (if collar-top seat); clear Ø72 for the clamp, Ø50 above; **do not fully enclose** | Air-cooled; dead-sealed plenum cooks it in 2–3 min | Follows U4 |
| **Clamp ring** | Separate PETG, on the 4 duct pilots, gasket under the lip | Fan loads from above | FREE detail |
| **Grille** | Ø48 in the flat top over the duct, ≥ 65 % open, 3 mm bars, inner ≥ Z 64 | Exhaust straight up | Follows duct X |
| **Fan-off case** | Chassis must be printable and competitive with EDF, ESC and duct deleted; a duct plug | Mid-Sep kill gate | FROZEN |

### 7.4 Power

| Item | Where | Why | Status |
|---|---|---|---|
| **Battery** | **Rear (−X), low, long axis along Y.** Sunk tub: interior ≥ 110 (Y) × 38 (X) × 24, inner floor Z 3.90, outer floor Z 2.70, walls **only to Z 13**, rear corners chamfered 2 × 2. v9 outer X −85…−46.6 | "As bottom-heavy as practical" (you, 11 Sep). Rear balances the fan/ESC forward. Sunk costs no downforce (tub underside is still plenum ceiling). Walls to 13 so the pack lifts clear — v6's Z 20 walls trapped it. Chamfers keep the tub inside the lid skirt | FROZEN rear/low/along-Y. FREE exact X within the tub rules. Note: **Astra's straight rear slide-out at deck level (no lift) is the better extraction solution — keep that idea** even in a sunk tub: sill ≤ tub floor + pack height |
| **Battery retention** | Strap through two 12 × 3 slots in the long walls at Z 7.5–10.5, **not the floor**; 20 × 6 finger relief at Y 0 | LiPos swell — strap, never pinch. Floor slots leak | FROZEN |
| **Battery access** | Open slit in the rear tower, centred −X, ≥ 112 wide × ≥ 24 tall, **no hatch, no latch** | "You just need a small rectangle slit the battery can slide out" (you). Costs zero downforce — the bay is ambient | FROZEN intent. **ASK sill Z**: v9's Z 22 needs an 18 mm lift (DEC-13, unsolved); postmortem option 1 = frame the aperture through the skirt with a 3 mm boxed frame and keep the sill at the tub floor |
| **ESC** | On Board A (power board), zip-tied, motor-pad end toward the EDF, **≤ 60 mm** wire run to the bus. No printed saddle. Not fully enclosed | 80 mm leads. Heat. The v6 saddle collided with a bleed hole and a post | FROZEN "on Board A within 60 mm"; FREE exact spot |
| **XT60 loop key** | **No v7/v8/v9 position — you must give one.** v6 had it in the rear tower, cut-out 15.9 × 8.4 at Y −20, Z 47, recessed 2 mm. Needs 21 mm behind the wall, 11 mm outside | Only real power disconnect. Recessed so 11 mm of key isn't a lever arm | **ASK** — pick a place. Astra put it in the flat top at (64, 49) in a recessed cup; that's a legitimate answer if you like it |
| **LiPo alarm** | Pocket 34 × 27 × 13 hanging from the flat-top underside at v9 (−20, −45), lying flat, display up; 30 × 20 window, 2 × Ø4 vents at 12.2 c-c over the domes, Ø8 finger hole; friction pocket + strap | Must be within 75 mm of the pack (balance lead). Vents or it's inaudible. On the flat top because the tower had no flat seat and the "no hole below Z 38" rule | FROZEN flat-top + within 75 mm of the pack; FREE exact XY |
| **Start button** | Flat top, v9 (10, 40), Ø18.7+shrink through a Ø26 pad whose total thickness = `btn_panel_t`; Ø20 keep-out column Z 33–64 below it. Signal only | Operator reaches it, a rival can't. Snap clips only grip a panel inside their range — measure it. A counterbore into a 1.6 skin is impossible | FROZEN flat-top; **FREE XY but must not sit over a wellcap** (v9's (10, 40) does — D8 in the v9 review) |
| **Bulk caps** | On Board A, < 20 mm leads to the ESC input, ~18 standing | Ripple | FROZEN adjacency |

### 7.5 Electronics

| Item | Where | Why | Status |
|---|---|---|---|
| **Boards** | **Flat on the roof (Z 10.9)** on 6 mm M3 nylon standoffs, flush pilots, no printed standoffs. v9: Board A (power + ESC) X 20…77, Y −76…−36; Board B (logic + TTGO) X 46.6…78, Y 32…68. Stack ≤ Z 31, lid inner ≥ 34 | "Getting the PCB off the Z 40 posts was the single biggest CG win (−1.84 mm)… 65 g on posts at Z 40 cost more CG than the 151 g battery." "Nothing stands proud of the roof except the well walls" | FROZEN: flat on the roof, not on a tray. **ASK**: Board B is 31 × 36 and the TTGO is 51.5 × 25.5 — it doesn't fit. Either one bigger board zone or tell Astra the area available and let it cut the protoboard to it |
| **TTGO** | Flat, display **up**, on Board B, 34 × 22 window in the flat top (v9 (62, 50)), acetate cover. No USB port in the shell — program lid-off or OTA. No tilted pocket | v7's tilted pocket + tower window overlapped by 7 mm | FROZEN orientation; FREE XY with the board |
| **DRV8871 ×2, buck ×1, PCF8574 ×1** | On the board zones; no coordinates in any doc | — | FREE. Tell Astra: "pack them; report the board area you need" |
| **Comparator boards ×4** | "Inboard on the roof", ~40 mm of flown wire from each corner sensor | Module doesn't fit the corner band (needs 16.4 mm radially, 11 available) | FREE within 40 mm of its sensor |
| **Lid harness** | ONE 4-way JST-XH through a Ø10 gland in the flat top (v9 (−20, 20)) to a second PCF8574 inside the lid driving ToF XSHUT + LED + button | "Four wires, one plug, lid off in one action." The only base↔lid penetration | FROZEN concept; FREE gland XY |

### 7.6 Sensors

| Item | Where | Why | Status |
|---|---|---|---|
| **ToF** | In the **lid tower wall**, flush pockets 12 (H) × 26 (V) × 4 deep, board long-axis **vertical**, pilots 19.79 c-c vertical, slot 14 × 8, centres Z 48 (rear Z 51). Yaws v9 `[0, ±25, ±90, 180]` | Vertical because a 26 mm pocket falls 3.7 mm across a curved leaning wall; a 12 mm one only 0.95. ±25 not ±30 because FoV is 25° (±30 leaves a 5° blind seam). Rear raised to clear the battery slit | FROZEN: in the wall, flush, vertical, front trio at 0/±25. **ASK count**: 3 / 5 / 6 (you own 5). Do **not** let it bolt carriers on the outside |
| **Line sensors ×4** | **Bare TCRT5000** on each 45° diagonal, in a downward-open pocket under the wedge, optical face **Z 2.20**, long axis tangential, IR-opaque walls. v9: corner pods at r 120.15 (wedge surface +2.5 uniform). Postmortem: **delete the pods**, mount at RIM INSET 24.03 where 7 mm exists under the wedge | Corners are deepest; four diagonals give edge detection in any heading. The whole module needs 16.4 mm radially, the band has 11 — desoldering is the only thing that fits. Pods cost 8 failures over two generations | FROZEN: bare, corners, face Z 2.2, wire hole **inboard of the knee** (a pod-ceiling hole faces atmosphere — v7's mistake). **ASK**: pods vs under-brim pocket (recommend no pods) |

### 7.7 Lid

| Item | Where | Why | Status |
|---|---|---|---|
| **Skirt ring** | Vertical prismatic extrusion of the RIM INSET curve, outer 36.4 / inner 38.4, Z 10.9–20.9, no taper | Registers inside the base collar | FROZEN |
| **Tower** | Superellipse section leaning inward **from Z 20.90 as the datum**, lean 5° (v9) or 10° (postmortem rec.) | Measuring the lean from Z 10.9 made a 1.763 mm up-facing 90° ledge — "the single highest-value line in the postmortem." A superellipse can't rotate on the base | FROZEN datum. **ASK lean**: 10° gives room for a 6 mm lip at Z 53; 5° leaves 0.4 mm |
| **Anti-climb lip** | 6.0 proud, widest at **Z 53**, flat horizontal underside, ~45° upper face back to Z 59; interrupted only at ToF slots; widest point still inboard of the base collar | The real loss mode is being wedged and lifted; a square catch edge stops it | FROZEN. Depends on lean |
| **Flat top** | **Z 65.60**, 1.6 skin → inner Z 64 = grille requirement | Printed flat-top-down; a dome needs support, a skirt-down flat top is a 160 mm bridge | FROZEN (moves with U4) |
| **No radial holes below Z 38** except the battery slit | Structural band on the tower | FROZEN |
| **Flat-top furniture** (all of these in the flat top, zero overlaps, each named): EDF grille Ø48 over the duct · TTGO window 34 × 22 · alarm window + vents + finger hole · button pad Ø26 · **opponent LED Ø5.2** · **group-number recess 60 × 25 × 0.6** · harness gland Ø10 | LED and group number are **rules** (R6, R7) — nearly deleted twice; move them, never delete | FROZEN existence; FREE XY subject to no-overlap |
| **Fixings** | 4 × M3 vertical from above at (±74, ±74) into Ø8.5 bosses hanging below the roof; lid lug 16 × 16 × 3 with a Ø7 × 1.5 counterbore | The (0, ±82) pair's pads reached into the wells — one mistake, seven symptoms | FROZEN four |
| **Hard rule** | **No lid surface ever radially proud of the base.** No wedge, claw, horns, ears, guards on the lid. "If you find yourself modelling anything on the lid reaching toward the rim, stop and say so" | A blade sliding up the wedge must never meet an outward step | FROZEN |
| **Print** | Upside-down, flat top on the bed, PLA 0.2, 4 walls, 15 %, **no supports anywhere**, ≤ 55° overhang, report the worst location by name | | FROZEN |

### 7.8 Ground furniture

| Item | Where | Why | Status |
|---|---|---|---|
| **Scraper blade** | No coordinate in any doc. v5: 105 × 14 × 2 slot along the front rim, blade 0.5 proud, PETG leaf 0.8 × 8 with a 3 mm stop | Fan-off fallback is "ballast + tyres + sprung scraper lip" | **ASK**: do you want it at all? If yes, front rim only, 100 mm wide, compliant, tip at the rim line |
| **Pitch support** | Nothing in your docs beyond "the rim lip at Z 0.50 is the scraper line — it will touch under load, accepted" | 2WD needs a third contact; the rim is it | ASK: do you want Astra's adjustable skids? If yes, **one per side, symmetric** |
| **Ballast** | Stick-on at weigh-in (v9) vs restore two 24 × 40 × 12 pockets at the point-symmetric low spots (postmortem LOST-4) | 23 g headroom, no place to put it | ASK |

---

## 8. Decisions only you can make before the next prompt

In the order they unblock geometry:

1. **Motors: measure length and weight.** Then: stagger yes/no, track 110 vs wider, fan at (0,0) vs (52,0).
2. **Footprint: 250.00 or 240 (`125 → 120`).** Superellipse either way.
3. **EDF seat plane (fan top Z 50 vs 62) and PCD (60 vs 62).** Sets the lid height.
4. **ToF count (3/5/6) and line-sensor mount (pods vs under-brim pocket).**
5. **Battery slit sill height** (the DEC-13 fix — recommend the skirt-frame option or Astra's deck-level slide).
6. **Tower lean 5° vs 10°.**
7. **XT60 location.** (Astra's recessed flat-top cup is a fair answer.)
8. **Scraper / skids / ballast pockets: in or out.**
9. **Board area:** tell Astra the zones and let it cut the protoboard, or fix the TTGO-doesn't-fit-Board-B problem first.

Once these are answered, §7 becomes the PLACED section of the new brief almost verbatim, §5 becomes the register, §6 shrinks to whatever's still unmeasured, and §4.1 is the skeleton. That's the prompt.
