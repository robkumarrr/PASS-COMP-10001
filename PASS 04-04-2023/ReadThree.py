# -------------------------------------
# Read 3 characters at a time from a string. If the substring is a valid number
# add it to a total which will be reported after the whole string is finished.
# If the substring is a valid character, add it to a total string.
# Assume the string length is a multiple of 3 to simplify the solution.
# -------------------------------------

user_input = str( input("Provide any string input with a length that is a multiple of 3 :"))

# "123abc456def" acceptable input for example

n = 0 # our index (where we are in the string)
num_output = 0 # variable to store the total numbers from the inputted string
str_output = "" # variable to store all the string characters from the inputted string

while n < len( user_input ): # while the index is less than the length of the inputted string

    substring = user_input[ n:n+3 ] # n is where we are, n + 3 gives us an exclusive range
    print( substring ) # debug

    for i in substring: # i is the character within the substring

        if i.isdecimal(): # check if the character is a number
            num_output += int( i ) # add number if it's a number

        else: # could also do elif i.isalpha() if we want to target the alphabet
            str_output += i
    
    n += 3

print( f"Total Number: {num_output}" )
print( "Total number: " + str(num_output) )
print( f"Final String: {str_output}" )
print( "Final String: " + str_output )
