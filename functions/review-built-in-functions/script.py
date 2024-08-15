def distance_from_zero(dist):
  if type(dist) == int or type(dist) == float:
    return abs(dist)
  else:
    return "Nope"
  
print(distance_from_zero(-45))