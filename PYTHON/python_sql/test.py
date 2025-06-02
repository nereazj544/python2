from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

client = MongoClient('mongodb://localhost:27017/') #Configuración de conexión

database_name = client['test_python_db'] # Nombre de la base de datos
collection = database_name['Lenguajes'] # Nombre de la colección

doc = collection.find()

for docmnt in doc:
    # print(docmnt)
    print (f"Lenguaje: {docmnt['nombre']}")
print("Nombre del lenguaje a buscar: ")
nombre = input().capitalize() # Solicitar al usuario el nombre del lenguaje a buscar

# Buscar un documento específico por nombre y despues filtrar los paises donde se habla
r = collection.find_one({'nombre': nombre}) # Buscar un documento específico
if r:
    print(f"Lenguaje encontrado: {r['nombre']}")
    if 'paises' in r:
        print("Pais(es) donde se habla:")
        print(", ".join(r['paises']))
else:
    print("Lenguaje no encontrado.")


rs = collection.find({'paises': 'España'}) # Buscar documentos donde se habla en España
