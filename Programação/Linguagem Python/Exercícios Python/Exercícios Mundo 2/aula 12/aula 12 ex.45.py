from random import choice
from time import sleep

print('\033[33m-'*40)
print('\033[1;35mJO KEN PÔ!'.center(45))
print('\033[33m-'*40)
sleep(2)
print('\033[34m Vamos jogar JOKENPÔ! Escolha uma das opções:')
sleep(0.8)
print('\033[33m1 -> JO (Pedra)')
sleep(0.8)
print('\033[35m2 -> KEN (Papel)')
sleep(0.8)
print('\033[36m3 -> PO (Tesoura)')
sleep(0.8)
escolha = input('\033[1;31mEscolha: \033[m').strip().upper()
print('\033[33mJO\033[m')
sleep(0.5)
print('\033[35mKEN\033[m')
sleep(0.5)
print('\033[36mPO\033[1;31m!\033[m')
sleep(1)

pedra = ['PEDRA', 'JO', '1']
papel = ['PAPEL', 'KEN', '2']
tesoura = ['TESOURA', 'PO', '3']
lista = ["PEDRA", "PAPEL", "TESOURA"]
pc = str(choice(lista))

#transformação
if escolha in pedra:
    jogador = 'PEDRA'
elif escolha in papel:
    jogador = 'PAPEL'
elif escolha in tesoura:
    jogador = 'TESOURA'
else:
    jogador = 'invalid'
#Resultados
if jogador == 'invalid':
    print('\033[1;31m ENTRADA INVÁlIDA!')
elif jogador == pc:
    print(f'Eu escolhi \033[1;33m{pc}\033[m e você escolheu \033[1;33m{jogador}\033[m... \033[1;33mEMPATAMOS!!!')
else:
    if(
            (pc in pedra and jogador in tesoura) or
            (pc in papel and jogador in pedra) or
            (pc in tesoura and jogador in papel)
    ):
        print(f'Eu escolhi \033[1;32m{pc}\033[m e você escolheu \033[31m{jogador}\033[m... \033[1;31mEU GANHEI MUAHAHAHAHHAHAH!!!')
    else:
        print(f'Eu escolhi \033[31m{pc}\033[m e você escolheu \033[1;32m{jogador}\033[m... \033[1;32mEU PERDI!!! NÃOOOOOOOOOOOO!!!!!!')
