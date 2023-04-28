from datetime import date
from datetime import datetime
today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

item = 'Menu'
qty = 'Qty'
sizee = 'Size'
totall = 'Total'

thelist = "\nSelect Code"
classic = ['Okinawa', '   Wintermelon', '   Cookies n Cream']
classic16oz = 75
classic22oz = 85

premium = [' --- Dark Choco',' --- Ube', ' --- Salted Caramel']
premium16oz = 85
premium22oz = 100

fruitblend = ['Green apple', 'Lemon', 'Strawberry']
fruitblend16oz = 65
fruitblend22oz = 75
listorder = ['1)', '2)', '3)']
orderlist = []
sizelist = []
subtotal = []
quantitytotal = []
accounts = ['uyguangco', 'catid', 'saludes', 'otero', 'jabulan', 'dumangcas', 'casing']
password_data = ['uyguangco', 'catid', 'saludes', 'otero', 'jabulan', 'dumangcas', 'casing']

while True:
    log_in = str(input("Log in: "))
    password = str(input("Password: ")) 
    if log_in.lower() == accounts[0] and password == password_data[0]:
        print()
        print("Welcome back!\nCashier: Francis Uyguangco")
        print()
        break
    elif log_in.lower() == accounts[1] and password == password_data[1]:
        print()
        print("Welcome back!\nCashier: Edmarlen Catid")
        print()
        break
    elif log_in.lower() == accounts[1] and password == password_data[1]:
        print()
        print("Welcome back!\nCashier: Edmarlen Catid")
        print()
        break
    elif log_in.lower() == accounts[2] and password == password_data[2]:
        print()
        print("Welcome back!\nCashier: Joshua Saludes")
        print()
        break
    elif log_in.lower() == accounts[3] and password == password_data[3]:
        print()
        print("Welcome back!\nCashier: Kenneth Otero")
        print()
        break
    elif log_in.lower() == accounts[4] and password == password_data[4]:
        print()
        print("Welcome back!\nCashier: Mae Jabulan")
        print()
        break
    elif log_in.lower() == accounts[5] and password == password_data[5]:
        print()
        print("Welcome back!\nCashier: Mary Coelen Dumangcas")
        print()
        break
    elif log_in.lower() == accounts[6] and password == password_data[6]:
        print()
        print("Welcome back!\nCashier: Chricelle Casing")
        print()
        break
    else:
        print("Please check your password and account name and try again.")
        print()


print("\nWelcome to I-tea Milktea Shop!\n")

