import re
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root@localhost:5432/mitiendadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.secret_key = 'some_secret_key'

db = SQLAlchemy(app)

# Importar modelos
from models import Product

#Crear el esquema del DB
db.create_all()
db.session.commit()


# Rutas de páginas

@app.route('/')
def get_home():
    return "¡Este es el home!"

@app.route('/signup')
def sign_up():
    return 'Esta es la página de registro'

@app.route('/room')
def enter_room():
    return 'Esta es una sala'

# Ruta de otras acciones 

@app.route('/product', methods=['GET','POST'])
def crud_product():
    if request.method == 'GET':
        print("Legó un get")

        # Insertar un producto 
        code_product = '12345'
        name = 'Gaseosa'
        product_type = "Bedidas"
        brand = 'Postobón'
        measure_unit = "2"

        entry= Product(code_product, name, product_type, brand, measure_unit)
        db.session.add(entry)
        db.session.commit()

        return 'Eso fue un GET'

    elif request.method == 'POST':
        # Registrar una canción 
        request_data = request.form
        name = request_data['name']
        size = request_data['size']
        brand = request_data['brand']
        kind = request_data['kind']

        print("Nombre:" + name)
        print("Tamaño:" + size)
        print("Marca:" + brand)
        print("Tipo de producto:" + kind)

        # Insertar en la base de datos 
        return 'Se registró la canción exitosamente'