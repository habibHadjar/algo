def FindSubChain(list_to_search,list_to_find):
    index = 0
    while index < len(list_to_search):
        if list_to_search[index] == list_to_find[0]:
            if list_to_search[index:index + len(list_to_find)] == list_to_find:
                return index
        index += 1
    return -1
            
print(FindSubChain([12, 14, 70, 35, 25, 12],[14, 70, 35]))