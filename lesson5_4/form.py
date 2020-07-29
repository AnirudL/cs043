import wsgiref.simple_server


def application(environ, start_response):
    page = '''<!DOCTYPE html>
<html>
<head><title>Simple Form</title></head>
<body>
<h1>A web form</h1>
<form>
    Username <input type="text" name="username"value="Enter username"><br>
    Password <input type="password" name="pw"><br>
    <input type="submit" value="Log me in">
</form>
<hr>
<p>PATH_INFO: {}</p>
<p>QUERY_STRING: {}</p>
</body></html>'''.format(environ['PATH_INFO'], environ['QUERY_STRING'])

    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    return [page.encode()]

httpd = wsgiref.simple_server.make_server('', 3000, application)
httpd.serve_forever()