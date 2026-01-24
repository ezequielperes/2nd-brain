km = float(input('How many kilometers is the trip?'))
if  -200 <= km <= 200:
    pay = abs(km) * 0.5
    print(f'The trip pay is: {pay:.2f}')
else:
    pay = abs(km) * 0.45
    print(f'The trip pay is: {pay:.2f}')
