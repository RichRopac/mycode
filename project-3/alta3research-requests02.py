#!/usr/bin/env python3
import json
import requests
from pprint import pprint

URL = "http://127.0.0.1:2224/breeds"

# GET all initial records
resp = requests.get(URL).json()
print("\nThis is the Inital Dogs Dictionary GET request for all the records:\n")
pprint(resp)

# GET just the Cane Corso
resp = requests.get(URL+"/Cane%20Corso").json()
print("\nThis is the GET request for just the Cane Corso:\n")
pprint(resp)

# POST - Creating a new record to add to the dictionary
headers = {
    'Content-Type' : 'application/json',
}
json_data = {
    "breed": "Poodle",
    "country": "France",
    "category": "Friendly",
    "lives": "15 years",
    "height": "Small to Large",
    "weight": "Medium"
}
response = requests.post('http://localhost:2224/breeds',headers=headers,json=json_data)

print("\nThis is the POST request to add Poodle to the Dogs Dictionary:\n")
pprint(response.json())

# PUT - Modifying the Poodle entry in the dictionary
headers = {
    'Content-Type' : 'application/json',
}
json_data = {
    "weight": "Slim Waisted"
}
response = requests.put('http://localhost:2224/breeds/Poodle',headers=headers,json=json_data)

print("\nThis is the PUT request to modify Poodle in the Dogs Dictionary:\n")
pprint(response.json())

# DELETE - removing Poodle from the Dogs Dictionary
response = requests.delete('http://localhost:2224/breeds/Poodle')

print("\nThis is the DELETE request to remove Poodle from the Dogs Dictionary:\n")
pprint(response.json())

# GET all initial records
resp = requests.get(URL).json()
print("\nThis is the Final Dogs Dictionary after all the modifications:\n")
pprint(resp)

