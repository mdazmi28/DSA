class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def push(self, item):
        self.data[self.length] = item
        self.length+=1
        return self.data
    
    def get(self, i):
        return self.data[i]
    

newArray1 = MyArray()



print(newArray1.push("a"))
print(newArray1.push("b"))
print(newArray1.push("c"))
print(newArray1.get(1))
