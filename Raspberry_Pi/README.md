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
