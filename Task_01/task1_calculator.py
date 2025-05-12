#Select the operator
print("Select an operation to perform: ")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
#choose the operation you need tyo perform
operation=input("Enter the operation: ")
#addition
if operation== "1":
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    print(f"The sum of {num1} + {num2} is {num1+num2}")
#subtraction
elif operation=="2":
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    print(f"The difference of {num1} - {num2} is {num1-num2}")
#multiplication
elif operation=="3":
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    print(f"The product of {num1} * {num2} is {num1*num2}")
#division
elif operation=="4":
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    print(f"The result of {num1} / {num2} is {num1/num2}")
#error message
else:
    print("Inavild Entry")
