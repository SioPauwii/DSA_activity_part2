#number 1
def Findgcd(int1, int2):
    while int2 != 0:
        int1, int2 = int2, int1 % int2
    
    return int1

#number 2
def checkPerfNum(num):
    if num <= 1: return False

    checkSum = 0
    for i in range (1, num):
            if num % i == 0:
                checkSum += i
    if checkSum == num:
        return 'Yes!'
    else:
        return 'No :<'
    
#number 3
def BinAdd(b1, b2):
    num1 = int(b1, 2)
    num2 = int(b2, 2)

    binSum = num1 + num2
    
    return bin(binSum)[2:]

#number 4
def hexAdd(hex1, hex2):
    num1 = int(hex1, 16)
    num2 = int(hex2, 16)

    hexSum = num1 + num2

    return hex(hexSum)[2:].upper()

#number 5
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

#number 6
def PascalsTri(rows):
    triangle = []

    for i in range(rows):
        xAxis = [1] * (i + 1)
        for j in range(1, i):
            xAxis[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(xAxis)

    maxRowLen = len(str(triangle[-1][len(triangle[-1]) // 2]))

    baseLen = rows * (maxRowLen + 1) - 1

    for xAxis in triangle:
        stringXaxis = ' '.join(f'{num:>{maxRowLen}}' for num in xAxis)
        startAlign = ' ' * ((baseLen - len(stringXaxis)) // 2)
        print(startAlign + stringXaxis)

print('Computing the Greatest Common Denominator')
num1_1 = int(input("Enter your first number: "))
num1_2 = int(input("Enter your second number: "))
print(f'The greatest common denominator of these numbers is {Findgcd(num1_1, num1_2)}\n\n')

print('Check if a number is a perfect number')
num2_1 = int(input("Enter your number: "))
print(f'Is {num2_1} a perfect number? \nAnswer: {checkPerfNum(num2_1)}\n\n')

print('Add two binary strings')
binary1 = input('Enter your first binary string: ')
binary2 = input('Enter your second binary string: ')
print(f'There sum is {BinAdd(binary1, binary2)}\n\n')

print('Add two hexadecimal strings')
hex1 = input('Enter your first hexadecimal string: ')
hex2 = input('Enter your second hexadecimal string: ')
print(f'There sum is {hexAdd(hex1, hex2)}\n\n')

print('Add two base5Digit strings')
quinary1 = input('Enter your first base5Digit string: ')
quinary2 = input('Enter your second base5Digit string: ')
print(f'There sum is {quinAdd(quinary1, quinary2)}\n\n')

print('Pascal\'s Triangle')
numOfRows = int(input('Enter desired number of rows: \n'))
PascalsTri(numOfRows)