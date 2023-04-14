def StringToDecimal(string):
    dec_value = 0
    index = 0
    while index < len(string):
        dec_value = dec_value * 10 + ord(string[index]) - ord('0')
        index = index + 1
    return dec_value

print(StringToDecimal('123')-StringToDecimal('10'))