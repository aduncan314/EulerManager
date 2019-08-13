import unittest

import executor

# The value must be an id for which the module exists, but the function does not
VALUE = 1


class TestExecutor(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(('_0', 'one'), executor._parse_id(1))
        self.assertEqual(('_1', 'two'), executor._parse_id(12))
        self.assertEqual(('_13', 'five'), executor._parse_id(135))

        with self.assertRaises(ValueError):
            executor._parse_id(-1)

    def test_get_func(self):
        self.assertEqual("Test function successfully completed", executor._get_soln_func(0)())
        with self.assertRaises(RuntimeError):
            executor._get_soln_func(99999999)

        with self.assertRaises(RuntimeError):
            executor._get_soln_func(VALUE)
