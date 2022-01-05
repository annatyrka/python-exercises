def sort_string(phrase):
    print("Enter words to be sorted")
    phrase = input()
    list1 = phrase.split()
    list1.sort()
    return " ".join(list1)


print(sort_string(input()))
