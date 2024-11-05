FAHRENHEIT_TO_CELSIUS_FACTOR =  5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = float(input("Enter the temperature to convert: "))

def convert_to_celsius(fahrenheit):
    
    celcius = float(input(FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit - 32)))
    print(celcius)

def convert_to_fahreheit(celsius):
    celsius = 0 
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR*celsius) + 32
    print(fahrenheit)
 
type_of_temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if  type_of_temp == "C":
    convert_to_fahreheit(0)
elif type_of_temp == "F": convert_to_celsius(0)
else: print("Invalid temperature")


