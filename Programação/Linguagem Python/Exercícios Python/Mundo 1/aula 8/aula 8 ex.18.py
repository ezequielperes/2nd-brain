from math import sin, cos, tan, radians

angle = float(input('enter an angle in degrees: '))
rad = radians(angle)

print(f'the sine of the angle is {sin(rad):.2f}\n'
      f'the cosine of the angle is {cos(rad):.2f}\n'
      f'the tangent of the angle is {tan(rad):.2f}')