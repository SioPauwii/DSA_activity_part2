import math

def PascalsTri(rows):

    triShape = []
    for i in range(rows):
        row = [math.comb(i, k) for k in range (i + 1)]
        triShape.append(row)

    maxRowLen = len(str(triShape[-1][len(triShape[-1]) // 2]))

    baseLen = rows * (maxRowLen + 1) - 1

    for xAxis in triShape:
        stringXaxis = ' '.join(f'{num:>{maxRowLen}}' for num in xAxis)
        startAlign = ' ' * ((baseLen - len(stringXaxis)) // 2)
        print(startAlign + stringXaxis)

print('Pascal\'s Triangle')
numOfRows = int(input('Enter desired number of rows: '))
PascalsTri(numOfRows)