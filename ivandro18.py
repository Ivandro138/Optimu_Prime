def is_triangular_number(number):
    n = 1
    product = 1
    while product < number:
        product *= n
        n += 1
    return product == number

n = int(input("Enter a number: "))
if is_triangular_number(n):
    print(n, "is a triangular number.")
else:
    print(n, "is not a triangular number try again.")
