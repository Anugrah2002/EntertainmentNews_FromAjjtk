# from firebase import Firebase
from firebase import Firebase
from datetime import datetime
import requests, json
import re
import firebase_admin
from firebase_admin import storage as admin_storage, credentials, firestore
# from firebase_admin import bucket


firebaseConfig = {
    'apiKey': "AIzaSyBexTA9lK-ruTMWVWEFaAzSKuIrNBjZ7vs",
    'authDomain': "tiktokvideos-378aa.firebaseapp.com",
    'storageBucket': "tiktokvideos-378aa.appspot.com",
    "databaseURL": "https://tiktokvideos-378aa-default-rtdb.firebaseio.com/",
    "serviceAccount": "./service_account.json",
}

firebase = Firebase(firebaseConfig)
storage=firebase.storage()


def cleanupFunction():
    data=requests.get('http://ytserver.eu-gb.cf.appdomain.cloud/entertain_news/clean/')
    data=data.json()
    print(data)

    for i in data:
        data=i['videoPublicId']
        storage.delete(data)
    requests.get('http://ytserver.eu-gb.cf.appdomain.cloud/entertain_news/cleanfromdb/')
cleanupFunction()



    