# YEHIA RASHEED
# TP072510
def insertItem():
    newItem = []
    alreadyExists = False
    while alreadyExists == False: #While loop exists to ensure code chosen doesn't already exist
        codeAdd = input("Enter code of your item: ")
        with open("inventory.txt", 'r') as f:
            lines = f.readlines()
        finderIndex = []
        finder = -1 #find function returns -1 at negative output and 2 at positive output
        used = False
        for x in lines:
            finder = x.find(codeAdd)
            finderIndex.append(finder)
            if finder >= 1: #output of 2 by find function implies the code has been found in the list
                alreadyExists = False #makes entire while loop repeat
                used = True #prevents code from progressing to next input
                print("This code is already being used, pick another one.")
        if used == False:
           alreadyExists = True
    descriptionAdd = input("Enter description of your item: ")
    categoryAdd = input("Enter category of your item: ")
    unitAdd = input("Enter unit of your item: ")
    priceAdd = input("Enter price of your item: ")
    quantityAdd = input("Enter quantity of your items: ")
    minimumAdd = input("Enter minimum number of items allowed of this: ")
    newItem.append(codeAdd)
    newItem.append(descriptionAdd)
    newItem.append(categoryAdd)
    newItem.append(unitAdd)
    newItem.append(priceAdd)
    newItem.append(quantityAdd)
    newItem.append(minimumAdd)
    finalList = str(newItem) 
    with open('inventory.txt', 'a') as f:
        f.write('\n')        
        f.write(finalList)
    print("Item has been added to the inventory.")
    Backtomenu = input("Do you want to go back to menu? (yes/no)")
    if Backtomenu == "yes":
        loginauth()
    else:
        print("Ok")
def updateItem():
    ask = input("Enter product code of item you would like to update: ")
    with open("inventory.txt", 'r') as f:
        lines = f.readlines()
    finderIndex = []
    finder = -1
    for x in lines:
        finder = x.find(ask)
        finderIndex.append(finder)
        if finder >= 1:
            linesIndex = len(finderIndex) - 1
            finalList = lines[linesIndex]
            print(finalList)
            question = input("What would you like to change? ")
            ans = input("What would you like to replace it with? ")
            changedList = finalList.replace(question, ans)
            print(changedList)
            lines.pop(linesIndex)
            lines.insert(linesIndex, changedList)
            print(lines)
            with open("inventory.txt", 'w') as file:
                file.writelines(lines)
    Backtomenu = input("Do you want to go back to menu? (yes/no)")
    if Backtomenu == "yes":
        loginauth()
    else:
        print("Ok")
def deleteItem():
        ask = input("Enter Product Code of item you would like deleted: ")
        with open("inventory.txt", 'r') as f:
             lines = f.readlines()
        finderIndex = []
        finder = -1
        for x in lines:
             finder = x.find(ask)
             finderIndex.append(finder)
             if finder >= 1:
                  linesIndex = len(finderIndex) - 1
                  finalList = lines[linesIndex]
                  print("This item has been deleted: " + finalList)
                  lines.pop(linesIndex)
                  lines.pop(linesIndex)
                  print(lines)
                  with open("inventory.txt", 'w') as file:  
                    file.writelines(lines)
        Backtomenu = input("Do you want to go back to menu? (yes/no)")
        if Backtomenu == "yes":
            loginauth()
        else:
            print("Ok")
def stockTaking():
    ask = input("Enter Product Code of item whose stock you would like updated: ")
    with open("inventory.txt", 'r') as f:
        lines = f.readlines()
    finderIndex = []
    finder = -1
    for x in lines:
        finder = x.find(ask)
        finderIndex.append(finder)
        if finder >= 1:
            linesIndex = len(finderIndex) - 1
            finalList = lines[linesIndex]
            print(finalList)
            splitlist = finalList.split(',')
            print("Quantity of stock is " + splitlist[5])
            ans = input("Would you like to change this quantity(yes/no)? ")
            if ans == "yes":
                ask2 = input("What would you like to change it to? ")
                splitlist.pop(5)
                splitlist.insert(5, " '" + ask2 + "'")
                mySeparator = ","
                y = mySeparator.join(splitlist)
                print(y)
                lines.pop(linesIndex)
                lines.insert(linesIndex, y)
                with open("inventory.txt", 'w') as file:
                    file.writelines(lines)         
                
            elif ans == "no":
                print("Okay")
            else:
                print("That is not a valid input: ")
    Backtomenu = input("Do you want to go back to menu? (yes/no)")
    if Backtomenu == "yes":
        loginauth()
    else:
        print("Ok")
