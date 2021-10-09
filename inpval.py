import re
import sys

from inpval_formats import UnknownFormatError, Formats


def print_all_formats():
    for format in Formats.formats:
        sys.stdout.write(f"{format}\n")


if __name__ == "__main__":
    try:
        option = sys.argv[1]
        match_against = sys.argv[2]
        if option == '-p' or option == '--pattern':
            try:
                pattern = Formats.get_regex_pattern(match_against)
                sys.stdout.write(f"{pattern}\n")
            except IndexError:
                sys.exit(f"inpval: Error: missing format for '{option}' option")
            except UnknownFormatError:
                sys.exit(f"inpval: Error: unknown format: {match_against}")
        elif option == '-l' or option == '--list':
            print_all_formats()
        else:
            try:
                if Formats.matches_format(option, match_against):
                    sys.stdout.write(f"{match_against}\n")
                sys.exit(0)
            except IndexError:
                sys.exit("inpval: Error: missing input string")
    except IndexError:
        sys.exit("Usage: inpval [OPTION] [FORMAT] [INPUT]")
    except UnknownFormatError:
        sys.exit(f"inpval: Error: unknown format: {option}")
        