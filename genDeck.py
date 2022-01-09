import genanki

class GenkiDeck:
    def __init__(self, deckname: str):
        self.model = genanki.Model(
            1741083659,
            'Duolinguo tips',
            fields=[
                {'name': 'Lesson Title'},
                {'name': 'Contents'}
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{Lesson Title}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Contents}}'
                }
            ]
        )
        self.deck = genanki.Deck(
            1886337849,
            deckname
        )
    
    def add_note(self, title: str, content:str):
        new_note = genanki.Note(
            model=self.model,
            fields=[title, content]
        )
        self.deck.add_note(new_note)

    def output_deck(self, filepath:str):
        genanki.Package(self.deck).write_to_file(filepath)
