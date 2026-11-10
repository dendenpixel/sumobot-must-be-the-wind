# Battery frame v2 — rear snap fingers (15 Sep 2026)

**On the bot (23 Sep), printed in PLA.** File: `hardware/cad/v11/stl/v11_battery_frame_v2_clip.stl` (mesh-edited from Astra's `v11_battery_frame.stl`, watertight, 3.47 g PETG est., bbox X −87.5…−37.5 / Y ±66.5 (+76 bracket) / Z 15.06). Everything outside the rear 15 mm of each rail is byte-identical to v1.

Print settings: `../../printing/PRESETS_battery_frame_v2_PLA.md` — note that the preset that was actually built is **PLA**, not the PETG this change doc specs; the mechanical consequence is recorded there.

## Why
Report after printing v1: sideways rattle is fine (1.85 mm per side), but the pack **slides back and forth in X** — nothing behind it, the rear is open for the slide-out. v1 relied on the strap for everything.

## What changed (per side, +Y described, −Y mirrored)
- **Rear strap tunnel (X −83…−68) deleted**: rear stub, the rail top bar over it, and the floor's inner strip Y 53…57.2 in that span. Floor stays from Y 57.2 outboard, so the (−78, ±61) bolt tab keeps a 2.0 mm ligament to its Ø3.6 hole.
- **Root block** X −68…−60, Y 55…57.4, Z 0…8 (replaces the middle stub, taller). **Web** X −68…−66, Y 53.8…55.
- **Finger arm** X −83…−66, Y 53.8…55.0 (1.2 thick), Z 0…5. Free length ~17 mm. Inner face 0.65 mm off the pack edge (53.15).
- **Hook** at the rail's back edge: catch face at X −83.0 (pack rear face −82.5 → 0.5 mm play), tip Y 51.95 (1.2 mm overlap over the pack edge), 45° lead-in ramp from (−84.5, 51.95) to (−87.5, 55.0). Tip overhangs the frame by 4 mm in free air over the wedge, inside the lid slit (Y ±62, Z 10.9–34) — nothing to clash.
- **+Y only**: block X −72…−70, Y 56.9…58.0, Z 0…5 — ties the XT60 bracket's inner post (Y 56.6…57.4, Z 5–12.4) to the plate and floor now that the rail bar under it is gone; doubles as the finger's over-travel stop.
- Front strap tunnel (X −60…−48.6) untouched — one strap still goes through per side for Z hold-down.

## Numbers
- Deflection to pass the pack: 1.65 mm. Strain ≈ 3tδ/(2L²) = 3·1.2·1.65/(2·17²) ≈ 1.0 % (PETG yields ~5 %).
- Spring rate ≈ 0.9 N/mm per finger (E 2.1 GPa, I = 5·1.2³/12) → ~1.5 N lateral, ~2 N push per finger through the 45° ramp. Insertion is light; retention is positive (square catch face, doesn't cam out).
- Deflected outer face reaches Y 56.65: clear of the +Y bracket plate (57.6) and the M3 heads on the tabs (≥ 58.25).
- Checks (trimesh/manifold): watertight; pack envelope X −82.5…−48.1 × Y ±53.15 × Z 21.46 overlap **0 mm³**; swept finger (arm+hook shifted +1.65) vs rest of frame **0 mm³** both sides.

## Use
- **Pack orientation: leads toward the XT60 bracket end (+Y).** The stop wall's 5 mm notch (Y > 38) and Board A rear-left are laid out for that.
- Insert: slide straight in +X through the slit; the fingers open on the ramps and snap behind the pack.
- Remove: through the slit, pinch both hooks outward (~2 mm), pull the pack −X.
- Print: PETG, flange down as v1, 3 walls, no support. Fingers are 1.2 mm = 3 perimeters, bend in the layer plane.

## Not done / open
- Strain and force are hand calcs on nominal PETG. If the fingers feel stiff, the arm can go to 1.0 mm; if floppy, raise Z 5 → 6 (still clears the bracket post support only if that block grows with it).
- Pack rear face position assumes the pack seats on the stop wall (−48.1). A shorter pack gets foam tape on the hook catch face, not a tighter hook.
