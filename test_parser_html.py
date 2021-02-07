import unittest
from parserHtml import MyHTMLParser


class TestParseHTML(unittest.TestCase):
        def test_get_currency_list(self):
            self.parser_1 = MyHTMLParser()
            self.html_code_1 = '<table><tr><td>data1</td><td>data2</td></tr></table>'
            self.parser_1.feed(self.html_code_1)
            self.assertEqual(self.parser_1.get_currency_list(),[['data1','data2']])
            
            self.parser_2 = MyHTMLParser()
            self.html_code_2 = '<tr><td>data1</td><td>data2</td></tr><tr><td>data3</td><td>data4</td></tr>'
            self.parser_2.feed(self.html_code_2)
            self.assertEqual(self.parser_2.get_currency_list(),[['data1','data2'],['data3','data4']])

            self.parser_3 = MyHTMLParser()
            self.html_code_3 = '<tr></tr>'
            self.parser_3.feed(self.html_code_3)
            self.assertEqual(self.parser_3.get_currency_list(),[])



if __name__ == '__main__':
    unittest.main()