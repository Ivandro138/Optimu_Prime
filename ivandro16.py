print('input the value in the following spaces')
operand1 = float(input("Enter the first operand: "))
operand2 = float(input("Enter the second operand: "))
operator = input("Enter the operator (+, -, *, /): ")

result = {
    '+': operand1 + operand2,
    '-': operand1 - operand2,
    '*': operand1 * operand2,
    '/': operand1 / operand2 if operand2 != 0 else "Error: Division by zero"
}.get(operator, "Error: Invalid operator")

print("Result:", result)
print('welldone')
