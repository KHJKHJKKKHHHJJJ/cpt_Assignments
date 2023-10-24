pricelist = []
while len(pricelist)<5:
    try:
        a = int(input(f"Enter a price of the menu No.{len(pricelist) + 1}: "))
        if a < 100 or a > 2000:
            raise ValueError
    except:
        print("Enter the right values.")
        continue
    pricelist.append(a)

print(min([pricelist[i] + pricelist[j] - 50 for i in range(3) for j in range(2,5)]))
