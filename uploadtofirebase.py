from firebase import Firebase
from datetime import datetime
import requests
from firebase_admin import storage as admin_storage, credentials, firestore


def uploadfiletofirebase(filepath,YTtitle):

  current_time=str(datetime.now())
  print(current_time)


  firebaseConfig = {
      'apiKey': "AIzaSyBexTA9lK-ruTMWVWEFaAzSKuIrNBjZ7vs",
      'authDomain': "tiktokvideos-378aa.firebaseapp.com",
      'storageBucket': "tiktokvideos-378aa.appspot.com",
      "databaseURL": "https://tiktokvideos-378aa-default-rtdb.firebaseio.com/",
      "serviceAccount": "./service_account.json"
    }


    # https://tiktokvideos-378aa-default-rtdb.firebaseio.com/



  firebase = Firebase(firebaseConfig)

  storage = firebase.storage()
  filepath = "final.mp4"


  # as admin
  storage.child(filepath[:-5]+current_time+'.mp4').put(filepath)
  url=storage.child(filepath[:-5]+current_time+'.mp4').get_url(1)
  print(url)
  nameofVideo=filepath[:-5]+current_time+'.mp4'
  #nameofVideo = "final.mp4"
# 'http://ytserver.eu-gb.cf.appdomain.cloud/entertain_news/savevideoofaajtk/'
# http://127.0.0.1:8000/entertain_news/savevideoofaajtk/

  myurl = 'http://ytserver.eu-gb.cf.appdomain.cloud/entertain_news/savevideoofaajtk/'

  
  titletopost = YTtitle

  
  postdatas = requests.post(myurl,data={'title':titletopost,'videoUrl':url,'name':nameofVideo})
