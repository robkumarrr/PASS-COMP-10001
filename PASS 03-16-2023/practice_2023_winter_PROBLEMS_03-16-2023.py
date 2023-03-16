# Python Practice - 2023 Winter
# Author: Robert I. Kumar

# Hello! I hope you find these practice problems useful.
# Make sure to read the questions CAREFULLY, there are key
# words that can make or break your solution. I have provided
# all of the solutions so you can check your work, but
# give everything a try before you look at the answers.



# -------------------------------------------------------------------------------------
# 1. Create a module/function called pos_neg that checks if a non-zero number is
# positive or negative, and returns True if the number is positive, or returns False 
# if the number is negative.

# ----- Solution -----
# Module
def pos_neg( number ):
    if number < 0:
        return False
    elif number > 0:
        return True
    else:
        return "that was a zero!!!!!"


# Main (test area)
# print("Question 1 example runs: ")
# print( pos_neg( -3 ) ) # returns False
# print( pos_neg( 5 ) ) # returns True
# print( pos_neg( 0 ) ) # returns None (no condition for 0)




# -------------------------------------------------------------------------------------
# 2. Ask the user for a number to be inputted and print that number.
# NOTE: No module is required for this.

# ----- Solution -----
# x = int( input("Give us a number! ") )
# x = input("Give us a number! ")
# print( x )




# -------------------------------------------------------------------------------------
# 3. Write a module/function called inRange to check if a number is within two specific ranges.
# The first range is 5 to 18 (inclusive), and the second range is 48 to 91 (exclusive).
# If a value is within either range, return True, and return False if it's outside of
# either range. 
# NOTE: Inclusive means that the numbers in the range are included as part of the
# range, while exclusive means that the numbers in the range are not part of the range.

# ----- Solution -----
def inRange( num ):
    if num in range(5, 19) or num in range(49, 91):
    #if ( num >= 5 and num <= 18 ) or ( num > 48 and num < 91 ):
        return True
    else:
        return False
    

# Main (test area)
#print("Question 3 example runs: ")
#print( inRange( 1 ) ) # returns False
#print( inRange( 5 ) ) # returns True
#print( inRange( 48 ) ) # returns False




# -------------------------------------------------------------------------------------
# 4. Create a module/function called addStars that accepts a string as an argument and returns a string that 
# has been modified to include a set of stars (*) that are equal to the length of the original
# string. For examples see the Main (test area) below.
# NOTE: len() checks the length of strings.

# ----- Solution -----
# Module


# Main (test area)
#print( addStars ( "python" ) ) # returns: python******
#print( addStars ( "class" ) )  # returns: class*****
#print( addStars ( "hi" ))      # returns: hi**




# -------------------------------------------------------------------------------------
# 5. Create a while loop that exits the loop when a number is less than 10.
# Note: Assume that the user enters integers, don't worry about invalid input like strings.
# Note: No module required.
# Note: use input() to get an input from a user
# Note: make sure to use int() to explicitly convert the input to an integer:
#   Like such: user_input = int( input( "Enter a number: "))

# ----- Solution -----




# -------------------------------------------------------------------------------------
# 6. Create a module/function called lotsOfConditions that checks the following conditions a number:
#   Condition 1: value is positive
#       Nested Condition: value is divisible by 2
#           Nested Condition: value is divisible by 3
#   Condition 2: value is negative
#       Nested Condition: value is divisible by 2
#           Nested Condition: value is divisible by 3
# For each condition, make a printout, such as "4 is positive", "4 is visible by 2" and
# "4 is not divisible by 3"

# NOTE: This requires a LOT of conditions! It's okay to take your time with this one.
# Try to draw out a flow chart to help, or use pseudocode to break it down step by step.
# YOU CAN DO THIS! :)

# ----- Solution -----
# Module




# Main (test area) and sample outputs
# lotsOfConditions( 14 )
    # returns:
    # 14 is a positive number!
    # 14 is divisible by 2
    # 14 is not divisible by 3
# lotsOfConditions( 0 )
    # returns:
    # You entered 0
# lotsOfConditions( -18 )
    # -18 is a negative number!
    # -18 is divisible by 2
    # -18 is divisible by 3
# lotsOfConditions( -19 )
    # -19 is a negative number!
    # -19 is not divisible by 2
    # -19 is not divisible by 3
# lotsOfConditions( 10 )
    # 10  is a positive number!
    # 10  is divisible by 2
    # 10  is not divisible by 3




# -------------------------------------------------------------------------------------
# 7. Create a module/function called isPrime that checks if an integer
# is prime. Remember: a prime number is a value that is
# only divisible by itself and 1.
# NOTE: 1 is typically excluded as a prime, so keep that in mind for your for loop.

# ----- Solution -----
# Module
def isPrime( num ):
    if num >= 2:
        prime = True # placeholding for if a number is prime or not
        for i in range(2, num):
            #print(i)
            if num % i == 0:
                prime = False # setting prime to FALSE if num % i is equal to 0
            return prime # show user if number is prime or not
    else:
        return "That is not a number greater than 2!!!!!"

# 10 % 2 = 0 -> NOT PRIME


# Main (test area)
#print("Question 7 example runs: ")
print( isPrime( 10 ) ) # returns False
print( isPrime( 5 ) ) # returns True
print( isPrime( 809 ) ) # returns True
print( isPrime( -1 ) ) # not going to work




# -------------------------------------------------------------------------------------
# 8. Modify #7 to only run the function if the argument is a positive value
# and greater than 1. If the number isn't positive or it's equal to 1, return
# an error message that says "That number was less than or equal to 1."

# ----- Solution -----
# Module






# Main (test area)
#print("Question 8 example runs: ")
#print( isPrimeGreaterThan2( 10 ) ) # returns False
#print( isPrimeGreaterThan2( 5 ) ) # returns True
#print( isPrimeGreaterThan2( -41 ) ) # returns "That number was less than or equal to 1."

    
