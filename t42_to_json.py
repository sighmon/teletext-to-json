import json

# Color mapping for teletext colors
COLOR_MAP = {
    0x00: "black", 0x01: "red", 0x02: "green", 0x03: "yellow",
    0x04: "blue", 0x05: "magenta", 0x06: "cyan", 0x07: "white"
}

# Expanded alphanumeric mapping (Western European teletext set)
ALPHANUMERIC_MAP = {
    0x20: " ", 0x21: "!", 0x22: '"', 0x23: "£", 0x24: "$", 0x25: "%", 0x26: "&", 0x27: "'",
    0x28: "(", 0x29: ")", 0x2A: "*", 0x2B: "+", 0x2C: ",", 0x2D: "-", 0x2E: ".", 0x2F: "/",
    0x30: "0", 0x31: "1", 0x32: "2", 0x33: "3", 0x34: "4", 0x35: "5", 0x36: "6", 0x37: "7",
    0x38: "8", 0x39: "9", 0x3A: ":", 0x3B: ";", 0x3C: "<", 0x3D: "=", 0x3E: ">", 0x3F: "?",
    0x40: "@", 0x41: "A", 0x42: "B", 0x43: "C", 0x44: "D", 0x45: "E", 0x46: "F", 0x47: "G",
    0x48: "H", 0x49: "I", 0x4A: "J", 0x4B: "K", 0x4C: "L", 0x4D: "M", 0x4E: "N", 0x4F: "O",
    0x50: "P", 0x51: "Q", 0x52: "R", 0x53: "S", 0x54: "T", 0x55: "U", 0x56: "V", 0x57: "W",
    0x58: "X", 0x59: "Y", 0x5A: "Z", 0x5B: "←", 0x5C: "½", 0x5D: "→", 0x5E: "↑", 0x5F: "#",
    0x60: "—", 0x61: "a", 0x62: "b", 0x63: "c", 0x64: "d", 0x65: "e", 0x66: "f", 0x67: "g",
    0x68: "h", 0x69: "i", 0x6A: "j", 0x6B: "k", 0x6C: "l", 0x6D: "m", 0x6E: "n", 0x6F: "o",
    0x70: "p", 0x71: "q", 0x72: "r", 0x73: "s", 0x74: "t", 0x75: "u", 0x76: "v", 0x77: "w",
    0x78: "x", 0x79: "y", 0x7A: "z", 0x7B: "¼", 0x7C: "│", 0x7D: "¾", 0x7E: "÷", 0x7F: "■",
    0xA0: " ", 0xA1: "¡", 0xA2: "¢", 0xA3: "£", 0xA4: "¤", 0xA5: "¥", 0xA6: "¦", 0xA7: "§",
    0xA8: "¨", 0xA9: "©", 0xAA: "ª", 0xAB: "«", 0xAC: "¬", 0xAD: "­", 0xAE: "®", 0xAF: "¯",
    0xB0: "°", 0xB1: "±", 0xB2: "²", 0xB3: "³", 0xB4: "´", 0xB5: "µ", 0xB6: "¶", 0xB7: "·",
    0xB8: "¸", 0xB9: "¹", 0xBA: ":", 0xBB: "»", 0xBC: "¼", 0xBD: "½", 0xBE: "¾", 0xBF: "¿",
    0xC0: "À", 0xC1: "Á", 0xC2: "Â", 0xC3: "Ã", 0xC4: "Ä", 0xC5: "Å", 0xC6: "Æ", 0xC7: "Ç",
    0xC8: "È", 0xC9: "É", 0xCA: "Ê", 0xCB: "Ë", 0xCC: "Ì", 0xCD: "Í", 0xCE: "Î", 0xCF: "Ï",
    0xD0: "Ð", 0xD1: "Ñ", 0xD2: "Ò", 0xD3: "Ó", 0xD4: "Ô", 0xD5: "Õ", 0xD6: "Ö", 0xD7: "×",
    0xD8: "Ø", 0xD9: "Ù", 0xDA: "Ú", 0xDB: "Û", 0xDC: "Ü", 0xDD: "Ý", 0xDE: "Þ", 0xDF: "ß",
    0xE0: "à", 0xE1: "á", 0xE2: "â", 0xE3: "ã", 0xE4: "ä", 0xE5: "å", 0xE6: "æ", 0xE7: "ç",
    0xE8: "è", 0xE9: "é", 0xEA: "ê", 0xEB: "ë", 0xEC: "ì", 0xED: "í", 0xEE: "î", 0xEF: "ï",
    0xF0: "ð", 0xF1: "ñ", 0xF2: "ò", 0xF3: "ó", 0xF4: "ô", 0xF5: "õ", 0xF6: "ö", 0xF7: "÷",
    0xF8: "ø", 0xF9: "ù", 0xFA: "ú", 0xFB: "û", 0xFC: "ü", 0xFD: "ý", 0xFE: "þ", 0xFF: "ÿ"
}

