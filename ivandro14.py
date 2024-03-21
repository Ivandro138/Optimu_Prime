def convert_to_roman(number):
    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                      90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    
    return ''.join([roman_numerals[value] * (number // value) for value in roman_numerals])

number = int(input("Enter a positive value: "))
roman_number = convert_to_roman(number)
print("the roman conversion is: {}".format(roman_number))
