

# TODO
def euclid(a,b):
  while b!=0:
    a, b = b, a%b
  return a
def coprime(a,b):
  return euclid(a,b)==1
    

import random
s = 0
for i in range(100000):
  a = random.randint(1,10000)
  b = random.randint(1,10000)
  if coprime(a,b):
    s += 1
print(s/100000)
  