import funciones as f
import json

db = open('./agenda.json','r')

agenda = json.load(db)
db.close()

f.imprimirOrdenado(agenda)

contacto = f.agregarContacto(len(agenda)+1)
agenda.append(contacto)


db = open('./agenda.json','w')
db.write(json.dumps(agenda))
db.close()

db = open('./agenda.json','r')
agenda = json.load(db)
f.imprimirOrdenado(agenda)



