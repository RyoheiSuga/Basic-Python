from math import sin
import math
# --example--
# print(sin(0))
# >>> 0
# -----------

# TODO
def a(x):
  return sin(x)
def b(x):
  return 4/(1+x**2)
def c(x):
  return math.pi**(1/2)*math.exp(-x**2)
def tra(d,a=0,b=1,n=100):
  h = (b-a)/n
  S = 0
  for k in range(1,n+1):
    S += h*(d(a+(k-1)*h)+d(a+k*h))/2
  return S
result1 = tra(a,0,math.pi/2,50)
result2 = tra(b,0,1,100)
result3 = tra(c,-100,100,1000)

print("(1)", result1)
print("(2)", result2)
print("(3)", result3)
