import fontforge
import os
import sys

SIZE = 13

ff = fontforge.open(sys.argv[1])
ff.generate(sys.argv[2])
sized_file = sys.argv[2].replace(".bdf", f"-{SIZE}.bdf")
try:
    os.rename(sized_file, sys.argv[2])
except: 
    pass
