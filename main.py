from bs4 import BeautifulSoup
import urllib.request
from os import cpu_count, listdir
from os.path import isfile, join, abspath

url = 'https://duonotes.fandom.com/wiki/Japanese'
with urllib.request.urlopen(url) as response:
    soup = BeautifulSoup(response.read(), 'html.parser')

toc = soup.find(id="toc")

