from flask import Flask

app=Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/<name>')           # passing variable in <>
def greet(name):
    return f"Hello {name}!!"


@app.route('/username/<name>')
def greet_user(name):
    return f"Hey there {name}!!"


@app.route('/username/<name>/<int:age>')        # passing parameter with datatype(int,float(both positive))
def greet_age(name,age):
    return f"Hello there {name}. You are {age} years old."


def make_bold(function):
    def wrapper():
      return "<b>"+function()+"</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>"+function()+"</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return "<u>"+function()+"</u>"
    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return 'Bye!!!'


if __name__=="__main__":
    # run in debug mode to reload automatically
    app.run(debug=True)