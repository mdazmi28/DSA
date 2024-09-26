x = int(input("Input: "))


def starPrint(x):
    for i in range(x):
        print("*",end="")
        for j in  range(i):
            print("*",end="")
        print("")
    for i in range(x,-1,-1):
        print("*",end="")
        for j in  range(i):
            print("*",end="")
        print("")
starPrint(x)