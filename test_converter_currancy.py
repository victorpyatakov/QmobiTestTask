import unittest
from converter import ConverterCurrancy

class TestConverterCurrancy(unittest.TestCase):
    def setUp(self):
        self.currancy_list = [['USD','75,4'],['EUR','89,9']]

    def test_get_currancy_cource(self):
        req_par_1 = {'currancy':'usd', 'amount': '44549'}
        converter_curruncy_1 = ConverterCurrancy(self.currancy_list,req_par_1)
        self.assertEqual(converter_curruncy_1.get_currancy_cource(), '75.4')
        
        req_par_2 = {'currancy':'USSR', 'amount': '44549'}
        converter_curruncy_2 = ConverterCurrancy(self.currancy_list,req_par_2)
        self.assertEqual(converter_curruncy_2.get_currancy_cource(), -1)

        req_par_3 = {'currancy1':'USSR', 'amount': '44549'}
        converter_curruncy_3 = ConverterCurrancy(self.currancy_list,req_par_3)
        self.assertEqual(converter_curruncy_3.get_currancy_cource(), -1)
        
    def test_get_convert_currancy(self):
        req_par_1 = {'currancy':'usd', 'amount': '44549'}
        converter_curruncy_1 = ConverterCurrancy(self.currancy_list,req_par_1)
        self.assertEqual(converter_curruncy_1.get_convert_currancy(), '{:.2f}'.format(44549 / 75.4) )
        
        req_par_2 = {'currancy':'usd', 'amount': '0'}
        converter_curruncy_2 = ConverterCurrancy(self.currancy_list,req_par_2)
        self.assertEqual(converter_curruncy_2.get_convert_currancy(), '{:.2f}'.format(0) )
        
        req_par_3 = {'currancy':'usd', 'amount1': '44549'}
        converter_curruncy_3 = ConverterCurrancy(self.currancy_list,req_par_3)
        self.assertEqual(converter_curruncy_3.get_convert_currancy(), -1)
        
        req_par_4 = {'currancy':'usd1', 'amount': '44549'}
        converter_curruncy_4 = ConverterCurrancy(self.currancy_list,req_par_4)
        self.assertEqual(converter_curruncy_4.get_convert_currancy(), -1)

        req_par_5 = {'currancy1':'usd', 'amount': '44549'}
        converter_curruncy_5 = ConverterCurrancy(self.currancy_list,req_par_5)
        self.assertEqual(converter_curruncy_5.get_convert_currancy(), -1)
        

if __name__ == "__main__":
    unittest.main()