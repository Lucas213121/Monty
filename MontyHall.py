'''
Created on Nov 15, 2018
 
@author: lsadoulet22
'''
import random
car=random.randint(1,3)
guess=int(input('Which door would you like to  pick: '))
while guess > 3 or guess < 1:
  guess = int(input('Try a number bettween 1 though 3'))
if guess == 1:
    if car != 2:
        print('There is a goat behind door #2')
        reveal = 2
    elif car != 3:
        print('There is a goat behind door #3')
        reveal = 3
    elif car == 1:
        print('There is a goat behind door #2')
        reveal = 2
if guess == 2:
    if car != 1:
        print('There is a goat behind door #1')
        reveal = 1
    elif car != 3:
        print('There is a goat behind door #3')
        reveal = 3
    elif car == 2:
        print('There is a goat behind door #3')
        reveal = 3
if guess == 3:
    if car != 1:
        print('There is a goat behind door #1')
        reveal = 1
    elif car != 2:
        print('There is a goat behind door #2')
        reveal = 2
    elif car == 3:
        print('There is a goat behind door #1')
        reveal = 1
switch=input('Would you like to switch doors? (y/n)')
while switch != 'n' and switch != 'y':
  print('invalid answer')
  switch = input('try again')
if switch =='y':
  if guess == 1:
    if reveal == 2:
        guess = 3   
    if reveal == 3:
        guess = 2
  elif guess == 2:
    if reveal == 1:
      guess = 3
    if reveal == 3:
      guess = 1
  elif guess == 3:
    if reveal == 1:
      guess = 2
    if reveal == 2:
      guess = 1
print('You picked door ',guess,sep='#')
print('The car was behind door ',car,sep='#')
if guess == car:
        print('You win a car')
elif guess != car:
        print('You got goat')
