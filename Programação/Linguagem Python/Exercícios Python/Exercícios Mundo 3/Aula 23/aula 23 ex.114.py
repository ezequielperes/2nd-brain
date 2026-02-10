import requests

try:
    site = requests.get('https://www.pudim.com.br')
    print('\033[32mO site pudim está acessível no momento!\033[m')
except:
    print('\033[31mO site pudim não está acessível no momento!\033[m')
