lst = [64, 25, 12, 22, 11]

for i in range(len(lst)):
    min_index = i
    # print(min_index)
    for j in range(i+1, len(lst)):
        if lst[j] < lst[min_index]:  # Compare elements, not indices
            min_index = j  # Update min_index to the smallest element found
    # Swap elements outside of the inner loop
    lst[i], lst[min_index] = lst[min_index], lst[i]

print(lst)
