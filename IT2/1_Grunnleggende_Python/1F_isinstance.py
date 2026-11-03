import random as rd

verdier = [3.5, 4, "6","m",True,False,(4,5)]

# True blir tolket som 1, False som 0, i begge tilfeller under:

for verdi in verdier:
  if isinstance(verdi,(int,float)):  # får ikke "6" med som et tall
    tall = float(verdi) 
    print(tall + 5)
  else:
    print(str(verdi) + "5")

for verdi in verdier:
  try:
    tall = float(verdi) # får med "6" som et tall
    print(tall + 5)
  except:
    print(str(verdi) + "5")