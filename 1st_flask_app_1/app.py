from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('first_app.html')

def main():
    app.run()
    
if __name__ == '__main__':
    main()