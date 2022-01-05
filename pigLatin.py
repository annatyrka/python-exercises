# begins with a vowel - yay added at the end
# begins with consonant ot consonant cluster - moved to the end followed by ay

message = input()
vowels = ("a", "e", "i", "o", "u", "y")

pigLatin = []

words = message.split()

for word in words:
    # Separate the non-letters at the start of the word
    non_letters = ""
    while len(word) > 0 and not word[0].isalpha():
        non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(non_letter)

    non_letters_end = ""
    while not word[-1].isalpha():
        non_letters_end += word[-1]
        word = word[:-1]

# Remember if the word was in uppercase or title case.
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()  # Make the word lowercase for translation.
