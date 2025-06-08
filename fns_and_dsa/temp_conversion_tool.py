FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    C =  (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    print(f"{fahrenheit}°F is {C}°C")

def convert_to_fahrenheit(celsius):
    F = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    print(f"{celsius}°C is {F}°F")
    
def main():
    temp = float(input("Enter the temperature to convert: "))
    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    
    if scale.upper() == "F":
        convert_to_celsius(temp)
    elif scale.upper() == "C":
        convert_to_fahrenheit(temp)
    
if __name__ == "__main__":
    main()