def  perform_operations(num1 = float(input()),
                          num2 = float(input()),
                          operation = input("+","-","*","/")):
    print("Arithmetic operation")
    num1 = float(input())
    num2 = float(input())
    if operation == "+":
        print(num1+num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1/num2)



perform_operations()

 









