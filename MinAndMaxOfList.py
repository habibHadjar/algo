def MinAndMaxOfList(integer_list):
    min = integer_list[0]
    max = integer_list[0]
    index = 1
    while index < len(integer_list):
        min = integer_list[index] if integer_list[index] < min else min
        max = integer_list[index] if integer_list[index] > max else max
        index += 1
    return min, max

print(MinAndMaxOfList([1,2,3]))