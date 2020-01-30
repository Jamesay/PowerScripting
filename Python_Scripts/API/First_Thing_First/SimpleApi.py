import requests, json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

parameters = {
    "lat":5.319506,
    "lon":-4.015731
}

reponse = requests.get("http://api.open-notify.org/astros.json")

# reponse = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# print("There actually are " + reponse.json("number").values)

# jprint(reponse.json())

people_in_space = reponse.json()["number"]
people_in_space_names = reponse.json()["people"]

print("There are "+ str(people_in_space) +" people in space right now!")

