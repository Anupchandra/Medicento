from pymongo import MongoClient
import pymongo
import telegram

class Inserter:
    def InsertDoc(self,category,name,description,mrp,sp,manufacturer,address):
        self.category = category
        self.name = name
        self.description = description
        self.mrp = mrp
        self.sp = sp
        self.manufacturer = manufacturer
        self.address =address
        record = {"Name" : self.name,"Description" : self.description,"Max Retail Price" : self.mrp,"Discounted Price" : self.sp,"Manufacturer Name" : self.manufacturer,"Manufacturer Address" :self.address}
        myClient = MongoClient()
        db = myClient.Medicento
        data = db[self.category]
        data.insert_one(record)