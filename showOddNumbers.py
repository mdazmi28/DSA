x = int(input("Enter a Number: "))

def findOdd(n):
    sum = 0
    sum1 = 0
    while n!= 0:
        x = n % 10
        if x % 2 != 0:
           sum = sum * 10 + x
        n = n // 10
    # print(sum)
    while (sum != 0):
        z = sum % 10
        sum1 = sum1 * 10 + z
        sum = sum // 10
    print(sum1)


findOdd(x)