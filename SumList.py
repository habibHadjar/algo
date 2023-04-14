def SumList(number_list):
    if len(number_list) == 0:
        return 0
    else:
        return number_list[0] + SumList(number_list[1:])

print(SumList([1,1,1]))