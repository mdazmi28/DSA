# Overall Time Complexity:
# O(n2)+O(n)=O(n2)
# O(n2)+O(n)=O(n2)

# Thus, the overall time complexity of the ONpow2 function is O(n²) due to the nested loop structure in the first part.

a = [1,2,3,4,5]

def ONpow2(a):
    for x in a:
        for y in a:
            print(f"{x} " f"{y}")
    
    for z in a:
        print("__________" f"{z}")


ONpow2(a);