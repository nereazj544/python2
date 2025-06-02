from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

client = MongoClient('mongodb://localhost:27017/') #Configuración de conexión

database_name = client['test_python_db'] # Nombre de la base de datos
collection = database_name['Lenguajes'] # Nombre de la colección

doc = collection.find()

for docmnt in doc:
    print(docmnt)

