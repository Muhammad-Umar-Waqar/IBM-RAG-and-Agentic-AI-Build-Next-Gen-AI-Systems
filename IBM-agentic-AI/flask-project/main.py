from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello World'


@app.route('/home')
def Home():
    return 'Home Content'

@app.route('/about')
def About():
    return 'About Content'


if __name__=='__main__':
    app.run(debug=True)