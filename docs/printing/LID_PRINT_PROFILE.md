# SumoBot v11 Lid — Bambu Studio Print Profile

**Part:** `v11_lid.stl` · 176.6 × 176.7 × 54.7 mm
**Printer:** Bambu Lab X1C, 0.4 nozzle, Textured PEI plate
**Printed and on the bot (23 Sep) in PETG translucent.** Preset json `hardware/cad/v11/presets/SumoBot_Lid_PETG_SupIF.json`. The lid stage report and `LAYOUT_PASS.md` say PLA, that was the design assumption.
**Material:** PETG Translucent (slot 1) + Bambu Support for PLA/PETG (slot 4, interface only)
**Base profile:** `0.20mm Standard @BBL X1C`
**Orientation:** flat outer face down on the plate (as supplied in the STL, Z0 = flat face)

---

## Why this profile looks the way it does — geometry analysis

Measured from the mesh (25,084 facets), down-facing surfaces above the plate:

| Slope from horizontal | Area | Needs support? |
|---|---|---|
| 0–5° (flat ceilings) | 523 mm² | **yes** |
| 5–30° | 49 mm² | yes |
| 30–40° | 10 mm² | marginal |
| **40–45°** | **4,292 mm²** | **no** — perimeter skirt, self-supports |
| 45–90° | 18,300 mm² | no |

**Total real support need: 572 mm²**, concentrated in four thin Z bands:

| Z height | Area | Feature |
|---|---|---|
| 29.5 mm | 216 mm² | rectangular slot ceilings, lower row |
| 38.7 mm | 195 mm² | rectangular slot ceilings, upper row |
| 44.7 mm | 26 mm² | small wall feature |
| **51.7 mm** | **122 mm²** | **corner screw bosses** — the precision-critical ones |

Two consequences:

1. **Do not raise the threshold angle past ~38.** The 4,292 mm² skirt sits at 40–45°. Raising the threshold wraps the entire perimeter in supports for no benefit.
2. **"On build plate only" MUST be off.** All four bands sit over the lid's own floor, not over open plate. With it ticked, the slicer refuses to build columns that land on the part and all four bands get nothing.

Bed contact is 22,230 mm² — adhesion is a non-issue, no brim needed.

---

## Filaments

Load **only** these two. Delete any unused slots — unused/half-configured filament profiles still get validated at slice time and can throw `Flow::mm3_per_mm() produced negative flow`.

- Slot 1 — PETG Translucent
- Slot 4 — Bambu **Support for PLA/PETG** (the PLA-only "Support for PLA" SKU is *not* rated for PETG)

## Quality

| Setting | Stock | Set to |
|---|---|---|
| Layer height | 0.20 | **0.16** |
| X-Y hole compensation | 0 | **0.15** |
| Wall generator | Classic | **Arachne** |

Leave stock: all line widths (0.42 / 0.5 / 0.42 / 0.45 / 0.42 / 0.45 / 0.42 / 0.42), elephant foot 0.15, initial layer height 0.2.

## Strength

| Setting | Stock | Set to |
|---|---|---|
| Wall loops | 2 | **4** |
| Bottom shell layers | 3 | **5** |
| Sparse infill density | 15% | **25%** |

Leave stock: top shell 5, Grid infill, Monotonic top/bottom surface, Ensure vertical shell thickness = Enabled.

Note: "bottom" here is the lid's outer face sitting on the plate — the visible/mating surface.

## Speed

| Setting | Stock | Set to |
|---|---|---|
| Bridge | 50 | **30** |
| Overhang speed — 50% band | 30 | **20** |
| Support interface | 80 | **50** (optional) |

Leave the 75% and 100% overhang bands at **10 mm/s** — higher % = more overhanging = the bands that protect the boss ceilings. Keep "Slow down for overhangs" ticked.

## Support

| Setting | Stock | Set to |
|---|---|---|
| Enable support | off | **on** |
| Type | tree(auto) | **normal(auto)** |
| Style | Default | **Snug** |
| Threshold angle | 30 | **35** |
| **On build plate only** | off | **off — leave unticked, critical** |
| Remove small overhangs | on | **on** |
| Support/raft base | Default | **Default** (= the PETG) |
| Support/raft interface | Default | **slot 4, Support for PLA/PETG** |
| Support wall loops | -1 | **0** |
| **Top Z distance** | 0.2 | **0** |
| **Bottom Z distance** | 0.2 | **0** |
| Top interface layers | 2 | **2** |
| Bottom interface layers | 2 | **2** |
| Interface pattern | Default | **Rectilinear** |
| Top interface spacing | 0.5 | **0** |
| Support/object xy distance | 0.35 | **0.40** |
| Independent support layer height | on | **off** |

Zero Z gap + solid interface spacing is the whole point of the interface material — the support touches the part and still peels. A non-zero gap throws the benefit away; leaving the interface on "Default" with a zero gap welds it on permanently.

## Others

| Setting | Stock | Set to |
|---|---|---|
| Purge into objects' infill | off | **on** |
| Purge into objects' support | off | **on** |

Prime tower stays enabled. No brim.

---

## Off-slicer

- **Dry the PETG** — 8 h at 65 °C. Translucent shows every steam bubble as haze.
- **Print with the chamber door open.** Bambu's guidance for PLA/PETG mixed prints — the PLA-based support softens in a hot enclosed chamber.
- **Glue stick on the textured PEI** as a release agent, not for adhesion. PETG bonds hard enough to pull plate texture off.

## Verify after slicing

1. Support present under **Z 29.5 / 38.7 / 44.7 / 51.7 mm**. Nothing else on this part matters.
2. Slot 4 usage reads a **couple of grams**, not tens. If it's 20 g+, interface is going somewhere unintended.
3. Colour check — thin band of support-filament colour only where support meets the part; towers in PETG. A whole tower in support colour means the base dropdown got set by mistake.
4. If the 44.7 mm band has no support, untick **Remove small overhangs** — that band is only 26 mm² and may be getting discarded.

---

## Known failure modes

| Symptom | Cause |
|---|---|
| `Flow::mm3_per_mm() produced negative flow` | a line width is zero or too small for the layer height. Bisect: set layer height back to 0.20 and reslice. Then check unused filament slots, filament-level width overrides, object-level overrides, and Arachne (revert to Classic to test). |
| Slot ceilings / screw bosses droop | "On build plate only" was left ticked |
| Support welded on, unremovable | interface filament left on "Default" while Z gap is 0 |
| Support falls off mid-print | base filament set to the support material — base must be the model filament |
| Haze / bubbles in the translucent | PETG not dried |

## Material notes

PETG HF runs ~230 °C nozzle / 60 °C bed; the PLA-side support runs ~220 °C. That 10° delta is why this pairing works. If running a third-party translucent PETG on a 250 °C profile, the PLA-based support will struggle — fall back to single-material PETG supports with Top Z **0.4** and interface layers **1**.

**Translucency vs structure:** 4 wall loops and 25% infill make this lid read as frosted, not clear — light scatters at every internal boundary. Accepted deliberately; this part is structural. Save the clear look for the thin flat scoreboard panel, which can run 100% infill.

Sources: [Support for PLA/PETG — Bambu Lab Store](https://us.store.bambulab.com/products/support-for-pla-petg) · [PLA/PETG mutual support — Bambu Lab Wiki](https://wiki.bambulab.com/en/filament-acc/filament/h2d-pla-and-petg-mutual-support)
