import csv

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./serviceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()


details=[]

with open('Vortex1.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        details.append(row)
print(details)

for row in details:
    print(row["ï»¿Email"])
    index = next((index for (index, d) in enumerate(details) if d["ï»¿Email"] == row["ï»¿Email"]))
    store.collection('Emails').document().set(row)