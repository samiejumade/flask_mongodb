from dotenv import load_dotenv
import os
import pymongo

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['flask_tutorials']