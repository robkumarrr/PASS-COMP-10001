# Tracing a flow chart:

# Trace in a table:
# ________    Value
#    X    | 48, 4.8, 0.48 
#    S    | 1, 2,


# 1. S = 1
# 2. SET X = 48
# 3. X = X / 10 -> X = 4.8
# 4. Is X < 1? -> FALSE
# 5. S = S + 1 -> S = 2
# 6. X = X / 10 -> X = 0.48
# 7. Is X < 1? -> TRUE
# 8. PRINT S = 2


# Trace in a table:
# ________    Value
#    N   | 2, 1

# 1. N = 2
# 2. Is N even? -> TRUE
# 3. N = N / 2 -> N = 1
# 4. PRINT N = 1
# 5. Is N == 1? -> Yes
# 6. STOP

# Trace in a table:
# ________    Value
#    N   | 3, 10, 5, 16, 8, 4, 2, 1 

# 1. N = 3
# 2. Is N even? -> FALSE
# 3. N = 3 * N + 1 -> N = 10
# 4. PRINT N = 10
# 5. Is N == 1? -> FALSE
# 6. Is N even? -> TRUE
# 7. N = N / 2 -> N = 5
# 8. PRINT N = 5
# 9. Is N == 1? -> FALSE
# 10. Is N even? -> FALSE
# 11. N = 3 * N + 1 -> N = 16
# 12. PRINT N = 16
# 13. Is N == 1? -> FALSE
# 14. Is N even? -> TRUE
# 15. N = N / 2 -> N = 8
# 16. PRINT N = 8
# 17. Is N == 1? -> FALSE
# 18. Is N even? -> TRUE
# 19. N = N / 2 -> N = 4
# 20. PRINT N = 4
# 21. Is N == 1? -> FALSE
# 22. Is N even? -> TRUE
# 23. N = N / 2 -> N = 2
# 24. PRINT N = 2
# 25. Is N == 1? -> FALSE
# 26. Is N even? -> TRUE
# 27. N = N / 2 -> N = 1
# 28. PRINT N = 1
# 29. Is N == 1? -> TRUE
# 30. STOP




# Create and add elements into a list using .insert(index, value)

myList = []
myList.insert( 0, 10.4 )
myList.insert( 1, 20 )
myList.insert( 2, 30 )
myList.insert( 3, "40" )

##print(myList)


fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
##print(fruits)




# Create and add elements into a list using the list + operator

myList2 = []
myList2 = myList2 + [10]
myList2 = myList2 + [20]
myList2 = myList2 + [30]

##print(myList2)




# Create and add elements into a list using the list + operator
# Use a backwards for loop to populate the list

myList3 = []
for i in range(3, 0, -1):
    myList3 = myList3 + [i]
##    print(myList3)

# https://pythontutor.com/visualize.html#code=myList3%20%3D%20%5B%5D%0Afor%20i%20in%20range%283,%200,%20-1%29%3A%0A%20%20%20%20myList3%20%3D%20myList3%20%2B%20%5Bi%5D%0A%20%20%20%20print%28myList3%29&cumulative=false&curInstr=11&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false





# Remove the year 1978 from this list.

years = [2017,1977,2016,1978,2015,1980,2008,1983,1984,1985,1999,1978,2002,2005,2019]
##print(years)

while 1978 in years:
##    print(years.index(1978))
    years.remove(1978)
##    print( f"Removing 1978 : {years}" )





# Take a string, and add each of the characters of the string into a list.
# Ignore spaces when adding the characters to the list.

str = "h e l l o w o r l d"
strList = []

for i in str:

    if i != " ":
        strList += [i]
    else:
        continue
    
print(strList)














