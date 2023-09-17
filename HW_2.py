result = 0

def sum_func(d,e,result):
    result += e[d]
    if d == 0:
        print(result)
        return result
    sum_func(d-1,e,result)

while True:
    b = []
    a = input("Enter integers separated by spaces ==> ")

    if a == 'done':
        print('program terminated. good bye !!')
        break
    else:
        a = a.split(' ')

    try:
        for i in a:
            b.append(int(i))
    except ValueError:
        print('must enter integers separated by spaces')
        continue

    if len(b) == 1:
        print("must enter more than one integer")
        continue

    sum_func(len(b)-1, b, result)
    break