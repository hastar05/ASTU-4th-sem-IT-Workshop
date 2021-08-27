s = str(input("Enter a string with the letter 'a': "))
i = 0
for c in s:
    print(c, end = '')
    i += 1
    if(c == 'a'):
        print()
        break;
for j in range(i, len(s)):
    print(s[j], end = '')               
