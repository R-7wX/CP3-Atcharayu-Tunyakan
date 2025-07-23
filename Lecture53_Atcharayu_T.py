def VatCal(Sum):
    result = Sum+(Sum*7/100)
    return result
Sum = int(input("Enter Your Product Price: "))
print(VatCal(Sum))