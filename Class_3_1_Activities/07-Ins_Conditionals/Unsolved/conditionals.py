x = 1
y = 10

# Checks if one value is equal to another
if x == y:
    print(True)
else:
    print(False)
# Checks if one value is NOT equal to another
if x != y:
    print (True)
else:
    print (False)
# Checks if one value is less than another
if x < y:
    print(True)
else:
    print(False)
# Checks if one value is greater than another
if x > y:
    print(True)
else:
    print(False)
# Checks if a value is greater than or equal to another
if x >= y:
    print(True)
else:
    print(False)
# Checks for two conditions to be met using "and"
if x <= y and y %2 == 0:
    print(True)
else:
    print(False)
# Checks if either of two conditions is met
if x <= y or y %2 == 0:
    print(True)
else:
    print(False)
# Nested if statements
if x % 2 == 0:
    
    if y % 2 == 0:
        print(True)