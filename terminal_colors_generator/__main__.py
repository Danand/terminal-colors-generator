from sys import stderr, stdin, argv
from operator import xor
from json import load, dumps
from argparse import ArgumentError, ArgumentParser
from typing import Dict

from .generator import generate

argument_parser = ArgumentParser(
    'Terminal Colors Generator',
    'Generates new color scheme from given color scheme.\n\nstdin: Colors JSON object.')

argument_parser.add_argument(
    '--color-from',
    type=str,
    help='Color which considered to be initial value for color wheel rotation',
    required=True
)

argument_parser.add_argument(
    '--color-to',
    type=str,
    help='Color which considered to be destination value for color wheel rotation',
    required=True
)

argument_parser.add_argument(
    '--background',
    type=str,
    help='Color which considered to be background for readability correction',
    required=False
)

argument_parser.add_argument(
    '--accent',
    type=str,
    help='Color which not be altered for readability correction',
    required=False
)

argument_parser.add_argument(
    '--export',
    help='Outputs Bash variable exports.',
    action='store_true'
)

args = argument_parser.parse_args(argv[1:])

colors: Dict[str, str] = load(stdin)

color_from: str = args.color_from
color_to: str = args.color_to

background: str = args.background
accent: str = args.accent
export: bool = args.export

if xor(background is not None, accent is not None):
    raise ArgumentError(None, "Both `--background` and `--accent` must be specified")
else:
    print("warning: Readability correction may take a while, please wait...", file=stderr)

result = generate(colors, color_from, color_to, background, accent)

if export:
    print(f"export TERMINAL_THEME_NAME=\"{result['name']}\"")
    print(f"export TERMINAL_THEME_BLACK=\"{result['black']}\"")
    print(f"export TERMINAL_THEME_RED=\"{result['red']}\"")
    print(f"export TERMINAL_THEME_GREEN=\"{result['green']}\"")
    print(f"export TERMINAL_THEME_YELLOW=\"{result['yellow']}\"")
    print(f"export TERMINAL_THEME_BLUE=\"{result['blue']}\"")
    print(f"export TERMINAL_THEME_MAGENTA=\"{result['purple']}\"")
    print(f"export TERMINAL_THEME_CYAN=\"{result['cyan']}\"")
    print(f"export TERMINAL_THEME_WHITE=\"{result['white']}\"")
    print(f"export TERMINAL_THEME_BRIGHT_BLACK=\"{result['brightBlack']}\"")
    print(f"export TERMINAL_THEME_BRIGHT_RED=\"{result['brightRed']}\"")
    print(f"export TERMINAL_THEME_BRIGHT_GREEN=\"{result['brightGreen']}\"")
    print(f"export TERMINAL_THEME_BRIGHT_YELLOW=\"{result['brightYellow']}\"")
    print(f"export TERMINAL_THEME_BRIGHT_BLUE=\"{result['brightBlue']}\"")
    print(f"export TERMINAL_THEME_BRIGHT_MAGENTA=\"{result['brightPurple']}\"")
    print(f"export TERMINAL_THEME_BRIGHT_CYAN=\"{result['brightCyan']}\"")
    print(f"export TERMINAL_THEME_BRIGHT_WHITE=\"{result['brightWhite']}\"")
    print(f"export TERMINAL_THEME_BACKGROUND=\"{result['background']}\"")
    print(f"export TERMINAL_THEME_FOREGROUND=\"{result['foreground']}\"")
    print(f"export TERMINAL_THEME_CURSOR=\"{result['cursorColor']}\"")
    print(f"export TERMINAL_THEME_SELECTION_BACKGROUND=\"{result['selectionBackground']}\"")
else:
    result_json = dumps(result, indent=2)
    print(result_json)

