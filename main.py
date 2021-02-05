from html.parser import HTMLParser
from urllib.request import urlopen
import ssl

#  для работы urlopen
context = ssl._create_unverified_context()

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
            
        
    def get_currancy(self):
        """
        Возвращает итоговый список после обработки
        """
        return self.__usd_currency

    

# скачали страницу
f = urlopen('https://cbr.ru/currency_base/daily/',context=context).read().decode('utf-8')

# учимся парсить страницу
parser = MyHTMLParser()
page = '<tbody><tr><td>036</td><td>AUD</td><td>1</td><td>Австралийский доллар</td><td>57,9959</td></tr></tbody>'
parser.feed(f)
usd_currency = parser.get_currancy()
for ls in usd_currency:
    print(ls, end='\n')


