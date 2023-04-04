# Convert a FlowChart to Python code

# START
num = int( input( "Give a number: "))

x = num // 10
print(x)

y = "30"
print(y)

while int(y) < 40: # done
    x = x % 2 # done
    print(x) 

    if x > 0: # done
        y = y + str(x) # YES condition -> done
        print(y)
        
    else: # x is NOT greater than 0
        y = y + str(45) # NO condition -> done
        print(y)
        
print(y)
# STOP
