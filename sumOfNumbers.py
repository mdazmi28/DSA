import math
def changeindex(data):
   #   if(len(str(data))==3):
   #      s = data % 10
   #      n = math.floor((data /10)) % 10
   #      d = math.floor(((data /10) / 10))% 10
   #      reverse = s +n+d
   #      return reverse
   #   return "Input must be not less or grater that 3 digit"
   sum = 0
   while data !=0:
      eq = data % 10
      sum = sum + eq
      data = data // 10
   return sum
      

y = int(input("Inpuy: "))

z = changeindex(y)

print("Total Sum is: "f"{z}")


