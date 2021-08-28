def merge(l1, l2):
    print("(a) Merging and Sorting using sort() method")
    res = l1 + l2
    res.sort()
    print(res)

    print("\n(b) Merging and Sorting without sort() method")
    size_1 = len(l1)
    size_2 = len(l2)
      
    res = []
    i, j = 0, 0
      
    while i < size_1 and j < size_2:
        if l1[i] < l2[j]:
          res.append(l1[i])
          i += 1
      
        else:
          res.append(l2[j])
          j += 1
      
    res = res + l1[i:] + l2[j:]
    print(res)
    

print("List 1 = [1, 3, 5, 7, 9]\nList 2 = [4, 6, 7, 10, 12]\n")
merge([1, 3, 5, 7, 9], [4, 6, 7, 10, 12])
