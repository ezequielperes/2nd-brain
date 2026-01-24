km = float(input("How fast is the car?"))
if km > 80:
    fine = (km - 80) * 7
    print(f'The fine you will pay is: ${fine:.2f}')
elif -80 <= km < 0:
    print('Wait, are you driving wrong way ?!')
elif km < -80:
    fine2 = (abs(km) - 80) * 14
    print('WTF?!?! You exceeded the speed going the wrong way ????'
          f'The fine you will pay is: ${fine2:.2f}')
else:
    print('Everything is fine! Have a good day!')