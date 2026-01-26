wage = float(input('Congratulations!!! You against a new wage\nenter your old wage:'))
if wage > 1250:
    print(f'Your new wage is: ${wage * 1.1:.2f}')
else:
    print(f'Your new wage is: ${wage * 1.15:.2f}')
