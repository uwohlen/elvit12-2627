while True:
  verdi1 = input("Skriv inn et tall: ")
  try:
    total = float(verdi1.replace(',', '.'))
  except ValueError:
    break
  verdi2 = input("Skriv inn et annet tall: ")
  try:
    total += float(verdi2.replace(',', '.'))
    print(f"{verdi1} og {verdi2} er {total}")
  except ValueError:
    break