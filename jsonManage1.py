# jsonManage1.py

import json

json_object = '''{
    "nombre" : "Eduardo",
    "edad": 27,
    "correo": "eduardo78@gmail.com",
    "cursos": ["Python", "MongoDB", "Flask"]
    }'''

user = json.loads(json_object)
print(user)
print("SPACE\n")

json_object = json.dumps(user)

print(json_object)
print(type(json_object))

print("Usando objetos con clases\n")

class Usuario:
    def __init__(self, username, email):
        self.username = username
        self.email = email


usuario = Usuario('eduardo_gpg', 'eduardo78@gmail.com')
# Crear diccionarios a partir de objetos JSON
data = json.dumps(usuario.__dict__)

print(data)

