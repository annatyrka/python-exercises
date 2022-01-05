def switcheroo(string):
    word = ""
    for letter in string:
        if letter == "a":
            word += "b"
        elif letter == "b":
            word += "a"
        else:
            word += letter
    return word


print(switcheroo("aba"))
