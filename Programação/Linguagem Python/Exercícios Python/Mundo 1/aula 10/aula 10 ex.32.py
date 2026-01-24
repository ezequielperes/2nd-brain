year = int(input("Enter the year to check if it's leap year:"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It's a leap Year!")

else:
    print("It's not a leap Year!")
