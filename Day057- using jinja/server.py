import random
from datetime import date
from flask import Flask,render_template
import requests

app=Flask(__name__)


@app.route('/')
def home():
    curr_year=date.today().year
    ran_num=random.randint(0,9)
    return render_template('signup.html',num=ran_num,current_year=curr_year)


@app.route('/guess/<name>')
def guess(name):
    gender_url=f"https://api.genderize.io?name={name}"
    gender_response=requests.get(gender_url)
    gender_data=gender_response.json()
    gender=gender_data['gender'].title()

    age_url=f"https://api.agify.io?name={name}"
    age_response=requests.get(age_url)
    age_data=age_response.json()
    age=age_data['age']

    return render_template('guess.html',name=name,gender=gender,age=age)


@app.route('/blogs')
def blog():
    blog_url="https://api.npoint.io/3121234e75170ee30f54"
    blog_response=requests.get(blog_url)
    all_blogs=blog_response.json()
    return render_template('blog.html',posts=all_blogs)


if __name__=='__main__':
    app.run(debug=True)