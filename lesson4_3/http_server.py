#http_server.py
import wsgiref.simple_server

def application(environ, start_response: object):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    start_response('200 OK', headers)
    return ['Hello World!'.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()