# Bill of materials

> **Superseded at project close (16 Oct 2026).** Frozen at 23 Sep 2026. The final bot weighed 1.000 kg at weigh-in.

Three lists: **ordered** (AliExpress, 2 Sep 2026), **on hand** (from last semester), **local**. `bom.csv` is the tabular export of this file. This file is the working truth. On-hand parts go in the BOM at $0 "Existing Stock".

**Updated 23 Sep 2026.** Everything in the 2 Sep order has arrived. A second small order (low-ESR caps, Schottky, JST-PH pair) is placed, the fan consumables in §1b are bought & the Mold Star 15 is collected. Lines tagged **[M]** carry a calipered or weighed value from `hardware/MEASURED_PARTS.md`, which is the source of truth for dimensions; everything else is still a seller figure or an estimate. Several parts arrived different from what was ordered, and those lines are corrected in place below rather than deleted.

## 1. Ordered — AliExpress, 2 Sep 2026 (~$200 total)
**Arrival: everything received 11–17 Sep 2026.** (The 2 Sep estimate was ~1 wk for the Ovonic battery, 1–2 wk for Choice items, 2–5 wk for the global sellers — it held.)

| Item | Listing ID | Qty | AUD | Notes |
|---|---|---|---|---|
| 40 mm 12-blade EDF, XFLY 1413 KV5000, 3S/4S | 1005006160350568 | **1 — no spare** | 41.39 | **[M]** Measured 17 Sep: flange OD **47.81** worst case, flange thickness **3.31–3.50** (spread 0.19, flagged), duct OD 42.87. Bare motor leads — solder to ESC. Mass still unweighed (~40 g assumed). **One fan and no spare: do not bench-test it loose** — verify all wiring and code first, plug it in last, one shot |
| LittleBee 30 A BLHeli_S ESC | 1005011869750683 | 1 | 13.91 | 2-wire white/black signal lead (measured), no BEC. Count in hand unconfirmed |
| DRV8871 motor driver module (3 pcs) | 1005009324702642 | 3 | 12.49 | 4 in hand in total: 2 in use, 2 spare. ILIM resistor value unconfirmed |
| MP1584EN 3 A buck | 32828603866 | 3 | 1.74 ea | 4 in hand in total: 1 in use (Brain 5V), 1 burnt, 2 spare. Set the voltage before connecting anything |
| PCF8574 I2C IO expander | 1893663874 | 2 | 0.52 ea | |
| TCRT5000 line sensor, 5 pack | 1005001593848689 | 1 | 2.81 | **The LM393 comparator module is not used.** v11 runs the **bare TCRT5000 block** desoldered off the module, straight into ADC1 on the S3 (390 Ω LED limiter + 10 kΩ pull-up per sensor on the base protoboard). 4 fitted in the corner pockets, 1 spare |
| Amass XT60 pairs (5) | 1005001279983590 | 1 | 5.54 | Two panel halves = Pack Socket & Key Socket, one plug bridged = loop key (which half carries pins is unconfirmed) |
| 1S–8S LiPo buzzer | 4000160682280 | 1 | 5.10 | Balance-lead alarm, the only low-voltage warning on the bot (no firmware LVC). Not fitted yet, location & trip unconfirmed |
| Cap assortment (1000 µF / 220 µF 25 V) | 1005005963545987 | 1 | 4.79 | General-purpose, not low-ESR. As built: 220 µF on each DRV8871 supply, 1000 µF bulk at the XT60 input. Fan at idle only until the low-ESR set lands |
| Silicone rubber sheet 1 mm 250 × 250 | 4000298907420 | 1 | 7.10 | Skirt |
| Feeler gauge 32 blade | 1005006995172687 | 1 | 5.49 | 0.30 blade = scraper lip |
| Ovonic AIR 3S **2200 mAh 120C, XT60**, 2-pack | 1005010640249531 | 1 (=2 packs) | 39.59 | **[M]** The supplier substituted **up**: 2200 mAh / 120C against an ordered 1500 mAh, and **XT60, not XT30** — confirmed by label, barcode and 24.42 Wh. Measured 11 Sep: **151.2 g**, **106.29 × 34.39 × 21.46 mm**; bay is 110 × 38 × 24. One fights, one charges. **Anything anywhere still saying 1500 mAh or XT30 is wrong** |
| B3 Pro 2S/3S balance charger (AU plug) | — | 1 | ~8–10 | 0.8 A → ~2 h per pack |
| M3 heat-set inserts | — | 1 pack | ~4 | Chassis is M3 only |
| 16 AWG silicone wire red/black 1 m ea | — | 1 | ~5 | XT60 bus |
| Blue threadlocker 10 mL | — | 1 | ~2 | Grub screws |

## 1b. Added since the 2 Sep order — required by the as-built design

