def ReverseList(integer_list):
    index = 0
    index_barre = len(integer_list) - 1
    while index < index_barre:
        integer_list[index], integer_list[index_barre] = integer_list[index_barre], integer_list[index]
        index += 1
        index_barre -= 1
    return integer_list

print(ReverseList([1,2,3]))