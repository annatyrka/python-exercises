spam = {"color": "red", "age": 42}
for v in spam.items():
    print(v)
print(list(spam.keys()))
print("name" in spam.keys())

picnic_items = {"apples": 5, "cups": 2}
print("I am brining " + str(picnic_items.get("cups", 0)) + " cups")
print("I am brining " + str(picnic_items.get("eggs", 0)) + " eggs")

print(spam.setdefault("weight", 56))
print(spam["weight"])
