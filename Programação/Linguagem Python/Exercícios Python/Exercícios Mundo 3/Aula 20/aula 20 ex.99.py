from time import sleep
def maior(* num):
    maiorr = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for c, v in enumerate(num):
        print(v, end= ' ')
        sleep(0.25)
        if  c == 0:
            maiorr = v
        elif v > maiorr:
            maiorr = v
    print(f'Foram informados {len(num)} valores ao todo'
          f'\nO maior valor informado foi {maiorr} ')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
