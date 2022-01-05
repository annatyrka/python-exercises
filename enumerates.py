letters = ['a', 'b', 'c']

dicts1 = {1: "a", 2: "b", 3: "c"}

for letter in enumerate(letters):
    print(letter)

for count, item in enumerate(letters):
    print(count, item)
letters.insert(1, "d")
letters.pop(0)
print(letters)
