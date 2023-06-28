# Data Base and API implementation 

## Dependencias
```
import os
from datetime import datetime
from flask import Flask,jsonify,request,Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
```
## Creating a Data Base using Flask

In order to create the desired Data Base and being able to write and read information form it we will use the tools provided by Flask

### 1. Instance the Flask Application

```
app = Flask(__name__)
```

### 2. Write the Data Base

#### Define the file in which the DB will be stored  ```database.db```

```
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

#### Instance the DB ```db```

```
db = SQLAlchemy(app)
```

#### Instance a table using flaskj DB [Model](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)
As many tables as required can be created and they will be stored on the file prevously defined
Note: check the data type that suits best the type of data to be published
```
class SensorRead(db.Model):
    SensorRead_id = db.Column('SensorRead_id',db.Integer,primary_key=True)
    SensorRead_ts = db.Column('SensorRead_ts', db.DateTime(timezone=True), default=datetime.utcnow)
    SensorRead_data  = db.Column('SensorRead_data',db.Float,nullable=False)
    def __init__(self,SensorRead):
        self.SensorRead = SensorRead
```
The table can have as many columns as desired, simply follow the sintaxis using [sql_data-Types](https://www.ibm.com/docs/es/iis/11.5?topic=stage-sql-data-types) 

```
columnName = db.Column('columnName',db.dataType)
```
### Importante 
Utilizar el comando db.create_all() dentro de este archivo genera un error, por lo que las bases de datos se crean dentro de la terminal de flask ```flask shell```
- Dentro del ambiente virtual creado con ```virtualenv "nombre_del_ambiente"```
```
(source)pi@pi:~/flaskProyectDirectory$ export FLASK_APP=app 
(source)pi@pi:~/flaskProyectDirectory$ flask shell
>>> from app import db, ModelName
>>> db.create_all()
```
### Nota
No se pueden sobrescribir las bases de datos, si se hace algún cambio se tiene que eliminar la anterior y crearla de nuevo:
```
(source)pi@pi:~/flaskProyectDirectory$ flask shell
>>> from app import db, ModelName
>>> db.drop_all()
>>> db.create_all()
```

## Métodos route para la Api
- POST
Los POST y GET se hacen mediante la herramienta [requests](https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests) de python, la cuál cuenta con métodos para subir archivos.

```
@app.route("/newData", methods=["POST"])
def push_data():
    
    file = request.files['file']
    # se crea un objeto Medicion para la tabla con el archivo a subir
    db.session.add(Medicion(file.read()))
    db.session.commit()
```
- Referencia al método POST para archivos
```
url = ' http://siteUrl/Medicion/newData'
files = {'file': open('image.png', 'rb')}

r = requests.post(url,files=files)
```
- GET
```
url = ' http://siteUrl/Medicion/getData'

r = requests.get(url)
# guardar los datos en un archivo .png
with open("response.png","wb") as file:
	file.write(r.content)
```
## Programa principal 
Cada 15 segundos se obtiene, de la base de datos, la fotografía a analizar; Se ejecuta el reconocimiento facial, se genera una respuesta y se hace POST de 
esa respuesta a la tabla Results. 
- Se usó [dlib y opencv-python](https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65) para hacer el reconocimiento facial.
Dentro de ```main.py```:
-Obtener la imagen
```
def getData(URL,filename):
```
-Subir el resultado del reconocimiento facial
```
def postResponse(response,URL):
```
-Reconocimiento facial
```
def faceRecon(filename):
```
