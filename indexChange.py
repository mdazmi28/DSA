# input:  3 2 1 0
# output : 2 1 0 3

a = input("a: ")
b = input("b: ")
c = input("c: ")
d = input("d: ")

x = a;
a = b
b = c
c  = x

print("a: "f"{a}, ""b: "f"{b}, ""c: "f"{c}, ""d: "f"{d}")
