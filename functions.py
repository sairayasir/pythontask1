#block_head:
    # Ist blockline
    # 2nd blockline
    # ....

#simple function
def my_function():
    print("hello from my function")

my_function()

#receiive arguments
def my_function_with_argument(username, psswd):
    print("hello %s from my function your password is %s" %(username,psswd))


def sum_two_no(x ,y):
    return x+y


my_function()
my_function_with_argument("saira", 1234)
x =sum_two_no(2,3)
print(x)

#Exercise
# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
