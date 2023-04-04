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
##print(myList2D_2[1][1])


# Task:
# Create a WHILE LOOP that asks users to input a food and the rating.
# Store each pairing of food and rating within a 2-D array such that the output
# looks like:
# [["food", "Rating"], ["food", "Rating"], ["food", "Rating"]] ...etc
# Use a sentinel value of "quit" to quit the loop

# Link for i += 1
# https://www.tutorialspoint.com/increment-and-decrement-operators-in-python

# First, what is a sentinel value?

# -----------------------
# Original Version with no inner while loop
# -----------------------

##food_and_ratings = [ ["", ""] ]
##user_input = ""
##i = 0

##while user_input.lower() != "quit": # QUIT or qUiT or qUIT will all work now
##    food = input("Enter your favourite food or type quit to exit: ")
##    if food.lower() == "quit":
##        user_input = "quit"
##    elif food.lower() != "quit":
##        # while 
##        rating = str(input("Please enter a rating for the food or type quit to exit: "))
##        if rating.lower() == "quit":
##            user_input = "quit"
##            break
##        elif rating.lower() != "quit":
##            if rating.isdecimal():
##                int_rating = int(rating)
##                if 0 <= int_rating <= 10:
##                    ##print("the value is within 0 and 10")
##                    food_and_ratings[i][0] = food
##                    food_and_ratings[i][1] = rating
##                    print(food_and_ratings)
##                    food_and_ratings += [["", ""]]
##                    i += 1
##                else:
##                    print(f"Please enter a number between 0 and 10. You entered: {rating}.")
##            else:
##                print(f"Please enter a number between 0 and 10. You entered: {rating}.")

 
# -----------------------
# Modified Version with the while loop
# -----------------------

food_and_ratings = [ ["", ""] ]
user_input = ""
i = 0

while user_input.lower() != "quit": # QUIT or qUiT or qUIT will all work now
    food = input("Enter your favourite food or type quit to exit: ")
    if food.lower() == "quit":
        user_input = "quit"
    elif food.lower() != "quit":
        # enter rating here
        rating = str(input("Please enter a rating for the food or type quit to exit: "))
        # just like normal, check to see if it says 'quit'
        if rating.lower() == "quit":
                user_input = "quit"
                break
        # if it says anything besides "quit" continue to here:
        else:
            # while loop checks to see if the value is a number, OR if the rating is < 0 or > 10
            while (rating.isdecimal() == False and rating.lower() != "quit") or \
                  (rating.isdecimal() and (int(rating) < 0 or int(rating) > 10)):
                print(f"Please enter a number between 0 and 10. You entered: {rating}.")
                rating = str(input("Please enter a rating for the food or type quit to exit: "))
##                if rating.lower() == "quit":
##                    break

            if rating.lower() != "quit":
                # Leave the while loop and add items to our list                 
                food_and_ratings[i][0] = food
                food_and_ratings[i][1] = rating
                print(food_and_ratings)
                food_and_ratings += [["", ""]]
            else:
                break
            
            i += 1 # increment counter to place new list items
                    

