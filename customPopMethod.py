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
    
    def pop(self):
        if self.length == 0:  # Check if the array is empty to avoid errors
            return None  # Or raise an error

        lastItem = self.data[self.length - 1]  # Get the last item
        del self.data[self.length - 1]         # Remove the last item using its index
        self.length -= 1                       # Decrease the length of the array
        # return lastItem                        # Return the popped item

    

newArray1 = MyArray()



print(newArray1.push("a"))
print(newArray1.push("b"))
print(newArray1.push("c"))
# print(newArray1.get(1))
print(newArray1.pop())

print(newArray1.data)
