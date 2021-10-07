from flask import Flask, request, render_template
from flask.wrappers import Request #request importado para manejar peticiones que llegan al servidor
from flask_sqlalchemy import SQLAlchemy #importada para trabajar de python a SQL bases de datos
from sqlalchemy.orm import session

app = Flask(__name__)
#conexion a la base de datos: 'postgresql://<usuario>:<contraseña>@<direccion de la db>:<puerto>/<nombre de la db>'
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://vkxloqhhabrinb:6afc88e11ca5780df6635e9113813dcad93c3a94a8c3337f98ba2711ebcda892@ec2-35-171-171-27.compute-1.amazonaws.com:5432/dam05ju1pfpbir'
# esta es la direccion para la base de datos local, ahora es remota de heroku linea anterior, y se va'postgresql://postgres:root@localhost:5432/mitiendadb2'
#app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:root@localhost:5432/mitiendadb2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key ='some-secret-key'

# definiendo la basse de datos en el codigo
db = SQLAlchemy(app) # este app o lo que sea va en el procfile kkllk:app

# importar los modelos de las tablas que cree en el otro archivo
from models import Product, NewUser


#crear el esquema de la base de datos en postgre
db.create_all()
db.session.commit() #guardar los cambios siempre, crea  las tablas


# Rutas del Proyecto, este es como el controlador
# que conecta la vista
# y el modelo, en este caso DB

# Pagina principal de la aplicacion, envia al registro o al ingreso como Admin o Tendero
@app.route('/')
def get_home():
    return render_template("index.html") # Home

# ingreso para registro, viene de home
@app.route('/signup')
def sing_up():
    return  render_template("register.html") #'Aqui va redirigido a otra html con el formulario de registro /sign_updata

