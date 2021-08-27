s = str(input("Enter list of integers separated by space:"))
l = [int(x) for x in s.split()]
print(l,"\n")
print("(a) Number of items in the list:", len(l))
print("(b) Last item in the list:", l[-1])
print("(c) List in reverse order:", l[::-1])
print("(d) List contains a 5?:", end = ' ')
if 5 in l:
    print("Yes")
else:
    print("No")
print("(e) The number of fives in the list:", l.count(5))
print("(f) Remove the first and last items from the list, sort the remaining items:", sorted(l[1:-1]))
count = 0
for i in l:
    if i < 5:
        count += 1
print("(g) Number of integers in the list less than 5:", count)
