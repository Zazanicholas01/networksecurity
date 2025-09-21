from pymongo.mongo_client import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

def connect_to_mongodb(host='localhost', port=27017, username='admin', password='password', database='mydatabase'):
    try:
        uri = f"mongodb://{username}:{password}@{host}:{port}/{database}?authSource=admin"

        client = MongoClient(uri, serverSelectionTimeoutMS=5000)

        client.admin.command('ping')
        print("✅ Successfully connected to MongoDB!")

        return client

    except ConnectionFailure:
        print("❌ Could not connect to MongoDB. Make sure the container is running.")
        return None
    except OperationFailure as e:
        print(f"❌ Authentication failed: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None
    
connect_to_mongodb()
