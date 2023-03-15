# Practicing Python

# Four data types

# Integer - only whole numbers
num = 5
#print(num)

# Float - numbers with decimals
num2 = 15.5
#print(num2)

# Boolean - True or False
b1 = not True
#print("b1 variable: ", b1)

b2 =  not (5 < 3)
#print("b2 variable: ", b2)

b3 = not (3 <= 3)
#print("b3 variable: ", b3)

# String - character strings
word = "PASS Session"
#print(word)

# Functions
# Take 2 numbers and add them together
def sum(a, b):
    c = a + b
    return c

def product(a, b):
    c = a * b
    return c


#print("Sum 1: ", sum(5, 20) )
#print("Sum 2: ", sum(1000, 2023) )
#print("Product 1: ", product(55, 23) )

# always start with IF
# then add in ELIF
# or end with ELSE 


var = 4

if var == 3:
    print("Var is equal to 3: ",True)
elif var < 3:
    print("Var is NOT equal to 3: ",False)
else:
    print("This is the else condition")






