name = input('Enter your name: ').strip()

print(f'Your name in upper is: {name.upper()}')

print(f'Your name in lower is: {name.lower()}')

print(f"Your name has {len(name.replace(' ',''))} letters")

divided = name.split()
print(f'Your first name hasy {len(divided[0])} letters')
name.count

