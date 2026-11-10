#!/usr/bin/env python3
"""
SumoBot v11 layout pass — envelopes only, no solids.
Frame: mm, +X front, +Y left, Z=0 arena floor.
Outputs: plan.png, zstack.png, interfaces.json, checks.json

v11.2 LAYOUT UPDATE, 22 Sep 2026 (Den), for the drive-only build:
  - roof electronics re-laid for the drive-only build:
      Board B (bucks/diode/rails) front-right, 55 x 30, hot-glued, hole side up
      Driver R beside Board B, outboard (toward the -Y rim)
      Driver L rear-left, hot-glued straight to the roof (no Board A in this build)
      Star = two solder blobs where the old "bus_block" was, 24 mm apart
      Pack Socket + Key Socket both rear-left, Alarm on the roof centre in front of the battery stop (drive-only build)
  - buck box is the MEASURED 15 x 11 x 8.5 (spec sheet), NOT 22 x 17
  - board_pilots are NOT moved: the v11 base is already printed with them. Board B's new footprint still covers pilots A.
  - motor envelopes stay at the 69.3 worst case (carriers are printed); wire nodes use the MEASURED tail at 58.84.
"""
import json, math, sys
import numpy as np
from shapely.geometry import Polygon, Point, box as sbox
from shapely.ops import unary_union
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon as MPoly

# ------------------------------------------------------------------ PARAMETERS
P = dict(
    # hull
    rim_a=124.5,          # superellipse semi-axis -> 249 x 249 overall
    rim_n=4.0,            # exponent (v9 family)
    rim_z=0.50,           # rim lip underside
    pan_z=1.50,           # pan underside (plenum floor gap)
    roof_top=10.90,       # KNEE height / roof top
    roof_t=1.20,
    wedge_deg=15.13,      # atan(9.2/34)
    knee_inset=34.0,
    seal_out=20.0, seal_in=23.0,       # main seal wall faces (RIM INSET)
    collar_out=34.0, collar_in=36.0, collar_top=16.9,
    skirt_out=36.4, skirt_in=38.4, skirt_top=20.9,
    lean_deg=7.5,         # tower lean measured from skirt top Z 20.9
    lip_proud=4.5, lip_z=53.0,
    top_z=65.6, top_skin=1.6,
    hole_shrink=0.21,
    # drive
    wheel_od=46.8, tyre_w=27.0, hub_w=29.0,
    motor_d=25.0, motor_len=69.3,      # JGA25-371 1:75 worst case (L23+30.8+15.5)
    motor_len_real=58.84,              # MEASURED 17 Sep (spec sheet 2.1); wire-node tail positions only
    motor_x=14.0,                      # stagger: +Y motor at +14, -Y motor at -14
    face_y=39.0,                       # faceplate (well inner wall outer face) |Y|
    cheek_wall=1.6, well_wall=1.2, seal_wall=3.0,
    well_clr_x=2.5, well_clr_y=2.0,
    # fan
    duct_x=57.0, duct_bore=43.3, collar_d=52.0, pcd=60.0, boss_d=8.5,
    fan_body_d=43.0, fan_lip_d=47.0, fan_h=49.0, seat_z=10.9, grille_d=46.0,   # v11.1: lip seat recessed into the roof (no collar)
    # battery
    bat_l=106.29, bat_w=34.39, bat_h=21.46, bat_clr=(110, 38, 24),
    bat_rear_x=-82.5,
    # electronics boxes (measured + clearance)
    ttgo=(62.3, 25.65, 11.4),   # MEASURED 62.3 x 25.65 x 6.88 (14.6 with pins); 11.4 = 6.88 + 4.5 pin stubs hanging between two cap rails
    drv=(26.0, 22.5, 10.5), buck=(15.0, 11.0, 8.5), pcf=(56.0, 16.6, 12.0),   # buck = MEASURED 13.86 x 9.95 x 7.84 + clearance (spec sheet 2.4); the full wiring guide part card says ~22 x 17 and is wrong
    esc=(43.0, 19.2, 6.1), cap_d=11.0, cap_h=18.0,
    tof=(24.78, 10.32, 3.18), tof_fov=25.0,
    tcrt=(10.2, 5.8, 7.0),      # bare TCRT5000 nominal (MEASURE)
    tcrt_face_z=2.2, tcrt_inset=37.8,   # v11.1: under the flat roof plate (was 28 = in the wedge skin, 7 mm pocket did not fit)
    xt60=(15.56, 8.13, 20.31), key=(16.47, 9.23, 10.6),
    alarm=(33.22, 25.72, 12.21), button_d=18.51, button_h=29.33,
)
AXLE_Z = P["wheel_od"] / 2          # identity
LEAN = math.tan(math.radians(P["lean_deg"]))

# ------------------------------------------------------------------ CURVES
def superellipse(a, n, k=720):
    t = np.linspace(0, 2 * math.pi, k, endpoint=False)
    c, s = np.cos(t), np.sin(t)
    x = a * np.sign(c) * np.abs(c) ** (2 / n)
    y = a * np.sign(s) * np.abs(s) ** (2 / n)
    return Polygon(np.c_[x, y])

RIM = superellipse(P["rim_a"], P["rim_n"])
def inset(d):
    """RIM offset d inward along the local normal (shapely erosion)."""
    return RIM.buffer(-d, join_style=1, resolution=32) if d > 0 else RIM

