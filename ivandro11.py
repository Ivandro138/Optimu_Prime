def main():
    total_amount = 0
    average_purchase = 0
    above_100_count = 0
    below_50_count = 0

    for i in range(3):
        registration_number = int(input("Enter the registration number of customer {}: ".format(i+1)))
        purchase_amount = float(input("Enter the purchase amount (in MZN) of customer {}: ".format(i+1)))

        total_amount += purchase_amount
        average_purchase += purchase_amount

        if purchase_amount > 100:
            above_100_count += 1

        if purchase_amount < 50:
            below_50_count += 1

    average_purchase /= 3

    print("\nTotal amount paid by the three customers: {:.2f} MZN".format(total_amount))
    print("Average purchase value: {:.2f} MZN".format(average_purchase))
    print("Number of customers with purchases above 100 MZN: {}".format(above_100_count))
    print("Number of customers with purchases below 50 MZN: {}".format(below_50_count))

if __name__ == "__main__":
    main()