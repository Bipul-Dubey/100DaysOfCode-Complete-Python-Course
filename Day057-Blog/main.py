from flask import Flask, render_template

import requests
response=requests.get("https://api.npoint.io/4af156202f984d3464c3")
data=response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html",all_post=data)


@app.route('/post/<int:index>')
def post(index):
    return render_template("post.html",all_post=data,num=index)


if __name__ == "__main__":
    app.run(debug=True)
