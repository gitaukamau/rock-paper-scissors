import random
import time

print('Welcome to the rock,paper scissors game')
time.sleep(2)
print( 'Pick a choice between rock, paper or scissors')
time.sleep(2)
print( 'You have 5 rounds to play')
time.sleep(2)
print('Here we go!')

rounds = 5
user_count = 0
comp_count = 0
while 0 < rounds <= 5:
    users_choice = input('Enter your choice(rock,paper,scissors): ')
    choices = ('rock','paper','scissors')
    comp_choice = random.choice(choices)
    if users_choice == comp_choice:
        ('Tie')
        user_count = user_count + 0
        comp_count =comp_count + 0
    elif users_choice == 'rock' and comp_choice == 'scissors' or users_choice == 'paper' and comp_choice == 'rock' or users_choice == 'scissors'and comp_choice == 'paper':
        ('user wins')
        user_count = user_count + 1
    else:
        ('comp wins')
        comp_count = comp_count + 1   
    rounds = rounds -1
    
    if rounds == 0:
        break
print('Game over')
print(f'User count is {user_count} the computer count is {comp_count}')
    
if user_count == comp_count:
    print('Its a tie')
elif user_count > comp_count:
    print('User wins')
else:
    print('Comp wins')