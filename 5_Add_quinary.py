def quinAdd(q1, q2):
    num1 = int(q1, 5)
    num2 = int(q2, 5)

    quinSum = num1 + num2

    return quinaryConvert(quinSum)

def quinaryConvert(n):
    if n == 0:
        return '0'
    base5Digit = ''
    while n > 0:
        base5Digit = str(n % 5) + base5Digit
        n //= 5
    return base5Digit

print('Add two quinary strings')
quinary1 = input('Enter your first base5Digit string: ')
quinary2 = input('Enter your second base5Digit string: ')
print(f'There sum is {quinAdd(quinary1, quinary2)}')