from flask import Flask
from random import randint
rand_num=randint(0,9)
app=Flask(__name__)


@app.route('/')
def high_low():
    return "<h1>Guess A Number Between 0 to 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='gif' width='300' height='300'>"


@app.route('/<int:number>')
def guess_number(number):
    if number<rand_num:
        return '<h1 style="color:red">To low, Try again</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="gif" width="300" height="300">'
    elif number>rand_num:
        return '<h1 style="color: purple">To High, Try again</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="gif" width="300" ' \
               'height="300">'
    else:
        return '<h1 style="color:green">Yeh, You Got it!!!!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="gif" width="300" height="300">'


if __name__=="__main__":
    app.run(debug=True)