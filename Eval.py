def Eval(string_operation):
    # 2*3+5/6*3-15 = -6.5
    # 2*(3+5*2)/6*3-15 = -2
    # 23+3*(6+5*(5*2+6)) = 281

    if "(" in string_operation:
        open_idx = string_operation.index("(")
        close_idx = string_operation.rindex(")")

        inner_expression = string_operation[open_idx + 1 : close_idx]

        inner_result = Eval(inner_expression)
        string_operation = (
            string_operation[:open_idx]
            + str(inner_result)
            + string_operation[close_idx + 1 :]
        )
        return Eval(string_operation)

    if "+" in string_operation:
        operations_to_sum = string_operation.split("+")
        for i in range(len(operations_to_sum)):
            operations_to_sum[i] = Eval(operations_to_sum[i])
        return sum(operations_to_sum)
    
    if "-" in string_operation:
        operations_to_sub = string_operation.split("-")
        for i in range(len(operations_to_sub)):
            operations_to_sub[i] = Eval(operations_to_sub[i])
        return operations_to_sub[0] - sum(operations_to_sub[1:])
    
    if "*" in string_operation:
        operations_to_mul = string_operation.split("*")
        res = 1
        for i in range(len(operations_to_mul)):
            operations_to_mul[i] = Eval(operations_to_mul[i])
            res *= float(operations_to_mul[i])
        return res
    
    if "/" in string_operation:
        operations_to_div = string_operation.split("/")
        res = float(operations_to_div[0])
        for i in range(1, len(operations_to_div)):
            res /= float(operations_to_div[i])
        return res
    return float(string_operation)

print(Eval("23+3*(6+5*(5*2+6))"))