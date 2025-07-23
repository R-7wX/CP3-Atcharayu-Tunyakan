def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vatRate = 7/100
    result = totalPrice + (totalPrice * vatRate)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)


if login():
    showMenu()
    if menuSelect() == 1:
        totalPrice = int(input("Enter Total Price : "))
        print(vatCalculator(totalPrice))
    elif menuSelect() == 2:
        print(priceCalculator())