# Test 2 Recap
# Things to work on?




# Create a module/function called isPrime that checks if an integer
# is prime. Remember: a prime number is a value that is
# only divisible by itself and 1.
# NOTE: 1 is typically excluded as a prime, so keep that in mind for your
# for loop.


def isPrime( num ):
    prime = True # assume prime, but change based on conditional criteria
    for i in range (2, num): # checking up to num
        if num % i == 0: # only == 0 if a number is divisible by another number
            prime = False # change flag
        return prime # return True/False and leave the loop and module

print( "17: ", isPrime( 17 ) )            
print( "34820: ", isPrime( 34820 ) )

