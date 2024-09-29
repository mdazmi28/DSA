x = int(input("Enter a Number: "))

def sumOfOdd(n):
    sum = 0
    while n!= 0:
        x = (n % 10)
        if x % 2 != 0:
            sum = sum + x
            # print(x)
        n = n//10
    print(sum)

sumOfOdd(x)