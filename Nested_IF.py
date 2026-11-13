num1= int(input())
num2= int(input())

if(num1 >= num2):
    if(num1 == num2):
        print(f'{num1} and {num2} are equal')
    else:
        print(f'{num1} is greater than {num2} ')
else:
    print(f'{num1} is smaller than {num2} ')