| Item | Qty | AUD | Notes |
|---|---|---|---|
| **M3 × 8 button-head screws** | 4 + spares | ~2 | **Bought.** **Clamp ring → roof (EDF mount v2).** Usable insert engagement is ~5.7 mm, so M3 × 8 puts 2.8 mm through the ring and **5.20 mm into the insert (1.73 × D)** with 0.50 mm spare. **An M3 × 12 bottoms out about 4 mm early — it feels torqued while clamping nothing.** M3 × 6 engages only 1.07 × D. See `chassis/v11/CLAMP_RING_V2_CHANGE.md` |
| **3 mm EPDM sheet** (or 3 × 1 mm silicone stacked) | one small piece | ~5 | **Bought.** **Fan gasket.** Cut ID 43.5 / OD 47.0 and fit it **on top** of the EDF flange. Not the 1 mm silicone sheet already on hand — that is the *skirt* material, and 1 mm has nowhere near the stroke to absorb the seat-depth band. The old ID 44 / OD 52 figure is left over from the deleted Ø52 collar and never fitted the pocket. Compression verified 17–43 % across the whole tolerance box |
| M3 flat-head screws, ≈ M3 × 8 | 4 + spares | ~2 | **Bought.** Motor faceplate → carrier, driven through the wheel hub. **Head Ø must be ≤ 6 mm** to pass the hub’s Ø6.5 driver holes. See `wheels/WHEEL_HUB_V5_CHANGE.md` |
| Low-ESR 105 °C electrolytics, 25 V: 1000 µF ×1, 470 µF ×1, 220 µF ×3 | 1 set | unconfirmed | **Ordered.** Bus, ESC & driver/lid caps |
| Schottky SS34 / 1N5819 | 1+ | unconfirmed | **Ordered.** Not fitted, the 5V feed runs without a diode as of 23 Sep |
| JST-PH 6-pin pigtail pair | 1 | unconfirmed | **Ordered.** The Lid Plug (W56–W63) |

## 2. On hand (inventoried 2 Sep 2026)
| Item | Qty | Spec | Status |
|---|---|---|---|
| Gear motor with encoder, 25D — the **old faded pair** | 2 | 12 V (assumed), 6-pin encoder loom | **[M]** Measured 11 Sep: body **39.29**, gearbox 21.00, can 17.53 → this is most likely a **JGA25-310, not a 371**. Shaft Ø**4.10** / flat 3.46, tapped M3 at 17.0 c-c, boss Ø7.05 — **same faceplate interface as the new pair**, so it drops into the same carrier. **Bench spares only**, the 23 Sep first drive ran on the JGA25-371 pair. Ratio still unknown |
| LEGO Technic balloon tyre 62.4 × 20 (32019) on printed hubs | 2 | 62.4 mm OD | **Superseded 4 Sep — 6.5 N/mm squat grounds the brim at ~210 Pa and makes the fan a net negative (`WHEEL_TYRE.md` §1). Bench and mock-up use only** |
| Brass shaft coupler, 4 mm bore, grub | 3 | 2 hex, 1 round | Epoxy into hex pocket in hub |
| NXE 850 mAh 3S 30C LiPo, JST-RCY | 1 | 11.1 V | **Bench only, never the fan** (sags, 3 A connector) |
| MX1508 / TC1508A dual H-bridge | 1 | 1.5 A cont, 2–10 V | Bench only at ≤9 V. Replaced by DRV8871 |
| VL53L0X ToF breakout (GY-VL53L0XV2) | **8 in hand** (3 old + 5 new) | I2C, XSHUT, ~2 m | **7 used, 1 spare** — count settled 17 Sep. v11 runs seven: front 0/±25, sides ±90, rear 180±25. Documented fallback if more than one dies: front + rear only, drop the side sensors |
| LM7805 stripboard carrier w/ TTGO headers | 1 | Linear 5 V | Retired (MP1584 replaces) |
| Latching push-button switch | 1 | 1–3 A | Logic arm switch only |
| Old printed chassis | 1 | Black PLA | Superseded; test plank for the early drive tests |
| JST-XH/PH, splices, M3 hardware, Dupont, resistors (10k, 4.7k, 2.2k) | lot | — | Sort before build |
| CO2 bike inflator cartridges 16 g / 25 g | — | — | Not used (concept dropped) |
| **LilyGO T-Display S3** (ESP32-S3, non-touch) | 1 | 62.3 × 25.65 × 6.88 mm, 14.6 over the header pins | **[M]** In hand and measured 12 Sep. It is a **T-Display S3, not a classic-ESP32 TTGO** — see `PIN_MAP.md`. Too long for the roof; it sits on the −Y wellcap under a window in the lid |

## 3. Buy locally (~$15)
Selleys **Glass** Silicone (acetoxy, ~$10, Bunnings) — skirt bonding and skim coat, *not* the neutral-cure Roof & Gutter, and *not* for tyres · rubber bands No. 64 (Officeworks, ~$7) — interim tyre for the early drive tests · steel washers/coins for ballast (20c = 11.3 g, 50c = 15.55 g) · HDPE chopping-board offcut (rear skid) · aquarium airline (manometer).

