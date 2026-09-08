def lad_mobil(gammel,endring):
  if endring < 0:
    raise Exception("Lading må være et positivt tall.")
  if gammel + endring > 100:
    return 100
  else:
    return gammel + endring

batteri = 50

while True:
  print(f"Ladenivået er: {batteri} %.")
  svar = input("Hvor mye vil du lade batteriet? (eller q) ")
  if svar == "q":
    break
  else:
    try:
      lading = float(svar)
      ny = lad_mobil(batteri,lading)
    except ValueError:
      print("Ladingen angis som et tall.")
    except Exception as tekst:
      print(f"Feilmelding: {tekst}")
    else:
      print(f"Nytt ladenivå: {ny}")
      batteri = ny
  