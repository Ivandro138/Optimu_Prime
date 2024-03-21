from datetime import date

while True:
    year1 = int(input("Enter the year of the first date (or 0 to quit): "))
    if year1 == 0:
        break
    month1 = int(input("Enter the month of the first date: "))
    day1 = int(input("Enter the day of the first date: "))

    year2 = int(input("Enter the year of the second date: "))
    month2 = int(input("Enter the month of the second date: "))
    day2 = int(input("Enter the day of the second date: "))

    date1 = date(year1, month1, day1)
    date2 = date(year2, month2, day2)

    days = (date2 - date1).days
    print("Number of days between the two dates:", days)