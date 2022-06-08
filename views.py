import os 
from processArticle import *
from makeVideos import *
from wsgiref.util import FileWrapper
from uploadToYT import *
import os
import shutil
from gtts import gTTS
import random
import settings
import requests, json
from uploadfiletoheroku import *
from uploadtofirebase import *
from datetime import datetime, timezone
import urllib.request


def checktime():
    fetchdata=requests.get('http://ytserver.eu-gb.cf.appdomain.cloud/entertain_news/nextrandomforaajtk/')
    data=fetchdata.json()
    nextran= datetime.strptime(data['nextrandom'],"%Y-%m-%dT%H:%M:%SZ")
    print(nextran)
    datime=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    print(datime)
    dateee=datetime.strptime(datime,"%Y-%m-%d %H:%M:%S")
    if (nextran < dateee):
       print("We will post video")
       requestVideo()
    else:
        print("We will wait for minutes since it is time error")


def replaceConflictsWords(content):
    #Replace Words which needs to be removed because of copyright or advertisement
    if (content != ''):
        content = content.replace('विज्ञापन','')
        content = content.replace('\n','')
        content = content.replace("Copyright © 2022 Living Media India Limited. For reprint rights: Syndications Today Add Aaj Tak to Home Screen", "")
        return content
    else:
        return content

    #All words replaced
    
def fixYTtitle(YTtitle):
    YTtitle = YTtitle.replace(",", "")
    if len(YTtitle) > 100:
        #Invalid Title
        YTtitlewordlist = YTtitle.split(" ")
        updatedTitle = YTtitlewordlist[0]
        for words in YTtitlewordlist[1:]:
            if len(updatedTitle + " " + words) < 100:
                updatedTitle = updatedTitle + " " + words
            else:
                return updatedTitle
    return YTtitle
   

def requestVideo():
    
    try:       
        # 'http://ytserver.eu-gb.cf.appdomain.cloud/entertain_news/gettitlefromaajtk/'
        r=requests.get('http://ytserver.eu-gb.cf.appdomain.cloud/entertain_news/gettitlefromaajtk/')
        print(r)

        title=(r.json()['title'])
        YTtitle=(r.json()['Ytitle'])
        content=(r.json()['content'])
        image_url = (r.json()['image_url'])
        print('line 70')
        print(os.getcwd())
        print('line 72')
        imagedownload = urllib.request.urlretrieve(image_url,'/EntertainmentNews_FromAjjtk/EntertainmentNews_FromAjjtk/dataset/'+ title + '/' +'thumbnailimage.jpg')
        #imagedownload = urllib.request.urlretrieve(image_url,'image.jpg')
        content = replaceConflictsWords(content)
        print(content)
        summary=(r.json()['summary'])

        file = open(r'thumbnailimages/' 'w')
        file.write(imagedownload)
        file.close

        if title == 0 or title is None or content is None or content == '':
            print("Content or title is either blank or incorrect")
            exit()
        

        newYTtitle = YTtitle
        p = makeVideo(newYTtitle+' hd',content)
        print('2')

        if p =='GTTS ERR':
            shutil.rmtree(os.path.join(settings.BASE_DIR, r"dataset"))
            print('3')
            return 'GTTS ERR'
            print('4')

        os.chdir(os.path.join(settings.BASE_DIR,''))

        credit = '''\nWe take DMCA very seriously. All the images are from Bing Images.Since all the contents are not moderated so If anyway we hurt anyone sentiment, send us a request with valid proof.
        '''
        keywords = ','.join(str(YTtitle).split())

        print(YTtitle)
        print("Video is generated")

        #command = 'python ./bott/uploadToYT.py --file="'+str(p)+'" --title="'+YTtitle+'" --description="'+(summary+'\n'+credit)+'" --keywords="'+keywords+',hour news,news" --category="24" --privacyStatus="public" --noauth_local_webserver ' 
        # uploadvideotoheroku(p,YTtitle)
        uploadfiletofirebase(p,fixYTtitle(YTtitle))
        
        #os.system(command) #comment this to stop uploading to youtube
        # shutil.rmtree(os.path.join(settings.BASE_DIR, r"dataset")) # comment this to stop removing the file from system
        print('Success')


    except Exception as e:
        print('views function')
        print(e)

    

#checktime()
requestVideo()
