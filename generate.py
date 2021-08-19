import fontforge
import psMat
from fontTools.ttLib import TTFont
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('weight')
parser.add_argument('shs_path')
parser.add_argument('fira_path')
args = parser.parse_args(sys.argv[1:])

familyname = 'Firsh'
weight = args.weight
version = '1.100'
copyright = 'Copyright 2021 negset'

shs_path = args.shs_path
fira_path = args.fira_path
firple_path = '{}-{}.ttf'.format(familyname, weight)

shs = fontforge.open(shs_path)
fira = fontforge.open(fira_path)

scale = 1.9
half_width = fira['A'].width
full_width = half_width * 2
overwrite_glyphs = ['「', '」']

print('### {} {} ###'.format(familyname, weight))

print('# Copying glyphs...')
for i in range(0x10ffff + 1):
    if shs.__contains__(i) and not fira.__contains__(i):
        shs.selection.select(i)
        fira.selection.select(i)
        shs.copy()
        fira.paste()
for glyph in overwrite_glyphs:
    shs.selection.select(ord(glyph))
    fira.selection.select(ord(glyph))
    shs.copy()
    fira.paste()

print('# Transforming glyphs...')
fira.selection.changed()
for glyph in fira.selection.byGlyphs:
    w = full_width if glyph.width * scale > half_width else half_width
    x = (w - glyph.width * scale) / 2
    glyph.transform(psMat.scale(scale))
    glyph.transform(psMat.translate(x, 0))
    glyph.width = w

print('# Setting font parameters...')
fira.familyname = familyname
fira.fontname = '{}-{}'.format(familyname, weight)
fira.fullname = '{} {}'.format(familyname, weight)
fira.weight = weight
fira.version = version
fira.copyright = '{}\n{}\n{}'.format(copyright, fira.copyright, shs.copyright)
fira.sfntRevision = None
fira.appendSFNTName('English (US)', 'UniqueID', '{};{}-{}'.format(version, familyname, weight))
fira.appendSFNTName('English (US)', 'Version', 'Version {}'.format(version))
fira.os2_unicoderanges = (-268434689, 1809841663, 33554454, 0)
fira.os2_codepages = (1613627807, 0)

print('# Generating fonts...')
fira.generate(firple_path)

print('# Fixing char width...')
fira = TTFont(fira_path)
firple = TTFont(firple_path)
firple['OS/2'].xAvgCharWidth = fira['OS/2'].xAvgCharWidth
firple.save(firple_path)