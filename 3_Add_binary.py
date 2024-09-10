def BinAdd(b1, b2):
    num1 = int(b1, 2)
    num2 = int(b2, 2)

    binSum = num1 + num2
    
    return bin(binSum)[2:]

print('Add two binary strings')
binary1 = input('Enter your first binary string: ')
binary2 = input('Enter your second binary string: ')
print(f'There sum is {BinAdd(binary1, binary2)}')