num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+": print(f"result = {num1 + num2}")
    case "-": print(f"result = {num1 - num2}")
    case "*": print(f"result = {num1 * num2}")
    case "/": print(f"result = {num1 / num2}")






