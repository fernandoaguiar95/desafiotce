import sqlalchemy
from flask import jsonify
import json
from user_model import User
from config import session

#definição de funções responsáveis por fazerem o CRUD de usuários
def add_user(user: User):
    newUser = user
    session.add(newUser)
    session.commit()

def update_user(user: User):
    existing_user = session.query(User).filter(User.id == user.id).one_or_none()
    if existing_user:
        existing_user = user
        session.merge(existing_user)
        session.commit()

def delete_user(id):
    existing_user = session.query(User).filter(User.id == id).one_or_none()
    session.delete(existing_user)
    session.commit()

def get_users(args):
    if len(args) > 0:

        username = args['username'] if args['username'] != '' or args['username'] != None else ''
        name = args['name'] if args['name'] != '' or args['name'] != None else ''
        email = args['email'] if args['email'] != '' or args['email'] != None else ''
        users = session.query(User).filter(
            User.email.like(f'%{email}%'),
            User.username.like(f'%{username}%'),        
            User.name.like(f'%{name}%')        
        ).all()

    else:
        users = session.query(User).all()
    to_json = json.dumps([user.serialize() for user in users], default=str, indent=4)
    users_json = json.loads(to_json)
    return users_json    

def verify_user_exists(username):
    user = session.query(User).filter(User.username == username).first()
    if user:
        return True
    else:
        return False