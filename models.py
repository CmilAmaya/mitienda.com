#creacion de tablas
from app import db #importo la tabla de app.py

#tabla producto, clase, atributos(lo que se debe añadir en la db), constructor(para pasar los otributos al modelo)
class Product(db.Model):
    __tablename__ = 'Product'

    id_Product = db.Column(db.Integer, primary_key = True, autoincrement = True)    
    name = db.Column(db.String)
    codeProduct = db.Column(db.Integer)
    brand = db.Column(db.String, nullable=True)
    productType = db.Column(db.String, nullable=True)
    measureUnit = db.Column(db.String)
    ivaTax = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    stockmin = db.Column(db.Integer)
    #amount = db.Column(db.ForeignKey("Input.amount"))
    salePrice = db.Column(db.Integer) # este se necesita pero formulado salePrice=Input.purchasePrice*ivaTax*%ganancia

    def __init__(self, name, codeProduct, brand, productType,  measureUnit, ivaTax, stock, stockmin, salePrice):
        self.name = name
        self.codeProduct = codeProduct
        self.brand = brand
        self.productType = productType
        self.measureUnit = measureUnit
        self.ivaTax = ivaTax
        self.stock = stock
        self.stockmin = stockmin
        #self.amount = amount
        self.salePrice = salePrice
   

#table inventary
class inventary (db.Model):
    __tablename__ = 'inventary'
    id = db.Column (db.Integer, primary_key = True, autoincrement = True) 
    id_Product = db.Column(db.ForeignKey("Product.id_Product"))
    #name = db.Column(db.ForeignKey("products.name"))
    #codeProduct = db.Column(db.ForeignKey("products.codeProduct"))
    #brand = db.Column(db.ForeignKey("products.brand"))
    #productType = db.Column(db.ForeignKey("products.productType"))
    admissionDate = db.Column(db.Integer)
    #measureUnit = db.Column(db.ForeignKey("products.measureUnit"))
    #ivaTax = db.Column(db.ForeignKey("products.ivaTax"))
    #stock = db.Column(db.ForeignKey("products.stock"))
    #stockmin = db.Column(db.Integer)
    id_input = db.Column(db.ForeignKey("Input.id"))
    #cantidad = db.Column("products.stock"+"Input.amount"-"Saledetail.amount_sale") amarrado a la llave foranea de id_product
    
    def __init__(self, id_product, admissionDate, id_input):
        self.id_product = id_product
        self.admissionDate = admissionDate
        self.id_input = id_input   

#tabla usuario, registro de ingreso
class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True)
    cedula = db.Column(db.Integer, unique=True)
    password = db.Column(db.String)
    secondKey = db.Column(db.String, unique=True, nullable=True)
    
    def __init__(self, email, password):
        self.email = email
        self.password = password

#tabla nuevo usuario
class NewUser(db.Model):
    __tablename__ = 'NewUser'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    cedula = db.Column(db.Integer, unique = True)
    telephone = db.Column(db.Integer)
    role = db.Column(db.String)
    name = db.Column(db.String)
    lastname = db.Column(db.String)
    birthDate =db.Column(db.String)

    def __init__(self, email, password, cedula, telephone, role, name, lastname, birthDate):
    #def __init__(self, email, password):
        self.email = email
        self.password = password
        self.cedula = cedula
        self.telephone = telephone
        self.role = role
        self.name = name
        self.lastname = lastname
        self.birthDate = birthDate


#tabla detalle de venta

class Saledetail (db.Model):
    __tablename__ = 'Saledetail'

    idOutput = db.Column(db.Integer, primary_key=True, autoincrement = True)
    id_Product = db.Column(db.ForeignKey("Product.id_Product")) ## Lorena: para concatenar con el producto
    ##idOutput = db.Column(db.Integer)
    amount_sale = db.Column(db.Integer)
    unitValue = db.Column(db.Integer) #este debe venir de otra tabla, como de input
    ivaTax = db.Column(db.Integer, unique = True)
    ##totalValue = db.Column(db.Integer)

    totalValue = db.Column(db.Integer, unique = True)  
    def __init__(self, id_Product, amount_sale, unitValue, ivaTax,totalValue):
        self.id_Product = id_Product
        self.amount_sale = amount_sale
        self.unitValue = unitValue
        self.ivaTax = ivaTax
        self.totalValue = totalValue

