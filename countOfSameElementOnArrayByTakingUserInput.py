a = ['z', 'b', 'h', 'e', 's', 'u', 'h', 'o', 'p', 'd', 'z','h','s','s', 'o']
# count = 0

x = input("Input: ")


# print(count)
def findChar(char):
    count = 0
    for i in a:
        if(i == char):
            count+=1
    return count;

z = findChar(x);

print(f"{x} is "f"{z} times")
       




