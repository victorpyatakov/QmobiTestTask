import unittest
from converter import ConverterCurrency

class TestConverterCurrency(unittest.TestCase):
    def setUp(self):
        self.currency_list = [['USD','75,4'],['EUR','89,9']]

    def test_get_currency_cource(self):
        req_par_1 = {'currency':'usd', 'amount': '44549'}
        converter_currency_1 = ConverterCurrency(self.currency_list,req_par_1)
        self.assertEqual(converter_currency_1.get_currency_cource(), '75.4')
        
        req_par_2 = {'currency':'USSR', 'amount': '44549'}
        converter_currency_2 = ConverterCurrency(self.currency_list,req_par_2)
        self.assertEqual(converter_currency_2.get_currency_cource(), -1)

        req_par_3 = {'currency1':'USSR', 'amount': '44549'}
        converter_currency_3 = ConverterCurrency(self.currency_list,req_par_3)
        self.assertEqual(converter_currency_3.get_currency_cource(), -1)
        
    def test_get_convert_currency(self):
        req_par_1 = {'currency':'usd', 'amount': '44549'}
        converter_currency_1 = ConverterCurrency(self.currency_list,req_par_1)
        self.assertEqual(converter_currency_1.get_convert_currency(), '{:.2f}'.format(44549 / 75.4) )
        
        req_par_2 = {'currency':'usd', 'amount': '0'}
        converter_currency_2 = ConverterCurrency(self.currency_list,req_par_2)
        self.assertEqual(converter_currency_2.get_convert_currency(), '{:.2f}'.format(0) )
        
        req_par_3 = {'currency':'usd', 'amount1': '44549'}
        converter_currency_3 = ConverterCurrency(self.currency_list,req_par_3)
        self.assertEqual(converter_currency_3.get_convert_currency(), -1)
        
        req_par_4 = {'currency':'usd1', 'amount': '44549'}
        converter_currency_4 = ConverterCurrency(self.currency_list,req_par_4)
        self.assertEqual(converter_currency_4.get_convert_currency(), -1)

        req_par_5 = {'currency1':'usd', 'amount': '44549'}
        converter_currency_5 = ConverterCurrency(self.currency_list,req_par_5)
        self.assertEqual(converter_currency_5.get_convert_currency(), -1)
        

if __name__ == "__main__":
    unittest.main()