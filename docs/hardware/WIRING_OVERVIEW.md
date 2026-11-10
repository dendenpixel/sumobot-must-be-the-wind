# Wiring overview (block level)

This is how the robot is wired, at the level of blocks and stages. The wire-by-wire build guide it comes from (every wire numbered, with meter checks at each stage) isn't published. The pins are in [`../PIN_MAP.md`](../PIN_MAP.md).

## Rules that applied to every stage

1. **Key out and pack out while you solder, plug or unplug anything.** The loop key (the small black XT60 plug) is the only power switch, but it only breaks the + line, so with the pack still in the Pack Socket every ground on the robot is bonded to the pack & the socket's tails stay live.
2. **Never plug in USB while the key is in.** Firmware goes on with the key out and the pack unplugged, and test results are read off the Brain's screen, not a laptop.
3. **Meter before power.** Every stage ends with a continuity & voltage check, and a failed check means stop and fix, not move on and hope.
4. **Wheels off the ground, fan duct clear, fingers out & safety glasses on for every key-in.** There are four polarised caps on the robot and no meter test tells you one's in backwards.
5. **The first key-in of every stage goes through a bench supply** with a low current limit, clipped onto the Pack Socket in place of the pack, so a short costs a beep instead of a wire.

There was no fuse fitted as of 23 Sep (a blade fuse in the Key Socket to Star + lead was still open), so every joint was soldered and heatshrunk before the pack ever went in.

## Map of the robot

Stand behind the robot. The fan end is the front and left is your left (the CAD calls front +X and left +Y).

```
PLAN VIEW OF THE ROOF (looking down, front = top of the page)

                    FRONT (fan end)
     ┌──────────────────────────────────────────┐
     │   Line 2 pocket ●            ● Line 1 pocket   (underneath, corners)
     │                                          │
     │            ( FAN COLLAR )   ┌──────────┐ │
     │             fan drops in    │ Board B  │ │
     │  ┌──────────┐               │ Driver R │ │
     │  │  LEFT    │  motor L      │ beside   │ │
     │  │  WHEEL   │═══cheek═══    └──────────┘ │
     │  │  CAP     │           ┌───────────┐    │
     │  │  (ESC on │   motor R │ RIGHT     │    │
     │  │   top)   │ ═══cheek══│ WHEEL CAP │    │
     │  └──────────┘           │ (Brain in │    │
     │                         │  pocket)  │    │
     │   ┌────────┐            └───────────┘    │
     │   │Board A │   STAR ●                    │
     │   │Driver L│   (beside battery stop)     │
     │   └────────┘                             │
     │ [XT60 bracket]  ▓▓▓ BATTERY BAY ▓▓▓      │
     │  Key Socket     pack slides out ↓        │
     │   Line 3 pocket ●            ● Line 4 pocket
     └──────────────────────────────────────────┘
                    REAR (pack slides out here)
```

The **base** is the printed tray and its top face is **the roof**, where almost everything mounts. The **lid** sits over it and carries the Expander, the seven ToFs, Board L, the Button & the alarm pocket. The left wheel cap carries the ESC, the right one has a pocket for the Brain, and the **Star** is two heavy solder joints (Star + and Star −) hot-glued beside the battery stop.

## The big picture

```
Pack ──XT60──► Pack Socket ──► Key Socket ──[Key]──► STAR + ──┬── ESC ──► Fan
                   │                                           ├── Motor Driver L ──► Motor L
                   └── ─────────────────────────► STAR − ──┐   ├── Motor Driver R ──► Motor R
                                                           │   └── Board B 12V rail ──► Buck 1 → 5 V ──────────► Brain (5V pin)
                                                           │                       │            └──► Line 1–4 LEDs
                                                           │                       └──► Buck 2 → 3V3L ──► Lid Plug ──► Expander + ToF 1–7
                                                           └── every GND on the robot
Brain ── 3V3 ──► encoder power, line-sensor + encoder pull-ups (base only)
Brain ── SDA/SCL ──► Lid Plug ──► Expander + ToF 1–7
Expander P0–P6 ──► ToF 1–7 XSHUT     Expander P7 ──► Button
Pack balance lead ──► Alarm
```

The Key is the power switch. The Button is a signal into the Expander and never carries motor current.

## Brain pins

| Brain pin | Goes to |
|---|---|
| `5V` | B5V point (from Buck 1, no diode) |
| `G` (any one) | Board B GND rail |
| `3V3` (either one) | Board B 3V3 rail |
| `11` / `12` | Motor Driver L IN1 / IN2 |
| `13` / `16` | Motor Driver R IN1 / IN2 |
| `21` | Motor L encoder A (via the ENC-L point) |
| `44` | Motor R encoder A (via the ENC-R point) |
| `43` | ESC signal (via a series resistor on Board B) |
| `1` / `2` / `3` / `10` | Line 1 (front-right) / Line 2 (front-left) / Line 3 (rear-left) / Line 4 (rear-right) |
| `18` / `17` | SDA / SCL → Lid Plug |

The other `G` and `3V3` pins stay empty, and nothing goes in the Brain's own 2-pin battery socket.

## The build, stage by stage

- **Stage 0, prep.** Cut the protoboards, fit the Brain's headers, identify the Key, the Button's pins & each motor's wires, and mount everything. Nothing gets power.
- **Stage 1, the power Star.** Every high-current wire is cut and landed at both ends: pack, key, ESC, both drivers & the Board B feed.
- **Stage 2, Board B power.** Both bucks are set with their outputs connected to nothing, then landed on the rails, then the Brain goes on.
- **Stage 3, drivers, motors & encoders.** Motor leads to the driver screw blocks, driver inputs to the Brain, encoder channel A to the Brain through Board B.
- **Stage 4, ESC signal & fan.** The signal lead goes in with the fan unplugged, and the fan is mated last (there is one fan and no spare).
- **Stage 5, line sensors.** Four bare TCRT5000s into Board B, one per corner pocket, each with its own LED resistor, pull-up and filter cap.
- **Stage 6, Lid Plug (base half).** Four wires across the lid joint: SDA, SCL, 3V3L & GND.
- **Stage 7, the lid.** Board L, the Expander, the seven ToFs & the Button.
- **Stage 8, the alarm.** The pack's balance lead onto the LiPo alarm.

## Three deliberate choices

**The drivers' header GND is left unwired.** On the DRV8871 module that pin is the same copper as the power − terminal, so a thin wire there would be a second return path, putting a share of the chopped motor current through Board B's logic ground. The inputs reference fine through the power terminal back to the Star.

**No USB with the key in, ever.** There's no diode on the 5V feed, so with the key in, USB & the buck would share the 5V node. Back-feed aside, the real reasons are a laptop ground tied into the motor fault path and motor transients on a shared 5 V node resetting the Brain.

**The I2C bus runs at standard-mode speed, with no external pull-ups.** The PCF8574 is a standard-mode part, and the ToF boards pull up to their own 2.8 V rail, only just above the Brain's input-high threshold. Seven ToF boards' pull-ups in parallel are already plenty, so none were added (one reviewer disagreed, and the fallback was a pair of pull-ups on Board L if the bus ever idled low).
