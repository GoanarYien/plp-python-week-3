count = 1
total = 0

# BUG: Added missing colon ':' at the end of the while loop statement.
# BUG: Changed loop condition from '< 5' to '<= 5' so it includes 5, correcting the sum from 10 to 15.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Converted integer total to a string using str() to fix the TypeError during string concatenation.
print("Sum of 1 to 5 is: " + str(total))