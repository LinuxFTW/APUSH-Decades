import genanki

AnkiModel = genanki.Model(
        1809338746,
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
        1716853254,
        'APUSH Decades Master Cards')

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
    questionList = []
    questionTmp = ''
    for char in question:
        if char == ',':
            if questionTmp[0] == ' ':
                questionTmp = questionTmp[1:]
            questionList.append(questionTmp)
            questionTmp = ''
        else:
            questionTmp = questionTmp + char
    for smallQ in questionList:
        AnkiNote = genanki.Note(
                model=AnkiModel,
                fields=[smallQ, answer])
        AnkiDeck.add_note(AnkiNote)

genanki.Package(AnkiDeck).write_to_file('Cards/APUSH Decades Master.apkg')
