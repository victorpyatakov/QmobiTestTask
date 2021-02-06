from html.parser import HTMLParser
from urllib.request import urlopen
import ssl

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__usd_currency = []
        self.__i = -1

    def handle_starttag(self, tag, attrs):
        """
        Обработка открывающего html тега
        """
        if tag == 'tr':
            self.__usd_currency.append([])
            self.__i+=1 
        
    def handle_endtag(self, tag):
        """
        Обработка закрывающего html тега
        """
        if tag == 'tr':
            if not self.__usd_currency[self.__i]:
                self.__usd_currency.remove(self.__usd_currency[self.__i])
                self.__i-=1
        
    def handle_data(self, data):
        """
        Обработка данных внутри тега
        """
        if self.get_starttag_text() == '<td>':
            if data.replace(" ", "") != '\r\n':
                self.__usd_currency[self.__i].append(data)
            
        
    def get_currancy_list(self):
        """
        Возвращает итоговый список после обработки
        """
        return self.__usd_currency
   
class ParserCurrancy():
    def __init__(self):
        self.context = ssl._create_unverified_context()
        self.page_currency = urlopen('https://cbr.ru/currency_base/daily/',context=self.context).read().decode('utf-8')
        self.parser = MyHTMLParser()
        self.parser.feed(self.page_currency)
        self.currency_list = self.parser.get_currancy_list()
    
    def get_curr_list(self):
        return  self.currency_list
        
