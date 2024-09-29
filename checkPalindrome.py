# import math
# def checkP(x):
#     # print(type(x))
#     s = math.floor(x % 10)
#     # print(s)
#     n = math.floor((x/10)%10)
#     d = math.floor((((x/10)/10))%10)
#     # print(d)

#     if s == d:
#         return True


# m = checkP(121)

# if m == True:
#     print("Yes")
# else:
#     print("no")


def checkPalindrome(num):
    inputNum = num

    sum = 0
    while num != 0:
        x = (num % 10) 
        sum = sum * 10 + x
        num =num//10
    # print(sum)
    # print(type(sum))

    if sum == inputNum:
        return True
    else:
        return False
        

x = checkPalindrome(127484)
if x == True:
    print("Yes")
else:
    print("No")