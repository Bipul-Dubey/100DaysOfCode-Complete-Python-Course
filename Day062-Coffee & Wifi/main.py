from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,URLField,SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe=StringField('Cafe name', validators=[DataRequired()])
    location=URLField('Location (URL from Google Map)')
    open_time=StringField('Open Time (e.g 8AM)')
    close_time=StringField('Close Time (e.g 9PM)')
    coffee_rating=SelectField('Coffee Rating',default='☕',choices=[('☕'),('☕☕'),('☕☕☕'),('☕☕☕☕'),('☕☕☕☕☕')])
    wifi=SelectField('WiFi Strength Rating',default='✘',choices=[('✘'),('💪'),('💪💪'),('💪💪💪'),('💪💪💪💪'),('💪💪💪💪💪')])
    socket=SelectField('Socket Availability',default='✘',choices=[('✘'),('🔌'),('🔌🔌'),('🔌🔌🔌'),('🔌🔌🔌🔌'),('🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("signup.html")


@app.route('/add',methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        if request.method=='POST':
            with open("cafe-data.csv","a",encoding="utf-8",newline='') as csvfile:
                write=csv.writer(csvfile)
                cafe=request.form['cafe']
                location=request.form['location']
                open_time=request.form['open_time']
                close_time=request.form['close_time']
                coffee_rating=request.form['coffee_rating']
                wifi=request.form['wifi']
                socket=request.form['socket']
                data=[cafe,location,open_time,close_time,coffee_rating,wifi,socket]
                write.writerow(data)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='',encoding="utf-8") as csv_file:
        csv_data=csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
