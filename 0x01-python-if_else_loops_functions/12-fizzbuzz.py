#!/usr/bin/python3
def fizzbuzz():
    for my_number in range(1, 101):
        if my_number % 3 == 0 and my_number % 5 != 0:
            print('Fizz', end=' ')
        elif my_number % 5 == 0 and my_number % 3 != 0:
            print('Buzz', end=' ')
        elif my_number % 3 == 0 and my_number % 5 == 0:
            print('FizzBuzz', end=' ')
        else:
            print(my_number, end=' ')
