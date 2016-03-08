def wsgi_application(environ, start_response):
    status = '200 OK'
    header = [
        ('Content-Type', 'text/plain')
    ]
    body = environ.get('QUERY_STRING')
    stroka = body[body.find('?')+1: ]
    stroka = stroka.split('&')
    start_response(status, header)
    return stroka[0], stroka[1], stroka[2]
