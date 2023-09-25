def rgba_to_hex(rgba_color: tuple[int, int, int, int]) -> str:
    r, g, b, a = rgba_color

    r = format(r, "02X")
    g = format(g, "02X")
    b = format(b, "02X")
    a = format(a, "02X")

    hex_color = f"#{r}{g}{b}{a}"

    return hex_color


def fade_color(color: str) -> str:
    # converts current color to RGBA
    color = color.lstrip("#")

    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)
    a = 64  # 25% opacity

    color = (r, g, b, a)
    faded_color = rgba_to_hex(color)

    return faded_color
