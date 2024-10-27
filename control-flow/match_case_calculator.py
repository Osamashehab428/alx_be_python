num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+": print("result = {num1 + num2}")
    case "-": print("result = {num1 - num2}")
    case "*": print("result = {num1 * num2}")
    case "/": print("result = {num1 / num2}")







