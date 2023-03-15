# Trace the variable through this
# python code:

### Function
##def tripleIt ( x ):
##	returnValue = x * 3
##	y = x + 10
##	return returnValue
##
### Main Method
##myNumber = 2
##newNumber = tripleIt( myNumber )
### print(newNumber)

# Keep track:
#   - myNumber
#   - newNumber
#   - returnValue
#
# 1. myNumber = 2
# 2. newNumber = tripleIt( myNumber )
# 3. returnValue = x * 3
# 4. returnValue = 6
# 5. y = 12
# 6. we return 6
# 7. newNumber = 6 


##def tripleIt ( x ):
##	returnValue = x * 3
##	myNumber = x + 10
##	print("Module version of myNumber ", myNumber)
##	return returnValue
##
##myNumber = 2
##newNumber = tripleIt( myNumber )
##print("Main method version of myNumber", myNumber)
##print("newNumber after running tripleIt module", newNumber)



# This part was to go over the scope of x
# Remember: there was an x that is local to the callNumber() module
# Remember: there was also an x outside in the main method
# both of these x variables are DIFFERENT!
# This is because of scope :)

### Modules ----
##def callNumber():
##    x = 5 # x in the module
##    print("x in module: ", x)
##    return x
##
##def callDiffNumber():
##    num = 8
##    print("num in module: ", num)
##    return num
##
### Main ---- 
##x = 10 # x in main method
##print("x in main: ", x)
##y = callNumber() 
##print("x in the main: ", x)
##z = callDiffNumber()



# while loop - runs until condition is met
var = 10
while (var > 0):
    print(var)
    var = var - 1

    
# for loop - runs for a finite number of iterations













