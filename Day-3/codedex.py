# Bài 1

#print('BANK OF CODEDEX')
#
#pin = int(input('Enter your 4 digit pin: '))
#
#while pin != 1234:
#    pin = int(input('Incorrect PIN. Enter your PIN again: '))
#
#if pin == 1234:
#    print('PIN accepted!')

# Bài 2

# Ví dụ
#guess = 0
#tries = 0
#
#while guess != 6 and tries < 5:
#  guess = int(input('Guess the number: '))
#  tries = tries + 1
#
#if guess != 6:
#  print('You ran out of tries.')
#else:
#  print('You got it!')

# Bài 3

#for i in range(99, 0, -1):
#    print(f'''
#{i} bottles of beer on the wall
#{i} bottles of beer
#Take one down, pass it around
#{i - 1} bottles of beer on the wall
#''')

# Bài 4
#for i in range(1, 100, 1):
#  if i % 5 == 0 and i % 3 == 0:
#    print('FizzBuzz')
#  elif i % 3 == 0:
#    print('Fizz')
#  elif i % 5 == 0:
#    print('Buzz')  
#  else:
#    print(i)

# Practice
#rating = 2.5
#
#if rating > 4.5:
#  print('Extraordinary')
#elif rating > 4:
#  print('Excellent')
#elif rating > 3:
#  print('Good')
#elif rating > 2:
#  print('Fair')
#else:
#  print('Poor')
#
#grade = int(input('Enter your grade: '))
#if grade == 9:
#  print('Freshman')
#elif grade == 10:
#  print('Sophomore')
#elif grade == 11:
#  print('Junior')
#elif grade == 12:
#  print('Senior')
#else:
#  print('TBD')
#
#import random
#
#a = random.randint(0, 5)
#if a == 0:
#  print('Flamingos turn pink from eating shrimp.')
#elif a == 1:
#  print('The only food that doesn\'t spoil is honey.')
#elif a == 2:
#  print('Shrimp can only swim backwards.')
#elif a == 3:
#  print('A taste bud\'s life span is about 10 days.')
#elif a == 4:
#  print('It is impossible to sneeze while sleeping.')
#else:
#  print('It is illegal to sing off-key in North Carolina.')
#
#month = int(input('Enter a month: '))
#if month == 1 or month == 2 or month == 3:
#  print('Winter 🌨️')
#elif month == 4 or month == 5 or month == 6:
#  print('Spring 🌱')
#elif month == 7 or month == 8 or month == 9:
#  print('Summer 🌻')
#elif month == 10 or month == 11 or month == 12:
#  print('Autumn 🍂')
#else:
#  print('Invalid')

mercury = 0.38
venus = 0.91
mars = 0.38
jupiter = 2.53
saturn = 1.07
uranus = 0.89
neptune = 1.14

a = float(input("Your Earth weight: "))
b = int(input('A planet number: '))

if b == 1:
    c = a * 0.38
    print(f'Your weight is {c}')
elif b == 2:
    c = a * 0.91
    print(f'Your weight is {c}')
elif b == 3:
    c = a * 0.38
    print(f'Your weight is {c}')
elif b == 4:
    c = a * 2.53
    print(f'Your weight is {c}')
elif b == 5:
    c = a * 1.07
    print(f'Your weight is {c}')
elif b == 6:
    c = a * 0.89
    print(f'Your weight is {c}')
elif b == 7:
    c = a * 1.14
    print(f'Your weight is {c}')
else:
    print('Invalid planet number')