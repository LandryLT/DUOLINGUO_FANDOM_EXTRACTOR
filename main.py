from bs4 import BeautifulSoup
import urllib.request
from os import cpu_count, listdir
from os.path import isfile, join, abspath
import copy

#Get HTML
url = 'https://duonotes.fandom.com/wiki/Japanese'
with urllib.request.urlopen(url) as response:
    fandompage = BeautifulSoup(response.read(), 'html.parser')

#Get all chapters from table of content
toc = fandompage.find(id="toc")
cntnt = fandompage.find(id="content")

tocas = dict()
contents = dict()

for a in toc.find_all('a'):
    href = a.get('href')
    ind = a.find('span', class_="tocnumber").string
    btext = a.find('span', class_="toctext").string
    tocas[href] = (ind, btext)

soups = dict()
for toca in tocas:
    c = fandompage.find(id=toca[1:]).parent
    chap = tocas[toca][1]

    newdiv = "<div id=\""+tocas[toca][0]+"\"></div>"    
    newsoup = BeautifulSoup(newdiv, "html.parser")
    newsoup.div.append(copy.copy(c))

    for s in c.next_siblings:
        if s.name in ["h1", "h2", "h3", "h4", "h5"]:
            soups[chap] = newsoup 
            print(soups[chap])
            break
        newsoup.div.append(copy.copy(s))   
           
for soup in soups:
    print(soups[soup])