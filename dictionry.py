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

phonebook.pop("saira")
print(phonebook)


#Exercise
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  

# your code goes here
phonebook["Jake"] = 938273443  
del phonebook["Jill"]  

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  