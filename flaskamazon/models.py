from flaskamazon import db , login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model , UserMixin) :

    __tablename__= 'user'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(20) , unique = True , nullable = False )
    email = db.Column(db.String(40) , unique = True , nullable = False )
    password = db.Column(db.String(40) , nullable = False )
    profile_img = db.Column(db.String(20) , nullable = False , default = 'default.jpg')

    def __repr__(self):
        return f'id =  {self.id} , username = {self.username} , email = {self.email} '


class Seller(User):
    id = db.Column(db.Integer , db.ForeignKey('user.id') , primary_key=True)
    products = db.relationship("Product" , backref='seller')


product_category_enrollement = db.Table('product_category_enrollement',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)



class Product(db.Model):
    __tablename__= 'product'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20) , nullable=False)
    content = db.Column(db.Text, nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_imgs = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'Product({self.title} , {self.content} )'



class Category(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    products = db.relationship('Product', secondary=product_category_enrollement, lazy='subquery',
                    backref=db.backref('categories', lazy=True))


class Message(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    sender = db.Column(db.Integer , db.ForeignKey('user.id'))
    recipient = db.Column(db.Integer,db.ForeignKey('user.id'))
    content = db.Column(db.String(200) , nullable=False)
    timestapm = db.Column(db.String(30) , nullable=False)
