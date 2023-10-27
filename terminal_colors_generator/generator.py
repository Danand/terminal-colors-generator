from sys import stderr
from typing import List, Dict

from colormath.color_objects import ColorBase, sRGBColor

from colormath.colorwheel import Wheel

def generate(
        colors_dict: Dict[str, str],
        color_from: str,
        color_to: str,
    ) -> Dict[str, str]:
    hex_colors: List[ColorBase] = []
    not_parsed: List[str] = []

    for key, value in colors_dict.items():
        try:
            sRGBColor.new_from_rgb_hex(value)
            hex_colors.append(value)
        except Exception as exception:
            print(f"warning: Failed to parse `{value}` as color", file=stderr)
            print(exception, file=stderr)
            not_parsed.append(key)

    wheel = Wheel.create_from_hex(hex_colors)

    colors_rotated = wheel.rotate_from_to_hex(color_from, color_to)

    colors_dict_result: Dict[str, str] = {}

    index = 0

    for key, value in colors_dict.items():
        if key in not_parsed:
            colors_dict_result[key] = value
        else:
            colors_dict_result[key] = colors_rotated[index]
            index += 1

    return colors_dict_result
