def number_of_factors(num):
    count = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count += 1
    if num == 1:
        return count
    else:
        return count + 1

num = int(input("Number (>= 1): "))
print(f"Number of factors of {num} = {number_of_factors(num)}")
