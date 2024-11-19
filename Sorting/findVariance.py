import math
lst = [1,2,2,3,4,5]
lenOfLst = len(lst)
result = 0
for i in range(len(lst)):
    result = (result + lst[i])
    a = result / lenOfLst
# print(result)
print("Mean is: " f"{a:.2f}")

# to calculate variance
for i in range(len(lst)):
    variance = math.pow((lst[i]-a),2)/lenOfLst
print("Variance is: " f"{variance}")