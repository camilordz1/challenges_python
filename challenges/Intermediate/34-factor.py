def getTotalX(a,b):
    
    factor = []

    mxB= max(b)
    for numB in b:
        for num in range(1,mxB+1):
            if numB%num == 0:
                factor.append(num)

    bFactor = set([num for num in factor if factor.count(num)==len(b)])

    factor = []
    for numBF in bFactor:
        for numA in a:
            if numBF%numA==0:
                factor.append(numBF)

    tFactor = set([num for num in factor if factor.count(num)==len(a)])
    return len(tFactor)


a=[2,4]
b=[16,32,96,100]
print(getTotalX(a,b) )             