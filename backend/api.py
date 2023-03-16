from app import app
from flask import jsonify
from flask import flash, request
import users

@app.route('/')
def home():
     return 'Bem-vindo a nossa API!'

@app.route('/users', methods=['POST'])
def create_user():
     try:
        _json = request.json
        _username = _json['username']
        _password = _json['password']
        _is_enable = True if _json['is_enable'] == 1 else False
        _register_date = _json['register_date']
        _name = _json['name']
        _surname = _json['surname']
        _email = _json['email']
        _phone = _json['phone']
        
        if _username and _password and _is_enable != None and _register_date and _name and _surname and \
            _email and _phone and request.method == 'POST':
             users.add_user(_username, _password, _is_enable, _register_date, _name,\
                            _surname, _email, _phone)
             response = jsonify('Usuário cadastrado com sucesso!')
             response.status_code = 200
             return response
        else:
            return show_message()
     except Exception as e:
         print(e)
      
          
@app.errorhandler(404)
def show_message():
     message = {
          'status': 404,
          'message': 'Erro ao processar a solicitação! ' + request.url
     }
     response = jsonify(message)
     response.status_code = 404
     return response

if __name__ == "__main__":
     app.run(debug=True,port=8080,use_reloader=True)