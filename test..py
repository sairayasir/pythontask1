import random

def function():

    count =0
    while(True):
        x = random.randint(1,10)
        print("enter no of your choice")
        num = int(input())
        if (x == num):
            print ("good job")
            break
        elif (x>num):
            print("your no is small")
        else:
            print("no u entered is large")
            
        count+=1
    print("no of turns are ", count)  

function()