order = True
while order == True:
    print('------------- Menu -------------\n')
    
    print("Code        Name\n")
    print('1) --- Classic Milktea')
    print('2) --- Premium Milktea')
    print('3) --- Fruit Blends Milktea')
    print()
    select = str(input("Select Code:"))
    if select == "1":
        print()
        print("***Classic Milktea***\n")
        print("Code        Name\n")
        for j in range(0, len(classic)):
            print(f"{listorder[j]}{classic[j]:>10s}")
        classicselect = str(input("Enter Code: "))
        if classicselect == "1":
            print("Your flavor: Okinawa")
            quantitytrue = True
            while quantitytrue == True:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("Invalid")
                    quantitytrue = True
                else:
                    quantitytotal.append(quantity)
                    quantitytrue = False
            sizeorder = True
            while sizeorder == True:
                print()
                size = str(input("Size     &     Price: \n1) -- 16 oz: 75php \n2) -- 22 oz: 85php \nEnter code:"))
                if size == "1":
                    size = 75
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Okinawa')
                    sizelist.append('16oz')
                    sizeorder = False
                elif size == "2":
                    size = 85
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Okinawa')
                    sizelist.append('22oz')
                    sizeorder = False
                else:
                    print("Invalid number")
                    sizeorder = True
            nextorder = True
            while nextorder == True:
                nextorder = input("Purchase another milktea? y/n: ")
                if nextorder.lower() == 'y':
                    order = True
                elif nextorder.lower() == 'n':
                    order = False
                else:
                    print("Invalid keyword")
                    nextorder = True
        elif classicselect == "2":
            print("Your Flavor: Wintermelon")
            quantitytrue = True
            while quantitytrue == True:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("Invalid")
                    quantitytrue = True
                else:
                    quantitytotal.append(quantity)
                    quantitytrue = False
            sizeorder = True
            while sizeorder == True:
                print()
                size = str(input("Size     &     Price: \n1) -- 16 oz: 75php \n2) -- 22 oz: 85php \nEnter code:"))
                if size == "1":
                    size = 75
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Wintermelon')
                    sizelist.append('16oz')
                    sizeorder = False
                elif size == "2":
                    size = 85
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Wintermelon')
                    sizelist.append('22oz')
                    sizeorder = False
                else:
                    print("Invalid number")
                    sizeorder = True
            nextorder = True
            while nextorder == True:
                nextorder = input("Purchase another milktea? y/n: ")
                if nextorder.lower() == 'y':
                    order = True
                elif nextorder.lower() == 'n':
                    order = False
                else:
                    print("Invalid keyword")
                    nextorder = True
        elif classicselect == "3":
            print("Your Flavor: Cookies n Cream")
            quantitytrue = True
            while quantitytrue == True:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("Invalid")
                    quantitytrue = True
                else:
                    quantitytotal.append(quantity)
                    quantitytrue = False
            sizeorder = True
            while sizeorder == True:
                print()
                size = str(input("Size     &     Price: \n1) -- 16 oz: 75php \n2) -- 22 oz: 85php \nEnter code:"))
                if size == "1":
                    size = 75
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Cookies n Cream')
                    sizelist.append('16oz')
                    sizeorder = False
                elif size == "2":
                    size = 85
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Cookies n Cream')
                    sizelist.append('22oz')
                    sizeorder = False
                else:
                    print("Invalid number")
                    sizeorder = True
            nextorder = True
            while nextorder == True:
                nextorder = input("Purchase another milktea? y/n: ")
                if nextorder.lower() == 'y':
                    order = True
                elif nextorder.lower() == 'n':
                    order = False
                else:
                    print("Invalid keyword")
                    nextorder = True
        else:
            print("Welcome back to Main Menu")
            order = True
    elif select == "2":
        print()
        print("***Premium Milktea***\n")
        print("Code        Name\n")
        for j in range(0, len(premium)):
            print(f"{listorder[j]}{premium[j]:>5s}")
        classicselect = str(input("Enter Code: "))
        if classicselect == "1":
            print("Your Flavor: Dark Choco")
            quantitytrue = True
            while quantitytrue == True:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("Invalid")
                    quantitytrue = True
                else:
                    quantitytotal.append(quantity)
                    quantitytrue = False
            sizeorder = True
            while sizeorder == True:
                print()
                size = str(input("Size     &     Price: \n1) -- 16 oz: 75php \n2) -- 22 oz: 85php \nEnter code:"))
                if size == "1":
                    size = 85
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Dark Choco')
                    sizelist.append('16oz')
                    sizeorder = False
                elif size == "2":
                    size = 100
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Dark Choco')
                    sizelist.append('22oz')
                    sizeorder = False
                else:
                    print("Invalid number")
                    sizeorder = True
            nextorder = True
            while nextorder == True:
                nextorder = input("Purchase another milktea? y/n: ")
                if nextorder.lower() == 'y':
                    order = True
                elif nextorder.lower() == 'n':
                    order = False
                else:
                    print("Invalid keyword")
                    nextorder = True

        elif classicselect == "2":
            print("Your Flavor: Ube")
            quantitytrue = True
            while quantitytrue == True:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("Invalid")
                    quantitytrue = True
                else:
                    quantitytotal.append(quantity)
                    quantitytrue = False
            sizeorder = True
            while sizeorder == True:
                print()
                size = str(input("Size     &     Price: \n1) -- 16 oz: 75php \n2) -- 22 oz: 85php \nEnter code:"))
                if size == "1":
                    size = 85
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Ube')
                    sizelist.append('16oz')
                    sizeorder = False
                elif size == "2":
                    size = 100
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Ube')
                    sizelist.append('22oz')
                    sizeorder = False
                else:
                    print("Invalid number")
                    sizeorder = True
            nextorder = True
            while nextorder == True:
                nextorder = input("Purchase another milktea? y/n: ")
                if nextorder.lower() == 'y':
                    order = True
                elif nextorder.lower() == 'n':
                    order = False
                else:
                    print("Invalid keyword")
                    nextorder = True
        elif classicselect == "3":
            print("Your Flavor: Salted Caramel")
            quantity = int(input("Quantity: "))
            quantitytotal.append(quantity)
            sizeorder = True
            while sizeorder == True:
                print()
                size = str(input("Size     &     Price: \n1) -- 16 oz: 75php \n2) -- 22 oz: 85php \nEnter code:"))
                if size == "1":
                    size = 85
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Salted Caramel')
                    sizelist.append('16oz')
                    sizeorder = False
                elif size == "2":
                    size = 100
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Salted Caramel')
                    sizelist.append('22oz')
                    sizeorder = False
                else:
                    print("Invalid number")
                    sizeorder = True
            nextorder = True
            while nextorder == True:
                nextorder = input("Purchase another milktea? y/n: ")
                if nextorder.lower() == 'y':
                    order = True
                elif nextorder.lower() == 'n':
                    order = False
                else:
                    print("Invalid keyword")
                    nextorder = True
        else:
            print("Welcome back to Main Menu")
            order = True

    elif select == "3":
        print()
        print("***Fruit Blends Milktea***\n")
        print("Code        Name\n")
        for j in range(0, len(fruitblend)):
            print(f"{listorder[j]}{fruitblend[j]:>5s}")
        classicselect = str(input("Enter Code:"))
        if classicselect == "1":
            print("You Flavor: Green Apple")
            quantitytrue = True
            while quantitytrue == True:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("Invalid")
                    quantitytrue = True
                else:
                    quantitytotal.append(quantity)
                    quantitytrue = False
            sizeorder = True
            while sizeorder == True:
                print()
                size = str(input("Size     &     Price: \n1) -- 16 oz: 75php \n2) -- 22 oz: 85php \nEnter code:"))
                if size == "1":
                    size = 65
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Green Apple')
                    sizelist.append('16oz')
                    sizeorder = False
                elif size == "2":
                    size = 75
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Green Apple')
                    sizelist.append('22oz')
                    sizeorder = False
                else:
                    print("Invalid number")
                    sizeorder = True
            nextorder = True
            while nextorder == True:
                nextorder = input("Purchase another milktea? y/n: ")
                if nextorder.lower() == 'y':
                    order = True
                elif nextorder.lower() == 'n':
                    order = False
                else:
                    print("Invalid keyword")
                    nextorder = True
        elif classicselect == "2":
            print("You Flavor: Lemon")
            quantity = True
            while quantity == True:
                quantity = int(input("Quantity: "))
                if quantity > 0:
                    quantity = False
                else:
                    quantity = True
                    print("Invalid code")
            quantitytotal.append(quantity)
            sizeorder = True
            while sizeorder == True:
                print()
                size = str(input("Size     &     Price: \n1) -- 16 oz: 75php \n2) -- 22 oz: 85php \nEnter code:"))
                if size == "1":
                    size = 65
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Lemon')
                    sizelist.append('16oz')
                    sizeorder = False
                elif size == "2":
                    size = 75
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Lemon')
                    sizelist.append('22oz')
                    sizeorder = False
                else:
                    print("Invalid number")
                    sizeorder = True
            nextorder = True
            while nextorder == True:
                nextorder = input("Purchase another milktea? y/n: ")
                if nextorder.lower() == 'y':
                    order = True
                elif nextorder.lower() == 'n':
                    order = False
                else:
                    print("Invalid keyword")
                    nextorder = True

        elif classicselect == "3":
            print("Your Flavor: Strawberry")
            quantitytrue = True
            while quantitytrue == True:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("Invalid")
                    quantitytrue = True
                else:
                    quantitytotal.append(quantity)
                    quantitytrue = False
            sizeorder = True
            while sizeorder == True:
                print()
                size = str(input("Size     &     Prize: \n1) -- 16 oz: 75php \n2) -- 22 oz: 85php \nEnter code:"))
                if size == "1":
                    size = 65
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Strawberry')
                    sizelist.append('16oz')
                    sizeorder = False
                elif size == "2":
                    size = 75
                    classictotal = quantity * size
                    subtotal.append(classictotal)
                    orderlist.append('Strawberry')
                    sizelist.append('22oz')
                    sizeorder = False
                else:
                    print("Invalid number")
                    sizeorder = True
            nextorder = True
            while nextorder == True:
                nextorder = input("Purchase another milktea? y/n: ")
                if nextorder.lower() == 'y':
                    order = True
                elif nextorder.lower() == 'n':
                    order = False
                else:
                    print("Invalid keyword")
                    nextorder = True
        else:
            print("Welcome back to Main Menu")
            order = True
    else:
        print("Invalid keyword")
        order = True

