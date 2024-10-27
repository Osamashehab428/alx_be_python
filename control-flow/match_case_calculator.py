num1 = float(input(f"Enter the first number: "))
num2 = float(input(f"Enter the second number: "))

operation = input(f"Choose the operation (+, -, *, /): ")

match operation:
    case "+": print(f"result = {num1 + num2}")
    case "-": print(f"result = {num1 - num2}")
    case "*": print(f"result = {num1 * num2}")
    case "/": print(f"result = {num1 / num2}")







