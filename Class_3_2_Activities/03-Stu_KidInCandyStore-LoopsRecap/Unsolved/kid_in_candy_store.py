# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]
shopping_cart = []
userExit = " "
userChoice = 0
# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
while(len(shopping_cart) < allowance):
    for i in candy_list:
        print(i)
        
    userChoice = int(input("What candies would you like to bring home?"))
    shopping_cart.append(candy_list[userChoice]) #the length of shopping cart and how you are getting it, is an issue
    userExit = input("Would you like to continue shopping? (y/n)")
    if userExit == "n":
        break