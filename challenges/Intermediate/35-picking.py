# Given an array of integers, find the longest subarray where the absolute 
# difference between any two elements is less than or equal to 1.
# return int: the length of the longest subarray that meets the criterion
# example
# a = [1,1,2,2,4,4,5,5,5]
# sub1 = [1,1,2,2]
# sub2 = [4,4,5,5,5]

def pickingNumbers(a):
    a.sort()
    arrSub, sub = [], []
    for num in a:
        if sub == []:
            sub.append(num)
        elif max([abs(num-min(sub)) for eval in sub]) <= 1:
            sub.append(num)
        else:
            arrSub.append(sub)
            sub = []
            sub.append(num) 
    arrSub.append(sub)  
        
    return max([len(sub) for sub in arrSub])    

if __name__ == "__main__":

    a = [4,6,5,3,3,1]
    print(pickingNumbers(a))