def tower_inset(z):
    """inset of the lid tower OUTER face at height z"""
    if z <= P["skirt_top"]:
        return P["skirt_out"]
    return P["skirt_out"] + (z - P["skirt_top"]) * LEAN
def tower_inner_inset(z):
    return tower_inset(z) + 2.0   # 2.0 mm skirt / tower wall

KNEE = inset(P["knee_inset"])
SEAL_OUT, SEAL_IN = inset(P["seal_out"]), inset(P["seal_in"])
SKIRT_IN = inset(P["skirt_in"])
TOP = inset(tower_inset(P["top_z"]))
LIP = inset(tower_inset(P["lip_z"]) - P["lip_proud"])

def diag_r(d):        # radius on the 45° diagonal at inset d
    return P["rim_a"] * 2 ** (0.5 - 1 / P["rim_n"]) - d

# ------------------------------------------------------------------ ENVELOPES
ENV = []   # dict(name, kind, poly, z0, z1, group, inside=(inset or None), note)
def add(name, poly, z0, z1, group, inside=None, note=""):
    ENV.append(dict(name=name, poly=poly, z0=z0, z1=z1, group=group, inside=inside, note=note))
def B(x0, x1, y0, y1): return sbox(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))
def C(x, y, d): return Point(x, y).buffer(d / 2, resolution=32)

# --- drive (+Y side built, -Y point-mirrored)
for sign in (+1, -1):
    tag = "L" if sign > 0 else "R"
    cx = sign * P["motor_x"]
    fy = sign * P["face_y"]
    r = P["motor_d"] / 2
    # motor body: from the faceplate inward along -sign*Y
    add(f"motor_{tag}", B(cx - r, cx + r, fy, fy - sign * P["motor_len"]),
        P["roof_top"], P["roof_top"] + P["motor_d"], "hardware", inside=P["skirt_in"],
        note="JGA25-371 body, rests on roof; axis Y at Z 23.40")
    # cheeks (two side walls + spine), open top
    add(f"cheeks_{tag}", B(cx - r - P["cheek_wall"], cx + r + P["cheek_wall"], fy, fy - sign * (P["motor_len"] + 1)),
        P["roof_top"], 33.0, "part", inside=P["skirt_in"], note="v11.1: part of the bolt-on motor/well carrier")
    # cable turn space at the tail
    tail = fy - sign * P["motor_len"]
    add(f"enc_cable_{tag}", B(cx - 8, cx + 8, tail, tail - sign * 5.0), 17.4, 29.4, "hardware",
        note="encoder connector/cable turn — only what fits before the opposite well wall")
    # wheel sweep
    wx0 = cx - P["wheel_od"] / 2; wx1 = cx + P["wheel_od"] / 2
    wy0 = fy + sign * (P["well_wall"] + 0.0); wy1 = wy0 + sign * P["hub_w"]
    hub_c = (wy0 + wy1) / 2
    add(f"wheel_{tag}", B(wx0, wx1, hub_c - sign * P["tyre_w"] / 2, hub_c + sign * P["tyre_w"] / 2),
        0.0, P["wheel_od"], "hardware", note=f"axle ({cx:.0f}, {hub_c:.1f}, {AXLE_Z:.2f})")
    # well interior (open to floor), walls to Z 39
    wix0 = cx - (P["wheel_od"] / 2 + P["well_clr_x"]); wix1 = cx + (P["wheel_od"] / 2 + P["well_clr_x"])
    wiy0 = fy; wiy1 = fy + sign * (P["tyre_w"] + 2 * P["well_clr_y"])
    add(f"well_int_{tag}", B(wix0, wix1, wiy0, wiy1), P["pan_z"], 39.0, "cavity")
    ow = P["well_wall"] + P["seal_wall"]
    add(f"well_outer_{tag}", B(wix0 - ow, wix1 + ow, wiy0 - sign * ow, wiy1 + sign * ow), P["pan_z"], P["roof_top"], "base",
        inside=P["knee_inset"], note="well seal wall (3.0) + inner wall, below the roof; its own skirt loop")
    ww = P["well_wall"]
    add(f"well_wall_{tag}", B(wix0 - ww, wix1 + ww, wiy0 - sign * ww, wiy1 + sign * ww), P["roof_top"], 39.0, "part",
        inside=P["skirt_in"], note="1.2 mm well wall above the roof (v11.1: carrier part); inboard face = motor faceplate")
    # v11.1: carrier flange (1.6 on the roof) + its four hanging bosses in the base, at the well corners just outside the seal wall
    cb = [(-19, 32), (47, 32), (-19, 77), (47, 77)]
    if sign < 0: cb = [(-x, -y) for x, y in cb]
    for k, (bxx, byy) in enumerate(cb):
        add(f"carrier_boss_{tag}{k}", C(bxx, byy, P["boss_d"]), P["pan_z"], P["roof_top"], "base", inside=P["skirt_in"] + 4.5,
            note="M3 pilot boss for the carrier flange")
    add(f"carrier_flange_{tag}", B(min(p[0] for p in cb) - 5, max(p[0] for p in cb) + 5, min(p[1] for p in cb) - 5, max(p[1] for p in cb) + 5).difference(B(wix0, wix1, wiy0, wiy1)),
        P["roof_top"], P["roof_top"] + 1.6, "part", inside=P["skirt_in"], note="carrier flange plate around the well")
    add(f"wellcap_{tag}", B(wix0 - ow - 1.4, wix1 + ow + 1.4, wiy0 - sign * (ow + 1.4), wiy1 + sign * (ow + 1.4)),
        36.0, 49.2, "part", inside=None, note="laps outside the well walls, EPDM on ledge")

