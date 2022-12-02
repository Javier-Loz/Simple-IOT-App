#https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
import os
from datetime import datetime
from flask import Flask,jsonify,request,Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_expects_json import expects_json

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Medicion(db.Model):
    idMedicion = db.Column('idMedicion',db.Integer,primary_key=True)
    tsMedicion = db.Column('tsMedicion', db.DateTime(timezone=True), default=datetime.utcnow)
    pict = db.Column('pict',db.Text,nullable=False)

    def __init__(self,pict):
        self.pict = pict 

class Results(db.Model):
    idResults = db.Column('idResults',db.Integer,primary_key=True)
    tsResults = db.Column('tsResults', db.DateTime(timezone=True), default=datetime.utcnow)
    resp = db.Column('resp',db.Text,nullable=False)

    def __init__(self,resp):
        self.resp = resp


schema = {
    'type':'object',
    'properties':{
        'file': {'type':'number'},
    },
    'required':['file']
}




@app.route("/Results/newData/<data>", methods=["POST"])
def push_res(data):
    db.session.add(Results(data))
    db.session.commit()

    response = jsonify({"message":"success"})
    response.status_code = 201
    return response


@app.route("/Medicion/newData", methods=["POST"])
def push_img():
    file = request.files['file']
    db.session.add(Medicion(file.read()))
    db.session.commit()

    response = jsonify({"message":"success"})
    response.status_code = 201
    return response

@app.route("/Medicion/getData", methods=["GET"])
def get_img():
    img = Medicion.query.order_by(Medicion.idMedicion.desc()).first()
    return Response(img.pict)

@app.route("/Results/getData", methods=["GET"])
def get_res():
    Res = Results.query.order_by(Results.idResults.desc()).first()
    return Response(Res.resp)

app.run(port=5000)