moneycheck = True
while moneycheck == True:
    print(f"{item:<20}{qty:<20}{sizee:<18}{totall}")
    for j in range(0, len(orderlist)):
        print(f"{orderlist[j]:<20}{quantitytotal[j]:<20}{sizelist[j]:<18}{subtotal[j]}")
    print()
    print("The total amount is: ", sum(subtotal))
    money = float(input("Cash:"))
    if money < sum(subtotal):
        print("Insufficient Amount")
        moneycheck = True
    elif money >= sum(subtotal):
        print("_____________________________________")
        print("         I-Tea Milktea Shop         ")
        print("Max Y. Suniel St, Cagayan de Oro City")
        print("     ",today, "at", current_time,"    ")
        print("_____________________________________")
        print("Register: 1")
        print("Cashier:", log_in.capitalize())
        print("            *****Sale*****           ")
        print(f"{qty:<5}{item:<20}{sizee:<10}{totall}")
        for quantities, orders, ounce, eachtotal in zip(quantitytotal, orderlist, sizelist, subtotal):
            print(f"{quantities:<5}{orders:<20}{ounce:<10}{eachtotal}")
        print("_____________________________________")
        print("Total Amount           ",sum(subtotal))
        print("Cash:                  ",money)
        print("Change:                ",               money - sum(subtotal))
        print()
        print("_____________________________________")
        print("Thank you for purchasing in I-Tea! \n        Please come again!")
        break