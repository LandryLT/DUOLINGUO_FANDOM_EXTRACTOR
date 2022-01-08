from bs4 import BeautifulSoup
import urllib.request
import copy

class FandomExtract:
    def __init__(self, url):
        with urllib.request.urlopen(url) as response:
            self.fullpage = BeautifulSoup(response.read(), 'html.parser')
            self.toc = self.fullpage.find(id="toc")
            self.content = self.fullpage.find(id="content")
            self.toc_dict = self.parse_toc(self.toc)
            self.content_dict = self.parse_content(self.toc_dict, self.content)

    def parse_toc(self, toc):
        toclis = dict()
        for li in toc.find_all(class_="toclevel-1"):
            href = li.a.get('href')
            ind = li.a.find('span', class_="tocnumber").string
            btext = li.a.find('span', class_="toctext").string
            toclis[href] = (ind, btext)
        return toclis

    def parse_content(self, toclis, content):
        soups = dict()
        for tocli in toclis:
            c = content.find(id=tocli[1:]).parent
            chap = toclis[tocli][1]
            newdiv = "<div id=\""+toclis[tocli][0]+"\"></div>"        
            newsoup = BeautifulSoup(newdiv, "html.parser")
            newsoup.div.append(copy.copy(c))

            for s in c.next_siblings:
                if s.name == "h2" or s.next_sibling is None:
                    soups[chap] = newsoup 
                    break
                newsoup.div.append(copy.copy(s)) 
        return soups
