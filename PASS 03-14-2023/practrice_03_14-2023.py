# Tracing Example 1 from PDF
#
# 1. S = 1
# 2. X = 48
#   - X/10 
# 3. X = 4.8
# 4. X < 1? -> FALSE
# 5. S = 2
# 6. X = 0.48 
# 7. X < 1? -> TRUE
# 8. prints S = 2


# Tracing Example 2 from PDF - N = 2
#
# 1. N = 2
# 2. is N even? -> TRUE
# 3. N = 1
# 4. print N = 1
# 5. is N == 1? -> TRUE


# Tracing Example 2 from PDF - N = 3
#
# 1. N = 3
# 2. is N even? -> FALSE
# 3. N = 10
# 4. print N = 10
# 5. is N == 1? -> FALSE
# 6. is N even? -> TRUE
# 7. N = 5
# 8. print N = 5
# 9. is N == 1? -> FALSE
# 10. is N even? -> FALSE
# 11. N = 16
# 12. print N = 16
# 13. is N == 1? -> FALSE
# 14. is N even? -> TRUE
# 15. N = 8
# 16. print N = 8
# 17. is N == 1? -> FALSE
# 18. is N even? -> TRUE
# 19. N = 4
# 20. print N = 4
# 21. is N == 1? -> FALSE
# 22. is N even? -> TRUE
# 23. N = 2
# 24. print N = 2
# 25. is N == 1? -> FALSE
# 26. is N even? -> TRUE
# 27. N = 1
# 28. print N = 1
# 29. is N == 1? -> TRUE
# 30. we are done!!!!!!!! 


# Write a trace for the following program:

# Modules/Functions --- 
def multiplyIt( myNumber ):
    
    if myNumber >= 5.8:
        myNumber = 10
        
    returnValue = myNumber * 22
    # myNumber = myNumber + 1
    return returnValue

# Main ---
myNumber = 5.8
print(myNumber)
newNumber = multiplyIt( myNumber )
print(newNumber)



# 1. myNumber = 5.7
# 2. newNumber = tripleIt( 5.7 )
# 3. returnValue = 5.7 * 22  ->  125.4
# 4. myNumber = 5.7 + 1 -> 6.7
# 5. return returnValue (125.4)
# 6. newNumber = 125.4 





