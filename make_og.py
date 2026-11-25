#!/usr/bin/env python3
"""og.png — 1200x630 share-card art for lacumis-cowffee. PIL, system serif fonts
(glob-resolved like sibling sites). Cow-print spot bands top/bottom, crema field,
mazapan gold rules. Shop identity only — no builder tokens (gate-checked)."""
import glob, re
from PIL import Image, ImageDraw, ImageFont

def find(pat):
    hits = glob.glob(pat)
    return hits[0] if hits else None

SERIF = find('/System/Library/Fonts/*Iowan*') or find('/System/Library/Fonts/Supplemental/Palatino*') or find('/System/Library/Fonts/Supplemental/Times*') or find('/System/Library/Fonts/Supplemental/Georgia*')
SANS = find('/System/Library/Fonts/*Futura*') or find('/System/Library/Fonts/Supplemental/*Helvetica*') or find('/System/Library/Fonts/Helvetica*') or SERIF
if not SERIF or not SANS:
    raise SystemExit('no fonts found for og render')
print('fonts:', SERIF, '|', SANS)

W, H = 1200, 630
INK = (35, 22, 17)
CREMA = (247, 239, 226)
ORO = (201, 143, 60)
ORO_DARK = (138, 95, 34)
ROJO = (184, 66, 46)
SAND = (138, 122, 99)

im = Image.new('RGB', (W, H), CREMA)
d = ImageDraw.Draw(im)

def font(path, size):
    return ImageFont.truetype(path, size)

def cowband(y, h):
    d.rectangle([0, y, W, y + h], fill=INK)
    for (cx, cy, rx, ry) in [
        (70, y + 9, 46, 16), (250, y + h - 12, 34, 12), (430, y + 7, 26, 10),
        (620, y + h - 10, 52, 15), (830, y + 8, 30, 12), (1010, y + h - 13, 44, 14), (1160, y + 6, 22, 9),
    ]:
        d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=CREMA)

BAND = 34
cowband(0, BAND)
cowband(H - BAND, BAND)

k = font(SANS, 27)
d.text((72, 86), 'WICHITA  KS  ·  MEXICAN-STYLE  COFFEES  ·  HOMEMADE  MEXICAN  PAN', font=k, fill=ORO_DARK)

s1 = font(SERIF, 104)
d.text((72, 140), 'La Cumis', font=s1, fill=INK)
d.text((72, 250), 'Cowffee', font=s1, fill=ROJO)

d.rectangle([72, 398, 402, 403], fill=ORO)

b = font(SERIF, 37)
d.text((72, 424), 'Mazapán lattes, Mexican mocha, banana lattes,', font=b, fill=INK)
d.text((72, 472), 'conchas, gorditas & croissants — opening now on 21st Street.', font=b, fill=INK)

t = font(SANS, 25)
d.text((72, 540), 'Opening now — 2040 W 21st St. N · (316) 737-7120', font=t, fill=SAND)

out = __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), 'public', 'og.png')
im.save(out, 'PNG')
print('wrote', out)
