from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    """
    Класс для обработки html тегов и данных
    """
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
   

        
