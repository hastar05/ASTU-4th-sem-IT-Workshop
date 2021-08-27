import random
l = [random.randint(1, 100) for i in range(20)]
print("(a) Created list:", l)
print("(b) Average of the elements in list:", sum(l) / len(l))
print("(c) Largest element in list:", max(l), "\n    Smallest element in list:", min(l))
l1 = l[::]
l1.remove(max(l))
l1.remove(min(l))
print("(d) Second largest element in list:", max(l1), "\n    Second smallest element in list:", min(l1))
count = 0
for i in l:
    if i % 2 == 0:
        count += 1

print("(e) Number of even numbers in the list:", count)
