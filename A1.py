l = []
for i in range(1, 10000):
    sum_ = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            sum_ += j

    if sum_ == i:
        l.append(i)

print("List of all perfect numbers from 1 to 10,000:")
print(l)
