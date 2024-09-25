import math
def changeindex(data):
     if(len(str(data))==3):
        s = data % 10
        n = math.floor((data /10)) % 10
        d = math.floor(((data /10) / 10))% 10
        reverse = s +n+d
        return reverse
     return "Input must be not less or grater that 3 digit"

y = int(input())

z = changeindex(y)

print(z)


