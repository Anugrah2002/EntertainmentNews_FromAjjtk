import urllib.request
import xmltodict
from bs4 import BeautifulSoup
# from . import models
import re
# from models import *
import settings







url = 'https://hindi.gadgets360.com/mobiles/cubot-kingkong-5-pro-rugged-smartphone-launch-soon-massive-8000mah-battery-4gb-ram-waterproof-dustproof-specifications-8000-news-2389286'

def getArticleWebpage(url):
    try:
        req = urllib.request.Request(
        url, 
        data=None, 
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
        }
        )

        return urllib.request.urlopen(req)
    except:
        print('pa fourth')


def scrapArticle(web_page):
    try:
        soup = BeautifulSoup(web_page, 'html.parser')
        content =  soup.find("div", {"class" : "content_text row description"})
        contentn = content.find("div",{"class":"content_text row description"})
        if contentn is not None:
            content = contentn

        for divs in content.findAll("div"):
            divs.extract()
        for divs in content.findAll("blockquote"):
            divs.extract()

        return content.get_text()
    except:
        print('pa fifth')

web_page = getArticleWebpage(url)
print(scrapArticle(web_page))