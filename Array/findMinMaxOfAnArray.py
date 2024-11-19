a = [1,0,2,590,7,0,90]

def findMax(arr):
    maxNumber  = arr[0]
    for i in arr:
        if i > maxNumber:
            maxNumber = i
    print(maxNumber)
findMax(a)