# --- fan / duct
add("duct_boss", C(P["duct_x"], 0, 58.0), P["pan_z"], P["roof_top"], "base", inside=P["skirt_in"],
    note="v11.1: hanging boss below the roof carrying the R5 bellmouth + the lip counterbore; no collar above the roof")
add("duct_bore", C(P["duct_x"], 0, P["duct_bore"]), -1, P["seat_z"], "cavity")
for ang in (45, 135, 225, 315):
    bx = P["duct_x"] + P["pcd"] / 2 * math.cos(math.radians(ang)); by = P["pcd"] / 2 * math.sin(math.radians(ang))
    add(f"duct_boss_{ang}", C(bx, by, P["boss_d"]), P["pan_z"], P["roof_top"], "base", inside=P["skirt_in"])
for sgn in (+1, -1):
    add(f"knockout_{'L' if sgn > 0 else 'R'}", C(P["duct_x"], sgn * 36, 12.0), P["roof_top"] - 1.2, P["roof_top"], "base", note="0.6 membrane knock-out")
add("fan_body", C(P["duct_x"], 0, P["fan_body_d"]), P["seat_z"] - 3, P["seat_z"] - 3 + P["fan_h"], "hardware",
    note="lip seats 3 mm down in the collar top; motor end up")
_ring = C(P["duct_x"], 0, 56)
for ang in (45, 135, 225, 315):
    _ring = _ring.union(C(P["duct_x"] + P["pcd"] / 2 * math.cos(math.radians(ang)), P["pcd"] / 2 * math.sin(math.radians(ang)), P["boss_d"] + 1))
add("clamp_ring", _ring, P["seat_z"], P["seat_z"] + 3, "part", note="Ø56 ring + 4 bolt ears on PCD 60 (EDF ears cut off)")
add("fan_clear", C(P["duct_x"], 0, 45), P["seat_z"] + 3, P["top_z"] - P["top_skin"], "keepout")

# --- battery (on the roof, rear, long axis Y)
bx0 = P["bat_rear_x"]; bx1 = bx0 + P["bat_w"]
add("battery", B(bx0, bx1, -P["bat_l"] / 2, P["bat_l"] / 2), P["roof_top"], P["roof_top"] + P["bat_h"], "hardware",
    inside=P["skirt_in"], note="slides straight out -X through the rear slit, lid on")
cl = P["bat_clr"]
add("battery_clr", B(bx1 - cl[1], bx1, -cl[0] / 2, cl[0] / 2), P["roof_top"], P["roof_top"] + cl[2], "keepout",
    note="110 x 38 x 24 puff allowance, open to the rear")
for s in (+1, -1):
    add(f"bat_rail_{'L' if s > 0 else 'R'}", B(-70, bx1 + 1.6, s * (cl[0] / 2), s * (cl[0] / 2 + 1.6)),
        P["roof_top"], P["roof_top"] + 6, "part", inside=P["skirt_in"], note="guide rail, strap slots (v11.1: battery frame part)")
add("bat_stop", B(bx1, bx1 + 1.6, -cl[0] / 2, cl[0] / 2), P["roof_top"], P["roof_top"] + 8, "part", inside=P["skirt_in"])
# v11.1: battery frame bosses in the base
FRAME_BOSSES = [(-60, 58), (-60, -58), (-47, 0)]
for k, (bxx, byy) in enumerate(FRAME_BOSSES):
    add(f"frame_boss_{k}", C(bxx, byy, P["boss_d"]), P["pan_z"], P["roof_top"], "base", inside=P["skirt_in"] + 4.5, note="M3 pilot boss for the battery frame")

# --- XT60 loop key: base-mounted at the rear, key facing -X, beside the pack
xt = P["xt60"]
add("xt60_socket", B(-72, -72 + xt[2], 57.6, 57.6 + xt[0]), 15.0, 15.0 + xt[1], "hardware", inside=P["skirt_in"],
    note="panel socket on a base bracket, face at X -72 facing rearward; ridge inside; 21 mm behind")
add("xt60_key", B(-72, -72 - 11, 57.2, 57.2 + P["key"][0]), 14.5, 14.5 + P["key"][1], "hardware",
    note="loop key, pulls out rearward through the slit opening")

# --- roof electronics (Z 10.9 + 6 mm standoff + 2.74 board = 19.64 board face)
# v11.2: laid out for the drive-only build. See docstring.
BF = P["roof_top"] + 6 + 2.74
t = P["ttgo"]
add("TTGO", B(-40, -40 + t[0], -40, -40 - t[1]), 49.2, 49.2 + t[2], "hardware",  # X -40..22.3, Y -40..-65.65, Z 49.2..60.6
    inside=tower_inner_inset(61.2), note="on the -Y (RIGHT) wellcap top, display UP, header pins DOWN clipped to ~4 mm; wires soldered to the stubs; USB-C + 2 buttons at the +X end. Not glued in the drive-only build (lifted out to flash)")
