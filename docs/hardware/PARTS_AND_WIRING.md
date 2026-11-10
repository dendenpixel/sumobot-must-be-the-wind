# SumoBot — Parts register + wiring topology (11 Sep 2026)

Single "what do we physically have and how does it plug together" sheet for the whole group.
Dimensions are **literal caliper readings in mm** — clearance is added in CAD, never here.
Sources: `MEASURED_PARTS.md`, `HARDWARE_SPEC_SHEET.md`, `MASS_BUDGET.md`, `POWER_BUTTON_SPEC.md` (all in this folder) and `../BOM.md`.

**Updated 23 Sep 2026.** The drive-only harness is wired & ran the 23 Sep first drive. Every printed part on the bot is the latest revision (carriers v13, hub v6.2, battery frame v2 clip, wellcaps +2, v11 base & lid, clamp ring v2). The whole bot is **765 g** on a scale (23 Sep, before ToF & line sensors).

Counts: **17** in hand + calipered · **6** in hand, partly measured · **7** retired.
**Everything in the 2 Sep order arrived 11–17 Sep 2026.** A second small order (low-ESR caps, Schottky, JST-PH pair) is placed, and the fan consumables are bought.
Whole bot on a scale: **765 g** (23 Sep, before ToF & line sensors, breadboard aboard). Individual parts on a scale: **343.6 g** of a **954.2 g** predicted total (battery 151.2 + the motor pair 192.4, both measured). The printed structure is **296.4 g modelled**, not weighed, and the retired 267 g reading was the v5 chassis. Ballast headroom: **35.8 g** to the 990 g target. Line items, tags and sources are in `MASS_BUDGET.md` §1, which is the mass authority.

---

## 1. In hand and measured — build with these

| Part | Qty | Key dimensions (mm) | Mass | Notes |
|---|---|---|---|---|
| LiPo — Ovonic AIR 3S 2200 mAh 120C XT60 | 2 | 106.29 × 34.39 × 21.46 · balance lead 75 · discharge 132 | **151.2 g** | 24.42 Wh. Supplier substituted up from 1500/45C — and **XT60, not XT30**. Bay 110 × 38 × 24 for puff; strap, don't pinch. Both packs in hand, measurements from one; **one pack on the bot** |
| ESC — LittleBee Spring 30 A BLHeli_S | unconfirmed (BOM lists 1) | board 35.1 × 18.16 × 5.55 · envelope **41.82** with heatshrink | ~25 g est | No mounting holes. **Power leads only 80 mm.** Signal lead is 2-wire white/black (measured), no BEC. Don't seal it in PLA |
| Downforce fan — XFly 1413 40 mm EDF, 12-blade, KV5000, 3S | **1 — no spare** | flange OD **47.81** (worst case; 47.71 repeated) × **3.31–3.50** thick ⚠ · duct OD 42.87 · duct section 26.44 (datum unstated) · motor stack past the duct 27.5 | ☐ (~40 g est) | Measured 17 Sep. **One fan, no spare: do not bench-test it loose — verify all wiring and code first, plug it in last, one shot.** Overall height still unmeasured and it gates the seat ream. The moulded ear is on the duct wall; its position is unmeasured, so the clamp-ring slots can't be cut |
| MCU — LilyGO T-Display **S3** (non-touch) | 1 | 62.3 × 25.65 × 6.88 without pins · **14.6 over the header pins** | ☐ | In hand and measured 12 Sep. Sits on the right wellcap in v11 (on a breadboard on top of the bot as of 23 Sep). Pins per `../PIN_MAP.md` |
| Motor driver — DRV8871 | 4 | 25.17 × 21.63 × 9.6 | ☐ | 2 in use, 2 spare. ILIM resistor value unconfirmed |
| 5 V buck — MP1584EN | 4 | 13.86 × 9.95 × 7.84 | ☐ | 1 in use (Brain 5V), 1 burnt, 2 spare. Set the voltage before anything is connected |
| I/O expander — PCF8574 (HW-171) | unconfirmed (BOM lists 2) | 54.64 × 15.62 × 11.29 | ☐ | **Design needs one**, in the lid |
| ToF — VL53L0X GY-VL53L0XV2 | **8** (3 old + 5 new) | PCB 24.78 × 10.32 × 3.18 · holes Ø2.94 @ 19.79 c-c | ~1 g | M2.5 clearance holes → pilots Ø2.1. **Count settled: 8 in hand, 7 in the design, 1 spare** against a soldering or wiring kill. If more die, fall back to **front + rear only and drop the sides** |
| XT60 + loop key (Amass) | 5 pr | socket 15.56 × 8.13 × 20.31, ridge 9.15 · key 16.47 × 9.23 × 10.6 | 7.7 g/pr | Panel cut **15.9 × 8.4** — body-sized so the ridge captures it from inside |
| LiPo alarm / buzzer 1S–8S | 1 | 33.22 × 25.72 × 12.21 (38.67 incl. pins) · domes 12.2 c-c | ☐ | No fixings — friction pocket + strap. Needs vents over both domes |
| Power / start button (snap-fit, 3-pin) | 1 | Ø18.51 body (19.28 max) · 29.33 tall | ☐ | Hole Ø18.7, not Ø12. **Signal only.** Pin functions unidentified |
| Drive motors — **new pair**, BRINGSMART JGA25-371, 12 V, ~130 rpm, Hall encoder | 2 | body **58.84** (gearbox 20.86 + can 32.71 + encoder cap 5.27) · OD 24.78 · overall incl. shaft 71.23, stick-out 12.39 · boss Ø6.99/7.00 · shaft Ø**3.99** / 3.45 across the flat · faceplate tapped M3 at **17.11** c-c (minor Ø2.50) · fitted Phillips pair at 17.07 c-c on the **perpendicular** axis · encoder 6-way JST exiting **radially**, body 14.03, 8.45 proud | **96.2 g ea** incl. loom (loom 2.9 g) | Measured 17 Sep, A ≡ B. **Tapped-hole axis at 3 and 9 o'clock with the D-flat at 12.** v12 carriers **OK — no reprint** (tail gap 16.76); hub v5 **OK — no change**; ±14 stagger still required; hub bore 4.10 → **4.05** candidate on the Ø3.99 shaft |
| Drive motors — old faded pair (310-class) | 2 | body 39.29 (gearbox 21.00 + can 17.53) · boss Ø7.05 × 2.36 · shaft Ø4.10 / 3.46 flat, 10.0 long, 8.0 flat · holes 17.0 c-c tapped M3 | ☐ | **Not 371s.** Bench spares only, the 23 Sep first drive ran on the JGA25-371 pair. Same faceplate interface as the new pair |
| Wheels — printed hub + cast silicone ring | 2 | OD with tyre **46.8** · rim OD 38.1 | ☐ | Hub **v6.2** (ABS) with Mold Star 15 tyres cast in the v1 ring mould, fitted on the JGA25-371 pair & driven 23 Sep. The bore figures in `MEASURED_PARTS.md` are from the older hubs |
| Caps — 1000 µF 25 V electrolytic | ~10 | can Ø10.38 × 16.99 · legs 21.6 / 26.8 | ☐ | General-purpose, not low-ESR (low-ESR set ordered). Grey stripe = −, go by the stripe once legs are trimmed. ~18 mm standing height. Lead pitch unmeasured |
| M3 heat-set inserts (all-M3 kit) | kit | standard = 4.96 × Ø4.48 knurl · pilot Ø4.15 × 6.0, boss Ø8.5 | — | One size for the whole bot. Never lubricate |
| Protoboard (breadboard pattern, 5-hole columns per bank) | 1 | 160 × 63.8 × 2.74 | ☐ | Score and snap to size. Board B is a 51 × 30 cut from the clean end, the 7805 end is scrap |

