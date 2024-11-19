# import numpy as np
lst = [1,4,1,7,8,9,3,6]

#sort first
sort = []
for i in range(len(lst)):
    for j in range(len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
sort= lst
print(sort)

if len(sort) % 2 == 0:
    middleIndex = len(sort)//2
    x = sort[middleIndex-1]
    y = sort[middleIndex]
    # print(x)
    # print(y)
    median = (x+y)//2
    print(median)
else:
    middleIndex = len(sort)//2
    print(sort[middleIndex])