d = P["drv"]
# guide "Board B": bucks + diode + rails, front-right, hot-glued hole-side-up. 51 x 30 (20 columns of 2.54): X 29 clears the left motor cheek (to X 28.1), X 80 is the rim; 60 x 24 cols does not fit here.
add("board_B", B(29, 80, -29, -59), P["roof_top"], BF, "part", inside=P["skirt_in"],
    note="WIRING GUIDE Board B: 12V/5V/GND/3V3 rails (top bank, inboard edge Y -33), ENC-L/ENC-R/B5V points (bottom bank, outboard edge Y -55), Buck 1 at cols 15-20. Column 1 at the -X (rear) end. Hot-glued; pilots A land inside it if screws are wanted")
add("DRV8871_R", B(24.5, 24.5 + d[0], -60, -60 - d[1]), BF, BF + d[2], "hardware", inside=P["skirt_in"],
    note="WIRING GUIDE Driver R: beside Board B, outboard, hot-glued on its back. Own 20 AWG pair to the Star")
add("DRV8871_L", B(-41, -41 + d[0], 46, 46 + d[1]), BF, BF + d[2], "hardware", inside=P["skirt_in"],
    note="WIRING GUIDE Driver L: rear-left, hot-glued straight to the roof (no Board A in the drive-only build)")
b = P["buck"]
add("buck", B(64, 64 + b[0], -31, -31 - b[1]), BF, BF + b[2], "hardware", inside=P["skirt_in"],
    note="Buck 1 (5 V) on Board B cols 15-20, top-bank side, OUT pads toward col 15. Buck 2 (3V3L, lid stage) goes on the bottom-bank side of the same columns")
# the Star: two solder blobs, 14 AWG in, 20 AWG out. Old 'bus_block' footprint. Star + nearer the key socket.
add("star_plus", C(-37, 35, 12), P["roof_top"], P["roof_top"] + 14, "part", inside=P["skirt_in"],
    note="Star + blob: five wires + Bus Cap. Hot-glued, 12 mm heatshrink")
add("star_minus", C(-37, 5, 12), P["roof_top"], P["roof_top"] + 14, "part", inside=P["skirt_in"],
    note="Star - blob: six wires + Bus Cap. 30 mm from Star +, along Y")
add("cap_bus", C(-37, 20, P["cap_d"]), P["roof_top"], P["roof_top"] + P["cap_h"], "hardware", inside=P["skirt_in"],
    note="1000 uF Bus Cap between the blobs, legs ~9 mm to each")
e = P["esc"]
add("ESC", B(-16, -16 + e[0], 41, 41 + e[1]), 49.2, 49.2 + e[2], "hardware", inside=None,
    note="VHB + zip tie on the +Y (LEFT) wellcap top; thick leads exit -X toward the Star (80 mm, only just reach); 3 motor pads at the +X end, taped over in the drive-only build")
xt = P["xt60"]
add("pack_socket", B(-39.5, -24.5, 70, 78), P["roof_top"], P["roof_top"] + 20.3, "hardware", inside=P["skirt_in"],
    note="DRIVE-ONLY SUGGESTION, to confirm: XT60E-M Pack Socket epoxied/zip-tied on the roof rear-left, outboard of Driver L, lying on its side with the opening toward -X (rear) so the pack's own 132 mm plug reaches it. Tabs toward +X. 20 mm clear of the Key Socket's body")
al = P["alarm"]
add("alarm_roof", B(-80, -80 + al[0], -13, -13 + al[1]), P["roof_top"] + P["bat_h"] + 0.1, P["roof_top"] + P["bat_h"] + 0.1 + al[2], "hardware", inside=P["skirt_in"],
    note="DRIVE-ONLY BUILD: LiPo alarm strapped/taped flat ON TOP of the pack, display up, buzzer clear. No lid in this build so nothing is above the pack. Comes off with the pack; moves to the lid pocket at the lid stage")
add("pressure_port", C(-30, -10, 6), P["pan_z"], P["roof_top"], "base", note="M3 sealed test port")
# v11.1: board / bus-block pilot bosses (hanging, Ø8.5) — 8 mm inboard of the board corners
BOARD_PILOTS = {"A": [(31, -50), (62, -50), (31, -41), (62, -41)], "B": [(-36.5, 47), (-26, 47), (-36.5, 56), (-26, 56)],
                "bus": [(-42, 22.5), (-31, 34.5)]}
for grp, pts in BOARD_PILOTS.items():
    for k, (bxx, byy) in enumerate(pts):
        add(f"pilot_{grp}{k}", C(bxx, byy, P["boss_d"]), P["pan_z"], P["roof_top"], "base", inside=P["skirt_in"] + 4.5)

# --- lid furniture (flat top at Z 65.6; positions are plan XY)
add("grille", C(P["duct_x"], 0, P["grille_d"]), P["top_z"] - 2, P["top_z"], "lid", inside=tower_inset(P["top_z"]))
add("ttgo_window", B(-40 - 1, -40 + t[0] + 1, -40 + 1, -40 - t[1] - 1), P["top_z"] - 2, P["top_z"], "lid", inside=tower_inset(P["top_z"]),
    note="acetate cover, 1 mm ledge")
al = P["alarm"]
add("alarm_pocket", B(-58, -58 + al[0] + 1, 21, 21 + al[1] + 1.3), P["top_z"] - P["top_skin"] - 13, P["top_z"] - P["top_skin"], "lid",
    inside=tower_inner_inset(P["top_z"] - 14), note="hangs from the flat top; window + 2x vents + finger hole above")
