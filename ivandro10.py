def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius
def inches_to_mm(inches):
    mm = inches * 25.4
    return mm
def mm_to_inches(mm):
    inches = mm / 25.4
    return inches
def main():
    option = int(input("Choose the conversion:\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n3 - Inches to Millimeters\n4 - Millimeters to Inches\n"))

    if option == 1:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("The temperature in Fahrenheit is:", fahrenheit)
    elif option == 2:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("The temperature in Celsius is:", celsius)
    elif option == 3:
        inches = float(input("Enter the measurement in inches: "))
        mm = inches_to_mm(inches)
        print("The measurement in millimeters is:", mm)
    elif option == 4:
        mm = float(input("Enter the measurement in millimeters: "))
        inches = mm_to_inches(mm)
        print("The measurement in inches is:", inches)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
#really teacher 
# this is too much
# joke but i like it   