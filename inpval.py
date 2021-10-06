import re
import sys

from inpval_formats import UnknownFormatError, Formats


def print_all_formats():
    for format in Formats.formats:
        sys.stdout.write(f"{format}\n")


if __name__ == "__main__":
    try:
        if sys.argv[1].startswith('-'):
            option = sys.argv[1]
            if option == '-p' or option == '--pattern':
                try:
                    pattern = Formats.get_regex_pattern(sys.argv[2])
                    sys.stdout.write(f"{pattern}\n")
                except IndexError:
                    sys.exit(f"inpval: Error: missing format for '{option}' option")
                except UnknownFormatError:
                    sys.exit(f"inpval: Error: unknown format: {sys.argv[2]}")
            elif option == '-l' or option == '--list':
                print_all_formats()
        else:
            try:
                if Formats.matches_format(sys.argv[1], sys.argv[2]):
                    sys.stdout.write(f"{sys.argv[2]}\n")
                sys.exit(0)
            except IndexError:
                sys.exit("inpval: Error: missing input string")
    except IndexError:
        sys.exit("Usage: inpval [OPTION] [FORMAT] [INPUT]")
    except UnknownFormatError:
        sys.exit(f"inpval: Error: unknown format: {sys.argv[1]}")
        