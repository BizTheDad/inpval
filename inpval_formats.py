from re import IGNORECASE, ASCII, fullmatch


class UnknownFormatError(Exception):
    pass


class Formats:
    dt_frags = {
        'days_2': "(0[1-9]|[1-2][0-9]|3[0-1])",
        'days_1_or_2': "(0?[1-9]|[1-2][0-9]|3[0-1])",
        'dt12_2': "(0[1-9]|1[0-2])",
        'dt12_1_or_2': "(0?[1-9]|1[0-2])",
        'time24_2': "(0[0-9]|1[0-9]|2[0-3])",
        'd_delims': "(\/|\.|-)",
        'years_2': "\d{2}",
        'years_4': "\d{3}[1-9]",
        'num60_2': "([0-5][0-9])",
        't_delims': "(\:|\s)"
    }

    formats = {
        '-word': {
            'pattern': "(\w+)",
            'flags': ASCII
        },
        '-date-4md': {
            'pattern': f"{dt_frags['dt12_2']}{dt_frags['days_2']}",
            'flags': 0
        },
        '-date-4md-d': {
            'pattern': f"{dt_frags['dt12_1_or_2']}{dt_frags['d_delims']}{dt_frags['days_1_or_2']}",
            'flags': 0
        },
        '-date-6mdy': {
            'pattern': f"{dt_frags['dt12_2']}{dt_frags['days_2']}{dt_frags['years_2']}",
            'flags': 0
        },
        '-date-6mdy-d': {
            'pattern': f"{dt_frags['dt12_1_or_2']}{dt_frags['d_delims']}{dt_frags['days_1_or_2']}{dt_frags['d_delims']}{dt_frags['years_2']}",
            'flags': 0
        },
        '-date-6dmy': {
            'pattern': f"{dt_frags['days_2']}{dt_frags['dt12_2']}{dt_frags['years_2']}",
            'flags': 0
        },
        '-date-6dmy-d': {
            'pattern': f"{dt_frags['days_1_or_2']}{dt_frags['d_delims']}{dt_frags['dt12_1_or_2']}{dt_frags['d_delims']}{dt_frags['years_2']}",
            'flags': 0
        },
        '-date-8mdy': {
            'pattern': f"{dt_frags['dt12_2']}{dt_frags['days_2']}{dt_frags['years_4']}",
            'flags': 0
        },
        '-date-8mdy-d': {
            'pattern': f"{dt_frags['dt12_1_or_2']}{dt_frags['d_delims']}{dt_frags['days_1_or_2']}{dt_frags['d_delims']}{dt_frags['years_4']}",
            'flags': 0
        },
        '-date-8dmy': {
            'pattern': f"{dt_frags['days_2']}{dt_frags['dt12_2']}{dt_frags['years_4']}",
            'flags': 0
        },
        '-date-8dmy-d': {
            'pattern': f"{dt_frags['days_1_or_2']}{dt_frags['d_delims']}{dt_frags['dt12_1_or_2']}{dt_frags['d_delims']}{dt_frags['years_4']}",
            'flags': 0
        },
        '-date-8ymd': {
            'pattern': f"{dt_frags['years_4']}{dt_frags['dt12_2']}{dt_frags['days_2']}",
            'flags': 0
        },
        '-date-8ymd-d': {
            'pattern': f"{dt_frags['years_4']}{dt_frags['d_delims']}{dt_frags['dt12_1_or_2']}{dt_frags['d_delims']}{dt_frags['days_1_or_2']}",
            'flags': 0
        },
        '-date-9mdy-d': {
            'pattern': f"(jan|feb|mar|apr|may|jun|jul|aug|sept?|oct|nov|dec){dt_frags['d_delims']}{dt_frags['days_1_or_2']}{dt_frags['d_delims']}{dt_frags['years_4']}",
            'flags': IGNORECASE
        },
        '-time-12-s': {
            'pattern': f"{dt_frags['dt12_2']}{dt_frags['t_delims']}{dt_frags['num60_2']}{dt_frags['t_delims']}{dt_frags['num60_2']}\s([AaPp][Mm])",
            'flags': 0
        },
        '-time-12': {
            'pattern': f"{dt_frags['dt12_2']}{dt_frags['t_delims']}{dt_frags['num60_2']}\s([AaPp][Mm])",
            'flags': 0
        },
        '-time-24-s': {
            'pattern': f"{dt_frags['time24_2']}{dt_frags['t_delims']}{dt_frags['num60_2']}{dt_frags['t_delims']}{dt_frags['num60_2']}",
            'flags': 0
        },
        '-time-24': {
            'pattern': f"{dt_frags['time24_2']}{dt_frags['t_delims']}{dt_frags['num60_2']}",
            'flags': 0
        },
        '-email': {
            'pattern': "(([^<>()\[\]\\.,;:\s@\"]+(\.[^<>()\[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))",
            'flags': IGNORECASE
        },
        '-ip4': {
            'pattern': "((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",
            'flags': 0
        },
        '-url': {
            'pattern': "((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)",
            'flags': 0
        }
    }

    @classmethod
    def get_regex_pattern(cls, format: str) -> str:
        try:
            return cls.formats[format]['pattern']
        except KeyError:
            raise UnknownFormatError

    @classmethod
    def matches_format(cls, format: str, input: str) -> bool:
        try:
            params = cls.formats[format]
            pattern = params['pattern']
            if fullmatch(
                pattern,
                input,
                flags=params['flags']
            ):
                return True
            return False
        except KeyError:
            raise UnknownFormatError