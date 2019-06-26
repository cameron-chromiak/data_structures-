
def is_square(n):
  if(n>=0):
    for i in range(n+1):
      if (i*i == n):
        return True
    return False
  else:
      return False

is_square(25)
