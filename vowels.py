def shortcut(text):
    return "".join(letter for letter in text if letter not in "aeiou")


def shortcut2(text):
    for vowel in "aeiou":
        text = text.replace(vowel, "")
    return text


print(shortcut("Anna is smart"))