add("button_col", C(-38, 10, 20), 36.5, P["top_z"], "keepout", inside=tower_inner_inset(P["top_z"]),
    note="Ø18.7 hole in a Ø26 pad; 29.3 mm body below")
add("group_panel", B(-35, 25, 49, 74), P["top_z"] - 0.6, P["top_z"], "lid", inside=tower_inset(P["top_z"]), note="60 x 25 x 0.6 recess — RULE R7")
pc = P["pcf"]
add("PCF8574_lid", B(-80, -80 + pc[0], -5, -5 - pc[1]), P["top_z"] - P["top_skin"] - pc[2], P["top_z"] - P["top_skin"], "hardware",
    inside=tower_inner_inset(P["top_z"] - 13), note="in the lid: 7 XSHUT + start button; one 4-wire JST-XH to the base")
add("gland", C(-10, 5, 10), P["top_z"] - 2, P["top_z"], "lid", inside=tower_inset(P["top_z"]), note="the ONLY base<->lid harness hole")
add("led_opt", C(30, -72, 5.2), P["top_z"] - 2, P["top_z"], "lid", inside=tower_inset(P["top_z"]), note="optional LED (display satisfies R6)")

# --- ToF: facet nose blocks on the tower, front 0/±25, sides ±90, rear 180±25
TOFS = []
def tof_at(yaw_deg, z, tag):
    """place a ToF on the tower outer face at bearing yaw (deg from +X), optical axis = yaw"""
    r = math.radians(yaw_deg)
    # find the tower outer surface point along the bearing
    ins = tower_inset(z)
    poly = inset(ins)
    far = Point(300 * math.cos(r), 300 * math.sin(r))
    from shapely.geometry import LineString
    seg = LineString([(0, 0), (far.x, far.y)]).intersection(poly.exterior)
    p = seg if seg.geom_type == "Point" else list(seg.geoms)[-1]
    TOFS.append(dict(tag=tag, yaw=yaw_deg, x=round(p.x, 2), y=round(p.y, 2), z=z))
    # pocket: 12 wide x 26 tall x 4 deep behind the facet (board long axis vertical)
    w = 12.0; dep = 4.5
    ux, uy = math.cos(r), math.sin(r); vx, vy = -uy, ux
    pts = [(p.x + vx * w / 2, p.y + vy * w / 2), (p.x - vx * w / 2, p.y - vy * w / 2),
           (p.x - vx * w / 2 - ux * dep, p.y - vy * w / 2 - uy * dep), (p.x + vx * w / 2 - ux * dep, p.y + vy * w / 2 - uy * dep)]
    add(f"tof_{tag}", Polygon(pts), z - 13, z + 13, "lid", note=f"yaw {yaw_deg}")
for yaw, tag in ((0, "F0"), (25, "F+25"), (-25, "F-25"), (90, "L90"), (-90, "R90"), (155, "B+25"), (-155, "B-25")):
    tof_at(yaw, 50.0 if abs(yaw) > 100 else 48.0, tag)

# --- line sensors: bare TCRT5000 in the wedge underside on the diagonals
TCRT = []
for sx in (+1, -1):
    for sy in (+1, -1):
        rr = diag_r(P["tcrt_inset"]) / math.sqrt(2)
        x, y = sx * rr, sy * rr
        s = P["tcrt"]
        add(f"tcrt_{'F' if sx>0 else 'B'}{'L' if sy>0 else 'R'}", C(x, y, 12.0), P["tcrt_face_z"], P["tcrt_face_z"] + s[2], "hardware",
            note="pocket open downward in the plenum ceiling, face at Z 2.2, wire hole inboard of the knee")
        TCRT.append(dict(x=round(x, 2), y=round(y, 2)))

# --- lid fixings
LIDFIX = [(70, 70), (-46, 72), (-50, -73), (70, -70)]
for i, (x, y) in enumerate(LIDFIX):
    add(f"lidfix_{i}", C(x, y, P["boss_d"]), P["pan_z"], P["roof_top"], "base", inside=P["skirt_in"] + 4.5,
        note="M3 insert boss hanging below the roof; lid lug 16x16 above")
    add(f"lidlug_{i}", B(x - 6, x + 6, y - 6, y + 6), P["roof_top"], P["roof_top"] + 3, "lid", inside=P["skirt_in"])

# --- rear slit (through collar + skirt + tower) for the battery and the key
add("rear_slit", B(-95, -75, -58, 75), P["roof_top"], 34.0, "cavity", note="opening in collar/skirt/tower: pack + key pass through")

