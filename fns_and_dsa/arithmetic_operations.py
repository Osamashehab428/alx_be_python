def perform_operation(num1,num2,operation):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")

    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1*num2)
    elif operation == "/":
        print(num1/num2)
    else: print("Invalid")
        

perform_operation()