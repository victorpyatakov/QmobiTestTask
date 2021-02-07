import unittest
from http.server import HTTPServer
from server import RequestHandler
import json
import urllib.request
import urllib.error

class TestServer(unittest.TestCase):  
    def get_code_response(self,url:str)->str:
        """
        Метод для получения кода http ответа
        """
        try:
            conn = urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
           return '{}'.format(e.code)
        except urllib.error.URLError as e:
            return'{}'.format(e.reason)
        else:
            return '200'

    def get_json_response(self, url:str)->dict:
        """
        Метод для получения json по запросу
        """
        webURL = urllib.request.urlopen(url)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        return json.loads(data.decode(encoding))

    def test_code_response(self):
        urlData_1 = "http://localhost:8080/converter/api?currency=usd&amount=54400"
        self.assertEqual(self.get_code_response(urlData_1), '200')

        urlData_2 = "http://localhost:8080/converter/Rapi?currency=usd&amount=54400"
        self.assertEqual(self.get_code_response(urlData_2), '404')
        
        urlData_3 = "http://localhost:8080/converter/api?curran333cy=usd&amount=54400"
        self.assertEqual(self.get_code_response(urlData_3), '404')
        
        urlData_4 = "http://localhost:8080/converter/api?currency=usd&amount=-54400"
        self.assertEqual(self.get_code_response(urlData_4), '404')

        urlData_5 = "http://localhost:8080/converter/api?currency=USSR&amount=54400"
        self.assertEqual(self.get_code_response(urlData_4), '404')

    def test_response_json(self):
        json_1 = {
                'currency': 'usd',
                'amount'  : float('54400'),
                'course'  : 75.1107,
                'result'  : float('{:.2f}'.format(float('54400') / 75.1107) )
        }
        urlData_1 = "http://localhost:8080/converter/api?currency=usd&amount=54400"
        self.assertEqual(self.get_json_response(urlData_1), json_1)

        json_2 = {
                'currency': 'eur',
                'amount'  : float('8000000'),
                'course'  : 89.8850,
                'result'  : float('{:.2f}'.format(float('8000000') / 89.8850) )
        }
        urlData_2 = "http://localhost:8080/converter/api?Currency=eur&Amount=8000000"
        self.assertEqual(self.get_json_response(urlData_2), json_2)


if __name__ == '__main__':
    unittest.main()