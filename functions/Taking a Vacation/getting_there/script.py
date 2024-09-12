def hotel_cost(nights):
  return 140 * nights
  
def plane_ride_cost(city):
  price = 0
  if city == "Charlotte":
    price = 183
  elif city == "Tampa":
    price = 220
  elif city == "Pittsburgh":
    price = 222
  else:
    price = 475
  return price

print(hotel_cost(10))

print(plane_ride_cost("Charlotte"))