value_house = float(input("What's the value of the house? "))
wage = float(input("What's Your wage? "))
year = int(input("How many years do you want to pay?"))

portion_month = value_house / (year * 12)

if portion_month <= wage * 0.3:
    print(f'\033[32mYou will pay ${portion_month:.2f} your loan was approved ')
else:
    print(f"\033[31mYou will pay ${portion_month:.2f}, your loan wasn't approved")
print(f'\033[33mTo be approved, your salary needs to be at least: ${float(portion_month * 100 / 30):.2f} !')