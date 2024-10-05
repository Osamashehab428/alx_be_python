FAHRENHEIT_TO_CELSIUS_FACTOR =  5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
 
def convert_Temp():
    print("Enter the temperature to convert: ")
    Temp = float(input())
    print("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    TypeOfTemp = input()
    match TypeOfTemp:
        case 'F':
            print(FAHRENHEIT_TO_CELSIUS_FACTOR * Temp -32)
        case 'C':
            print((CELSIUS_TO_FAHRENHEIT_FACTOR * Temp)- 32)

convert_Temp()

 
