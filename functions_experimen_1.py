def sum_digits(num):
    sum = 0
    while num >= 1:
        r = num % 10
        sum += r
        num = num // 10

    return sum

num = int(input("Number: "))
print("Sum of digits =", sum_digits(num))
