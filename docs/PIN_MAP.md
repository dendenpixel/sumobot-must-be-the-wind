# LILYGO T-Display S3 pin map (block level)

**Board: LILYGO T-Display S3 (ESP32-S3), the NON-touch version.** Not a classic ESP32, not a TTGO
T-Display. This page is the block-level map: which pin group does what. The firmware settings that
drive these pins aren't published.

## Allocation
| Function | GPIO | Notes |
|---|---|---|
| Motor L IN1 / IN2 | 11 / 12 | → DRV8871-L (rear-left, on the roof) |
| Motor R IN1 / IN2 | 13 / 16 | → DRV8871-R (front-right, outboard of Board B) |
| Encoder L A | 21 | Single channel, pull-up to the Brain's 3V3 |
| Encoder R A | 44 | Same. **44, not 43 — see the note below** |
| Encoder L B / R B | — | **Deliberately not wired.** No quadrature: direction comes from the sign we commanded, speed from the edge rate |
| Line FR / FL / RL / RR | 1 / 2 / 3 / 10 | ADC1. **Bare TCRT5000 phototransistor**, LED fed from the 5 V rail, analog read calibrated on the arena |
| ESC signal | 43 | Series resistor + pull-down on Board B. **43, not 44 — see the note below** |
| I2C SDA / SCL | 18 / 17 | No external pull-ups, the seven ToF boards' own pull-ups already parallel down |
| VL53L0X ×7 | I2C | All ship on the same address, re-addressed one at a time at every boot through the expander |
| PCF8574 | I2C | P0–P6 = the seven XSHUT lines, P7 = start button. Lives in the lid |
| Start button | PCF8574 P7 | Pressed = P7 pulled to GND |
| Battery voltage | — | **No ADC, no divider, no pin.** Watched by the LiPo alarm buzzer off the balance lead |
| Buttons A / B | 0 / 14 | Onboard buttons only, bench use |
| Board power enable | 15 | Reserved by the board, drives the screen's power |
| LCD bus & control, backlight | 5–9, 38–42, 45–48 | Reserved by the board |
| Serial console | native USB | **UART0 is never used.** See the 43/44 note |

**Free and used by this robot:** 1, 2, 3, 10, 11, 12, 13, 16, 17, 18, 21, 43, 44. That is thirteen
pins and this map uses all thirteen. There is no spare GPIO.

**Why the ESC is on 43 and encoder R is on 44.** GPIO 43 is UART0 TX, and the ROM bootloader drives it
for a moment at every reset. An encoder input fighting a driven pin is bus contention on every boot.
The ESC does not care: it is still playing its own power-up beeps through that window and is not
looking for a signal yet, so the line that gets stamped on at boot is the one we can afford to have
stamped on.

## The seven ToFs
| Index | Nose tag | Where it points | Facet centre (x, y) |
|---|---|---|---|
| 0 | F0 | Front centre | (88.30, 0.00) |
| 1 | F+25 | Front, 25° left | (82.97, 64.38) |
| 2 | F−25 | Front, 25° right | (82.97, −64.38) |
| 3 | L90 | Left side | (−25.17, 88.10) |
| 4 | R90 | Right side | (32.10, −87.91) |
| 5 | B+25 | Rear, 25° left | (−81.43, 72.14) |
| 6 | B−25 | Rear, 25° right | (−81.43, −72.14) |

Optical axis is at **Z 39.9** on every one of them (the noses sit under the anti-climb lip).
Coordinates are the CAD frame: **+X front, +Y left, Z 0 = arena floor**. Nose tags match
`chassis/v11/REPORT_lid_stage.md` §2.

The wiring at block level is in [`docs/hardware/WIRING_OVERVIEW.md`](hardware/WIRING_OVERVIEW.md).
