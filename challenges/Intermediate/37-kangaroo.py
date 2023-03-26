
def kangaroo(x1, v1, x2, v2):
    d = x2-x1
    while True:
        x1 += v1
        x2 += v2
        print((x2-x1)/d)
        if x1==x2:
            return "YES"
        if x1>x2 or (x2-x1)/d>=1:
            return "NO"



print(kangaroo(43, 2, 70, 2))
