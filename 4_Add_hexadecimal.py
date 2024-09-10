def hexAdd(hex1, hex2):
    num1 = int(hex1, 16)
    num2 = int(hex2, 16)

    hexSum = num1 + num2

    return hex(hexSum)[2:].upper()

print('Add two hexadecimal strings')
hex1 = input('Enter your first hexadecimal string: ')
hex2 = input('Enter your second hexadecimal string: ')
print(f'There sum is {hexAdd(hex1, hex2)}')