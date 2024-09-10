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

print('Pascal\'s Triangle')
numOfRows = int(input('Enter desired number of rows: '))
PascalsTri(numOfRows)