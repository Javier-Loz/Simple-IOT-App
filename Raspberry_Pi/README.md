# Implementación en Raspberry Pi

## Instalación de Dependencias

## Creación de Base de Datos con FLASK

Se requiere de dos tablas para lamacenar información, la tabla "Mediciones" y la tabla "Respuestas". 
Ambas se diseñaron usando la herramienta [Flask](https://flask.palletsprojects.com/en/2.2.x/)

Instanciar la aplicaión ```app```

```
app = Flask(__name__)
```

Declarar el directorio en el que se almacenará la base de datos ```database.db```

```
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

Instanciar la base de datos ```db```

```
db = SQLAlchemy(app)
```
Declarar el tabla de almacenamiento como un objetio de tipo [Model](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)

```
class Medicion(db.Model):
    idMedicion = db.Column('idMedicion',db.Integer,primary_key=True)
    tsMedicion = db.Column('tsMedicion', db.DateTime(timezone=True), default=datetime.utcnow)
    pict = db.Column('pict',db.Text,nullable=False)

    def __init__(self,pict):
        self.pict = pict   
```
Cada columna se declara como un atributo de la siguiente manera:

- Se declaran según los [tipos de datos](https://www.ibm.com/docs/es/iis/11.5?topic=stage-sql-data-types) en SQL

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

## Hacer POST de archivos a la DB
Los POST se hacen mediante la herramienta [requests](https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests) de python, la cuál cuenta con métodos para subir archivos.

```
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


