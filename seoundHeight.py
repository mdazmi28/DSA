a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

def secoundHeight(num):
    print(f"{num} is the secound heighest")

if(c > a and c > b and c<d):
    secoundHeight(c)
elif(c > b and c > d and c < a):
    secoundHeight(c)
elif(c > d and c > b and c < a):
    secoundHeight(c)
elif(a > c and a > b and a<d):
    secoundHeight(a)
elif(a > b and a > d and a < c):
    secoundHeight(a)
elif(a > d and a > b and a < c):
    secoundHeight(a)
#######################################
elif(b > c and b > a and b<d):
    secoundHeight(b)
elif(b > a and b > d and b < c):
    secoundHeight(b)
elif(b > d and b > a and b < c):
    secoundHeight(b)
else:
    secoundHeight(d)