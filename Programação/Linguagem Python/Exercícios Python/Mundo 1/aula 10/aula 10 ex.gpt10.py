name = input("What's your name? ").strip().title()
year = int(input("How old are you? "))
year_str = str(year)
print(f"{name + ' | ' + year_str + ' Years old' :=^40}")
if year >= 18:
    print(f"{'You are of legal age':=^40}")
else:
    print(f"{'You are underage':=^40}")