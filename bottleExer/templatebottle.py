from bottle import route, request, run, template


@route('/hello')
def index(user=''):
    username = request.query.get('user')
    return template('<h1>Helll {{ user }}</h1>', user=username)

run(host='0.0.0.0', port=8080)
