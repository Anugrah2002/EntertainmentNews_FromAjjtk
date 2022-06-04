# from firebase import Firebase
from firebase import Firebase
# from datetime import date
# from datetime import datetime
import requests, json
import re,datetime
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

"""
line 30 me clenaup function json file se 1st index #

in line 30 cleanup function is taking the fina2022-06-04 09:14:53.963409.mp4 of thr 1st index of json file
in line 31 it is getting the previous day date it svalue is 2022-06-03 10:28:08.501052
in line 32 it is printing the date 
in line 33 it is conerting the datetime.datetime class into string class and fromat is yy-mm-dd
in line 34 it is printing the type of conversion
in line 35 it is printing the 1st index of json file it value is fina2022-06-04 09:14:53.963409.mp4
in line 36 it is using search operation for finding the string date into the 1st index of json file
in line 37 it is deleting if it is fined
in line 38 it is returning ok 

"""

    