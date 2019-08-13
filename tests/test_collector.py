import unittest

import collector


class TestCollector(unittest.TestCase):
    def test_call_by_id(self):
        parsed = ('Multiples of 3 and 5',
                  'If we list all the natural numbers below 10 that are multiples of 3 or 5, we '
                  'get 3, 5, 6 and 9. The sum of these multiples is 23.\n'
                  'Find the sum of all the multiples of 3 or 5 below 1000.')
        self.assertEqual(parsed, collector.call_by_id(1))
        self.assertEqual(2, len(collector.call_by_id(57)))

    def test_parse_question(self):
        html = "<h2>title</h2><h3>NOT TITLE</h3><div class='problem_content'><p>content</p></div" \
               "<div><p>NOT CONTENT</p></div>"
        self.assertEqual(('title', 'content'), collector._parse_question(html))
        with self.assertRaises(IndexError):
            collector._parse_question('<h1>kljs</h1>')
        with self.assertRaises(IndexError):
            collector._parse_question('<h2>kljs</h2>')
