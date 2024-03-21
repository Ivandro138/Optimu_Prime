def calculate_pi(error):
    pi = 0
    numerator = 1
    denominator = 1

    while True:
        value = numerator / denominator
        pi += value

        if abs(value) < error:
            break
        numerator *= -1
        denominator += 2

    return pi * 4
acceptable_error = float(input("Enter the acceptable error: "))

pi_value = calculate_pi(acceptable_error)

print("The calculated value of Pi: {:.2f}".format(pi_value))
