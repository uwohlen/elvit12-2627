while True:
  verdi1 = input("Skriv inn et tall: ")
  try:
    sum = float(verdi1.replace(',', '.'))
  except ValueError:
    break
  verdi2 = input("Skriv inn et annet tall: ")
  try:
    sum += float(verdi2.replace(',', '.'))
    print(f"{verdi1} og {verdi2} er {sum}")
  except ValueError:
    break