supporters = [0, 0, 0, 0, 0]  # Number of supporters for each club
salaries = [0, 0, 0, 0, 0]  # Total salary for each club
maputo_birth_no_support = 0
total_people = 0

# Conduct the survey
while True:
    choice = int(input("Enter the preferred football club (1-5), or 0 to exit: "))
    if choice == 0:
        break

    salary = float(input("Enter the salary: "))
    birth_city = int(input("Enter the city of birth (1-2): "))

    # Update the data based on the survey responses
    supporters[choice - 1] += 1
    salaries[choice - 1] += salary
    total_people += 1

    if birth_city == 1 and choice > 5:
        maputo_birth_no_support += 1

# Calculate the average salary for each club
avg_salaries = [salaries[i] / supporters[i] if supporters[i] > 0 else 0 for i in range(len(supporters))]

# Print the results
print("Number of supporters per club:")
for i in range(len(supporters)):
    print(f"Club {i+1}: {supporters[i]}")

print("\nAverage salary of supporters for each club:")
for i in range(len(avg_salaries)):
    print(f"Club {i+1}: {avg_salaries[i]:.2f}")

print("\nNumber of people born in Maputo who do not support any of the main Maputo clubs:", maputo_birth_no_support)
print("Number of people interviewed:", total_people)
