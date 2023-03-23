# Strings

var = "python"
var_len = len(var)

#for i in range(var_len): # go from 0 to the end of var
    #print( var[i] )

# Testing out the sort on Characters:
test_list = ["p", "P", "y", "t", "T"] # p = 112, P = 80
test_list.sort()
#print(test_list)


# Lists

##years = [2017,1977,2016,1978,2015,1977,1980,2008,1983,1984,1985,1999,2002,2005,2019]
##years.append(2023)

##for i in range(len(years)):
##    if years[i] == 1977:
##        print("1977 is at index ", i)

#print(years.index(1977))

#print("Before removing 2023")
#for i in range(len(years)):
    #print(years[i])

#print("After removing 2023")
#years.remove(2023)
#for i in range(len(years)):
    #print( years[i])

#print("Sorted list after removing 2023")
#years.sort()
#for i in range(len(years)):
    #print( years[i])

#print("Reverse list after removing 2023 using .reverse()")
#years.reverse()
#for i in range(len(years)):
    #print( years[i])

#print("Reverse list after removing 2023 using .sort(reverse = True)")
#years.sort(reverse=True)
#for i in range(len(years)):
    #print( years[i])


# Create a list called myList, and use a backwards for loop to add 1 element at a time,
# print the list after each change.
# Without using any list methods.

myList = []
for i in range(9, 0, -1): # can also use i--
    #myList = myList + [0]
    myList += [0]
    print(myList)





















