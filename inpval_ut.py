import unittest
from re import fullmatch

from inpval_formats import Formats, UnknownFormatError


class TestPatternMatching(unittest.TestCase):
    def test_exceptions(self):
        with self.assertRaises(UnknownFormatError):
            Formats.matches_format('wegw', 'input string')

    #
    # The fragment tests will do the bounds testing. All other match testing for
    # dates and times will be one random True and one random False test.
    #
    def test_frags(self):
        self.assertTrue(fullmatch(Formats.dt_frags['days_2'], '01', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['days_2'], '31', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['days_2'], '10', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['days_2'], '29', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['days_2'], '00', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['days_2'], '32', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['days_1_or_2'], '1', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['days_1_or_2'], '01', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['days_1_or_2'], '31', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['days_1_or_2'], '10', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['days_1_or_2'], '29', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['days_1_or_2'], '0', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['days_1_or_2'], '00', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['days_1_or_2'], '32', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['dt12_2'], '01', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['dt12_2'], '12', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['dt12_2'], '00', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['dt12_2'], '13', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['time24_2'], '01', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['time24_2'], '09', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['time24_2'], '10', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['time24_2'], '19', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['time24_2'], '20', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['time24_2'], '23', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['time24_2'], '1', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['time24_2'], '24', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['dt12_1_or_2'], '1', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['dt12_1_or_2'], '01', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['dt12_1_or_2'], '12', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['dt12_1_or_2'], '0', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['dt12_1_or_2'], '00', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['dt12_1_or_2'], '13', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['d_delims'], '.', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['d_delims'], '/', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['d_delims'], '-', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['d_delims'], '1', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['d_delims'], ' ', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['d_delims'], '*', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['years_2'], '11', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['years_2'], '1', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['years_2'], '111', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['years_4'], '1111', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['years_4'], '111', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['years_4'], '11111', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['num60_2'], '00', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['num60_2'], '59', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['num60_2'], '6', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['num60_2'], '591', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['num60_2'], '-1', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['t_delims'], ':', 0))
        self.assertTrue(fullmatch(Formats.dt_frags['t_delims'], ' ', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['t_delims'], '.', 0))
        self.assertFalse(fullmatch(Formats.dt_frags['t_delims'], '/', 0))

    def test_date_4_formats(self):
        self.assertTrue(Formats.matches_format('-date-4md', '0101'))
        self.assertFalse(Formats.matches_format('-date-4md', '0132'))
        self.assertTrue(Formats.matches_format('-date-4md-d', '1.23'))
        self.assertFalse(Formats.matches_format('-date-4md-d', '1229'))

    def test_date_6_formats(self):
        self.assertTrue(Formats.matches_format('-date-6mdy', '013100'))
        self.assertFalse(Formats.matches_format('-date-6mdy', '32434'))
        self.assertTrue(Formats.matches_format('-date-6mdy-d', '1.23.00'))
        self.assertFalse(Formats.matches_format('-date-6mdy-d', '122988'))
        self.assertTrue(Formats.matches_format('-date-6dmy', '301100'))
        self.assertFalse(Formats.matches_format('-date-6dmy', '32434'))
        self.assertTrue(Formats.matches_format('-date-6dmy-d', '30-11.00'))
        self.assertFalse(Formats.matches_format('-date-6dmy-d', '01-3214'))

    def test_date_8_formats(self):
        self.assertTrue(Formats.matches_format('-date-8mdy', '01310001'))
        self.assertFalse(Formats.matches_format('-date-8mdy', '01230000'))
        self.assertTrue(Formats.matches_format('-date-8mdy-d', '10.10.1001'))
        self.assertFalse(Formats.matches_format('-date-8mdy-d', '01/30/1'))

    def test_date_9_formats(self):
        self.assertTrue(Formats.matches_format('-date-9mdy-d', 'jan-6-2441'))
        self.assertTrue(Formats.matches_format('-date-9mdy-d', 'feb.10.1001'))
        self.assertFalse(Formats.matches_format('-date-9mdy-d', 'feds.6.3252'))
        self.assertFalse(Formats.matches_format('-date-9mdy-d', 'dec.6.311'))

    def test_word_format(self):
        self.assertTrue(Formats.matches_format('-word', 'aliugaugyLgUKyyu'))
        self.assertTrue(Formats.matches_format('-word', '2732fsgdgs_'))
        self.assertFalse(Formats.matches_format('-word', 'wo rd'))
        self.assertFalse(Formats.matches_format('-word', '^%$&djdrjd%'))
        self.assertFalse(Formats.matches_format('-word', 'word^'))

    def test_time_formats(self):
        self.assertTrue(Formats.matches_format('-time-12', '12:43 AM'))
        self.assertFalse(Formats.matches_format('-time-12', '2:51 Ao'))
        self.assertTrue(Formats.matches_format('-time-12-s', '12:43:45 AM'))
        self.assertFalse(Formats.matches_format('-time-12-s', '1:25:253 P'))
        self.assertTrue(Formats.matches_format('-time-24', '15:43'))
        self.assertFalse(Formats.matches_format('-time-24', '24:09'))
        self.assertTrue(Formats.matches_format('-time-24-s', '17:43:45'))
        self.assertFalse(Formats.matches_format('-time-24-s', '09:73:13 PM'))

    def test_email_format(self):
        self.assertTrue(Formats.matches_format('-email', 'justyhg.egife@hotmail.com'))
        self.assertTrue(Formats.matches_format('-email', 'HUGEHG.EGFUI@gasdg.com'))
        self.assertFalse(Formats.matches_format('-email', 'HUGEHG. EGFUI@gasdg.com'))
        self.assertFalse(Formats.matches_format('-email', '&%^%HUGE(HG.EGFUI@gasdg.com'))
        self.assertFalse(Formats.matches_format('-email', 'HUGEHG.EGFUIgasdg.com'))

    def test_ip4_format(self):
        self.assertTrue(Formats.matches_format('-ip4', '1.1.1.1'))
        self.assertTrue(Formats.matches_format('-ip4', '255.255.255.255'))
        self.assertFalse(Formats.matches_format('-ip4', '98.46.141.255:1000'))
        self.assertFalse(Formats.matches_format('-ip4', '12.6.1.4/24'))
        self.assertFalse(Formats.matches_format('-ip4', '256.0.0.1'))
        self.assertFalse(Formats.matches_format('-ip4', 'sag.14.f31t1'))
        self.assertFalse(Formats.matches_format('-ip4', '1531'))

    def test_url_format(self):
        self.assertFalse(Formats.matches_format('-url', 'espn.com'))
        self.assertTrue(Formats.matches_format('-url', 'www.espn.com'))
        self.assertTrue(Formats.matches_format('-url', 'https://espn.com'))
        self.assertTrue(Formats.matches_format('-url', 'http://url.com'))
        self.assertFalse(Formats.matches_format('-url', '213459aav876va'))
        self.assertFalse(Formats.matches_format('-url', ';287t8c;.com'))
        self.assertFalse(Formats.matches_format('-url', '141.iyiuyiu@hg'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
    