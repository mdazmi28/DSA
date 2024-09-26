y = input("Input: ")

def findSecoundLargest(input):
    for i in range(len(input)):
        if(input[i] > input[i+1]):
            z = input[i]
    return z


r = findSecoundLargest(y)
print(r)
