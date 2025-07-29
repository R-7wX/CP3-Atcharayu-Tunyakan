menuList = []
priceList = []
totalPrice = 0
while True:
    menuInput = input("menu: ")
    if menuInput.lower() == "exit":
        break
    else:
        priceInput = input("price: ")
        menuList.append(menuInput)
        priceList.append(priceInput)
        totalPrice+=int(priceInput)
def showBill():
    print('-----Bill-----')
    for number in range(len(menuList)):
        print(menuList[number],"->",priceList[number])
    print("---------------")
    print("Total:",totalPrice,"THB")

showBill()
