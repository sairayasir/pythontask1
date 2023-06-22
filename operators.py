#Arithmatic operator
number = 1+2+3/4.0
print (number)

#for getting remainder
remainder = 11%3
print(remainder)

#power
squared = 7** 2
cubed = 2 **3
print (squared)
print(cubed)

#multiplying string for repeating sequence
repeatingwords = "hello" * 15
print(repeatingwords)

#using operators with lists
even_no = [2,4,6,8]
odd_no = [1,3,5,7]
total_no = odd_no+even_no
print(total_no)

#repeatv list
print([1,2,3,4] * 5)

#exercise
x = object()
y = object()
x_list =[x] *10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" %len(x_list))
print("y_list contains %d objects" %len(y_list))
print("big_list contains %d objects" %len(big_list))

#testing codeee
if x_list.count(x) ==10 and y_list.count(y) == 10:
    print("almost there...........")
if  big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great Jjob....")


#string formatting
name = "yasir"
age = 23
print ("hello, %s" % name)
print("%s is %d years old" % (name,age))

mylist = [1,2,3,4]
print("Alist: %s" %mylist)
#Exercise

data =("john" , "Doe" ,53.44)
format_string ="hello %s %s. Your current balance is $%s" 
print(format_string% data)