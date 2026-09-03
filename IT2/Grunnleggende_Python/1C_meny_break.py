while True:
  print("Meny")
  print("a - ananas")
  print("b - banan")
  print("q - quit")
  svar = input("Hva velger du? ")
  if svar == "q":
    break
  else:
    print(svar)
  # mer kode utenfor else blir ikke kjørt før slutt
  print("Mer kode")

