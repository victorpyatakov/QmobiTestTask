class ConverterCurrancy():
    def __init__(self, currency_list: list, request_params: dict):
        self.__currency_list = currency_list
        self.__request_params = request_params

    def get_currancy_cource(self):
        curruncy = self.__request_params['currancy']
        for ls in self.__currency_list:
            if curruncy.upper() in ls:
                return ls[-1].replace(',','.')
        return 1.0
    
    def get_convert_currancy(self):
        amount = self.__request_params['amount']
        course = self.get_currancy_cource()
        result = float(amount) / float(course.replace(',','.'))
        return  '{:.2f}'.format(result) 
        