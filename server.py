
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse
from parser import ParserCurrancy
from converter import ConverterCurrancy

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if parse.urlsplit(self.path).path.endswith('/converter/api'):
                params = dict(parse.parse_qsl(parse.urlsplit(self.path).query))

                parser_currancy = ParserCurrancy()
                currency_list = parser_currancy.get_curr_list()
                converter_curr = ConverterCurrancy(currency_list,params)
                result = converter_curr.get_currancy_cource()
                dict_response = {
                    'currancy': params['currancy'],
                    'amount'  : float(params['amount']),
                    'course'  : float(converter_curr.get_currancy_cource()),
                    'result'  : float(converter_curr.get_convert_currancy())
                }

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(dict_response).encode('utf-8'))

            else:
                self.send_error(404,'Page not Found: %s' % self.path)
        except:
            self.send_error(404,'Not correct request parameters: %s' % self.path)

    def get_response(slef,response_parameters:dict):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({'currancy': params['currancy'], 'amount'   : params['amount']}).encode('utf-8'))


port = 8080
print('Listening on localhost:%s' % port)
server = HTTPServer(('', port), RequestHandler)
print('press CTRL + C that stop it')
server.serve_forever()

