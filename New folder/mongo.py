import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
# print(client)

mydb = client["Employee"]

info = mydb.employeeinfo

record = {"fname": "Sudhanshu", "lname": "choudhary", "dep": "ANA"}

info.insert_one(record)
