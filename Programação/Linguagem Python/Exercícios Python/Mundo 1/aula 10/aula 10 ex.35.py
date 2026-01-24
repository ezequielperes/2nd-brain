print('-=-' *20)
print(f"{'Analyzing Triangles':^60}")
print('-=-' *20)

l1 = float(input('Enter a line: '))
l2 = float(input('Enter another line: '))
l3 = float(input('Enter one more line: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('These lines can form a triangle')
else:
    print('These lines cannot form a triangle')
