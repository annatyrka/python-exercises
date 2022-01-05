myPets = ["Zophie", "Pooka", "Fat-tail"]
print("Enter pet name:")
pet_name = input(">")
if pet_name in myPets:
    print("The name already exists")
else:
    myPets += [pet_name]
    print("Name " + pet_name + " has been added to the list.")
print(myPets)
