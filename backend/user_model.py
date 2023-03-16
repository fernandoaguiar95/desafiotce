import sqlalchemy
import datetime
from sqlalchemy.ext.declarative import declarative_base


Base = sqlalchemy.orm.declarative_base()

engine = sqlalchemy.create_engine("mysql+mysqlconnector://root:@127.0.0.1:3306/desafiotce")


class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, unique=True)
    username = sqlalchemy.Column(sqlalchemy.String(length=255), nullable=False, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String(length=255), nullable=False)
    is_enable = sqlalchemy.Column(sqlalchemy.Boolean, default=True, nullable=False)
    register_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String(length=255), nullable=False)
    surname = sqlalchemy.Column(sqlalchemy.String(length=255), nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String(length=255), nullable=False)
    phone = sqlalchemy.Column(sqlalchemy.String(length=11), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'is_enable': self.is_enable,
            'register_date': self.register_date,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'phone': self.phone
        }

Base.metadata.create_all(engine)
