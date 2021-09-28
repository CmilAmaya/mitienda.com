from flask.scaffold import _matching_loader_thinks_module_is_package
from app import db

# Tabla Product
class Product(db.Model):
    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    code_product = db.Column(db.Integer)
    name = db.Column(db.String)
    product_type = db.Column(db.String)
    brand = db.Column(db.String)
    measure_unit = db.Column(db.Integer)
    '''IVA_task = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    sale_price = db.Column(db.Integer)'''

    def __init__(self, code_product, name, product_type, brand, measure_unit):
        self.code_product= code_product
        self.name = name
        self.product_type = product_type
        self.brand = brand
        self.measure_unit = measure_unit

# Tabla User
class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    telephone = db.Column(db.String)
    role = db.Column(db.String)
    name = db.Column(db.String)
    last_name = db.Column(db.String)

# Tabla Input
'''class Input(db.Model):
    __tablename__ = "Input"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    code_product = db.Column(db.ForeignKey("Product.code_product"))
    amount = db.Column(db.Integer)
    date = db.Column(db.Integer)
    purchase_price = db.Column(db.Integer)
    percentage_profit = db.Column(db.Integer)'''

# Tabla Output
class Output(db.Model):
    __tablename__ = "Output"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    id_user = db.Column(db.ForeignKey("User.id"))
    id_saleDetail = db.Column(db.ForeignKey("SaleDetail.id"))
    date = db.Column(db.Integer)
    
# Tabla SaleDetail
class SaleDetail(db.Model):
    __tablename__ = "SaleDetail"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    id_product = db.Column(db.ForeignKey("Product.id"))
    amount = db.Column(db.Integer)
    unit_value = db.Column(db.Integer)
    IVA_task = db.Column(db.Integer)
    total_value = db.Column(db.Integer)