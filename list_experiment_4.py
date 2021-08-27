s = str(input("Enter list of integers between 1 and 12 (separated by single space):\n"))
l = [int(x) for x in s.split()]
print("Original list:", l)
for index, ele in enumerate(l):
    if ele > 10:
        l[index] = 10

print("Modified list:", l)
