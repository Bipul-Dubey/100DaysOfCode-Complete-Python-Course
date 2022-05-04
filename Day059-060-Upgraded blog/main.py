from flask import Flask, render_template, request
import requests
import smtplib

data=requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

# example data in api
"""
data=[
  {
    "id": 1,
    "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.",
    "title": "The Life of Cactus",
    "subtitle": "Who knew that cacti lived such interesting lives.",
    "author": "author_name",
    "date": "21 sept 2022"
  }
]
"""

app=Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html",all_post=data)


@app.route('/<int:index>')
# @app.route('/post/<int:index>')
def show_post(index):
    req_post=None
    for blog_post in data:
        if blog_post['id']==index:
            req_post=blog_post
    return render_template("post.html",post=req_post)


@app.route('/about')
def about():
    return render_template("about.html")


SENDER_MAIL="smtpcheck9@gmail.com"
SENDER_PASSWORD="Smtp@1111"
RECEIVER_EMAIL="raj12kumar21@yahoo.com"


def sendmail(name,email,phone,msg):
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=SENDER_MAIL,password=SENDER_PASSWORD)
    connection.sendmail(from_addr=SENDER_MAIL,to_addrs=RECEIVER_EMAIL,
                        msg=f"Subject:Connection\n\n"
                            f"Name: {name}\n"
                            f"email: {email}\n"
                            f"phone:{phone}\n"
                            f"Message: {msg}")


@app.route('/contact',methods=["POST","GET"])
def contact():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        number=request.form["phone"]
        msg=request.form["message"]
        sendmail(name,email,number,msg)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__=="__main__":
    app.run(debug=True)
