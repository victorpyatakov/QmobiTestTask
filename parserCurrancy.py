from parserHtml import MyHTMLParser
from urllib.request import urlopen
import ssl

class ParserCurrancy():
    """
    Класс для получения списка валют после парсинга страницы
    """
    '''
    def __init__(self):
        self.__context = ssl._create_unverified_context()
        self.__page_currency = urlopen('https://cbr.ru/currency_base/daily/',context=self.__context).read().decode('utf-8')
        self.__parser = MyHTMLParser()
        self.__parser.feed(self.__page_currency)
        self.__currency_list = self.__parser.get_currancy_list()
    '''
    @staticmethod
    def get_curr_list():
        """
        Метод для получения списка валют
        """
        context = ssl._create_unverified_context()
        page_currency = urlopen('https://cbr.ru/currency_base/daily/',context=context).read().decode('utf-8')
        parser = MyHTMLParser()
        parser.feed(page_currency)
        currency_list = parser.get_currancy_list()
        return currency_list