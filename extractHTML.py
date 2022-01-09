from bs4 import BeautifulSoup
import urllib.request
import copy

import bs4

class FandomExtract:
    def __init__(self, url: str):
        with urllib.request.urlopen(url) as response:
            self.fullpage = BeautifulSoup(response.read(), 'html.parser')
            self.toc = self.fullpage.find(id="toc")
            self.content = self.fullpage.find(id="content").div.div
            self.toc_dict = self.parse_toc(self.toc)
            self.content_dict = self.parse_content(self.toc_dict, self.content)

    def parse_toc(self, toc: bs4.element.Tag) -> dict:
        toclis = dict()
        for li in toc.find_all(class_="toclevel-1"):
            href = li.a.get('href')
            ind = li.a.find('span', class_="tocnumber").string
            btext = li.a.find('span', class_="toctext").string
            toclis[href] = (ind, btext)
        return toclis

    def parse_content(self, toclis: dict, content: bs4.element.Tag) -> dict:
        soups = dict()
        for tocli in toclis:
            c = content.find(id=tocli[1:]).parent
            chap = toclis[tocli][0] + ". " + toclis[tocli][1]
            newdiv = "<div id=\"" + toclis[tocli][0] + "\"></div>"        
            newsoup = BeautifulSoup(newdiv, "html.parser")
            newsoup.div.append(copy.copy(c))

            for s in c.next_siblings:
                if s.name == "h2" or s.next_sibling is None:
                    soups[chap] = newsoup
                    break
                if type(s) is bs4.element.Comment:
                    continue
                newsoup.div.append(copy.copy(s)) 
        return soups

    def stringify_content(content: dict) -> dict:
        stringsoup = dict()
        for soup in content:            
            stringsoup[soup] = str(content[soup])
        
        return stringsoup


class FandomExtractWStyle(FandomExtract):
    def __init__(self, url: str):
        super().__init__(url)
        self.clean_up_content_dict()

    def clean_up_content_dict(self):
        for chap in self.content_dict:
            #Remove edit brackets
            for editbrackets in self.content_dict[chap].find_all(class_="mw-editsection"):
                editbrackets.extract()

            #Remove useless classes
            for every in self.content_dict[chap].find_all():
                del every["class"]

    def stylise(self, tag_name: str, style: str):
        for chap in self.content_dict:
            for every in self.content_dict[chap].find_all(): 
                if every.name == tag_name:
                    every["style"] = style