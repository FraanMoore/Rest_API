from flask import Flask, request, json
from models import db

app = Flask(__name__)

# @app.route("/", methods=["GET", "POST", "PUT", "DELETE"]) #decorador, escucha la ruta y metodo declarada para entrar a ese recurso
# def home():
#     if request.method == "GET":
#         return "Hola GET"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

@app.route("/")
def home():
    return "sql alchemy"

with app.app_context():
    db.create_all()

app.run(host="localhost", port=8000)
