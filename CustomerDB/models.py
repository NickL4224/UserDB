from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CustomerModel(db.Model):

    __tablename__ = "customers"

    id = db.Column('cust_id', db.Integer, primary_key= True)
    first_name = db.Column('first_name', db.String(50))
    last_name = db.Column('last_name', db.String(50))
    email = db.Column('email', db.String(100))
    phone = db.Column('phone', db.String(20))
    city = db.Column('city', db.String(50))
    state = db.Column('state', db.String(50))

    def __init__(self, first_name, last_name, email, phone, city, state):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.city = city
        self.state = state

    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"