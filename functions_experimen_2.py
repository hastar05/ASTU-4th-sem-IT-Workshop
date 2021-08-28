def first_diff(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return i

    return -1

str1 = str(input("String 1: "))
str2 = str(input("String 2: "))
print("First index where the strings differ:", first_diff(str1, str2))
