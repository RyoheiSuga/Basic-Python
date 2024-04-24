a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
def euclid(a,b):
  while b!=0:
    a, b = b, a%b
  return a
def so(a,b):
  if euclid(a,b)==1:
    return True
  else:
    return False

import random
s = 0
for i in range(100000):
  a = random.randint(1,10000)
  b = random.randint(1,10000)
  if so(a,b)==True:
    s += 1
print(s/100000)
  