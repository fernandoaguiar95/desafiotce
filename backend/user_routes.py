from __main__ import app
from flask import jsonify
from flask import flash, request
import user_controller
from user_model import User

@app.route('/users', methods=['POST'])
def create_user():
     try:
        _json = request.json
        _username = _json['username']
        _password = _json['password']
        _is_enable = True if _json['is_enable'] == 1 else False
        _register_date = None
        _name = _json['name']
        _surname = _json['surname']
        _email = _json['email']
        _phone = _json['phone']

        if user_controller.verify_user_exists(_username) == False:
          
          if _username and _password and _is_enable != None and _name and _surname and \
               _email and _phone and request.method == 'POST':

               new_user = User(username=_username, password=_password, is_enable=_is_enable,\
                   register_date=_register_date, name=_name, surname=_surname,\
                    email=_email, phone=_phone)
               
               user_controller.add_user(new_user)
               message = {
                    'status': True,
                    'message': 'Usuário cadastrado com sucesso!'
               }
               response = jsonify(message)
               response.status_code = 200
               return response

          else:
               message = {
                    'status': False,
                    'message': 'Campos inválidos!'
               }
               response = jsonify(message)
               response.status_code = 200
               return response

        else:
          message = {
                    'status': False,
                    'message': 'Username já existe!'
               }
          response = jsonify(message)
          response.status_code = 200
          return response  

     except Exception as e:
         print(e)

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
     try:
        _json = request.json
        _id = id
        _username = _json['username']
        _password = _json['password']
        _is_enable = True if _json['is_enable'] == '1' else False
        _register_date = _json['register_date']
        _name = _json['name']
        _surname = _json['surname']
        _email = _json['email']
        _phone = _json['phone']
        
        if _id and _username and _password and _is_enable != None and _register_date and _name and _surname and \
            _email and _phone and request.method == 'PUT':

             update_user = User(id=_id, username=_username, password=_password, is_enable=_is_enable,\
                   register_date=_register_date, name=_name, surname=_surname,\
                    email=_email, phone=_phone)

             user_controller.update_user(update_user)
             message = {
                    'status': True,
                    'message': 'Usuário alterado com sucesso!'
               }
             response = jsonify(message)
             response.status_code = 200
             return response

        else:
            return show_message('Campos inválidos!')

     except Exception as e:
         print(e) 

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
     try:
          _id = id

          if _id and request.method == 'DELETE':

               user_controller.delete_user(_id)
               message = {
                    'status': True,
                    'message': 'Usuário deletado com sucesso!'
               }
               response = jsonify(message)
               response.status_code = 200
               return response

          else:
               return show_message('Campos inválidos!')

     except Exception as e:
          print(e)

@app.route('/users', methods=['GET'])
def get_users():
     try:
          if request.method == 'GET':

               args = request.args.to_dict()
               users = user_controller.get_users(args)
               response = jsonify(users)
               response.status_code = 200
               return response

          else:
               return show_message('Erro ao processar solicitação')

     except Exception as e:
          print(e)

          
@app.errorhandler(404)
def show_message(message):
     message = {
          'status': 404,
          'message': message + ' ' + request.url
     }
     response = jsonify(message)
     response.status_code = 404
     return response