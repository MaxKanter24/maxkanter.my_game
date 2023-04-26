# file created by Max Kanter

# built in function that displays something in the terminal
print("Hello there...")

# Syntax error 
# example of a syntax error
# we are telling the computer to assign a value to a label of x 
x = 5

# Syntax error 
# example of syntax error 
x !=6 
# will print true because x declared value is already 5 
print(x != 6)
# this will print false because value of x is not equal to 6
print(x == 6)
# a new value is assigned to x
x = 6
print(x == 6) 
# when printing my_name max prints
my_name = "Max"
# define a function called my_func that prints something    
def my_func(message, name):

    # return  "I can write functions!!!"
    #last thing a function does is return, does not return twice
    return message + name  
# calls the function...
# prints message and name
print(my_func("hello there,", my_name))

def evaluate(x,y):
    if x > y:
        #returns a boolean value
        return x > y 
    else:
        #if return is false, prints NOPE
        return "NOPE"

print (evaluate(6,12))
# function gives message that indicates when a number is divided by another
def find_remainder(x,y):
    # modulo % divides x by y
    # return The remainder of x and y is % (data type)
    return "The remainder of " + str(x) + " and " + str(y) + " is " + str(x%y)

   

# input values to be used in function
# Prints remainder into terminal
# call the function
print(find_remainder(5,6))  