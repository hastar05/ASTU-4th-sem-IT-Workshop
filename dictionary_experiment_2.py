days = {'January' : 31, 'February' : 28, 'March' : 31, 'April' : 30,'May' : 31, 'June' : 30, 'July' : 31, 'August' : 31, 'September' : 30, 'October' : 31, 'November' : 30, 'December' : 31}
m = str(input("(a) Enter a month name: "))
if m in days:
    print("Number of days in", m, "is", days[m])
else:
    print("Invalid month name!")

print("\n(b) Keys in alphabetical order")
for key in sorted(days):
    print(key)

print("\n(c) All of the months with 31 days")
for key in days:
    if days[key] == 31:
        print(key)

print("\n(d) (key-value) pairs sorted by the number of days in each month")
d1 = dict(sorted(days.items(), key = lambda item: item[1]))
for key in d1:
    print((key, d1[key]))
