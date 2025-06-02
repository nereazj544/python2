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


# rs = collection.find({'paises': 'España'}) # Buscar documentos donde se habla en España

#* Insertar un nuevo documento

nombre = input("Ingrese el nombre del nuevo lenguaje: ").capitalize()
paises = input("Ingrese los paises donde se habla (separados por comas): ").capitalize().split(", ")

nuevo_lenguaje = {
    'id' : collection.count_documents({}) + 1,  # Generar un ID único
    'nombre': nombre,
    'paises': paises
}

nl = collection.insert_one(nuevo_lenguaje)  # Insertar el nuevo documento



# if not collection.find_one({'nombre': nuevo_lenguaje['nombre']}):
#     # Verificar si el lenguaje ya existe
#     print(f"El lenguaje '{nuevo_lenguaje['nombre']}' ya existe.")
# else:
#     print(f"El lenguaje '{nuevo_lenguaje['nombre']}' no existe, se procederá a insertar.")
#     collection.insert_one(nuevo_lenguaje)  # Insertar el nuevo documento

# collection.insert_one(nuevo_lenguaje)  # Insertar el nuevo documento
# print(f"Nuevo lenguaje '{nuevo_lenguaje['nombre']}' insertado correctamente.")