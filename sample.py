import pymongo
from pymongo import MongoClient
import ssl
import datetime

cluster = MongoClient("mongodb+srv://madhan:1234@cluster0.a0liu.mongodb.net/database?retryWrites=true&w=majority",
                      ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

db = cluster["data"]
collection = db["user_info"]
_date_ = datetime.datetime.now()


data = [{"_id": 21, "date": _date_, "name": "Anandh", "email": "anandh78@gmail.com.com", "phone": "7889201118"},
        {"_id": 22, "date": _date_, "name": "Praveen", "email": "praveenpappu3130@gmail.com.com", "phone": "9151181245"},
        {"_id": 23, "date": _date_, "name": "Udhay", "email": "udhayakumar@gmail.com", "phone": "9725511580"}]

# collection.insert_many(data)
collection.delete_one({"_id": 4})
collection.insert_one({"_id": 4, "date": _date_, "name": "Sundar", "email": "sundar78@gmail.com.com", "phone": "7889201018"})
res = collection.find({})

for x in res:
    print(x)

