word1 = "abcd"
word2 = "pqr"

def margeWord(word1, word2):
    result = ""
    for i in range(len(word1)):
        # print(word1[i])
        result = result + word1[i]
        for j in range(i, len(word2)):
            result= result + word2[j]
            break
    print(result)
            
        


margeWord(word1, word2)