# "pip install autopep8"
# "==" equal to
# "!=" not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

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