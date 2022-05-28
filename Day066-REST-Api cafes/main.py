from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,URLField,BooleanField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key="secret_code"
Bootstrap(app)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # convert to dictionary
    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Form(FlaskForm):
    name=StringField("Cafe Name: ",validators=[DataRequired()])
    map_url=URLField("Google Map Url: ",validators=[DataRequired()])
    img_url=URLField("Cafe Image Url: ",validators=[DataRequired()])
    loc=StringField("Location: ",validators=[DataRequired()])
    seats = StringField("No of Seats: ",validators=[DataRequired()])
    toilet= BooleanField("Has Toilets?: ")
    wifi=BooleanField("Has Wifi?: ")
    sockets=BooleanField("Has Sockets? (1/0): ")
    calls=BooleanField("Can Take Calls (1/0): ")
    coffee_price=StringField("Coffee Price: ",validators=[DataRequired()])
    submit=SubmitField("ADD CAFE")


class EditForm(FlaskForm):
    new_price=StringField("Enter New Price: ",validators=[DataRequired()])
    submit=SubmitField("Update Price")


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def random():
    cafes=Cafe.query.all()
    random_cafe=choice(cafes)

    # return jsonify(
    #     {
    #         'cafe':{
    #             'id':random_cafe.id,
    #             'name':random_cafe.name,
    #             'map_url':random_cafe.map_url,
    #             'img_url':random_cafe.img_url,
    #             'location':random_cafe.location,
    #             'has_sockets':random_cafe.has_sockets,
    #             'has_toilet':random_cafe.has_toilet,
    #             'has_wifi':random_cafe.has_wifi,
    #             'can_take_calls':random_cafe.can_take_calls,
    #             'seats':random_cafe.seats,
    #             'coffee price':random_cafe.coffee_price
    #         }
    #     }
    # )

    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def all_cafe():
    cafes=Cafe.query.all()
    cafe_list=[]
    for cafe in cafes:
        cafe_dict={
            'id':cafe.id,
            'name':cafe.name,
            'map_url':cafe.map_url,
            'img_url':cafe.img_url,
            'location':cafe.location,
            'has_sockets':cafe.has_sockets,
            'has_toilet':cafe.has_toilet,
            'has_wifi':cafe.has_wifi,
            'can_take_calls':cafe.can_take_calls,
            'seats':cafe.seats,
            'coffee price':cafe.coffee_price
        }
        cafe_list.append(cafe_dict)
    all_cafes={'cafes':cafe_list}
    all_cafes_json=jsonify(cafes=all_cafes['cafes'])
    return all_cafes_json


@app.route('/search')
def get_cafe_location():
    query_location=request.args.get("loc")
    cafe=Cafe.query.filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={'Not Found':"Sorry, We don't have cafe at this location"})


# HTTP POST - Create Record
@app.route('/add',methods=['POST','GET'])
def add_new_cafe():
    form=Form()
    if form.validate_on_submit():
        new_cafe=Cafe(
                name=request.form.get("name"),
                map_url = request.form.get("map_url"),
                img_url = request.form.get("img_url"),
                location = request.form.get("loc"),
                has_sockets = bool(request.form.get("sockets")),
                has_toilet = bool(request.form.get("toilet")),
                has_wifi = bool(request.form.get("wifi")),
                can_take_calls = bool(request.form.get("calls")),
                seats = request.form.get("seats"),
                coffee_price = request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"Success":"Successfully added a new cafe"})
    return render_template("add.html", form=form)


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>',methods=['POST','GET'])
def update(cafe_id):
    form=EditForm()
    new_price=request.form.get('new_price')
    cafe=Cafe.query.get(cafe_id)
    if form.validate_on_submit():
        if cafe:
            cafe.coffee_price=new_price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
    return render_template('update.html',form=form)


# HTTP DELETE - Delete Record
@app.route('/delete/<int:cafe_id>',methods=["GET","POST"])
def delete_record(cafe_id):
    cafe=Cafe.query.get(cafe_id)
    api_key=request.args.get("api-key")
    if api_key=="TopSecretAPIKey":
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
    else:
        return jsonify(error={"Forbidden":"Sorry, that's not allowed."})

if __name__ == '__main__':
    app.run(debug=True)
