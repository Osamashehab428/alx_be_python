FAHRENHEIT_TO_CELSIUS_FACTOR =  5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
 
def convert_to_celsius(fahrenheit):
    celcius = FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit - 32)
    print(celcius)


convert_to_celsius(100)


 