# ------------------------------------------------------------------ CHECKS
DECLARED = {("motor_L", "cheeks_L"), ("motor_R", "cheeks_R"), ("enc_cable_L", "cheeks_L"), ("enc_cable_R", "cheeks_R"),
            ("wheel_L", "well_int_L"), ("wheel_R", "well_int_R"), ("well_int_L", "well_outer_L"), ("well_int_R", "well_outer_R"),
            ("well_outer_L", "wellcap_L"), ("well_outer_R", "wellcap_R"), ("well_int_L", "wellcap_L"), ("well_int_R", "wellcap_R"),
            ("duct_bore", "duct_collar"), ("fan_body", "duct_bore"), ("fan_body", "duct_collar"), ("clamp_ring", "fan_body"),
            ("clamp_ring", "fan_clear"), ("fan_body", "fan_clear"), ("battery", "battery_clr"), ("grille", "fan_clear"),
            ("battery_clr", "bat_rail_L"), ("battery_clr", "bat_rail_R"), ("battery_clr", "bat_stop"), ("battery", "rear_slit"),
            ("battery_clr", "rear_slit"), ("xt60_key", "rear_slit"), ("xt60_socket", "rear_slit"), ("xt60_key", "xt60_socket"),
            ("ESC", "wellcap_L"), ("board_B", "buck"), ("star_plus", "cap_bus"), ("star_minus", "cap_bus"), 
            ("duct_collar", "duct_boss_45"), ("duct_collar", "duct_boss_135"),
            ("duct_collar", "duct_boss_225"), ("duct_collar", "duct_boss_315"), ("clamp_ring", "duct_boss_45"),
            ("clamp_ring", "duct_boss_135"), ("clamp_ring", "duct_boss_225"), ("clamp_ring", "duct_boss_315"),
            ("grille", "ttgo_window"), ("cheeks_L", "cheeks_R"), ("wheel_L", "well_outer_L"), ("wheel_R", "well_outer_R"),
            ("wheel_L", "wellcap_L"), ("wheel_R", "wellcap_R"), ("wheel_L", "well_wall_L"), ("wheel_R", "well_wall_R"),
            ("motor_L", "well_wall_L"), ("motor_R", "well_wall_R"), ("cheeks_L", "well_wall_L"), ("cheeks_R", "well_wall_R"),
            ("well_int_L", "well_wall_L"), ("well_int_R", "well_wall_R"), ("well_wall_L", "wellcap_L"), ("well_wall_R", "wellcap_R"),
            ("TTGO", "ttgo_window"), ("TTGO", "wellcap_R"), ("well_outer_L", "well_wall_L"), ("well_outer_R", "well_wall_R"),
            ("motor_L", "enc_cable_L"), ("motor_R", "enc_cable_R"), ("motor_L", "well_int_L"), ("motor_R", "well_int_R"),
            ("cheeks_L", "well_int_L"), ("cheeks_R", "well_int_R"), ("battery", "bat_stop"), ("bat_rail_L", "bat_stop"), ("bat_rail_R", "bat_stop"),
            # v11.1 declared: carrier flange laps its own bosses / seal wall / cheeks / well wall; duct boss merges its 4 pilot bosses; frame bosses under rails/stop
            ("alarm_roof", "battery_clr"), ("alarm_roof", "button_col"), ("alarm_roof", "rear_slit"), ("board_B", "pilot_A0"), ("board_B", "pilot_A1"), ("board_B", "pilot_A2"), ("board_B", "pilot_A3"), ("carrier_flange_L", "well_outer_L"), ("carrier_flange_R", "well_outer_R"), ("carrier_flange_L", "well_wall_L"), ("carrier_flange_R", "well_wall_R"),
            ("carrier_flange_L", "cheeks_L"), ("carrier_flange_R", "cheeks_R"), ("carrier_flange_L", "cheeks_R"), ("carrier_flange_R", "cheeks_L"),
            ("carrier_flange_L", "carrier_flange_R"), ("carrier_flange_L", "motor_R"), ("carrier_flange_R", "motor_L"), ("carrier_flange_L", "enc_cable_R"), ("carrier_flange_R", "enc_cable_L"),
            ("duct_boss", "duct_boss_45"), ("duct_boss", "duct_boss_135"), ("duct_boss", "duct_boss_225"), ("duct_boss", "duct_boss_315"), ("duct_boss", "duct_bore"),
            ("clamp_ring", "duct_boss"), ("fan_body", "duct_boss"), ("frame_boss_0", "bat_rail_L"), ("frame_boss_1", "bat_rail_R"), ("frame_boss_2", "bat_stop"),
            ("frame_boss_2", "battery_clr"), ("knockout_L", "duct_boss"), ("knockout_R", "duct_boss")} | {(f"carrier_boss_{t}{k}", f"carrier_flange_{t}") for t in "LR" for k in range(4)} \
           | {(f"carrier_boss_{t}{k}", f"well_outer_{t}") for t in "LR" for k in range(4)}
def zover(a, b): return min(a["z1"], b["z1"]) - max(a["z0"], b["z0"]) > 0.01
MIN_GAP = 0.8
overlaps, near = [], []
for i in range(len(ENV)):
    for j in range(i + 1, len(ENV)):
        a, b = ENV[i], ENV[j]
        if (a["name"], b["name"]) in DECLARED or (b["name"], a["name"]) in DECLARED: continue
        if not zover(a, b): continue
        if a["group"] == "keepout" and b["group"] == "keepout": continue
        inter = a["poly"].intersection(b["poly"]).area
        if inter > 0.01:
            overlaps.append((a["name"], b["name"], round(inter, 1)))
        else:
            dmin = a["poly"].distance(b["poly"])
            if dmin < MIN_GAP: near.append((a["name"], b["name"], round(dmin, 2)))
outside = []
for e in ENV:
    if e["inside"] is None: continue
    if not inset(e["inside"]).contains(e["poly"]):
        d = e["poly"].difference(inset(e["inside"]))
        outside.append((e["name"], e["inside"], round(d.area, 1)))

# wheel-to-well clearances
def clr(a, b): return round(next(x for x in ENV if x["name"] == a)["poly"].exterior.distance(next(x for x in ENV if x["name"] == b)["poly"].exterior), 2)
# plenum area
plenum = SEAL_OUT
for e in ENV:
    if e["name"].startswith("well_outer"): plenum = plenum.difference(e["poly"])
