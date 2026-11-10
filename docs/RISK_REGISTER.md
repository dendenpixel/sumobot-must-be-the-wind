# Risk register (rev 4–5 Sep 2026 — rows 16–20 added after the geometry pivot, rows 1, 4, 6, 8, 9, 13, 20 corrected and 21–25 added 18 Sep from the repo audit, rows 2, 3, 5, 9, 10, 11, 20, 23–25 updated and 26–28 added 23 Sep after the first drive)

> **Superseded at project close (16 Oct 2026).** Frozen at the 23 Sep revision, outcomes are in [`status/2026-10-16_project_final.md`](status/2026-10-16_project_final.md).

Ranked by "loses a bout first". Row 15 (a team-process item) is left out of this copy.

| # | Failure | Mitigation |
|---|---|---|
| 1 | Voltage sag mid-push | One Ovonic 3S 2200 mAh 120C XT60 pack (measured 151.2 g). No firmware LVC & no divider on the S3, a plug-in LiPo alarm on the balance lead & a human pulls the key. The alarm isn't wired yet, its location & trip voltage are unconfirmed. Fan cut before motors |
| 2 | Lower opponent wedge vents the plenum → downforce goes to zero | v11 has no scraper lip, the defence is the continuous 15° wedge with its rim 0.5 mm off the floor. Keep ballast, never fan-only |
| 3 | Real downforce 0.8–1.5 kg, not 2–4 (skirt gap ≈ 30 % of throat area) | The kill gate is the in-chassis one-shot commissioning run, no loose bench test. Tuneable bleed, coarse mesh over bellmouth |
| 4 | AliExpress delivery slips past mid-September | **Closed 17 Sep, everything ordered has arrived** (`docs/hardware/MEASURED_PARTS.md`) |
| 5 | Clone DRV8871 DOA or thermal shutdown (~2 A bare) | 4 bought, 2 fitted, 2 spare. ILIM value & thermal mounting unconfirmed, see row 24. Cytron MDD3A fallback |
| 6 | LittleBee ESC ships with no servo lead | Solder a 3-wire lead. **Check the part: the wiring guide says this ESC has no BEC lead, six older docs say cut the red one. If a red wire is there, cut it** |
| 7 | I2C hang → WDT reset → ESC re-arm delay | I2C timeout set & every return checked, all XSHUT low first thing at boot, sensor wires ≥30 mm from ESC/motor leads; line detection never on I2C |
| 8 | ESC arming glitch at boot | ESC on **GPIO 43** with 1 kΩ series + 10 kΩ pulldown (GPIO 15 is the LCD power enable on the S3, and 43 is the pin the bootloader stamps on at reset, which the ESC doesn't care about); ESC held at minimum throttle from the start of boot; fan stays off in calibrate/stop |
| 9 | Coordinator refuses ESC or suction | **Closed: suction approved 8 Sep, ESC as a motor controller & fan pre-spool allowed, confirmed by 23 Sep** ([`docs/admin/DESIGN_APPROVALS.md`](admin/DESIGN_APPROVALS.md)) |
| 10 | Rear corners blind to the line | 4 sensors, one per corner, polled every loop, thresholds calibrated in CAL mode on the real arena |
| 11 | Drivetrain under ~3 kg normal load: grub slip, tyre squat jams skirt, skid drag | 2 grubs 90° + threadlocker; **skirt gap 0.4–0.6 mm set with the fan RUNNING**, since silicone squat under clamp is 0.35 mm |
| 12 | PLA rim warp ≥0.5 mm kills the seal | Print rim flat / plane it; 6 perimeters; check the 250 cube with guard fitted |
| 13 | Motor ratio too fast (on-hand pair unknown) | **Closed: JGA25-371 12 V 130 rpm pair bought 6 Sep & measured 17 Sep** (`docs/hardware/MEASURED_PARTS.md`). Encoder counts per rev still to be counted on the bench |
| 14 | EDF overheats sealed (no cooling flow) | Slight leak is a feature; 3-min thermal check at 100 %; fan rule: run only if last thermal check passed |
| 16 | **A rigid part grounds before the tyres and the fan makes push *worse*.** This already happened once: LEGO balloon tyres ground the brim at ~210 Pa, net −3.4 N at 800 Pa | Cast silicone on a rigid hub (~96 N/mm pair) closes it on paper. **Confirm with the push-vs-throttle test — if push does not rise monotonically with throttle, something is grounding** |
| 17 | Silicone will not bond to PETG. No datasheet supports a reliable cured-silicone-to-thermoplastic shear bond | Retention is mechanical only: 10–12 radial Ø3.5 mm through-holes with an inside counterbore (mushroom rivets) + 1.5–2 mm side flanges. Do not rely on adhesive |
| 18 | Arena board is not flat. A 1 m MDF board bows 1–3 mm; a 1 mm rigid brim has no margin for that or for a taped seam | Straightedge + feeler gauges on the **actual** arena before trusting any skirt gap |
| 19 | **Encoder counts do not measure heading under fan clamp.** A skid-steer pivot is slip-governed: the wheels turn, the bot does not, and EDGE_ESCAPE terminates early | Terminate the escape on a gyro, or turn the fan off for the turn. Do not ship encoder-terminated escapes |
| 20 | **The sombrero geometry is unmodelled and the first drive is close.** | **Closed: v11 modelled, printed & driving.** The 23 Sep first drive was on the v11 chassis with the JGA25-371 pair ([`docs/status/2026-09-23_first_drive.md`](status/2026-09-23_first_drive.md)) |
| 21 | **One EDF, no spare** | No loose bench test. Mating bullets on the ESC, verify every wire & the code first, mate the fan last. Which end is the intake gets established before it goes in the collar |
| 22 | Encoder connector fouls the carrier tail | **Closed 17 Sep: connector exits radially, tail gap 16.76, v12 carriers OK, carriers now v13** |
| 23 | **First power-up straight off a 2200 mAh 120C pack** | Every first power-up after new wiring or a rework goes through a bench supply at 12 V limited to 1 A into the **Pack Socket**, key in as normal (the first power-up rule in [`docs/hardware/WIRING_OVERVIEW.md`](hardware/WIRING_OVERVIEW.md)). Done for the 23 Sep rework. The fuse is row 27 |
| 24 | DRV8871 thermal shutdown under stall with the pad hot-glued to PLA | Whether the drivers stay hot-glued & which ILIM resistor is fitted are both unconfirmed. Copper pour or heatsink under the thermal pad, ILIM set (30 kΩ → 2.1 A), the motor check gets a reject number for the winding |
| 25 | Printed lid has no gland & the wellcaps have no Brain pocket, but the full wiring guide assumes both | No gland was printed, the plan is to melt a hole with the soldering iron when the lid is cabled. For the first drive the Brain sits on a breadboard on top of the bot, it moves to protoboard next |
| 26 | **Open-loop drift.** The timed first drive runs about 100 mm right over the forward metre & finishes about 50 mm right of the start | Measure track width, check carriers for toe, trim the faster side in the timed build, then move to the encoder-counted drive, which corrects heading from the tick difference |
| 27 | **No fuse fitted.** A dead short at the Star off a 120C pack is hundreds of amps & nothing opens before the wire does | 25 A blade fuse in the Key Socket to Star + lead, not fitted as of 23 Sep. Until then every joint is soldered & heatshrunk before the pack goes in |
| 28 | The 22 Sep power-up fault (right motor dead, encoders at 0) was cleared by a rework, and the exact joint wasn't pinned down | If it comes back, start from the first power-up notes in [`docs/status/2026-09-23_first_drive.md`](status/2026-09-23_first_drive.md), and meter each motor's leads before rewiring it |

## Added 4–5 Sep 2026
Rows 16–20 come out of the geometry pivot and the wheel/tyre trade — see `GEOMETRY.md` and `WHEEL_TYRE.md`.

## Corrections carried forward
- LVC divider: **none is fitted.** GPIO 34 doesn't exist on the S3 and no free pin is left for it (`docs/PIN_MAP.md`).
- Fan: pressure ∝ rpm², power ∝ rpm³, so part throttle keeps about half the pressure for about a third of the power. **Policy superseded 4 Sep — thermal is the limit (34 s from cold to 150 °C at full throttle): fan off while searching, on in short bursts only when attacking or pushing, off during an edge escape.** See `DOWNFORCE_FAN.md`.