# post de los datos del registro, viene de signup
@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form["email"] #trae los datos de los form de html
    password = request.form["password"]
    telephone = request.form["telephone"]
    role = request.form["role"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    birthDate = request.form["birthDate"]
    print (email, password, telephone, role, name, lastname, birthDate)
    newUser = NewUser(email, password, telephone, role, name, lastname, birthDate)  
    db.session.add(newUser)  #creado y agregado a base de datos
    db.session.commit()
    return "ok"
'''
# ingreso para ingreso, viene de home Administrador
@app.route('/signin')
def sing_in():
    return  render_template("signin_admin.html")

# acceso como administrador, debe ir al panel de administrador
@app.route('/signin_admin', methods=['POST'])
def sing_in_ad():
    email = request.form["email"]
    passwordin = request.form["password"]
    return (email, passwordin)
'''
'''def get_user():
    user = NewUser.query.email() 
    password_ok = NewUser.query.password()
    return (user, password_ok) 
if email == user & passwordin==pasword_ok:
    print ("Bienvenido")
    # enviar a panel de administrador
else:
    print ("Acceso Denegado")
    # retornar a home'''
'''
# acceso como tendero, viene de Home, va al manejo de ventas y compras
@app.route('/signin_grocer')
def sing_in():
    return 'Aqui va el Acceso' # Acceso

@app.route('/adminstock')
def admin_stock():
    return 'Aqui va el panel del administrar inventario, stock' # Panel de inventario

@app.route('/statistics')
def statistics():
    return 'Aqui va el panel de estadisticas e historial' # Historial y estadisticas

@app.route('/sales')
def sales():
    return 'Aqui va el panel de ventas' # Gestion de ventas de la tienda

@app.route('/purchases')
def purchases():
    return 'Aqui va el panel de compras a proveedores' # Gestion de compra de inventario

@app.route('/admin')
def admin():
    return 'Aqui va el panel del admin' # Panel de administrador

## Rutas de acciones

@app.route('/section')
def section():
    return "seccion"    
    #return render_template("section.html")

@app.route('/inventary', methods=['POST'])    
def inventary():
    code_product = request.form["code_product"]
    print ("The code product is: ")
    print(code_product)
    return "Inventary"
    #return render_template("inventary.html")

#insertar producto html
#@app.route('/newproducts')
#def newproducts():
    #return render_template("newproducts.html")

@app.route('/create-p', methods=['POST'])
def create_product():
    name = request.form["name"]
    codeproduct = request.form['codeproduct']   
    brand = request.form['brand']   
    productType = request.form['productType']   
    admissionDate = request.form['admissionDate']   
    measureUnit = request.form['measureUnit']   
    ivaTax = request.form['ivaTax']   
    stock = request.form['stock'] 
    # stockmin = request.form['stockmin'] 
    #  amount = request.form['amount'] 
    entry = Product(name, codeproduct, brand, productType, admissionDate, measureUnit, ivaTax, stock)  
    db.session.add(entry)  
    db.session.commit()
    return "ok"

# esto es una prueba de consulta y modificacion

@app.route('/updateproduct')
def update_product():
    old_name ="leche"
    new_name = "leche deslactosada"
    old_product = Product.query.filter_by(name=old_name).first() #esto es una consulta por columna name, el primer campo
    old_product.name = new_name # se cambia el nombre
    db.session.commit()
    return "actualizacion exitosa" 

## aqui consulta la lista de productos
@app.route('/getproducts')
def get_products():
    products = Product.query.all() #para traerlo todo, el producto es un objeto
    print(products[0].name)
    return "trae lista de productos"

#aqui borra productos
@app.route('/deleteproducts')
def delete_product():
    product_name="leche deslactosada"
    product = Product.query.filteer_by(name=product_name).first()
    db.session.delete(product)
    db.session.commit()
    return "Se borro producto"


# cRUD User

@app.route('/updateUser')
def update_user():
    old_name ="leche"
    new_name = "leche deslactosada"
    old_product = Product.query.filter_by(name=old_name).first() #esto es una consulta por columna name, el primer campo
    old_product.name = new_name # se cambia el nombre
    db.session.commit()
    return "actualizacion exitosa" 

## aqui consulta la lista de user
@app.route('/getUser')
def get_user():
    products = Product.query.all() #para traerlo todo, el user es un objeto
    print(products[0].name)
    return "trae lista de user"

#aqui borra user
@app.route('/deleteuser')
def delete_user():
    product_name="leche deslactosada"
    product = Product.query.filteer_by(name=product_name).first()
    db.session.delete(product)
    db.session.commit()
    return "Se borro user"

'''
#Pruebas con postman

'''@app.route('/product', methods = ['GET','POST']) # definir ruta y le dije que acepte post y get una vez cambie datos no me acepta de nuevo

def crud_product(): # metodo, para probar es con postman
    if request.method == 'GET':
        # creo el producto en la db, mientras creamos la html, es uns prueba
        name = "Huevos"
        stock= 35
        measureUnit = "unidad A"
        codeProduct = 129
        productType = "Proteinas"
        brand = "Santa Lucia"
        date = 30
        price = 450
        ivaTax = 19
        salePrice = 2800

        entry = Product (name, stock, measureUnit, codeProduct, productType, brand, date, price, ivaTax,salePrice)
        db.session.add(entry)
        db.session.commit()
        
        print('llego un GET')
        return "Esto fue un GET"

    elif request.method == 'POST':
        # Registrar un producto
        request_data = request.form
        #form es el formato en que se envian los datos, request_data es la variable que es un diccionario
        
        name = request_data['name']
        stock= request_data['stock']
        measureUnit = request_data['measureUnit']
        codeProduct = request_data['codeProduct']
        productType = request_data['productType']
        brand = request_data['mark']
        date = request_data['date']
        price = request_data['price']
        ivaTax = request['ivaTax']
        salePrice = request['salePrice']

        # insertar en base de datos el producto

        print ('Producto: ' + name, 'Cantidad: ' + stock, 'Presentacion: ' + measureUnit, 'price: '+ price)
        print ('code: ' + codeProduct, 'productType: ' + productType, 'mark: ' + brand, 'date:'+ date, 'IVA: ' + ivaTax , 'salePrice: ' + salePrice)
        return "Registro Exitoso"

     '''

if __name__ == "__main__":
	    app.run()