def calculate_final_salary(fixed_salary, sales):
    if sales > 7500:
        bonus = 1000.00
    elif sales > 5000:
        bonus = 700.00
    elif sales > 1000:
        bonus = 500.00
    else:
        bonus = 0.00
    final_salary = fixed_salary + bonus
    return final_salary, bonus
def main():
    fixed_salary = float(input("Enter the salesperson's fixed salary: "))
    sales = float(input("Enter the total sales value for the month: "))

    final_salary, bonus = calculate_final_salary(fixed_salary, sales)

    print("\nFinal Salary: mzn {:.2f}".format(final_salary))
    print("Received Bonus: mzn {:.2f}".format(bonus))
if __name__ == "__main__":
    main()
print('finished')