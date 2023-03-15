
# Splicing allows us to basically cut out part
# of a string from a specified range
# The range must be within 0 and the length of the
# string we are working with. 

name = "Mohawk" # String we are starting with

# Get first 3 characters of the variable name
front = name[0:3] # Moh
back = name[4:] # wk

print("Front :", front)
print("Back :", back)

print(front + back)


# CodingBat:
def front3(str):
  return str[0:3]*3

def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or (not a_smile and not b_smile):
    return True
  return False

def missing_char(str, n):
  front = str[ : n ]
  back = str[ n+1 : ]
  return front + back
  
  # n = 3
  # name = "Mohawk" 
  # name[3] = "a"
  # name[ : n] = "Moh" 
  # name[ n+1 : ] = "hk"
