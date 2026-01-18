from pymongo import MongoClient
import pandas as pd

client= MongoClient("mongodb://localhost:27017/")
db= client["ml_pipeline"]
collection= db["raw_data"]

#fetch 5 documents
cursor= collection.find().limit(5)

#convert to dataframe
df= pd.DataFrame(list(cursor))

print(df.head())

print("\nColumns:", df.columns.tolist())
