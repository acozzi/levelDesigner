import json

def imprimirOrdenado(datos):
    text = json.dumps(datos, sort_keys=False,indent=4)
    print(text)

def agregarContacto(valorID):
    nombre = input('Ingrese el nombre: ')
    email = input('Ingrese el email: ')
    contacto = {
        "id": valorID,
        "nombre": nombre,
        "email": email
    }
    return contacto