from flask import Flask, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class TodoList(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(150), unique=True, nullable=False)

    def __repr__(self):
        return self.text

# db.create_all()


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=="POST":
        text=request.form.get("text")
        add_todo=TodoList(text=text)
        db.session.add(add_todo)
        db.session.commit()
    lists=TodoList.query.all()
    return render_template('index.html',lists=lists)


@app.route("/delete/<list_id>")
def delete(list_id):
    post_to_delete=TodoList.query.get(list_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__=='__main__':
    app.run(debug=True)