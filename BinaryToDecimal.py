def BinaryToDecimal(binaryList):
    dec_value = 0
    for i in range(len(binaryList)):
        dec_value = dec_value * 2 + binaryList[i]
    return dec_value
print(BinaryToDecimal([1, 0, 1, 1, 1, 1, 1, 0]))