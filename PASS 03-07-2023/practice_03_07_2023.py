# Basic For Loop structure

# rng = range(0, 10)
# print(rng)
# 
# for x in rng:
#     print("value of x: ", x)


# cars = ["f-150", "silverado", "3-series", "explorer", "tacoma" ]
# print("car index 0: ", cars[0])
# print("car index 1: ", cars[1])
# print("car index 2: ", cars[2])

# for model in cars:
    # print(cars[0, 4]) Need integer or slices to get model 
    # print(model) # print model as it changes in loop

# Make a list of values from 0 to 9

# list() will create a list given a range of values
# range(x, y) x = start value    y = stop value (exclusive)
rng = list(range(0,10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(rng)

for num in rng:
    if num % 2 == 0 and num != 0:
        print(num, " is even")
    












    
