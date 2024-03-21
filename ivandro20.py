x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

quotient = 0
while x >= y:
    x -= y
    quotient += 1
remainder = x
print("quotient is:", quotient)
print("remainderis :", remainder)
