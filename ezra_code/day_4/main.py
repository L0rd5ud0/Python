def only_floats(a,b):
  if isinstance(a, int) and isinstance(b, int):
    return 2
  elif isinstance(a, int) == False and isinstance(b, int) == True or isinstance(b, int) == False and isinstance(a, int) == True:
    return 1
  else:
    return 0
  
print(only_floats(22,23))
