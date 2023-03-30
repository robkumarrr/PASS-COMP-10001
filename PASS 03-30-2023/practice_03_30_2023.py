# Postal Code format:
# 7-character: A#A #A#
# 6-character: A#A#A#

# Note: \ is for a new line to continue a statement

# Hello! I went ahead and made the checkPostalCode a function and then I created a sample of
# how the code could be run below. 

# ---- MODULES
def checkPostalCode( postal_code ):
    if len(postal_code) == 7: 
        if postal_code[0].isalpha() and \
          postal_code[1].isdecimal() and \
          postal_code[2].isalpha() and \
          postal_code[3].isspace() and \
          postal_code[4].isdecimal() and \
          postal_code[5].isalpha() and \
          postal_code[6].isdecimal():
            return f"{postal_code} is valid!"
        else:
            return f"{postal_code} is NOT valid! Try again"
    if len(postal_code) == 6:
        if postal_code[0].isalpha() and \
           postal_code[1].isdecimal() and \
           postal_code[2].isalpha() and \
           postal_code[3].isdecimal() and \
           postal_code[4].isalpha() and \
           postal_code[5].isdecimal():
            return f"{postal_code} is valid!"
        else:
            return f"{postal_code} is NOT valid! Try again"


# ---- MAIN
postal_code = str(input("Enter a postal code: "))
print(checkPostalCode( postal_code ) )

