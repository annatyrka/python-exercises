def duplicate_count(text):
    # Your code goes here
    unique_letters = {}
    for letter in text:
        if letter.lower() not in unique_letters:
            unique_letters[letter.lower()] = 1
        elif letter.lower() in unique_letters:
            unique_letters[letter.lower()] += 1

    final = {}
    for item, value in unique_letters.items():
        if unique_letters[item] > 1:
            final[item] = value
    count = 0
    for item in final:
        count += 1
    return count


def duplicate_count2(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count


def duplicates2(text):
    return len([letter for letter in set(text.lower()) if text.count(letter) > 1])


print(duplicates2("Inndivisibility"))
