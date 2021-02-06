
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse
from parserCurrancy import ParserCurrancy
from converter import ConverterCurrancy

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if parse.urlsplit(self.path).path.endswith('/converter/api'):
                
                request_params = dict(parse.parse_qsl(parse.urlsplit(self.path).query))
                '''
                parser_currancy = ParserCurrancy()

                currency_list = parser_currancy.get_curr_list()
'''
                currency_list = ParserCurrancy.get_curr_list()

                converter_curr = ConverterCurrancy(currency_list, request_params)

                course = float(converter_curr.get_currancy_cource())
                if course < 0:
                    self.send_error(404,'currancy not found: %s' % self.path)
                    return

                result = float(converter_curr.get_convert_currancy())
                if result < 0:
                    self.send_error(404,'amount must be > 0 : %s' % self.path)
                    return

                dict_response = {
                    'currancy': request_params['currancy'],
                    'amount'  : float(request_params['amount']),
                    'course'  : course,
                    'result'  : result
                }
                self.get_response(dict_response)
            else:
                self.send_error(404,'Page not Found: %s' % self.path)
        except:
            self.send_error(404,'Not correct request parameters: %s' % parse.urlsplit(self.path).query)

    def get_response(self,response_parameters:dict):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response_parameters).encode('utf-8'))


port = 8080
print('Listening on localhost:%s' % port)
server = HTTPServer(('', port), RequestHandler)
print('press CTRL + C that stop it')
server.serve_forever()

