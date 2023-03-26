def birthday(s, d, m):

    way = []
    for j in range(0,len(s)+1):
        for i in range(j,len(s)+1):
            segment = s[j:i]
            print(segment)
            if d == sum(segment) and len(segment)==m:
                way.append(segment)

    return len(way)    


birthday([2,2,1,3,2,5],4,2)

