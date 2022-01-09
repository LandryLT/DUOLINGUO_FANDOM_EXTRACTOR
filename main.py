from extractHTML import FandomExtractWStyle
from genDeck import GenkiDeck

url = 'https://duonotes.fandom.com/wiki/Japanese'
outputapkg = 'C:/Users/landr/Desktop/Tiiiiips.apkg'

jap_fandom = FandomExtractWStyle(url)
jap_duolingo_ankideck = GenkiDeck("Tiiiiips")

jap_fandom.stylise("h2", 'color: red')
extracted_fandom = FandomExtractWStyle.stringify_content(jap_fandom.content_dict)

for chap in extracted_fandom:
    jap_duolingo_ankideck.add_note(chap, extracted_fandom[chap])

jap_duolingo_ankideck.output_deck(outputapkg)

print("done")
