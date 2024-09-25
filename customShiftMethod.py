class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.data
    
    def shift(self):
        firstIndex = self.data[0]
        for i in range(1, self.length):
            self.data[i-1] = self.data[i]
        del self.data[self.length -1]
        self.length-+1
        return self.data
    

newArray = MyArray()

print(newArray.push("a"))
print(newArray.push("b"))
print(newArray.push("c"))
print(newArray.shift())
print(newArray)