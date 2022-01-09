from extractHTML import FandomExtractWStyle
from genDeck import GenkiDeck

url = 'https://duonotes.fandom.com/wiki/Japanese'
outputapkg = 'C:/Users/landr/Desktop/Tiiiiips.apkg'

jap_fandom = FandomExtractWStyle(url)
jap_duolingo_ankideck = GenkiDeck("Tiiiiips")

jap_fandom.stylise("th", 'background-color: #ccc;text-align: left; border-bottom: 1px solid black')
jap_fandom.stylise("tr", 'background-color: #eee;text-align: left; border-bottom: 1px solid black')
extracted_fandom = FandomExtractWStyle.stringify_content(jap_fandom.content_dict)

for chap in extracted_fandom:
    jap_duolingo_ankideck.add_note(chap, extracted_fandom[chap])

jap_duolingo_ankideck.output_deck(outputapkg)

print("done")
