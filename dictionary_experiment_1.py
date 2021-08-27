ans = 'y'
d = {}
while ans == 'y' or ans == 'Y':
    p_name = str(input("Product name: "))
    price = float(input("Price: "))
    d[p_name] = price
    ans = str(input("\nDo you want to enter more products? (y / n): "))
    print()

ans = 'y'
while ans == 'y' or ans == 'Y':
    s = str(input("Enter the name of the required product: "))
    if s in d:
        print("Price of", s, ":", d[s])

    else:
        print("Product information not available!")

    ans = str(input("\nDo you want to view more products? (y / n): "))
    print()
                  
                 
