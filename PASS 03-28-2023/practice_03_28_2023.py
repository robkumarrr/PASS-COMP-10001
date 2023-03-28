# 1-D Lists
myList = ["A", "B", "C"]
##print(myList) # What will this print?


# 2-D Lists
myList2D = [["A", "B", "C"], ["A", "B", "C"], ["A", "B", "C"]]
myList2D_2 = [["A", "B", "C"]]*5
##print(myList2D_2)# What will this print?

# myList2D_2
# [ ["A", "B", "C"],
#   ["A", "B", "C"],
#   ["A", "B", "C"],
#   ["A", "B", "C"],
#   ["A", "B", "C"], ]

# myList2D_2.index( [0][0] )
##print(myList2D_2[0][0])


# Task:
# Create a WHILE LOOP that asks users to input a food and the rating.
# Store each pairing of food and rating within a 2-D array such that the output
# looks like:
# [["food", "Rating"], ["food", "Rating"], ["food", "Rating"]] ...etc
# Use a sentinel value of "quit" to quit the loop

# First, what is a sentinel value?

food_and_ratings = [ ["", ""] ]
user_input = ""
i = 0

while user_input.lower() != "quit": # QUIT or qUiT or qUIT will all work now
    food = input("Enter your favourite food or type quit to exit: ")
    if food.lower() == "quit":
        user_input = "quit"
    elif food.lower() != "quit":
        rating = str(input("Please enter a rating for the food or type quit to exit: "))
        if rating.lower() == "quit":
            user_input = "quit"
            break
        elif rating.lower() != "quit":
            food_and_ratings[i][0] = food
            food_and_ratings[i][1] = rating
            print(food_and_ratings)
            food_and_ratings += [["", ""]]
            i += 1 # https://www.tutorialspoint.com/increment-and-decrement-operators-in-python
    
    
# Hey! Great work on this code. Now that we know it works, we can make this EVEN BETTER!
# Next steps are to create a better dialogue with the user, and we can begin some data
# validation. That way we can make sure that the user is enterring the correct information.
# If we only want a rating between 0 and 10 (inclusive), what can we do? 




# Note: Don't worry about this below for now. 
# Placeholder code below: 

##for i in range(len(myList2D)):
##    for j in range(len(myList2D[i])):
##        print(myList2D[i][j])
