'''print('wllcome')
def is_perfect_number(number):
    divisor_sum = sum([divisor for divisor in range(1, number) if number % divisor == 0])
    return divisor_sum == number

def print_all_perfect_numbers(n):
    count = 0
    number = 1

    while count < n:
        if is_perfect_number(number):
            print(number)
            count += 1
        number += 1

n = int(input("Enter the value of n: "))
print("First", n, "perfect numbers:")
print_perfect_numbers(n)'''
def is_perfect_number(number):
    return sum([divisor for divisor in range(1, number) if number % divisor == 0]) == number

n = int(input("Enter the value of n: "))
perfect_numbers = [number for number in range(1, n*1000) if is_perfect_number(number)][:n]
print("First", n, "perfect numbers:")
print(perfect_numbers)

