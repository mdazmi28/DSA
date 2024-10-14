lst=[1,2,3,4,5,6,7]
positon=1
# # lst=[1,2,4,5,6,7]
# print(lst)
for i in range(positon-1,len(lst)-1):
    # print(i)
        lst[i] = lst[i+1]

del lst[len(lst)-1]
# print(x)

print(lst)