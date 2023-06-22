
phonebook ={}
phonebook["saira"] = 3175008890
phonebook["yasir"] = 3175008894
phonebook["sheeri"] = 3175008896

print(phonebook)

phonebook = {
    "saira"  : 3175008890,
     "yasir" : 3175008894,
     "sheeri": 3175008896
}
print(phonebook)
#iterating over dictionaries
for name, number in phonebook.items():
    print("phone no of %s is %d " %(name,number))

#removing a value
del phonebook["yasir"]
print(phonebook)