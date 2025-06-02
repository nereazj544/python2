from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
    print("Esto es un test de conexión a MongoDB")

main()

def test_mongodb_connection():
    

    try:
        client = MongoClient('mongodb://localhost:27017/')
        client.admin.command('ping')
        print("Conexión exitosa a MongoDB")
        return True
    except ConnectionFailure as e:
        print(f"Error de conexión a MongoDB: {e}")
        return False
    from pymongo.errors import ConnectionFailure

    try:
        client = MongoClient('mongodb://localhost:27017/')
        client.admin.command('ping')
        print("Conexión exitosa a MongoDB")
        return True
    except ConnectionFailure as e:
        print(f"Error de conexión a MongoDB: {e}")
        return False


test_mongodb_connection()