area_sealed = plenum.area
res = dict(
    overlaps=overlaps, near_misses=near, outside_curve=outside,
    sealed_area_mm2=round(area_sealed, 0), plan_area_mm2=round(RIM.area, 0),
    downforce_N={pa: round(pa * area_sealed * 1e-6, 1) for pa in (200, 400, 800)},
    axle_z=AXLE_Z, motor_bottom_minus_roof=round(AXLE_Z - P["motor_d"] / 2 - P["roof_top"], 2),
    tof=TOFS, tcrt=TCRT, lip_widest_inset=round(tower_inset(P["lip_z"]) - P["lip_proud"], 2),
    flat_top_axis_semi=round(P["rim_a"] - tower_inset(P["top_z"]), 1),
    motor_tail_gap_to_opposite_wall=round(P["face_y"] - P["motor_len"] - (-P["face_y"] + P["well_wall"]) if False else (2 * P["face_y"] - P["motor_len"] - P["well_wall"]), 2),
)
json.dump(res, open("checks.json", "w"), indent=1)


# ------------------------------------------------------------------ INTERFACES
IF = dict(
    frame="mm, +X front, +Y left, Z0 arena floor", rim=dict(a=P["rim_a"], n=P["rim_n"], diag_r=round(diag_r(0), 2)),
    z=dict(rim=P["rim_z"], pan=P["pan_z"], roof_top=P["roof_top"], collar_top=P["collar_top"], skirt_top=P["skirt_top"],
           lip=P["lip_z"], top=P["top_z"], axle=AXLE_Z, motor_top=P["roof_top"] + P["motor_d"], fan_top=P["seat_z"] - 3 + P["fan_h"]),
    insets=dict(seal_out=P["seal_out"], seal_in=P["seal_in"], knee=P["knee_inset"], collar_in=P["collar_in"],
                skirt_out=P["skirt_out"], skirt_in=P["skirt_in"], lip_widest=res["lip_widest_inset"],
                flat_top=round(tower_inset(P["top_z"]), 2)),
    lean_deg=P["lean_deg"], lip_proud=P["lip_proud"],
    wheels={t: dict(axle=[e["note"]]) for t, e in (("L", ENV[[x["name"] for x in ENV].index("wheel_L")]), ("R", ENV[[x["name"] for x in ENV].index("wheel_R")]))},
    wells={t: list(np.round(next(x for x in ENV if x["name"] == f"well_int_{t}")["poly"].bounds, 2)) for t in ("L", "R")},
    duct=dict(x=P["duct_x"], y=0, bore=P["duct_bore"], collar_d=P["collar_d"], pcd=P["pcd"], bolt_deg=[45, 135, 225, 315], seat_z=P["seat_z"]),
    battery=dict(pack_bounds=list(np.round(next(x for x in ENV if x["name"] == "battery")["poly"].bounds, 2)), floor_z=P["roof_top"],
                 slit=dict(y=[-58, 75], z=[P["roof_top"], 34.0])),
    xt60=dict(face_x=-72, y=[57.6, 73.16], z=[15, 23.13]),
    lid_fixings=LIDFIX, tof=TOFS, tcrt=TCRT, hole_shrink=P["hole_shrink"],
    architecture_note="Base carries NOTHING above the roof plane Z 10.9 (prints roof-face-down, no support under the roof). Well walls + cheeks = 2 bolt-on carriers; rails + stop + XT60 bracket = 1 battery frame; fan lip seat recessed into a roof boss; no collar.",
    carrier_bosses=dict(L=[[-19, 32], [47, 32], [-19, 77], [47, 77]], R=[[-47, -32], [19, -32], [-47, -77], [19, -77]],
                        note="Ø8.5 hanging bosses, Ø4.15x6 pilots, at the well corners just outside the seal wall — CAD session to confirm against ribs/bosses"),
    battery_frame_bosses=[list(p) for p in FRAME_BOSSES],
    board_pilots=BOARD_PILOTS,
    ttgo=dict(board_mm=[62.3, 25.65, 6.88], with_pins_mm=14.6, status="MEASURED 12 Sep",
              mount="-Y wellcap top, display up, pins down clipped to ~4 mm between two 4.5 mm cap rails"),
)
json.dump(IF, open("interfaces.json", "w"), indent=1)

# ------------------------------------------------------------------ RENDER
COL = dict(base="#4a6", cavity="#ddd", part="#39c", hardware="#e84", keepout="#fc0", lid="#a6c")
def draw(ax, groups, curves, title):
    for c, lab, st in curves:
        xs, ys = c.exterior.xy; ax.plot(xs, ys, st, lw=1, label=lab)
    for e in ENV:
        if e["group"] not in groups: continue
        p = e["poly"]; xs, ys = p.exterior.xy
        ax.fill(xs, ys, color=COL[e["group"]], alpha=0.35, ec=COL[e["group"]], lw=1)
        cx, cy = p.centroid.x, p.centroid.y
        ax.text(cx, cy, e["name"], fontsize=5, ha="center", va="center")
    ax.set_aspect("equal"); ax.set_xlim(-135, 135); ax.set_ylim(-135, 135); ax.grid(alpha=.2)
    ax.set_title(title, fontsize=9); ax.legend(fontsize=6, loc="lower left")
    ax.axhline(0, color="k", lw=.3); ax.axvline(0, color="k", lw=.3)
    ax.text(120, 0, "FRONT +X", fontsize=7, rotation=90, va="center")

