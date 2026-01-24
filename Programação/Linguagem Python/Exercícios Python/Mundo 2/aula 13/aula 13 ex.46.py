from time import sleep
from random import choice
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m', ]
for c in range(10, -1, -1 ):
    if c >6:
        print(colors[1], c)
    elif c >3:
        print(colors[2], c)
    else:
        print(colors[0], c, '\033[m')
    sleep(1)
print(f'{choice(colors)}L{choice(colors)}A{choice(colors)}N{choice(colors)}Ç{choice(colors)}A{choice(colors)}R{choice(colors)}R{choice(colors)}R{choice(colors)}R{choice(colors)}R{choice(colors)}R!{choice(colors)}!{choice(colors)}!{choice(colors)}!')
