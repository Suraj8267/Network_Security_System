import os
import sys
import json

from dotenv import load_dotenv  ## To call the environment variables kept in .env file
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")  ## This will get your environment varaibles that is kept in .env file 
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

## This is my ETL Pipeline which is responsible for the extracting the data from source, then transforming it and then pushing into the mongoDB Atlas Cloud Database.
class NetworkDataExctract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop= True, inplace= True)
            records = list(json.loads(data.T.to_json()).values()) ## json.loads : json string ko python dictionary me convert krta hai and .values() ye dictionary ke ander ke values dega           
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)  

    def insert_data_mongodb(self, records, database, collection):  ## collection is like table just like we have in sql
        try:
            self.database = database
            self.collection =collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)  ## here we are creating a mongo Client and pymongo is a library to connect with mongoDB database from python and MongoClient() : Ye MongoDB server se connection establish karne ke liye client object banata hai.
            self.database = self.mongo_client[self.database]  ## MongoDB client se my_database database ko access karo if self.database or mongoDB database ka naam my_database hai and phle self.database me string thi abb database object hai 

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__=='__main__':
    FILE_PATH = 'Network_Data/phisingData.csv'
    DATABASE = "SURAJAI"
    COLLECTION = "NetworkData"
    network_obj = NetworkDataExctract()
    records = network_obj.csv_to_json_convertor(FILE_PATH)
    print(records)
    no_of_records = network_obj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(no_of_records)

