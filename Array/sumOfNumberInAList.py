a = [1,2,3,4,5,6,7,8,9]

def sumOfAList(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    print(sum)

sumOfAList(a)
