from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World with Flask"

@app.route('/user/<name>')
def user(name):
    #example: access http://127.0.0.1:5000/user/dave
    return '<h1> Hello, %s </h1>' % name


def main():
    app.run(port=5000, debug=False, host='0.0.0.0')
if __name__ == '__main__':
    main()
