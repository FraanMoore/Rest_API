from flask import Flask, request, jsonify
from models import db, User, Character, Favorite

# @app.route("/", methods=["GET", "POST", "PUT", "DELETE"]) #decorador, escucha la ruta y metodo declarada para entrar a ese recurso
# def home():
#     if request.method == "GET":
#         return "Hola GET"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

@app.route("/")
def home():
    return "Hello backend"

@app.route("/users", methods=["POST"])
def create_user():
    user = User()
    user.username = request.json.get("username")
    user.password = request.json.get("password")
    user.age = request.json.get("age")

    db.session.add(user)
    db.session.commit()

    return "Usuario guardado"

@app.route("/users/list", methods=["GET"])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.serialize())
    return jsonify(result)

@app.route("/users/<int:id>", methods=["PUT", "DELETE"])
def update_user(id):
    user = User.query.get(id)
    if user is not None:
        if request.method == "DELETE":
            db.session.delete(user)
            db.session.commit()

            return jsonify("Eliminado"), 204
        else:
            user.age = request.json.get("age")
            
            db.session.commit()
            
            return jsonify("Usuario actualizado"), 200
    
    return jsonify("Usuario no encontrado"), 418

@app.route("/characters", methods=["POST"])
def create_character():
    character = Character()
    character.id = request.json.get("id")
    character.name = request.json.get("name")
    character.actor = request.json.get("actor")
    character.house = request.json.get("house")
    character.date_of_birth = request.json.get("date_of_birth")
    character.patronus = request.json.get("patronus")
    character.half_blood = request.json.get("half_blood")

    db.session.add(character)
    db.session.commit()

    return "personaje guardado"

@app.route("/characters/list", methods=["GET"])
def get_character():
    character = Character.query.all()
    result = []
    for character in character:
        result.append(character.serialize())
    return jsonify(result)

@app.route("/characters/<int:id>", methods=["PUT", "DELETE"])
def update_character(id):
    character = Character.query.get(id)
    if character is not None:
        if request.method == "DELETE":
            db.session.delete(character)
            db.session.commit()

            return jsonify("Eliminado"), 204
        else:
            character.name= request.json.get("name")
            
            db.session.commit()
            
            return jsonify("personaje actualizado"), 200
    
    return jsonify("personaje no encontrado"), 418

@app.route("/favorites", methods=["POST"])
def create_favorite():
    favorite = Favorite()
    favorite.username = request.json.get("username")
    favorite.name = request.json.get("name")
    favorite.character_id = request.json.get("character_id")
   
  
    db.session.add(favorite)
    db.session.commit()
    
    return jsonify("Favorito guardado"), 201

@app.route("/favorites/list", methods=["GET"])
def get_favorites():
    favorites = Favorite.query.all()
    result = []
    for favorite in favorites:
        result.append(favorite.serialize())
    return jsonify(result)

@app.route("/favorite/<int:id>", methods=["PUT", "DELETE"])
def update_favorite(id):
    favorite = Favorite.query.get(id)
    if favorite is not None:
        if request.method == "DELETE":
            db.session.delete(favorite)
            db.session.commit()
            
            return jsonify("Eliminado"), 204
        else:
            favorite.character_id = request.json.get("character_id")
            favorite.name = request.json.get("name")
            favorite.id_user = request.json.get("id_user")
       
            db.session.commit()
        
            return jsonify("Favorite actualizado"), 200
    
    return jsonify("Favorite no encontrado"), 404


@app.route("/favorite/user/<int:user_id>", methods=["GET"])
def get_favorite_user(user_id):
    favorites = Favorite.query.filter_by(id_user=user_id).all()
    result = []
    for favorite in favorites:
        result.append(favorite.serialize())
    return jsonify(result)


with app.app_context():
    db.create_all()

app.run(host="localhost", port=8000)
