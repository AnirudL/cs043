import wsgiref.simple_server


def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf-8')]
    start_response('200 OK', headers)

    path = environ['PATH_INFO']
    if path == '/biography':
        page = '''<!DOCTYPE html>
        <html><head><title>Biography</title></head><body>
        <h1>Hi, I'm Abraham Lincoln</h1>
        <h2>My Famous Speech</h2>
        <p>"Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal."</p>
        <p>"Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battlefield of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this."</p>
        <p>"But, in a larger sense, we can not dedicate, we can not consecrate, we can not hallow this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth."</p>
        <p>Abraham Lincoln's Gettysberg Address</p>
        <br />
        <img src="https://upload.wikimedia.org/wikipedia/commons/1/10/Lincolnatgettysburg.jpg" />
        <p>By David Bachrach (1845-1921) [Public domain], via Wikimedia Commons</p>
        </body>
        </html>'''

    return [page.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)

print("Serving on port 8000...")

httpd.serve_forever()