# Graphics mapping (simplified block elements)
GRAPHICS_MAP = {
    0x20: " ", 0x21: "▌", 0x22: "▐", 0x23: "▀", 0x24: "▄", 0x25: "▬", 0x26: "▙", 0x27: "▟",
    0x28: "▖", 0x29: "▗", 0x2A: "▘", 0x2B: "▝", 0x2C: "▞", 0x2D: "▛", 0x2E: "▜", 0x2F: "▚",
    0x30: "0", 0x31: "1", 0x32: "2", 0x33: "3", 0x34: "4", 0x35: "5", 0x36: "6", 0x37: "7",
    0x38: "8", 0x39: "9", 0x7F: "█"  # Extend as needed
}

def parse_row(row):
    """Parse a 40-byte teletext row into a list of character objects."""
    result = []
    fg_color = "white"
    bg_color = "black"
    graphics = False
    concealed = False

    for byte in row:
        if byte < 0x20:  # Control code
            if 0x00 <= byte <= 0x07:
                fg_color = COLOR_MAP[byte]
                graphics = False
            elif 0x10 <= byte <= 0x17:
                fg_color = COLOR_MAP[byte - 0x10]
                graphics = True
            elif byte == 0x1C:
                bg_color = "black"
            elif byte == 0x1D:
                bg_color = fg_color
            elif byte == 0x18:
                concealed = True
            char = " "
        else:
            if graphics:
                char = GRAPHICS_MAP.get(byte, "?")
            else:
                # In alphanumeric mode, strip high bit for bytes >= 0x80
                if byte >= 0x80:
                    byte = byte & 0x7F
                char = ALPHANUMERIC_MAP.get(byte, "?")
        
        result.append({
            "char": char,
            "fg": fg_color,
            "bg": bg_color,
            "is_graphics": graphics,
            "concealed": concealed
        })
    return result

def parse_page(data):
    """
    Parse 1000 bytes into 25 rows of 40 bytes each.
    
    Args:
        data (bytes): A 1000-byte sequence representing a teletext page.
    
    Returns:
        list: List of parsed rows.
    """
    rows = [data[i*40:(i+1)*40] for i in range(25)]
    return [parse_row(row) for row in rows]

def read_t42_file(filename):
    """Read a .t42 file and return a dictionary of pages."""
    with open(filename, "rb") as f:
        pages = []
        while True:
            header = f.read(26)  # Read 26-byte header
            if len(header) < 26:
                break  # End of file

            # Parse header (adjust based on actual .t42 spec)
            magazine = header[0]
            page_num = int.from_bytes(header[1:3], "little")
            subpage = int.from_bytes(header[3:5], "little")

            # Read 1000-byte page data
            data = f.read(1000)
            if len(data) < 1000:
                break  # Incomplete page

            parsed_rows = parse_page(data)
            pages.append({
                "magazine": magazine,
                "page": page_num,
                "subpage": subpage,
                "rows": parsed_rows
            })

        return {"pages": pages}

def convert_t42_to_json(t42_file, json_file):
    """Convert a .t42 file to JSON and save it."""
    data = read_t42_file(t42_file)
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)

# Example usage
if __name__ == "__main__":
    convert_t42_to_json("input.t42", "output.json")
