import requests, json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

parameters = {
    "lat":5.319506,
    "lon":-4.015731
}

# reponse = requests.get("http://10.109.249.27:3333/v1/admin/users")

reponse = requests.get("http://api.open-notify.org/astros.json")

# reponse = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# print("There actually are " + str(reponse.json()["number"]))

# jprint(reponse.json())

# users = reponse.json()["users"]["data"]

# jprint(users)

# for user in users:
#     name = user["username"]
#     print(name)

people_in_space = reponse.json()["number"]
people_in_space_names = reponse.json()["people"]

print("There are "+ str(people_in_space) +" people in space right now!\n")
# # jprint(people_in_space_names)

for people in people_in_space_names:
    name = people["name"]
    craft = people["craft"]
    print(name + "is in craft " + craft + "\n")
