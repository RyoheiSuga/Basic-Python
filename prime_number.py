

# TODO
def sosuu(n):
  if not isinstance(n,int):
    return False
  elif n <= 1:
    return False
  else:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
        
 