lst = [1,3,5,1,2,7]

for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1],lst[j]
print(lst)