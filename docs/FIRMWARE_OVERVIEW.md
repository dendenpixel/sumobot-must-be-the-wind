# Firmware overview

The competition firmware (v2.5, the build that fought on 15 Oct 2026) isn't published, at the course coordinator's request. This page is what it does, in words.

## A match, start to finish

Key in, and the first thing the firmware does is hold the fan at zero, because the fan's speed controller only arms if it sees zero throttle from power-up. Motors braked, screen on, then the seven distance sensors are woken one at a time through the expander chip in the lid, each one getting its own address before the next one wakes. A sensor that doesn't answer is skipped & shows on the status screen, so a dead eye turns up on the bench, not in the ring.

Once the speed controller has armed, the robot waits for GO. The countdown after GO is braked on purpose, so fan torque, or the suction settling, can't nudge it forward & earn a false start.

From there it searches, turning toward the side the opponent was last seen on. When a sensor picks him up it turns to face him, charges once the front sensors have him, and pushes once he's in contact. If a front corner finds the board edge mid-push, it holds for a moment instead of backing off, because the corner sensors sit behind the front rim, so by the time they see the edge he's already over it (reversing then would only let him go). Then it escapes.

An edge escape reverses away from whichever corner saw the edge, keeps going until every corner is clear with some margin, then turns back toward where the opponent was, and searches again.

## Who wins when two things happen at once

Every pass through the loop checks the modes in a fixed order and the first one that's true wins:

**edge > contact > charge > turn > search**

The edge beats everything that moves, contact beats charging, charging beats turning toward him, and turning toward him beats searching blind.

## Safety

- **Finger-off start.** The start button started the match when your finger came off it, so a finger resting on it while the key went in couldn't launch the robot. That was the start path until the lid button was lost late in the build.
- **All corners dark.** All four corners reading dark for a moment means it's been lifted, flipped or pushed off the plate. Motors stop & the fan goes to zero before anyone's fingers find the wheels.
- **GO & STOP from the laptop.** A second board plugged into the laptop by USB passes GO and STOP to the robot over ESP-NOW (Espressif's direct board-to-board radio link). STOP parks the robot with the wheels braked and the fan off.

## Lessons

Our encoders can't tell a stall from wheelspin, so stalemate handling ended up time-based, and the robot couldn't tell whether it was moving the opponent or just spinning its tyres.

The red line round the ring reads like white to an infrared sensor, since red reflects infrared, so the edge the firmware keys on is the black board itself and not the painted line.

The first version of the fight code was written, and run through a simulation on a PC, before it had ever been on the robot. It came with a written list of what still wasn't verified (motor polarity, the turn directions on the staggered axles, the edge thresholds under the venue lights, what each sensor reads in an empty ring). The simulation caught logic bugs, but it couldn't stand in for time on the real ring, and the final firmware got about a day of tuning.
