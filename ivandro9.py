A = float(input("Input the value of the major base (A): "))
B = float(input("Input the value of the minorbase (B): "))
C = float(input("Input the weight of c (C): "))

if A > 0 and B > 0 and C > 0:
    area = (A + B) * C / 2
    print("the area is:", area)
else:
    print("try to input the values again bro")