LIDSIDE = {"PCF8574_lid", "button_col", "alarm_pocket", "grille", "ttgo_window", "group_panel", "gland", "led_opt", "fan_clear"} | {e["name"] for e in ENV if e["name"].startswith("tof_") or e["name"].startswith("lidlug")}
def draw2(ax, pick, curves, title, cones=False):
    for c, lab, st in curves:
        xs, ys = c.exterior.xy; ax.plot(xs, ys, st, lw=1, label=lab)
    for e in ENV:
        if not pick(e): continue
        p = e["poly"]; xs, ys = p.exterior.xy
        ax.fill(xs, ys, color=COL[e["group"]], alpha=0.35, ec=COL[e["group"]], lw=1)
        ax.text(p.centroid.x, p.centroid.y, e["name"], fontsize=5.5, ha="center", va="center")
    if cones:
        for tf in TOFS:
            r = math.radians(tf["yaw"]); h = math.radians(P["tof_fov"] / 2)
            for sg in (-1, 1):
                ax.plot([tf["x"], tf["x"] + 70 * math.cos(r + sg * h)], [tf["y"], tf["y"] + 70 * math.sin(r + sg * h)], "m-", lw=.5)
    ax.set_aspect("equal"); ax.set_xlim(-135, 135); ax.set_ylim(-135, 135); ax.grid(alpha=.2)
    ax.set_title(title, fontsize=10); ax.legend(fontsize=6, loc="lower left")
    ax.axhline(0, color="k", lw=.3); ax.axvline(0, color="k", lw=.3)
    ax.annotate("FRONT +X", xy=(118, 118), fontsize=8, ha="right")

fig, axs = plt.subplots(1, 3, figsize=(27, 9.5))
draw2(axs[0], lambda e: e["group"] in ("base", "cavity") and e["name"] not in LIDSIDE,
      [(RIM, "rim 249", "k-"), (SEAL_OUT, "seal outer (inset 20)", "r--"), (SEAL_IN, "seal inner (23)", "r:"), (KNEE, "knee (inset 34)", "g-")],
      "1. BASE — printed features only (plan)")
draw2(axs[1], lambda e: e["group"] in ("hardware", "part", "keepout", "cavity") and e["name"] not in LIDSIDE,
      [(RIM, "rim", "k-"), (KNEE, "knee", "g-"), (SKIRT_IN, "lid skirt inner (38.4)", "b:")],
      "2. HARDWARE on the base, lid off")
draw2(axs[2], lambda e: e["name"] in LIDSIDE,
      [(RIM, "rim", "k-"), (KNEE, "knee", "g-"), (LIP, "anti-climb lip, widest", "m-"), (TOP, "flat top edge", "b-")],
      "3. LID — flat-top furniture, ToF facets (25° cones), lip", cones=True)
plt.tight_layout(); plt.savefig("plan.png", dpi=140); plt.close()

# Z-stack (side view, X-Z at Y=0 and Y=+55)
fig, ax = plt.subplots(figsize=(16, 6))
def zbox(e, color, alpha=.35):
    b = e["poly"].bounds
    ax.add_patch(Rectangle((b[0], e["z0"]), b[2] - b[0], e["z1"] - e["z0"], fc=color, ec=color, alpha=alpha, lw=.8))
    ax.text((b[0] + b[2]) / 2, (e["z0"] + e["z1"]) / 2, e["name"], fontsize=5, ha="center", va="center")
for e in ENV:
    if e["group"] in ("base", "hardware", "part", "lid", "keepout") and e["name"] not in ("rear_slit",):
        zbox(e, COL[e["group"]])
# hull profile on the X axis
a = P["rim_a"]; k = a - P["knee_inset"]
xs = np.linspace(-a, a, 400)
def hull(x):
    d = a - abs(x)
    if d <= 0: return P["rim_z"]
    if d < P["knee_inset"]: return P["rim_z"] + 1.2 + d * math.tan(math.radians(P["wedge_deg"]))
    return P["roof_top"]
ax.plot(xs, [hull(x) for x in xs], "k-", lw=1.5, label="wedge/roof (X axis)")
# tower profile
for sgn in (-1, 1):
    zz = np.linspace(P["roof_top"], P["top_z"], 50)
    ax.plot([sgn * (a - tower_inset(z)) for z in zz], zz, "b-", lw=1.5)
    ax.plot([sgn * (a - res["lip_widest_inset"]), sgn * (a - tower_inset(P["lip_z"]))], [P["lip_z"], P["lip_z"]], "m-", lw=2)
ax.plot([-a + tower_inset(P["top_z"]), a - tower_inset(P["top_z"])], [P["top_z"], P["top_z"]], "b-", lw=1.5, label="lid tower / flat top")
ax.axhline(0, color="k", lw=.5); ax.axhline(P["roof_top"], color="g", lw=.5, ls="--", label="roof top / knee Z 10.9")
ax.set_xlim(-135, 135); ax.set_ylim(-5, 75); ax.set_aspect("equal"); ax.grid(alpha=.2); ax.legend(fontsize=7)
ax.set_title("Z-STACK, side view (+X right). Boxes = envelope X-extent x Z-extent (not sectioned)", fontsize=9)
plt.tight_layout(); plt.savefig("zstack.png", dpi=150); plt.close()

print(json.dumps(res, indent=1))
