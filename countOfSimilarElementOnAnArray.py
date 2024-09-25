a = ['a','b','c','d','a']


# x = input("Input: ")


# print(count)
def findChar():
    count = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if(a[i] == a[j]):
                count+=1
                # print(f"{a[i]}---"f"{a[j]}")
    
    print(f"{a[i]} is "f"{count} times")


findChar()
        


       




