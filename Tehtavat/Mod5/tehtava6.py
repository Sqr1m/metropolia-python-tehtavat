import random

a = int(input(" arvottavien pisteiden määrän: "))
b = a
c = 0
Pi = 0
while a > 0:
  
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        c += 1
    a -= 1

Pi = 4 * c / b

print("Pi =", Pi)