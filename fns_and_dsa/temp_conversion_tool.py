FAHRENHEIT_TO_CELSIUS_FACTOR =  5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius():
    fahrenheit = float(input("Enter the temperature to convert: "))
    celcius = float(input(FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit - 32)))
    print(celcius)

def convert_to_fahreheit():
    celsius = float(input("Enter the temperature to convert: "))
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR*celsius) + 32
    print(fahrenheit)
 
temp = float(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))

match temp:
    case "C": convert_to_fahreheit()
    case "F": convert_to_celsius()
 
