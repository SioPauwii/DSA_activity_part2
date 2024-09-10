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
    
print('Check if a number is a perfect number')
num2_1 = int(input("Enter your number: "))
print(f'Is {num2_1} a perfect number? \nAnswer: {checkPerfNum(num2_1)}')
