import requests

# data = {
#     "bully" : "Saiyan",
#     "victim" : "Pranav",
#     "statement" : "I will explode you",
#     "toxicity" : 0.90,
#     "location" : "PennApps",
#     "associates" : ["Jhosh", "Yung Bav"],
# }

data = {
    "firstName" : "Sayan",
    "lastName" : "Chaudhry",
    "gender" : "Male",
    "race" : "Indian",
    "dateOfBirth" : "1999-05-10T00:01:00"
}

r = requests.post("https://lit-forest-54107.herokuapp.com/api/logBullyingEvent", data=data)
print(r.text)