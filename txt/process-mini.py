import genanki

AnkiModel = genanki.Model(
        1618648970,
        'Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            }
        ])

AnkiDeck = genanki.Deck(
        1509212728,
        'APUSH Decades Flash Cards')

with open('src/decades-review-merged.txt') as raw:
    rawLines = raw.readlines()

rawLines = [line[:-1] for line in rawLines]
for line in rawLines:
    if line[0] != '!':
        answer = line[:5]
        question = line[6:]
    elif line[0] == '!':
        answer = line[1:10]
        question = line[11:]
    AnkiNote = genanki.Note(
            model=AnkiModel,
            fields=[question, answer])
    AnkiDeck.add_note(AnkiNote)

genanki.Package(AnkiDeck).write_to_file('Cards/APUSH Decades.apkg')
