a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
def sosuu(n):
  if type(n) != int:
    return False
  elif n <= 1:
    return False
  else:
    A = 1
    for i in range(2, n):
      if n % i == 0:
        A = 0
    if A == 1:
      return True
    else:
      return False
 