#!/usr/bin/env python3
"""Project 3: FLASK API"""

from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
from flask import make_response
from flask import url_for

app= Flask(__name__)

dogs = [
    {
        "breed": "Cane Corso",
        "country": "Italy",
        "category": "Work",
        "lives": "10-12 years",
        "height": "34 inches",
        "weight": "150 pounds",
    },
    {
        "breed": "Great Dane",
        "country": "Germany",
        "category": "Work",
        "lives": "7-10 years",
        "height": "34 inches",
        "weight": "200 pounds",
    },
    {
        "breed": "Doberman",
        "country": "Apolda",
        "category": "Work",
        "lives": "10-13 years",
        "height": "26 inches",
        "weight": "90 pounds",
    }
]

# User friendly response when item not found
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Dog Breed Not Found, Check Spelling"}), 404)

#Function to add the record's url 
def make_public_dog(dog):
    new_dog = {}
    for field in dog:
        new_dog[field] = dog[field]
    new_dog[" url"] = url_for("get_dog", dog_breed=dog["breed"], _external=True)

    return new_dog

# Returns all the data
@app.route("/breeds", methods=["GET"])
def get_dogs():
    #return jsonify({"dogs": dogs})
    return jsonify({"dogs": [make_public_dog(dog) for dog in dogs]})

# Returns specific data on the dog breed searched for
@app.route("/breeds/<dog_breed>", methods=["GET"])
def get_dog(dog_breed):
    dog = [dog for dog in dogs if dog["breed"] == dog_breed]
    if len(dog) == 0:
        abort(404)
    return jsonify({"dog": dog[0]})

# Adds an entry to the dogs dictionary, input only requires breed name.
@app.route("/breeds", methods=['POST'])
def create_dog():
    if not request.json or not "breed" in request.json:
        abort(400)
    dog = {
        "breed": request.json["breed"],
        "country": request.json["country"],
        "category": request.json["category"],
        "lives": request.json["lives"],
        "height": request.json["height"],
        "weight": request.json["weight"]
    }
    dogs.append(dog)
    return jsonify({"dog": dog}), 201

# Edits an entry in the dogs dictionary
@app.route("/breeds/<dog_breed>", methods=["PUT"])
def update_dog(dog_breed):
    dog = [dog for dog in dogs if dog["breed"] == dog_breed]
    if len(dog) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if "breed" in request.json and type(request.json["breed"]) !=str:
        abort(400)
    if "country" in request.json and type(request.json["country"]) !=str:
        abort(400)
    if "category" in request.json and type(request.json["category"]) !=str:
        abort(400)
    if "lives" in request.json and type(request.json["lives"]) !=str:
        abort(400)
    if "height" in request.json and type(request.json["height"]) !=str:
        abort(400)
    if "weight" in request.json and type(request.json["weight"]) !=str:
        abort(400)   
    dog[0]["breed"] = request.json.get("breed", dog[0]["breed"])
    dog[0]["country"] = request.json.get("country", dog[0]["country"])
    dog[0]["category"] = request.json.get("category", dog[0]["category"])
    dog[0]["lives"] = request.json.get("lives", dog[0]["lives"])
    dog[0]["height"] = request.json.get("height", dog[0]["height"])
    dog[0]["weight"] = request.json.get("weight", dog[0]["weight"])

    return jsonify({"dog": dog[0]})

# Deletes an entry for the dogs dictionary
@app.route("/breeds/<dog_breed>", methods=['DELETE'])
def delete_dog(dog_breed):
    dog = [dog for dog in dogs if dog["breed"] == dog_breed]
    if len(dog) == 0:
        abort(404)
    dogs.remove(dog[0])
    return jsonify({"result": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) 
