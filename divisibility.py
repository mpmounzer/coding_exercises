# Marc Mounzer's divisibility.py for Bleacher Report
# 8/24/2018

def divisibility(first_int, second_int, third_int):
    divisible_numbers = []

    for x in range(1, 101):
        if x % first_int == 0 or x % second_int == 0 or x % third_int == 0:
            divisible_numbers.append(x)

    return divisible_numbers

print('Which of the numbers 1 to 100 are evenly divisible by any of the following three numbers?')
first_int = eval(input('Enter the first number: '))
second_int = eval(input('Enter the second number: '))
third_int = eval(input('Enter the third number: '))
print(f'The numbers that are divisible by any of the three numbers are: {divisibility(first_int,second_int,third_int)}')