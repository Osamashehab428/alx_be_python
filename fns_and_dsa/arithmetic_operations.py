 
def perform_operation():
    print("Enter the first number")
    num1 = float(input())
    print("Enter the second number")
    num2 = float(input())
    print("Enter the operation (add, subtract, multiply, divide):")
    operation = input()
    if(operation == '+'):
        print("Result: ",num1+num2)
    elif(operation == '-'):
        print("Result: ",num1-num2)
    elif(operation == '*'):
        print("Result: ",num1*num2)
    elif(operation == '/' and num1 !=0 and num2 !=0):            
        print("Result: ",num1/num2)
    elif(operation == '/'and num2 ==0):
        print("Please enter a valid number \"the second value shouldn't equal zero\"")


perform_operation()

