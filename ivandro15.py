x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

if x > 0 and y > 0:
    quadrant = 1
elif x < 0 and y > 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
elif x > 0 and y < 0:
    quadrant = 4
elif x == 0 or y == 0:
    quadrant = -1
else:
    quadrant = 0
print("Coordinates is: ({}, {})".format(x, y))
print("Quadrant is: {}".format(quadrant))
