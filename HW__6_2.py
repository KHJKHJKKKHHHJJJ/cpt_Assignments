numList = []
while len(numList) < 10:
    try:
        a = int(input("Enter a number: "))
        if a > 1000 or a < 0:
            raise ValueError
    except:
        print("Enter a Number")
    numList.append(a)

print(len(set([i%42 for i in numList])))
