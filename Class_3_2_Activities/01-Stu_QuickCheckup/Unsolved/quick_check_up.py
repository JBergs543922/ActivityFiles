import random

# Print Hello User!
print("Hello User!")

# Take in User Input
userName = " "
userName = input("What is your name: ")

# Respond Back with User Input
print(f"Hello {userName}")

# Take in the User Favorite Number
userNum = 0
userNum = int(input(f"What is your favorite number: "))

# Respond Back with a statement based on your favorite number
if userNum > 5280:
    print(f"Your number is bigger than my favorite number.")
elif userNum == 5280:
    print(f"Your number is equal to my favorite number.")
elif userNum < 5280:
     print(f"Your number is less than to my favorite number.")