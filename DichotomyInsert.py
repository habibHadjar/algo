def DichotomyInsert(ordered_list, value_to_insert):
    low = 0
    high = len(ordered_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if value_to_insert < ordered_list[mid]:
            high = mid - 1
        elif value_to_insert >= ordered_list[mid]:
            low = mid + 1
    ordered_list.insert(low, value_to_insert)
    return ordered_list

L = [1,2,3,4,4,5]
x = 3
print(DichotomyInsert(L, x))