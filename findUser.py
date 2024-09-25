array = ['a','b','c','d']

def findUser(arr, word):
    for x in arr:
        if(x == word):
            return f"{word} " "Found"
            
    return f"{word}" "Not Found"


print(findUser(array, "a"))