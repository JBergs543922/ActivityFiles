PieList = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
userSelect = 0
userControl = 1
while(userControl > 0):
    print("Welcome to the House of Pies! What pie would you like to choose?")
    print("-----------------------------")
    for i, item in enumerate(PieList,start=1):
        print(i, item, end = ' ') #you can put space between your outputs
    userControl = 0
    userSelect = input("Selection: ") - 1
    
    #will need to use append