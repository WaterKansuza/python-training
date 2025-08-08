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

#Bài 1

import random
#quest = input("Enter a question: ")
#
#first = "Yes - definitely"
#second = "It is decidedly so."
#third = "Without a doubt."
#fourth = "Reply hazy, try again."
#fifth = "Ask again later."
#sixth = "Better not tell you now."
#seventh = 'My sources say no.'
#eighth = 'Outlook not so good.'
#nineth = 'Very doubtful.'
#
#ans = random.randint(1, 9)
#if ans == 1:
#    print(first)
#elif ans == 2:
#    print(second)
#elif ans == 3:
#    print(third)
#elif ans == 4:
#    print(fourth)
#elif ans == 5:
#    print(fifth)
#elif ans == 6:
#    print(sixth)
#elif ans == 7:
#    print(seventh)
#elif ans == 8:
#    print(eighth)
#elif ans == 9:
#    print(nineth)

# Bài 2

#height = int(input("What is your height: "))
#credits = int(input("How many credits do you have: "))
#
#if height >= 137 and credits >= 10:
#    print('Enjoy the ride!')
#elif height < 137 and credits >= 10:
#    print('You are not tall enough to ride.')
#elif height >= 137 and credits < 10:
#    print('You don\'t have enough credits.')
#else:
#    print('You have not met either requirement.')

# Bài 3
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0


print(''' Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk
''')

a = int(input("Enter your choice: "))

if a == 1:
    Gryffindor += 1 
    Ravenclaw += 1
elif a == 2:
    Hufflepuff += 1 
    Slytherin += 1
else:
    print('Wrong input.')

print('''
      Q2) When I\’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold
      ''')

b = int(input("Enter your choice: "))

if b == 1:
    Hufflepuff += 2
elif b == 2:
    Slytherin += 2
elif b == 3:
    Ravenclaw += 2
elif b == 4:
    Gryffindor += 2
else:
    print('Wrong input.')

print('''
      Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
      ''')
c = int(input("Enter your choice: "))

if c == 1:
    Slytherin += 4
elif c == 2:
    Hufflepuff += 4
elif c == 3:
    Ravenclaw += 4
elif c == 4:
    Gryffindor += 4
else:
    print('Wrong input.')

print('Your point is:')
print(Gryffindor, 'Gryffindor')
print(Ravenclaw, 'Ravenclaw')
print(Hufflepuff, 'Hufflepuff')
print(Slytherin, 'Slytherin')

max = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
if max == Gryffindor:
    print('U r Gryffindor')
elif max == Ravenclaw:
    print('U R Ravenclaw')
elif max == Hufflepuff:
    print('U R Hufflepuff')
else:
    print('U R Slytherin')