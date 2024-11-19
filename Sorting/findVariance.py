import math
lst = [1,2,2,3,4,5]
lenOfLst = len(lst)
result = 0
# To calcualte MEAN
for i in range(len(lst)):
    result = (result + lst[i])
    a = result / lenOfLst
# print(result)
print("Mean is: " f"{a:.2f}")

# to calculate variance for popolation
population_variance_sum = 0
for i in range(len(lst)):
    population_variance_sum += (math.pow((lst[i]-a),2))/lenOfLst
print("Variance of population is: " f"{population_variance_sum:.2f}")
population_standard_diviation = math.sqrt(population_variance_sum)
print("Standard Division of population: " f"{population_standard_diviation}")

# to calculate variance for sample
sample_variance_sum = 0
for i in range(len(lst)):
    sample_variance_sum += (math.pow((lst[i]-a),2))/(lenOfLst - 1)
print("Variance of sample is: " f"{sample_variance_sum:.2f}")
sample_standard_diviation = math.sqrt(sample_variance_sum)
print("Standard Division of sample: " f"{sample_standard_diviation}")