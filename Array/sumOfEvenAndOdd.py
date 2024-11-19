a = [1,2,3,4,5,6,7,8,9]

def sumOfOddEven(arr):
    sumOfEven = 0
    sumOfOdd = 0
    for i in range(len(arr)):
        if arr[i] %2 == 0:
            sumOfEven = sumOfEven + arr[i]
        else:
            sumOfOdd =  sumOfOdd + arr[i]
    

    print(sumOfEven)
    print(sumOfOdd)

sumOfOddEven(a)

