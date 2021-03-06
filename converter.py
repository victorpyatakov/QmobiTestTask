class ConverterCurrency():
    """
    Класс конвертера валют
    """
    def __init__(self, currency_list: list, request_params: dict):
        self.__currency_list = currency_list
        self.__request_params = request_params

    def get_currency_cource(self):
        """
        Метод, который возвращает значение курса для валюты
        """
        try:
            currency = self.__request_params['currency']
            for ls in self.__currency_list:
                if currency.upper() in ls:
                    return ls[-1].replace(',','.')
        except:
            return -1
        return -1
    
    def get_convert_currency(self):
        """
        Метод, который возвращает результат конвертации
        """
        try:
            amount = self.__request_params['amount']
            course = self.get_currency_cource()
            result = float(amount) / float(course.replace(',','.'))
            return  '{:.2f}'.format(result) 
        except:
            return -1
        