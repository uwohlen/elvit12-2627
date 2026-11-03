svar = input("skriv noe: ")

for bokstav in svar:
  if bokstav == "x":
    print("kode ved break")
    break
  elif bokstav == "y":
    continue
  elif bokstav == "z":
    pass
  print(bokstav)
else:
  print("kode til slutt når ikke break")

print("denne koden er ikke en del av løkka")
