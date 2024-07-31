def selectionsort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range(idx + 1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
l = [22, 13, 4, 8, 17, 26, 53, 4]
selectionsort(l)
print("Sorted Elements : ",l)