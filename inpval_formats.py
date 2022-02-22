from re import IGNORECASE, ASCII, DEBUG, fullmatch
from typing import List


class UnknownOptionError(Exception):
    pass


class Formats:
    dt_frags = {
        'days_2': r"(0[1-9]|[1-2][0-9]|3[0-1])",
        'days_1_or_2': r"(0?[1-9]|[1-2][0-9]|3[0-1])",
        'dt12_2': r"(0[1-9]|1[0-2])",
        'dt12_1_or_2': r"(0?[1-9]|1[0-2])",
        'time24_2': r"(0[0-9]|1[0-9]|2[0-3])",
        'd_delims': r"(\/|\.|-)",
        'years_2': r"\d{2}",
        'years_4': r"\d{3}[1-9]",
        'num60_2': r"([0-5][0-9])",
        't_delims': r"(\:|\s)"
    }

    ip_frags = {
        'ip_255': r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
    }

    options = {
        '-word': {
            'notes': "word is defined as a string containing alphanumeric and/or underscore characters",
            'format': "<Word>",
            'pattern': r"(\w+)",
            'flags': ASCII
        },
        '-date_4md': {
            'notes': "days in month limits not checked",
            'format': "<MMDD>",
            'pattern': rf"{dt_frags['dt12_2']}{dt_frags['days_2']}",
            'flags': 0
        },
        '-date_4md_d': {
            'notes': "days in month limits not checked",
            'format': "<MM><'/' or '.' or ' '><DD>",
            'pattern': rf"{dt_frags['dt12_1_or_2']}{dt_frags['d_delims']}{dt_frags['days_1_or_2']}",
            'flags': 0
        },
        '-date_6mdy': {
            'notes': "days in month limits not checked",
            'format': "<MMDDYY>",
            'pattern': rf"{dt_frags['dt12_2']}{dt_frags['days_2']}{dt_frags['years_2']}",
            'flags': 0
        },
        '-date_6mdy_d': {
            'notes': "days in month limits not checked",
            'format': "<MM><'/' or '.' or ' '><DD><'/' or '.' or ' '><YY>",
            'pattern': rf"{dt_frags['dt12_1_or_2']}{dt_frags['d_delims']}{dt_frags['days_1_or_2']}{dt_frags['d_delims']}{dt_frags['years_2']}",
            'flags': 0
        },
        '-date_6dmy': {
            'notes': "days in month limits not checked",
            'format': "<DDMMYY>",
            'pattern': rf"{dt_frags['days_2']}{dt_frags['dt12_2']}{dt_frags['years_2']}",
            'flags': 0
        },
        '-date_6dmy_d': {
            'notes': "days in month limits not checked",
            'format': "<D[D]><'/' or '.' or ' '><M[M]><'/' or '.' or ' '><YY>",
            'pattern': rf"{dt_frags['days_1_or_2']}{dt_frags['d_delims']}{dt_frags['dt12_1_or_2']}{dt_frags['d_delims']}{dt_frags['years_2']}",
            'flags': 0
        },
        '-date_8mdy': {
            'notes': "days in month limits not checked",
            'format': "<MMDDYYYY>",
            'pattern': rf"{dt_frags['dt12_2']}{dt_frags['days_2']}{dt_frags['years_4']}",
            'flags': 0
        },
        '-date_8mdy_d': {
            'notes': "days in month limits not checked",
            'format': "<M[M]><'/' or '.' or ' '><D[D]><'/' or '.' or ' '><YYYY>",
            'pattern': rf"{dt_frags['dt12_1_or_2']}{dt_frags['d_delims']}{dt_frags['days_1_or_2']}{dt_frags['d_delims']}{dt_frags['years_4']}",
            'flags': 0
        },
        '-date_8dmy': {
            'notes': "days in month limits not checked",
            'format': "<DDMMYYYY>",
            'pattern': rf"{dt_frags['days_2']}{dt_frags['dt12_2']}{dt_frags['years_4']}",
            'flags': 0
        },
        '-date_8dmy_d': {
            'notes': "days in month limits not check",
            'format': "<D[D]><'/' or '.' or ' '><M[M]><'/' or '.' or ' '><YYYY>",
            'pattern': rf"{dt_frags['days_1_or_2']}{dt_frags['d_delims']}{dt_frags['dt12_1_or_2']}{dt_frags['d_delims']}{dt_frags['years_4']}",
            'flags': 0
        },
        '-date_8ymd': {
            'notes': "days in month limits not checked",
            'format': "<YYYYMMDD>",
            'pattern': rf"{dt_frags['years_4']}{dt_frags['dt12_2']}{dt_frags['days_2']}",
            'flags': 0
        },
        '-date_8ymd_d': {
            'notes': "days in month limits not check",
            'format': "<YYYY><'/' or '.' or ' '><M[M]><'/' or '.' or ' '><D[D]>",
            'pattern': rf"{dt_frags['years_4']}{dt_frags['d_delims']}{dt_frags['dt12_1_or_2']}{dt_frags['d_delims']}{dt_frags['days_1_or_2']}",
            'flags': 0
        },
        '-date_9mdy_d': {
            'notes': "days in month limits not checked, ignores case of the three letter month",
            'format': "<mon><'/' or '.' or ' '><D[D]><'/' or '.' or ' '><YYYY>",
            'pattern': rf"(jan|feb|mar|apr|may|jun|jul|aug|sept?|oct|nov|dec){dt_frags['d_delims']}{dt_frags['days_1_or_2']}{dt_frags['d_delims']}{dt_frags['years_4']}",
            'flags': IGNORECASE
        },
        '-time_12_s': {
            'notes': "",
            'format': "<HH (max 12 and min 1)><':' or ' '><MM><':' or ' '><SS>",
            'pattern': rf"{dt_frags['dt12_2']}{dt_frags['t_delims']}{dt_frags['num60_2']}{dt_frags['t_delims']}{dt_frags['num60_2']}\s([AaPp][Mm])",
            'flags': 0
        },
        '-time_12': {
            'notes': "",
            'format': "<HH (max 12 and min 1)><':' or ' '><MM>",
            'pattern': rf"{dt_frags['dt12_2']}{dt_frags['t_delims']}{dt_frags['num60_2']}\s([AaPp][Mm])",
            'flags': 0
        },
        '-time_24_s': {
            'notes': "",
            'format': "<HH (max 23 and min 0)><':' or ' '><MM><':' or ' '><SS>",
            'pattern': rf"{dt_frags['time24_2']}{dt_frags['t_delims']}{dt_frags['num60_2']}{dt_frags['t_delims']}{dt_frags['num60_2']}",
            'flags': 0
        },
        '-time_24': {
            'notes': "",
            'format': "<HH (max 23 and min 0)><':' or ' '><MM>",
            'pattern': rf"{dt_frags['time24_2']}{dt_frags['t_delims']}{dt_frags['num60_2']}",
            'flags': 0
        },
        '-email': {
            'notes': "won't check if email actually exists",
            'format': "<Valid Email Format>",
            'pattern': r"(([^<>()\[\]\\.,;:\s@\"]+(\.[^<>()\[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))",
            'flags': IGNORECASE
        },
        '-ip4': {
            'notes': "",
            'format': "<Octet>.<Octet>.<Octet>.<Octet>",
            'pattern': rf"({ip_frags['ip_255']}\.){{3}}{ip_frags['ip_255']}",
            'flags': 0
        },
        '-ip4_range': {
            'notes': "won't check for vaild IP range",
            'format': "<Octet>.<Octet>.<Octet>.<Octet>/<Octet>",
            'pattern': rf"({ip_frags['ip_255']}\.){{3}}{ip_frags['ip_255']}\/{ip_frags['ip_255']}",
            'flags': 0
        },
        '-url': {
            'notes': "won't check if URL actually exists",
            'format': "<Valid URL Format>",
            'pattern': r"((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)",
            'flags': 0
        },
        '-pw': {
            'notes': '',
            'format': "minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character (#?!@$%%^&*-)",
            'pattern': r"(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}",
            'flags': 0
        }
    }

    @classmethod
    def get_option_format(cls, option: str) -> str:
        try:
            return cls.options[option]['format']
        except KeyError:
            raise UnknownOptionError

    @classmethod
    def get_option_pattern(cls, option: str) -> str:
        try:
            return cls.options[option]['pattern']
        except KeyError:
            raise UnknownOptionError

    @classmethod
    def get_option_flags(cls, option: str) -> str:
        try:
            return cls.options[option]['flags']
        except KeyError:
            raise UnknownOptionError    

    @classmethod
    def matches_format(cls, option: str, input: str) -> bool:
        if fullmatch(
            Formats.get_option_pattern(option),
            input,
            Formats.get_option_flags(option)
        ):
            return True
        return False