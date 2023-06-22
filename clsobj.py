#classes nad objects creation
class myclass:
    variable= "how are you"
    def function(self):
        print("this is the msg inside dthe ckl")
    
myobjectx = myclass()
myobjecty = myclass()

myobjecty.variable ="good morning"

#accessing object variable
print(myobjectx.variable)
print(myobjecty.variable)

#accessing object function
myobjectx.function()

#init function is used for assigning value in a class when class is being initiated 
class memberholder:

    def __init__(self, number):
        self.number = number


#Exercise
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())