#tabla ingreso
class Input(db.Model):
    __tablename__ = 'Input'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    id_user = db.Column(db.ForeignKey("NewUser.id"))
    id_Product = db.Column(db.ForeignKey("Product.id_Product"))
    amount = db.Column(db.Integer)
    date = db.Column(db.Integer)
    purchasePrice = db.Column(db.Integer)
    percentageProfit = db.Column(db.Integer)  
    id_Vendor = db.Column(db.ForeignKey("Vendors.id")) #conecta con la tabla de vendedores

    def __init__(self, id_user, id_Product, amount, date, purchasePrice, percentageProfit, id_Vendor):
        self.id_user = id_user
        self.id_Product = id_Product
        self.amount = amount
        self.date = date
        self.purchasePrice = purchasePrice
        self.percentageProfit = percentageProfit
        self.id_Vendor = id_Vendor

#tabla salida
class Output (db.Model):
    __tablename__ = 'Output'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    iduser = db.Column(db.ForeignKey("User.id"))
    ## purchasePrice = db.Column(db.ForeignKey("Input.purchasePrice")) purchasePrice no es llave primaria en Input
    idSaledetail = db.Column(db.ForeignKey("Saledetail.idOutput"))
    date_out = db.Column(db.Integer) # debe ser date time con hora 

    def __init__(self, iduser, purchasePrice, idSaledetail, date_out):
        self.iduser = iduser
        self.purchasePrice = purchasePrice
        self.idSaledetail = idSaledetail
        self.date_out = date_out

#tabla datos tienda 
class store (db.Model):
    __tablename__ = 'Store'

    id = db.Column (db.Integer, primary_key = True, autoincrement = True)    
    nameStore = db.Column (db.String)
    ownerStore = db.Column (db.ForeignKey("User.id")) # deberia ir formulado para que sea el rol admin
    telephone = db.Column (db.Integer)
    email = db.Column (db.String)
    address = db.Column (db.String)

    def __init__(self, nameStore, ownerStore, telephone, email, address):
        self.nameStore = nameStore
        self.ownerStore = ownerStore
        self.telephone = telephone
        self.email = email
        self.address = address

#tabla provedores
class Vendors (db.Model):
    __tablename__ = 'Vendors'

    id = db.Column (db.Integer, primary_key = True, autoincrement = True)    
    name = db.Column(db.String)
    id_Product = db.Column(db.ForeignKey (Product.id_Product)) ## Asociado al codigo del producto
    brand = db.Column(db.String, nullable=True)
    productType = db.Column(db.String, nullable=True)
    #admissionDate = db.Column(db.Integer)
    #measureUnit = db.Column(db.Integer)
    #rolevendor = db.Column(db.String)
    namevendor = db.Column(db.String)
    lastnamevendor = db.Column(db.String)
    companyvendor = db.Column(db.String)
    orderday = db.Column(db.String)
    input = db.Column(db.ForeignKey(Input.id)) #conecta con las compras

    def __init__(self, name, id_Product, brand, productType, namevendor, lastnamevendor, companyvendor, orderday, input):
        self.name = name
        self.id_Product = id_Product
        self.brand = brand
        self.productType = productType
        #self.admissionDate = admissionDate
        #self.measureUnit = measureUnit
        #self.rolevendor = rolevendor
        self.namevendor = namevendor
        self.lastnamevendor = lastnamevendor 
        self.companyvendor = companyvendor 
        self.orderday = orderday
        #self.input = input
#merge