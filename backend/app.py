import flask
from flask_cors import CORS 

app = flask.Flask(__name__)
CORS(app)

#definindo uma rota vazia/inicial de boas vindas
@app.route('/', methods=['GET'])
def index():
     return 'Bem vindo a nossa API de usuários!'

#importanto as rotas para acesso via api
import user_routes

if __name__ == "__main__":
     app.run(debug=True,port=8080,use_reloader=True)