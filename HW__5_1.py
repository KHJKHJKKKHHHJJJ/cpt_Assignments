def solution(pri, loc):
    ilist = list(range(len(pri)))
    locVal = pri[loc]
    ordnum = 1
    nlist = list(zip(ilist, pri))

    while True:
        if nlist[0][1] == max(dict(nlist).values()):
            if nlist[0][1] == locVal:
                if nlist[0][0] == loc:
                    break
                else: 
                    nlist.pop(0)
                    ordnum += 1
            else:
                nlist.pop(0)
                ordnum += 1
        else:
            nlist.append(nlist[0])
            nlist.pop(0)
    return ordnum

if __name__ == '__main__':
    b  = [2,1,3,2]
    print(solution(b, 2))

    c = [1,1,9,2,3,4]
    print(solution(c,1))

    d = [1,1,2,1,1,1]
    print(solution(d,0))
