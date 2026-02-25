num1=float(input("Enter FRI num :  "))
num2=float(input("Enter SEC num :  "))
print("sum",num1+num2)
print("multiplication", num1*num2)
if num2!=0:
    print("Division:", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Remainder:", num1 % num2)
else:
    print(ZeroDivisionError)
