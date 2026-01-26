from random import randint
from emoji import emojize
Dice = str(randint(1, 6))
Text = f" :game_die: {Dice} :game_die: "

print('='*30)
print(emojize(f'{Text:-^46}'))
print('='*30)