## 4. Only if needed
| Item | Trigger | ~AUD |
|---|---|---|
| ~~2× JGA25-371 12 V 130 rpm encoder motors~~ — **BOUGHT, ARRIVED, MEASURED 17 Sep** | Trigger fired. **[M]** Body **58.84** (not the 65 assumed), OD 24.78, shaft Ø**3.99** / flat 3.45, tapped M3 c-c **17.11**, encoder connector exits **radially**, **96.2 g each including the loom** (93.3 g bare), A ≡ B. Tapped-hole axis 3/9 with the flat at 12. v12 carriers and hub v5 both check out against it — **no reprint** (17 Sep. Since replaced by carriers v13 and hub v6.2, see `chassis/v11/START_HERE.md`.) | 24–30 ea |
| 2× DRV8871 from Core Electronics (2–5 days) | AliExpress DRV8871s not here by 16 Sep | 28 |
| Cytron MDD3A | DRV8871 thermal-trips under stall | 25 |
| Brushed 5015/5020 24 V blower | ESC refused by coordinator | 6 |

## 5. Wheel materials — committed 5 Sep
Wheels are made in house: printed hubs + cast silicone tyres (`WHEEL_V1.md`). **Buying tyres or mounting hubs is dropped entirely — do not re-cost it.**

| Item | Qty | AUD | Source | Notes |
|---|---|---|---|---|
| Smooth-On **Mold Star 15 SLOW** 900 g | 1 | 52.00 | U Resin, Maddington 6109 (walk-in pickup) | **Collected.** A15, 1:1, **50 min pot life**. The fitted tyres were cast from it in the v1 ring mould. Enough for many pairs |
| ABS or PETG filament for hubs | — | on hand | — | Not PLA (Tg 60 °C, brittle at the bore) |
| PLA filament for the mould | — | on hand | — | PLA does not inhibit platinum-cure silicone |

Rejected: PinkySil and Mold Star 22T (6 min pot life — too short for a first cast), oogoo/caulk (never cures through a 20–25 mm ring), all AliExpress and JSumo bare tyres (see `WHEEL_V1.md`).

## Budget
Cart ~$120 + batteries/charger ~$50 + local ~$15 + silicone $52 ≈ **$237** — the 2 Sep figure, and it is now low. Two things have been added since: the **new JGA25-371 motor pair** (§4 trigger fired, ~$55 the pair) and the **§1b hardware** (M3 × 8, M3 flat-heads, 3 mm EPDM, ~$9). That is **≈ $301** all in. The 2200 mAh packs that arrived in place of the 1500 mAh cost no more — the supplier substituted up at the ordered price.

## Weight budget (target 990 g)
**Measured 23 Sep: 765 g** for the whole 23 Sep drive-only bot on a scale, before ToF & line sensors, with the Brain on a breadboard. The prediction for the finished bot is below.

Motors **192.4 [M]** · battery **151.2 [M]** · printed structure 296.4 est. · wheels, hub v5 + cast tyre, 74.2 est. · EDF 40 + ESC 25 est. · protoboard A/B/L 15 + modules and sensors 50 est. · alarm, button, XT60, wiring 60 est. · inserts, fasteners, gasket 30 + skirt 20 est. → **954.2 g total, 35.8 g of ballast headroom to the 990 g target** (rule limit 1000 g). Every figure above carries a source line in `hardware/MASS_BUDGET.md` §1, **and that file, not this line, is the mass authority.** Any part more than 15 % over its estimate gets flagged at the sync, because it comes out of the ballast and ballast is push.

Two of those lines are real scale readings. **Motors 190 → 192.4 g** (96.2 each *with* the loom, weighed 17 Sep) and **battery 121 → 151.2 g** (weighed 11 Sep, the pack that arrived is the 2200 mAh, which is 30 g heavier than the 1500 mAh that was costed). Everything else on the line is still an estimate, 610.6 g of the 954.2 g total, so read the headroom as a working figure and not a measurement.

**The chassis line is the one to watch, and no part of it is measured.** The v11 printed set totals **296.4 g modelled**, which is base 116.8 (`chassis/v11/REPORT_base_stage.md` line 86) + lid 128 (`REPORT_lid_stage.md` line 15) + 2 × carrier v12 15.8 (`CARRIER_V12_CHANGE.md` line 29) + battery frame v2 3.47 (`BATTERY_FRAME_V2_CHANGE.md` line 3) + 2 × wellcap 6.0 (`REPORT_lid_stage.md` line 33 plus `WELLCAP_PLUS2.md` line 9) + clamp ring v2 4.56 (`CLAMP_RING_V2_CHANGE.md` line 39). The lid alone is 18 g over its own 110 g gate. The earlier "≈297 g" here was the same set with the frame and ring rounded up, and the arithmetic was right.

**The 267 g figure is retired.** That was the **v5** chassis on a scale, v5 is not the robot, and nothing should quote it as current. `hardware/MASS_BUDGET.md` §1 carries the full accounting and **that file, not this line, is the mass authority**: 954.2 g total, 35.8 g of ballast headroom. Still unweighed and material: the six printed parts as a set, one finished wheel with its cast tyre, the ESC, and the EDF.
