from application import app, db
from flask import request, jsonify
from application.models import FriendsCharacter

def format_character(character):
    return {
        "id":character.id,
        "name":character.name,
        "age":character.age,
        "catch_phrase":character.catch_phrase
    }

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

# By default if you do not pass anything it is a GET route
@app.route("/characters", methods=['POST'])
def create_character():
    #Retrieve the body - req.body
    #data->{name:,age:,catch_phrase:}
    data=request.json
    character=FriendsCharacter(data['name'], data['age'],data['catch_phrase'])
    #add the character->add character in a temporary queue
    db.session.add(character)
    #commit->Sends the character to the databse and commit the changes
    db.session.commit()
    #Send back a JSON response
    #jsonify-> turns json output to a Response
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

 #GET route to all characters   
@app.route("/characters")
def get_characters():
    # SELECT * FROM FRiendsCharacters
    characters=FriendsCharacter.query.all()
    character_list=[]
    print(characters)
    for character in characters:
        character_list.append(format_character(character))
    return {'characters':character_list}

@app.route("/characters/<id>")
def get_character(id):
    #SELECT * FROM FriendCharacters WHERE id=
    #Takes in key id and value which is again id
    #By doing .first it just gonna return the first match
    character=FriendsCharacter.query.filter_by(id=id).first()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)
    

@app.route("/characters/<id>", methods=["DELETE"])
def delete_character(id):
     character=FriendsCharacter.query.filter_by(id=id).first()
     db.session.delete(character)
     db.session.commit()
     return "Character Deleted"

@app.route("/characters/<id>", methods=["PATCH"])
def update_character(id):
 #we will chain update
    character=FriendsCharacter.query.filter_by(id=id)
    data=request.json
    character.update(dict(name=data['name'], age=data['age'], catch_phrase=data['catch_phrase']))
    # list(), dict()

    #Commit the change to the database
    db.session.commit()
    #Retrieve the specific chracter from the filterinh
    updatedCharacter=character.first()
    #Return a JSON object of the updated character
    return jsonify(id=updatedCharacter.id,name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)