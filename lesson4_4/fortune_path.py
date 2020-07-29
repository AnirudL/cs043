fortune_path.py
fortune = […] #Enter all the fortunes here
def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    path = environ['PATH_INFO'].split('/') #Takes the environment variables (everything after .com or .net and splits it up at every / character, storing each part in a list.
    if path[1] == "fortune": #If the first entry in the list is “fortune”, then this code is executed
        start_response('200 OK', headers)
        cookie_number = int(path[2])
        return [fortune[cookie_number].encode()]
    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]