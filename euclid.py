a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
adef euclid(a,b):
  while b!=0:
    a, b = b, a%b
  return a
  