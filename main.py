from fandomExtract import FandomExtract
#Get HTML
url = 'https://duonotes.fandom.com/wiki/Japanese'

jap_fandom = FandomExtract(url)
for soup in jap_fandom.content_dict:
    print(soup)