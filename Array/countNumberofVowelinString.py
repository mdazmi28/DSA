x = 'HUelloiii'

y = x.lower()

vowels = ['a','e','i','o','u']
count = 0
for i in range(len(y)):
    for j in range(len(vowels)):
        if y[i] == vowels[j]:
            count+=1
        else:
            pass
print(count)