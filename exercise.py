import pprint
sentence = "This is a common interview question"

letter = {}

for character in sentence:
    letter.setdefault(character, 0)
    letter[character] = letter[character] + 1

pprint.pprint(letter)
