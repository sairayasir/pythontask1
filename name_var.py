print("this line will print hello world")
# #python indentaton k leay curly braces use nnh hoti blky tab or space use kea jata hai 

x =1
if x == 1:
    print("x is 1")

print ("hello, world")

#variable and types
myint = 7  for defining integers use this syntax
print(myint)

# for defining floating point number two ways

myfloat= 5.5
print(myfloat)
myfloat = float (7)
print(myfloat)

# string can be defined with single or double quote
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

#simple operators can be executeed on numbers and strings
one =1
two =2
three = one +two
print(three)

string1= "hello"
string2 ="world"
str = string1 +" "+ string2
print(str)

#assignment operator

a,b = 1,2
print(a,b)

#mixing operator between no and string not supported
one =1
two =2
string = "helllo"
print (one + two +string)

#exercise
mystring ="hello"
myfloat =float (10)
myint = 20

#testing code
if mystring == "hello":
    print("string: %s" % mystring)
if isinstance(myfloat , float) and myfloat == 10.0:
    print("float: %f" %myfloat)
if isinstance(myint , int) and myint ==20:
    print ("integer: %d" % myint)