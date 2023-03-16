# Module/Function
def formatNumber( number ):
    if number % 2 == 0:
        formattedNumber = "**" + str( number ) + "*"
    else:
        formattedNumber = "*" + str( number ) + "*"
    return formattedNumber

# Main 
c = 10 
p = 6
output = "" 
while c < 22:
    temp = c + p
    p = c
    c = temp
    output = output + formatNumber( c )
print(output)


# 1. SET c to 10
# 2. SET p to 6
# 3. SET output to ""

# ---- First time at start of While Loop
# 4. CHECK if c is < 22 -> TRUE
# 5. SET temp to c + p (temp = 16)
# 6. SET p to c (p = 10)
# 7. SET c to temp (c = 16)
# 8. SET output to output + formatNumber( c )
# 9.  [ in module ] number = 16
# 10. [ in module ] CHECK if number % 2 is equal to 0 -> TRUE
# 11. [ in module ] SET formattedNumber to "**16*"
# 12. SET output to "**16*"

# ---- Second time at start of While loop
# 13. CHECK if c is < 22 -> TRUE
# 14. SET temp to c (16) + p (10) (temp = c + p or -> 26)
# 15. SET p to c (p = 16)
# 16. SET c to temp (c = 26)
# 17. SET output to output + formatNumber( c )
# 18. [ in module ] number = 26
# 19. [ in module ] CHECK if number % 2 is equal to 0 -> TRUE
# 20. [ in module ] SET formattedNumber to "**26*"
# 21. SET output to output ("**16*") + formattedNumber ("**26*") (output = "**16***26*")

# ---- Third time at start of while loop
# 22. CHECK if c is < 22 -> FALSE
# 23. PRINT output (therefore printing "**16***26*")