def viewReplenishList():
    with open("inventory.txt", 'r') as f:
        lines = f.readlines()
    print("Replenish List:")
    print("~~~~~~~~~~~~~~~~~~~")
    for x in lines:
        item = x.strip().strip("[]").split(",")
        item = [value.strip().strip("'") for value in item]
        if len(item) >= 7:
            code = item[0]
            description = item[1]
            category = item[2]
            unit = item[3]
            price = item[4]
            quantity = int(item[5])
            minimum = int(item[6])
            if quantity < minimum:
                print("Code: {}".format(code))
                print("Description: {}".format(description))
                print("Category: {}".format(category))
                print("Unit: {}".format(unit))
                print("Price: {}".format(price))
                print("Quantity: {}".format(quantity))
                print("Minimum: {}".format(minimum))
                print("~~~~~~~~~~~~~~~~~~~")
                Backtomenu = input("Do you want to go back to menu? (yes/no)")
                if Backtomenu == "yes":
                    loginauth()
                else:
                    print("Ok")
def stockReplenish():
    ask = input("Enter code of item you want replenished: ")
    with open("inventory.txt", 'r') as f:
        lines = f.readlines()
        finderIndex = []
        finder = -1
        for x in lines:
            finder = x.find(ask)
            finderIndex.append(finder)
            if finder >= 1:
                linesIndex = len(finderIndex) - 1
                finalList = lines[linesIndex]
                splitList = finalList.strip().strip("[]").split(",")
                splitList = [y.strip().strip("'") for y in splitList]
                print(splitList)
                print("Quantity is: " + splitList[5])
                ask2 = input("Would you like to update the quantity? (yes/no) ")
                if ask2 == "yes":
                    ask3 = input("Enter new quantity: ")
                    print(splitList[5])
                    replacedList = finalList.replace(splitList[5], ask3)
                    print(replacedList)
                    lines.pop(linesIndex)
                    lines.insert(linesIndex, replacedList)
                    with open("inventory.txt", 'w') as file:
                        file.writelines(lines)
    Backtomenu = input("Do you want to go back to menu? (yes/no)")
    if Backtomenu == "yes":
        loginauth()
    else:
        print("Ok")
def searchItems():
    print("1 | Search item by description: " "\n" "2 | Search item by code range." )
    print("3 | Search items in a specific category")
    print("4 | Search items in a specific price range.")

    ans = input("Enter a number from 1 to 4: ")
    correctInput = True
    rangeCheck = False
    if ans == "1":
        ans2 = input("Enter description: ")
    elif ans == "2":
        ans2 = input("Enter a code range (ex. 3000, 5000): ")
        rangeCheck = True
        correctInput = False
    elif ans == "3":
        ans2 = input("Enter a category: ")        
    elif ans == "4":
        ans2 = input("Enter a price range (ex. 30, 50): ")
        rangeCheck = True
        correctInput = False
    else:
        print("Your entry was out of the range")
        correctInput = False

    if correctInput == True:
        with open("inventory.txt", 'r') as f:
            lines = f.readlines()
            finderIndex = []
            finder = -1
            for x in lines:
                finder = x.find(ans2)
                finderIndex.append(finder)
                if finder >= 1:
                    linesIndex = len(finderIndex) - 1
                    finalList = lines[linesIndex]
                    print(finalList)
    if rangeCheck == True:
        with open("inventory.txt", 'r') as f:
            lines = f.readlines()
        splitAns = ans2.split(", ")
        firstInput = splitAns[0]
        secondInput = splitAns[1]
        finderIndex = []
        finder = -1
        for line in lines:
            item = line.strip().strip("[]").split(", ")
            item = [value.strip().strip("'") for value in item]
            if len(item) >= 7:
                code = item[0]
                price = float(item[4])
                if ans == "2" and firstInput <= code <= secondInput:
                    print(line)
                elif ans == "4" and float(firstInput) <= price <= float(secondInput):
                    print(line)
    Backtomenu = input("Do you want to go back to menu? (yes/no)")
    if Backtomenu == "yes":
        loginauth()
    else:
        print("Ok")
