# serializeObject.py

import json

usuario = {
        'username': 'eduardo_gpg',
        'nombre': 'Eduardo Ismael',
        'age':27,
        'correo': 'edurado78d@gmail.com'

        }

data = json.dumps(usuario, indent=4, sort_keys=True)
print(data)
