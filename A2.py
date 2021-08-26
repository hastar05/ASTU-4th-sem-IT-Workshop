sum_ = 0

for i  in range(1, 2001):
    if i % 2 != 0:
        sum_ += i
    else:
        sum_ -= i

print("1 − 2 + 3 − 4 + · · · + 1999 − 2000 =", end = ' ')
print(sum_)
