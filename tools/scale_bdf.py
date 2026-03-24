def scale_bitmap(lines, width, height, scale_factor=2):
    """Scale bitmap lines by scale_factor."""
    all_bits = []
    for row in range(height):
        hex_bytes = [int(b, 16) for b in lines[row].split()]
        row_bits = []
        bits_needed = width
        for byte in hex_bytes:
            bits_to_extract = min(8, bits_needed)
            for i in range(bits_to_extract):
                row_bits.append((byte >> (7 - i)) & 1)
            bits_needed -= bits_to_extract
            if bits_needed <= 0:
                break
        all_bits.append(row_bits)
    
    scaled_bits = []
    for row_bits in all_bits:
        for _ in range(scale_factor):
            for bit in row_bits:
                for _ in range(scale_factor):
                    scaled_bits.append(bit)
    
    new_width = width * scale_factor
    new_height = height * scale_factor
    
    result = []
    bit_idx = 0
    for row in range(new_height):
        row_bits = []
        for col in range(new_width):
            row_bits.append(scaled_bits[bit_idx])
            bit_idx += 1
        
        # Pack bits into bytes for this row
        row_bytes = []
        for i in range(0, len(row_bits), 8):
            byte = 0
            for j in range(8):
                if i + j < len(row_bits):
                    byte |= row_bits[i + j] << (7 - j)
            row_bytes.append(byte)
        result.append(row_bytes)
    
    return result


def scale_font_property(line, scale_factor):
    """Scale a font property that contains numeric values."""
    parts = line.split()
    if len(parts) < 2:
        return line
    
    prop_name = parts[0]
    
    if prop_name in ('FONT_DESCENT', 'FONT_ASCENT', 'X_HEIGHT', 'CAP_HEIGHT'):
        value = int(parts[1]) * scale_factor
        return f"{prop_name} {value}"
    
    elif prop_name == 'FONTBOUNDINGBOX':
        if len(parts) >= 4:
            x_max = int(parts[1]) * scale_factor
            y_max = int(parts[2]) * scale_factor
            x_off = int(parts[3]) * scale_factor
            y_off = int(parts[4]) * scale_factor if len(parts) >= 5 else 0
            return f"FONTBOUNDINGBOX {x_max} {y_max} {x_off} {y_off}"
    
    elif prop_name == 'SIZE':
        if len(parts) >= 4:
            point_size = int(parts[1]) * scale_factor
            x_res = int(parts[2]) * scale_factor
            y_res = int(parts[3]) * scale_factor
            return f"SIZE {point_size} {x_res} {y_res}"
    
    return line


def scale_bdf(content, scale_factor=2):
    """Scale a BDF font by scale_factor."""
    lines = content.strip().split('\n')
    output = []
    in_bitmap = False
    bitmap_lines = []
    bbx = None
    dwidth = None
    glyph_name = None
    encoding = None
    glyph_properties = []
    
    def flush_glyph():
        nonlocal bbx, dwidth, glyph_name, encoding, bitmap_lines, glyph_properties
        if glyph_name and bbx:
            parts = bbx.split()
            width, height, x_off, y_off = int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4])
            new_width = width * scale_factor
            new_height = height * scale_factor
            new_x_off = x_off * scale_factor
            new_y_off = y_off * scale_factor
            new_bbx = f"BBX {new_width} {new_height} {new_x_off} {new_y_off}"
            
            new_dwidth = ""
            if dwidth:
                parts = dwidth.split()
                dw_x, dw_y = int(parts[1]), int(parts[2])
                new_dw_x = dw_x * scale_factor
                new_dw_y = dw_y * scale_factor
                new_dwidth = f"DWIDTH {new_dw_x} {new_dw_y}"
            
            scaled_bitmap = scale_bitmap(bitmap_lines, width, height, scale_factor)
            
            output.append(f"STARTCHAR {glyph_name}")
            if encoding:
                output.append(encoding)
            output.append(new_bbx)
            if new_dwidth:
                output.append(new_dwidth)
            for prop in glyph_properties:
                output.append(prop)
            output.append("BITMAP")
            for row_bytes in scaled_bitmap:
                output.append(" ".join(f"{b:02X}" for b in row_bytes))
            output.append("ENDCHAR")
        
        bitmap_lines = []
        bbx = None
        dwidth = None
        glyph_name = None
        encoding = None
        glyph_properties = []
    
    for line in lines:
        stripped = line.strip()
        
        if stripped.startswith('STARTFONT'):
            output.append(stripped)
            continue
        
        if stripped.startswith('ENDFONT'):
            flush_glyph()
            output.append(stripped)
            continue
        
        if stripped.startswith('STARTCHAR'):
            flush_glyph()
            glyph_name = stripped.split()[1]
            continue
        
        if stripped.startswith('ENCODING'):
            encoding = stripped
            continue
        
        if stripped.startswith('BBX'):
            bbx = stripped
            continue
        
        if stripped.startswith('DWIDTH'):
            dwidth = stripped
            continue
        
        if stripped == 'BITMAP':
            in_bitmap = True
            bitmap_lines = []
            continue
        
        if stripped == 'ENDCHAR':
            flush_glyph()
            in_bitmap = False
            continue
        
        if in_bitmap:
            bitmap_lines.append(stripped)
            continue
        
        if glyph_name and not in_bitmap:
            if stripped.startswith('SWIDTH') or stripped.startswith('CHAR') or stripped.startswith('NAMES'):
                glyph_properties.append(stripped)
            else:
                output.append(scale_font_property(stripped, scale_factor))
        else:
            output.append(scale_font_property(stripped, scale_factor))
    
    flush_glyph()
    
    return '\n'.join(output)


def main():
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description="Scale BDF bitmap font by 2x")
    parser.add_argument("input", help="Input BDF file")
    parser.add_argument("output", help="Output BDF file")
    parser.add_argument("-s", "--scale", type=int, default=2, help="Scale factor (default: 2)")
    
    args = parser.parse_args()
    
    with open(args.input, 'r') as f:
        content = f.read()
    
    scaled = scale_bdf(content, args.scale)
    
    with open(args.output, 'w') as f:
        f.write(scaled)
    
    print(f"Scaled {args.input} -> {args.output} ({args.scale}x)")


if __name__ == "__main__":
    main()
