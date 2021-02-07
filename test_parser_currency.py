import unittest
from parserCurrency import ParserCurrency

class TestParserCurrency(unittest.TestCase):
    def test_get_curr_list(self):
        self.assertIsInstance(ParserCurrency.get_curr_list(), list)

if __name__ == '__main__':
    unittest.main()