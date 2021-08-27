l = []
for i in range(11):
    l.append(10**i)
l.append(1)

l = list(map(str, l))

s = ''.join(l)
l = list(s)
print(l)