## 2. In hand, not yet measured

| Part | Qty | Claimed (mm) | Notes |
|---|---|---|---|
| TCRT5000 + LM393 line module | 5 | module 31.3 × 14.2 · bare sensor 10.01 × 5.6 (measured 13 Sep, `HARDWARE_SPEC_SHEET.md` §2.3) | 4 used. Bare sensor desoldered and flown on 4 wires into the corner pockets |
| Silicone sheet 1 mm | 1 | 250 × 250 × 1.0 | Skirt ring ID 196 / OD 208, notched around the wells |
| Feeler gauge set (0.30 blade) | 1 set | blade 100 × 12.7 × 0.30 | Scraper lip, 0.5 mm proud on a PETG leaf |
| Brass shaft couplers, 4 mm bore | 3 | — | Fallback only; wheel v3 drives on the D-flat |
| XT30 pairs | ? | — | Plan moved to XT60 throughout, so these are spares. Count them before any crimping |
| Wiring & hardware lot | lot | — | JST-XH 2/3, JST-PH 6, Dupont, splices, M3, resistors |

## 3. Retired — do not design around

NXE 850 mAh 3S 30C (JST-RCY rated ~5 A) · MX1508/TC1508A driver (over-voltage on 3S) ·
LM7805 protoboard (2–3 W of heat doing the MP1584's job) · LEGO 32019 tyres 62.4 × 20 (replaced by 46.8 cast silicone) ·
old latching power switch (1–3 A part) · old black PLA chassis · chassis print set v6 (pan + shell, 267 g, superseded by the v11 family).

---

## 4–5. Power & signal paths

The power and signal sections that were here were the classic-ESP32 plan from 3 Sep, superseded on 17 Sep when the board turned out to be a T-Display S3. They're left out of this copy. The current block-level wiring is in [`WIRING_OVERVIEW.md`](WIRING_OVERVIEW.md) and the pins are in [`../PIN_MAP.md`](../PIN_MAP.md). §1 to §3 above (the measured parts register) are current.

---

## 6. What's actually blocking (nothing is waiting on a parcel)

1. **Measure the EDF overall height** — one bench-to-nub-tip reading. It gates whether the fan seat gets reamed at all. Its ear position is the other fan blocker: the clamp-ring slots can't be cut without it. Which end is the intake has to be settled before the fan goes in the collar.
2. **Weigh the printed set, one wheel and the ESC.** The whole bot is 765 g (23 Sep, before sensors), the motor pair is 192.4 g and the battery 151.2 g. The 954.2 g prediction for the finished bot & the 35.8 g ballast headroom are in `MASS_BUDGET.md` §1, the mass authority.
3. **Measure the 1000 µF lead pitch** (same-side trick, leg to leg). Only matters for laying out Board B now.
4. **Meter the button's 3 pins and its panel grip thickness.** An NC contact in the start path gives a bot that runs until you press it; clips that can't reach past a 3 mm wall never latch.
5. **Print the hole-shrinkage coupon.** Ø4.00 bores printed 3.77–3.81 against a 4.10 shaft. That offset applies to every hole on the bot.
6. ~~Chase the suction ruling with the coordinator.~~ **Approved 8 Sep** ([`docs/admin/DESIGN_APPROVALS.md`](../admin/DESIGN_APPROVALS.md)). ESC as a motor controller and fan pre-spool are also confirmed allowed by staff (by 23 Sep).
7. **Unconfirmed, for the hardware build:** DRV8871 ILIM resistor value, whether the drivers stay hot-glued, LiPo alarm location & trip level, panel XT60 & key gender, whether the buck input is taken from the Star.
