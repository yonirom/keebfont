import fontforge
import os
import sys

SIZE = 13

print(f"Called on {sys.argv[1]} {sys.argv[2]}")
ff = fontforge.open(sys.argv[1])
ff = ff.removeOverlap()
ff.em = 2048
for g in ff.selection.all():
    try:
        ff[g].width = 1000
    except:
        pass
ff.generate(sys.argv[2])
sized_file = sys.argv[2].replace(".bdf", f"-{SIZE}.bdf")
try:
    os.rename(sized_file, sys.argv[2])
except:
    pass
