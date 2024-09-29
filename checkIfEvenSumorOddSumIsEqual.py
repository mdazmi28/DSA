x = int(input("Input: "))

def checkSum(n):
    sumOfOdd = 0
    sumOfEven = 0

    while(n != 0):
        x = n % 10
        if x % 2 == 0:
            sumOfEven = sumOfEven + x
        else:
            sumOfOdd = sumOfOdd + x
        n = n//10

    if (sumOfEven == sumOfOdd):
        print("The number of Two portion is equal")
    else:
        print("No More For Today")

checkSum(x)