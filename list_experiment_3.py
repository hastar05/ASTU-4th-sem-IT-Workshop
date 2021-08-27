l = [8, 9, 10]
print("Original list:", l)
l[1] = 17
l = l + [4, 5, 6]
l.pop(0)
l.sort()
l = l + l
l.insert(3, 25)
print("Final list:", l)