def adminFunction():
    print("1 | Insert new Item")
    print("2 | Update Item")
    print("3 | Delete Item")
    print("4 | Stock Taking")
    print("5 | View Replenish List")
    print("6 | Stock Replenish")
    print("7 | Search Item")
    print("8 | Add new user")
    print("9 | Exit")
    choice = input("Enter a number: ")
    if choice == "1":
        insertItem()
    elif choice == "2":
        updateItem()
    elif choice == "3":
        deleteItem()
    elif choice == "4":
        stockTaking()
    elif choice == "5":
        viewReplenishList()
    elif choice == "6":
        stockReplenish()
    elif choice == "7":
        searchItems()
    elif choice == "8":
        print("adding new user into userdata.txt")
        with open("userdata.txt", "r") as h:
            lines = h.readlines()
            askUserType = input("Which user would you like to add? (admin, inventory checker, or purchaser)")
            askUsername = input("Enter username you would like to add: ")
            askPassword = input("Enter password you would like to add: ")
            if askUserType == "admin":
                lines[0] = lines[0].replace('\n', '')
                adminIndex = lines[0]
                splitAdmins = adminIndex.split(", ")
                splitAdmins.append(askUsername)
                splitAdmins.append(askPassword + "\n")
                mySeparator = ", "
                x = mySeparator.join(splitAdmins)
                print(x)
                lines.pop(0)
                lines.insert(0, x)
                with open("userdata.txt", "w") as k:
                    k.writelines(lines)
            elif askUserType == "inventory checker":
                lines[1] = lines[1].replace('\n', '')
                adminIndex = lines[1]
                splitAdmins = adminIndex.split(", ")
                splitAdmins.append(askUsername)
                splitAdmins.append(askPassword + "\n")
                mySeparator = ", "
                x = mySeparator.join(splitAdmins)
                print(x)
                lines.pop(1)
                lines.insert(1, x)
                with open("userdata.txt", "w") as k:
                    k.writelines(lines)
            elif askUserType == "purchaser":
                lines[2] = lines[2].replace('\n', '')
                adminIndex = lines[2]
                splitAdmins = adminIndex.split(", ")
                splitAdmins.append(askUsername)
                splitAdmins.append(askPassword + "\n")
                mySeparator = ", "
                x = mySeparator.join(splitAdmins)
                print(x)
                lines.pop(2)
                lines.insert(2, x)
                with open("userdata.txt", "w") as k:
                    k.writelines(lines)
            else:
                print("This user type does not exist")

    elif choice == "9":
        print("Exited system")

def inventoryFunction():
    print("1 | Stock taking")
    print("2 | Search item")
    print("3 | Exit")
    choice = input("Enter a number: ")
    if choice == "1":
        stockTaking()
    elif choice == "2":
        searchItems()
    elif choice == "3":
        print("Exited system")

def purchaserFunction():
    print("1 | Replenish List")
    print("2 | Stock Replenish")
    print("3 | Search Item")
    print("4 | Exit")
    choice = input("Enter a number: ")
    if choice == "1":
        viewReplenishList()
    elif choice == "2":
        stockReplenish()
    elif choice == "3":
        searchItems()
    elif choice == "4":
        print("Exited system")  

def loginauth():
    with open("userdata.txt", 'r') as g:
        admin = g.readline()
        inventory = g.readline()
        purchaser = g.readline()
    adminList = admin.split(", ")
    adminList[-1] = adminList[-1].replace("\n", "")
    inventoryList = inventory.split(", ")
    purchaserList = purchaser.split(", ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    correctPass = False
    ask = input("Are you an admin, inventory checker, or a purchaser: ")
    if ask == "admin":
        for x in adminList:
                if correctPass == False:
                    while username == x:
                        index = adminList.index(x)
                        passIndex = index + 1
                        if password == adminList[passIndex]:
                            if correctPass == False:
                                print("Correct Username and Password")
                                correctPass = True
                                adminFunction()


    elif ask == "inventory checker":
        for y in inventoryList:
            if correctPass == False:
                if username == y:
                    index = inventoryList.index(y)
                    passIndex = index + 1
                    if password == inventoryList[passIndex]:
                        if correctPass == False:
                            print("Correct Username and Password")
                            correctPass = True
                            inventoryFunction()

    elif ask == "purchaser":
        for z in purchaserList:
            if correctPass == False:
                if username == z:
                    index = purchaserList.index(z)
                    passIndex = index + 1
                    if password == purchaserList[passIndex]:
                        if correctPass == False:
                            print("Correct Username and Password")
                            correctPass = True
                            purchaserFunction()


loginauth()



