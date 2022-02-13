import random
spam = ["cat", "bat", "rat", "elephant"]
print(len(spam))

print(random.choice(spam))

# random.shuffle() - to reorder the list, it modifies the list in place

# append() - adds an item to the end of the list
# insert() -  can inserts a value at any index in the list

spam.append("shark")
print(spam)

spam.insert(1, "dog")
print(spam)

# remove() - to remove a particular value (only the first one will be removed if more than 1)
# del statment - if we know the index, remove() - when we know the value

spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

spam.sort(key=str.lower)
