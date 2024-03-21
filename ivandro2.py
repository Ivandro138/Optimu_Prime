def adiction_inverse(a, b, c):
    inverse_a = 1 / a
    inverse_b = 1 / b
    inverse_c = 1 / c
    adiction = inverse_a + inverse_b + inverse_c
    return adiction
value1 = float(input('input one value: ' ))
value2 = float(input('tnput a number: '))
value3 = float(input('input the other number: '))
result = adiction_inverse(value1, value2, value3)
print("the sum of inverses is : ", result)

