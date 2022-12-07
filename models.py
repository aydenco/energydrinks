from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first_name = '', last_name = '', password = '', token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'

# Once initiallized, how do i change valid string length?
# Error I recieved : psycopg2.errors.StringDataRightTruncation: value too long for type character varying(4)

class Drink(db.Model):
    id = db.Column(db.String, primary_key = True)
    brand = db.Column(db.String(50), nullable = False)
    flavor = db.Column(db.String(50))
    caffeine = db.Column(db.String(10))
    sugar = db.Column(db.String(10))
    calories = db.Column(db.String(10))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, brand, flavor, caffeine, sugar, calories, user_token, id = ''):
        self.id = self.set_id()
        self.brand = brand
        self.flavor = flavor
        self.caffeine = caffeine
        self.sugar = sugar
        self.calories = calories
        self.user_token = user_token

    def __repr__(self):
        return f'The following energy drink has been added to your favorites: {self.make} {self.model}'
    
    def set_id(self):
        return (secrets.token_urlsafe())

class DrinkSchema(ma.Schema):
    class Meta:
        fields = ['id', 'brand', 'flavor', 'caffeine', 'sugar', 'calories']

drink_schema = DrinkSchema()
drinks_schema = DrinkSchema(many = True)
