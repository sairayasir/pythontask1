x = 2
print(x ==2)
print(x ==3)
print (x < 3)
print(x>3)

name ="yasir"
age ="23"
if name == "yasir" and age =="23":
    print("goood work")
if name =="yasir" or name == "saira":
    print("thats fine")

name ="yasir"
if name in ["yasir", "jillani"]:
    print("then your name is this")

x = 2
if x is 2:
    print("true")
else:
    print ("does not match")

#is operator (for comparison)
x =[1,2,3,4]
y =[5,6,7,8]
print( x ==y)
print (x is y)

#not operator
print (not False)
print ((not False) is (False))

#Exercise
# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

#for loop
print("for loooooooooooooooooooooooooooooop start")
primes = [2,3,5,7]
for prime in primes:
    print(prime) 

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

#while loop 
print("whillllllllllllllllllllllllllllllle loop start")

count =0
while count<5:
    print(count)
    count+=1

#break and continue statment
count = 0
while True :
    print(count)
    count +=1
    if count>=5:
        break
print("end of loop")
for x in range(10):
    if x%2 == 0:
        continue

    print(x)

print("end of loop")

count = 0;
while(count<5):
    print(count)
    count+=1
else:
    print("count value reached at %d" % (count))

for i in range(1,10):
    if (i%5 ==0):
        break
    print(i)

else:
    print("not printed because loop is terminatd")

#Exercise
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
for number in numbers:
    if number == 237:
        break

    if number %2 == 1:
        continue
    print(number)