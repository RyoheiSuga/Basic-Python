a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
a = int(a)
if a <= 1:
  print('素数でない')
else:
  A=1
  for i in range(2, a):
    if a % i == 0:
      A = 0
  if A == 1:
    print('素数である')
  else:
    print('素数でない')
 