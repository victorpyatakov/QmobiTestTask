
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse
from parserCurrency import ParserCurrency
from converter import ConverterCurrency

class RequestHandler(BaseHTTPRequestHandler):
    """
    Класс для обработки http запросов
    """
    def do_GET(self):
        try:
            if parse.urlsplit(self.path).path.endswith('/converter/api'):
                request_params = dict(parse.parse_qsl(parse.urlsplit(self.path).query.lower()))
                if 'currency' in request_params and 'amount' in request_params:
                    converter_currency = ConverterCurrency(ParserCurrency.get_curr_list(), request_params)
                    course = float(converter_currency.get_currency_cource())
                    if course < 0:
                        self.send_error(404,'currency not found: %s' % self.path)
                        return
                    result = float(converter_currency.get_convert_currency())
                    if result < 0:
                        self.send_error(404,'amount must be > 0 : %s' % self.path)
                        return
                    dict_response = self.get_response_json(request_params,course,result)
                    self.get_response(dict_response)
                else:
                    self.send_error(404,'Not correct request parameters: %s' % parse.urlsplit(self.path).query)
            else:
                self.send_error(404,'Page not Found: %s' % self.path)
                
        except:
            self.send_error(404,'Not correct request parameters: %s' % parse.urlsplit(self.path).query)

    def get_response(self,response_parameters:dict):
        """
        Метод для формирования ответов на запрос
        """
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response_parameters).encode('utf-8'))

    def get_response_json(self,request_params:dict, course:float, result:float)->dict:
        """
        Метод для формирования JSON 
        """
        dict_response = {
                            'currency': request_params['currency'],
                            'amount'  : float(request_params['amount']),
                            'course'  : course,
                            'result'  : result
        }
        return dict_response


