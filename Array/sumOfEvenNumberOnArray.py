number = [1,1,2,3]
sumOfEven = 0
sumOfOdd = 0
for i in range(len(number)):
    if number[i] %2 == 0:
        # print(number[i]) 
        sumOfEven = sumOfEven + number[i]

    if number[i] % 2 != 0:
        sumOfOdd = sumOfOdd + number[i]

x = sumOfEven - sumOfOdd

print("Differenct between even and odd is "f"{x}")