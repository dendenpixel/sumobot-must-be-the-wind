# Power / start button — as-measured (11 Sep 2026)

**Status 23 Sep 2026:** not fitted yet. The drive-only build starts on the Brain's own onboard buttons (GPIO 14 or BOOT), the panel button goes in with the lid at the next build stage. The v11 lid has a Ø18.7 hole in a Ø26 pad at (−38, 10). Pin identification was done in the full wiring guide (not published), and the panel grip thickness below is still unmeasured.

Snap-fit panel button, mounts through the top of the chassis. Retained by **two plastic clips on the sides**, not a threaded nut.

## Measured

| Dimension | Measured | Note |
|---|---|---|
| Overall height, pin tips → top of the button cap | **29.33** | sets internal depth behind the panel |
| **Body diameter (round section)** | **18.51** | this is what the hole is cut for |
| Widest point | **19.28** | across the clips or a bezel — **needs identifying, see below** |
| Pin count | **3** | function not yet identified |
| How much of it protrudes ABOVE the panel face | ☐ | |
| **Panel thickness the clips are designed to grip** | ☐ | **this is the one that will bite** |
| Bezel/flange diameter, if there is one | ☐ | |
| Mass | ☐ | |

## Panel hole

```
button_hole_d = 18.7      // body 18.51 + 0.2, then open up by hand if tight
```

Den's own rule applies and is the right one: **cut it undersize and drill out.** A hole that's 0.3 mm too small costs two minutes with a round file. A hole 0.3 mm too big cannot be fixed and the button rattles or falls through.

## The thing that will actually bite: panel thickness

Snap-fit panel components are designed for a **specific panel thickness range** — the gap between the underside of the bezel and the top of the clip barb. Commercial ones assume thin sheet metal or moulded plastic, often **1.0–2.5 mm**.

A 3D-printed chassis wall is usually **3 mm or more**. If the wall is thicker than the clips' grip range, **the clips never reach past it and the button will not latch at all** — no amount of hole-diameter tuning fixes that.

**Measure before designing the mount:** with the button on the bench, the vertical distance from the underside of the top flange down to the top edge of the clip barbs. That number is the maximum wall thickness at the button.

If the chassis wall there is thicker, the fix is a **local thin boss** — counterbore the inside face down to the clips' grip thickness in a ring around the hole, leaving the rest of the wall full thickness. Strength is unaffected; the button gets the thin panel it expects.

## The 3 pins are probably not what they look like

Den's read is ground / active / output. Three pins on a button is more commonly one of:

- **COM / NO / NC** — a changeover switch, one common plus both a normally-open and a normally-closed contact.
- **Switch + LED** — two switch pins and one LED pin sharing a ground.

These wire completely differently. **Multimeter on continuity, 30 seconds:** probe each pair with the button released, then pressed. A pair that goes open→closed is the switch. A pair that reads a diode drop (~2 V on diode mode) is the LED. If one pin is closed at rest and opens when pressed, it's the NC contact and it's a changeover.

Do this before anything is soldered — wiring an NC contact into a start path gives a bot that runs until you press the button.

## Current path — the button must not carry motor or EDF current

A panel button of this size is rated for signal-level current, low single-digit amps at most. The drive motors and the EDF together pull far more than that.

- **The XT60 loop key is the real power disconnect.** It's in the main current path and it's rated for it.
- **This button switches a signal only** — into the MCU, or into the gate of a MOSFET / coil of a relay that does the actual switching.

Putting it in series with the pack welds the contacts shut, and a power switch that can't turn off is worse than no switch. **Settled:** it's a signal into the PCF8574's P7 in the lid ([`../PIN_MAP.md`](../PIN_MAP.md)), read through the lid expander alongside the XSHUT lines.

## Internal clearance

29.33 total height. Minus whatever sits above the panel (still to measure), the body needs roughly **25–27 mm of clear space below the top face**, plus room for three wires or a connector on the pins. Nothing else can occupy that column.
