# Duolinguo Fandom Extractor

Duolinguo Fandom Extractor is a tiny script that allows you to extract the content of the [duonotes.fandom.com/wiki](https://duonotes.fandom.com/wiki/Duolingo_Tips_and_Notes_Wiki) and extract it into a Anki deck.

## Installation

Use the package manager pip to install this script :
'''bash
pip install requirements.txt
'''

## genDeck

genDeck solely uses a [library developped by Kerrick Staley](https://github.com/kerrickstaley/genanki)

## extractHTML

extractHTML solely uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). 

Some Extra options on stylizing :
You can use the method
'''python
FandomExtractWStyle.stylise(tag_name: str, style: str):
'''
to insert style in your HTML. 
Example :
'''python
FandomeExtractWStyle.stylise("h2", "color: red; border: 1px solid black")