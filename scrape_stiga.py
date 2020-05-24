import urllib
import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase

i = 1

def makesoup(url):
     thepage = urllib.request.urlopen(url)
     soupdata = BeautifulSoup(thepage, "html.parser")
     return soupdata

soup = makesoup("https://www.stiga.pl/sklep/koszenie-trawnika/agregaty-tnace/agregaty-tnace-park-villa/agregat-park-100-combi-3-el-qf")
for img in soup.findAll('img'):
    temp=img.get('src')
    if temp[:1]=="/":
        image = "https://www.stiga.pl/sklep/koszenie-trawnika/agregaty-tnace/agregaty-tnace-park-villa/agregat-park-100-combi-3-el-qf" + temp
    else:
        image = temp

    nametemp = img.get('alt','')
    if len(nametemp) == 0:
        filename = str(i)
        i = i + 1
    else: 
        filename = nametemp

    imagefile = open(filename + ".jpeg", "wb")
    imagefile.write(urllib .request.urlopen(image).read())
    imagefile.close()
