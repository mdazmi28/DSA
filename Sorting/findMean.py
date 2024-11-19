lst = [1,4,1,7,8,9,3,6,1,1]
print(len(lst))
result = 0
for i in range(len(lst)):
    result = (result + lst[i])
    a = result / len(lst)
print(result)
print(f"{a:.2f}")
