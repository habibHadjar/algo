def Delta_Max_And_Min_In_List(L):
    delta_min = 0
    delta_max = 0
    index = 0
    while index < len(L) - 1:
        current_delta = (L[index] - L[index + 1]) * -1
        if current_delta < delta_min:
            delta_min = current_delta
        elif current_delta > delta_max:
            delta_max = current_delta
        index += 1
    return delta_min, delta_max

L = [10, 22, 11, 45, 70, 100, 12]
print(Delta_Max_And_Min_In_List(L))