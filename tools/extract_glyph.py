
import fontforge
import sys
import os

try:
    font_path = sys.argv[1]
    glyph_unicode = int(sys.argv[2], 16) # Convert hex string to integer
    output_dir = sys.argv[3]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    font = fontforge.open(font_path)
    font.selection.none()
    font.selection.select(("unicode",), glyph_unicode)

    selected_glyphs = list(font.selection.byGlyphs)

    if not selected_glyphs:
        print(f"Error: Glyph U+{hex(glyph_unicode)[2:].upper()} not found or not selectable in the font.", file=sys.stderr)
        sys.exit(1)

    # Iterate directly through the glyph objects yielded by font.selection.byGlyphs
    for glyph in selected_glyphs:
        output_filename = os.path.join(output_dir, f"glyph_{hex(glyph_unicode)}.svg")
        glyph.export(output_filename)
        print(f"Successfully extracted glyph {hex(glyph_unicode)} to {output_filename}")

    font.close()
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
