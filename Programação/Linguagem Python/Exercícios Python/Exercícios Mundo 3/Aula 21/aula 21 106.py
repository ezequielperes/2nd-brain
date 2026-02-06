def linha(msg, cor='\033[m'):
    from time import sleep
    print(cor,'~' * (len(msg) + 4))
    sleep(0.5)
    print(cor,msg.center(len(msg) + 4))
    sleep(0.5)
    print(cor,'~' * (len(msg) + 4 ))
    sleep(0.5)


def syshelp(funcao_biblioteca):
    linha(f"Acessando o manual do comando '{funcao_biblioteca}'", '\033[33m')
    print('\033[32m')
    help(funcao_biblioteca)


while True:
    linha('Sistema de ajuda Pyhelp', '\033[34m')
    fun_lib = input('\033[35mFunção ou Biblioteca > ').strip().lower()
    if fun_lib == 'fim':
        break
    syshelp(fun_lib)
linha('Até Logo !', '\033[31m')
