# Given an array of integers, calculate the ratios of its elements that are positive, 
# negative, and zero. Print the decimal value of each fraction on a new line with 6
# places after the decimal.


def plusMinus(arr):

    zeros = len([num for num in arr if num==0])
    pos = len([num for num in arr if num>0])
    neg = len([num for num in arr if num<0])
    arr_len = len(arr)
    
    results = []
    results.append(round(pos/arr_len,6))  
    results.append(round(neg/arr_len,6))
    results.append(round(zeros/arr_len,6))
    
    for result in results:
        print(result)

if __name__ == '__main__':
    n = int(input("array length: ").strip())

    arr = list(map(int, input("array elements, separated by blank space: ").rstrip().split()))

    plusMinus(arr)
