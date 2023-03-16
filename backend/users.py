import sqlalchemy
import datetime
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:@127.0.0.1:3306/desafiotce")

Base = sqlalchemy.orm.declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String(length=255))
    password = sqlalchemy.Column(sqlalchemy.String(length=255))
    is_enable = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    register_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow)
    name = sqlalchemy.Column(sqlalchemy.String(length=255))
    surname = sqlalchemy.Column(sqlalchemy.String(length=255))
    email = sqlalchemy.Column(sqlalchemy.String(length=255))
    phone = sqlalchemy.Column(sqlalchemy.String(length=11))

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

def add_user(username, password, is_enable, register_date, name, surname, email, phone):
    newUser = User(username=username, password=password, is_enable=is_enable, register_date=register_date, name=name, surname=surname, email=email, phone=phone)
    session.add(newUser)
    session.commit()


