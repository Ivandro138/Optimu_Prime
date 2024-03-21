print('wellcome to Dark Nuggets store')
def can_buy_nuggets(num):
    if num < 6:
        return False

    for x in range(num // 6 + 1):
        for y in range(num // 9 + 1):
            for z in range(num // 20 + 1):
                if (6 * x) + (9 * y) + (20 * z) == num:
                    return True

    return False
num = int(input("Enter the number of Nuggets to buy: "))

can_buy_it = can_buy_nuggets(num)

print(can_buy_it)
