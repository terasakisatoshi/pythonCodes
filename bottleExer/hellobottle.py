import bottle


@bottle.route('/hello')
def index():
    return '<h1>Hello</h1>'

bottle.run(host='0.0.0.0', port=8080)
