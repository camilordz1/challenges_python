from itertools import permutations

def twoArrays(k, A, B):
    permuteA = tuple(permutations(A))

    for ap in permuteA:
        if compare(k,ap,tuple(B)):
            return "YES"
            
    return "NO"        

def compare(k,A,B):
    
    sumAB = [1 for i in range(len(A)) if A[i] + B[i] >= k]

    if len(A) == len(sumAB):
        print(A,B,sumAB)
        return True
    return False


A=[3, 6, 8, 5, 9, 9, 4, 8, 4, 7]
B=[5, 1, 0, 1, 6, 4, 1, 7, 4, 3]
k=9
print(twoArrays(k,A,B))

A=[2, 3, 1, 1, 1]
B=[1, 3, 4, 3, 3]
k=5

print(twoArrays(k,A,B))
    
