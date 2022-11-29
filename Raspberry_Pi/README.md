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

