def application(environ, start_response):
    status = '200 OK'
    header = [
        ('Content-Type', 'text/plain')
    ]
    resp = environ.get('QUERY_STRING').split("&")
    stroka = ''
    for item in resp:
        stroka += item+'\r\n'
    start_response(status, header)
    return stroka
