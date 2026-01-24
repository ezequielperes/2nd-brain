from random import randint
from time import sleep
n1 = randint(0, 5)
print('-=-' *20)
print("Let's discover if you can guess the number that i think!!!".upper())
print('-=-' *20)
n2 = int(input("Enter a number between 0 and 5: ".upper()))
print('Processing...')
sleep(2)
if n2 > 5:
    print('The number is greater than 5'.upper())
elif n2 < 0:
    print('The number is less than 0'.upper())
elif n1 == n2:
    print(f"YOU ARE AWESOME! YOU DISCOVER THE NUMBER THAT I THINK, IT'S {n2}!")
elif n2 >= (n1+2) or n2 <= (n1-2):
    print("MUAHAHAHAHA!!! YOU ARE VERY BAD!!!\n"
          f"IT'S {n1}, {n2} IS NOT {n1}!")
else:
    print(f"WRONG! I THINK {n1}, {n2} IS NOT {n1}!")
