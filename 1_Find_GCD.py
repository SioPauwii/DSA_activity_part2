def Findgcd(int1, int2):
    while int2 != 0:
        int1, int2 = int2, int1 % int2
    
    return int1

print('Computing the Greatest Common Denominator')
num1_1 = int(input("Enter your first number: "))
num1_2 = int(input("Enter your second number: "))
print(f'The greatest common denominator of these numbers is {Findgcd(num1_1, num1_2)}')
