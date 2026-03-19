from pymongo import MongoClient

def get_database(db):
    mongoURI = "mongodb+srv://lordgolgotha_db_user:8MjUx52QXftE9Hup@lastumus.em4hbak.mongodb.net/?appName=Lastumus"
    client = MongoClient(mongoURI)
    return client[db]

if  __name__ == "__main__":
    dbname = get_database()