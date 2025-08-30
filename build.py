import ipdb
from bdflib import reader, writer, effects


fixed6x13 = reader.read_bdf(open('src/6x13.bdf', "rb"))

fixed6x13b = reader.read_bdf(open('src/6x13B.bdf', "rb"))

fixed6x13bfull = effects.merge(fixed6x13, fixed6x13b)

fixed6x13bfull.properties[b'WEIGHT_NAME'] = b'Bold'

fixed6x13o = reader.read_bdf(open('src/6x13O.bdf', "rb"))

fixed6x13ifull = effects.merge(fixed6x13, fixed6x13o)

fixed6x13ifull.properties[b'WEIGHT_NAME'] = b'Italic'


for g in fixed6x13.glyphs:
    g.bbY += 1

for g in fixed6x13ifull.glyphs:
    g.bbY += 1

for g in fixed6x13bfull.glyphs:
    g.bbY += 1
# writer.write_bdf(, open("keeb.bdf", "wb"))


cozette = reader.read_bdf(open('tmp/Cozette.bdf', "rb"))

myglyphs = reader.read_bdf(open('tmp/Keebglyphs.bdf', "rb"))


cozette_with_new_glyphs = effects.merge(cozette, myglyphs)

writer.write_bdf(cozette_with_new_glyphs, open("tmp/merged.bdf", "wb"))

writer.write_bdf(effects.merge(cozette_with_new_glyphs,
                 fixed6x13), open("build/Keeb.bdf", "wb"))
writer.write_bdf(effects.merge(cozette_with_new_glyphs,
                 fixed6x13bfull), open("build/KeebBold.bdf", "wb"))
writer.write_bdf(effects.merge(cozette_with_new_glyphs,
                 fixed6x13ifull), open("build/KeebItalic.bdf", "wb"))
