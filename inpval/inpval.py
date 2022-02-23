import sys, argparse
from unittest.main import main

from inpval_formats import Formats, UnknownOptionError


def set_up_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='inpval',
        description='Test whether or not an input matches a given format. If no input is supplied then the regex pattern tied to the format is returned.',
        usage="usage: inpval [-h] FORMAT_OPTION [INPUT]"
    )
    for option in Formats.options:
        parser.add_argument(
            option,
            nargs="?",
            help=f"format --> {Formats.get_option_format(option)}",
            metavar='INPUT',
            const='pattern'
        )
    return parser

if __name__ == "__main__":
    parser = set_up_parser()
    args = parser.parse_args()
    try:
        input, set_option = "", ""
        options = vars(args)
        for option in options:
            input = options.get(option)
            if input:
                set_option = f"-{option}"
                break
        if input == 'pattern':
            output = Formats.get_option_pattern(set_option)
            sys.stdout.write(f"{output}\n")
        elif Formats.matches_format(
            set_option,
            input
        ):
            sys.stdout.write(f"{input}\n")
        sys.exit(0)
    except UnknownOptionError:
        sys.exit(1)
