def fill_vector():
    vector = []
    while True:
        value = int(input("Enter a value (negative to stop): "))
        if value < 0:
            break
        vector.append(value)
    return vector

vector = fill_vector()
print("Vector:", vector)
count_greater_than_5 = sum(1 for value in vector if value > 5)
print("Count of values greater than 5:", count_greater_than_5)

sum_even_values = sum(value for value in vector if value % 2 == 0)
print("Sum of even values:", sum_even_values)

sum_odd_values = sum(value for value in vector if value % 2 != 0)
print("Sum of odd values:", sum_odd_values)

count_total_values = len(vector)
print("Total count of values:", count_total_values)
#this is the last exercise Mr Metano