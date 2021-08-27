s = str(input("Enter a string: "))
print("(a) The total number of characters in the string =", len(s))
print("(b) The string repeated 10 times:")
for i in range(10):
    print(s)
print("(c) The first character of the string:", s[0])
print("(d) The first three characters of the string:", s[:3])
print("(e) The last three characters of the string:", s[-3:]) 
print("(f) The string backwards:", s[::-1])
if len(s) < 7:
    print("\'",s, "\' has fewer than 7 characters.")
else:
    print("(g) The seventh character of the string:", s[6])
print("(h) The string with its first and last characters removed:", s[1:-1])
print("(i) The string in all caps:", s.upper())

print("(j) The string with every a replaced with an e:", end = '')
for c in s:
    if c == 'a':
        print("e", end = '')
    else:
        print(c, end = '')
        
print("\n(k) The string with every letter replaced by a space:")
for c in s:
    if c.isalpha():
        print(" ", end = '')
    else:
        print(c, end = '')
