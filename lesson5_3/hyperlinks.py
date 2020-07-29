import wsgiref.simple_server


def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf-8')]
    start_response('200 OK', headers)

    path = environ['PATH_INFO']
    if path == '/page1':
        page = '''<!DOCTYPE html>
        <html><head><title>Page Title</title></head>
        <body>
        <h1>You are on Page 1</h1>
        <p>Hello</p>
        <p>Go to <a href="/page2">Page 2</a></p>
        </body>
        </html>'''

    elif path == '/page2':
        page = '''<!DOCTYPE html>
        <html><head><title>Page Title</title></head>
        <body>
        <h1>You are on Page 2</h1>
        <p>Goodbye</p>
        <p>Go to <a href="/page1">Page 1</a></p>
        </body>
        </html>'''

    return [page.encode()]

httpd = wsgiref.simple_server.make_server('', 4000, application)
httpd.serve_forever()