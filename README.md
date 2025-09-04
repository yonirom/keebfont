# KeebFont
Fixed 6x13 patched with NERD/Powerline glyphs

This font is a merge of multiple fonts with each overwriting the glyphs from the previous font.

It starts out with Cozette and patches a few missing icon glyphs from the custom keebglyphs.sfd, this result is patched with fixed6x13 (or a merge of fixed bold/italic)

This font tries to acheive pixel perfect scaling in both bitmap and outline formats (scaling this font with a non 2x multiplier will display badly).

```
=== Keeb.ttf ===
Version 001.000
SHA1: 44b02ec8ca8d22de77b9b1ea12f82c38c7c08f85

::::::::::::::::::::::::::::::::::::::::::::::::::
  Metrics
::::::::::::::::::::::::::::::::::::::::::::::::::
[head] Units per Em:   2048
[head] yMax:           1733
[head] yMin:          -316
[OS/2] CapHeight:      1417
[OS/2] xHeight:        945
[OS/2] TypoAscender:   1733
[OS/2] TypoDescender: -315
[OS/2] WinAscent:      1733
[OS/2] WinDescent:     316
[hhea] Ascent:         1733
[hhea] Descent:       -316

[hhea] LineGap:        0
[OS/2] TypoLineGap:    0

::::::::::::::::::::::::::::::::::::::::::::::::::
  Ascent to Descent Calculations
::::::::::::::::::::::::::::::::::::::::::::::::::
[hhea] Ascent to Descent:              2049
[OS/2] TypoAscender to TypoDescender:  2048
[OS/2] WinAscent to WinDescent:        2049

::::::::::::::::::::::::::::::::::::::::::::::::::
  Delta Values
::::::::::::::::::::::::::::::::::::::::::::::::::
[hhea] Ascent to [OS/2] TypoAscender:       0
[hhea] Descent to [OS/2] TypoDescender:     1
[OS/2] WinAscent to [OS/2] TypoAscender:    0
[OS/2] WinDescent to [OS/2] TypoDescender:  1

::::::::::::::::::::::::::::::::::::::::::::::::::
  Baseline to Baseline Distances
::::::::::::::::::::::::::::::::::::::::::::::::::
hhea metrics: 2049
typo metrics: 2048
win metrics:  2049

[OS/2] fsSelection USE_TYPO_METRICS bit set: True

::::::::::::::::::::::::::::::::::::::::::::::::::
  Ratios
::::::::::::::::::::::::::::::::::::::::::::::::::
hhea metrics / UPM:  1
typo metrics / UPM:  1
win metrics  / UPM:  1
```

## Merge structure

Medium
------
```
keebglyphs ---> fixed6x13 -> Keebfont
Cozette ----/
```

Bold
----
```
fixed6x13B -----\
keebglyphs --------> fixed6x13 -> Keebfont
Cozette ----/
```

Italic
----
```
fixed6x13O -----\
keebglyphs --------> fixed6x13 -> Keebfont
Cozette ----/
```
## Sources
This font is based on the original Fixed6x13 font ($Id: 6x13.bdf,v 1.115 2009-04-06 18:50:15+01 mgk25 Rel $ Send bug reports to Markus Kuhn <http://www.cl.cam.ac.uk/~mgk25/> $ COPYRIGHT "Public domain font.  Share and enjoy.")

Merged with additional glyphs from the similarly sized Cozette font https://github.com/the-moonwitch/Cozette ("Copyright (c) 2025 Ines <ines@moonwit.ch>+ Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the +ACIA-Software+ACIA), to deal in the Software with
out restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:+AAoACgAA-The above copyright not
ice and this permission notice shall be included in all copies or substantial portions of the Software.+AAoACgAA-THE SOFTWARE IS PROVIDED +ACIA-AS IS+ACIA, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTIC
ULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWAR
E." "https://opensource.org/licenses/MIT")

It also includes a patched bitfont2otb https://github.com/ctrlcctrlv/bitmapfont2otb (Fredrick R. Brennan) to skip glyphs that are not size compatible.

