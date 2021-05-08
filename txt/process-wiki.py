import genanki
import wikipediaapi

AnkiModel = genanki.Model(
        2104529555,
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
        1788047863,
        'APUSH Decades Masochist Cards')

wiki_wiki = wikipediaapi.Wikipedia('en')

with open('src/decades-review-merged.txt') as raw:
    rawLines = raw.readlines()

rawLines = [line[:-1] for line in rawLines]

for line in rawLines:
    if line[0] != '!':
        question = line[6:]
    elif line[0] == '!':
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
        wikisum = wiki_wiki.page(smallQ).summary.partition('\n')[0]
        AnkiNote = genanki.Note(
                model=AnkiModel,
                fields=[smallQ, wikisum])
        AnkiDeck.add_note(AnkiNote)

genanki.Package(AnkiDeck).write_to_file('Cards/APUSH Decades Masochist.apkg')
