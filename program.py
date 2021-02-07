from server import RequestHandler
from http.server import HTTPServer


if __name__ == '__main__':
    port = 8080
    host = 'localhost'
    print('Listening on localhost:%s' % port)
    server = HTTPServer((host, port), RequestHandler)
    print('press CTRL + C that stop server')
    server.serve_forever()
