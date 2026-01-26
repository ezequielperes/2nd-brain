from emoji import emojize
emoji = emojize(' :slightly_smiling_face: ')
name = input("What's your name? ").upper().strip() + ' | '
year = (input("how old are you? "))
print('-'*46)
print(f"{emoji + name + year + ' YEARS OLD' + emoji:-^46}")
print('-'*46)