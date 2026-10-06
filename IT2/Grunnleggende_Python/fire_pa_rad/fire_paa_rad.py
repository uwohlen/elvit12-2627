def alle_like(liste):
  """
  Sjekker at alle verdiene i listen er like
  Returnerer True hvis alle er like, False hvis minst en er ulik
  """
  for i in range(1,len(liste)):
    if liste[i] != liste[0]:
      return False
  return True


def sjekk_for_vinner(brett,fra_rad,til_rad,fra_kol,til_kol,rad_ref,kol_ref):
  """
  Sjekker om det er fire like på rad i den to-dimensjonale listen brett
  Sjekker fra og med, og til men ikke med
  De fire verdiene hentes fra brett etter mønster for rad: rad_ref, og kolonne kol_ref
  Returnerer enten "Ingen" eller verdien som har fire like, så lenge det ikke er "_"
  Eksempel på bruk:
    vinner = sjekk_for_vinner(brett,0,6,0,4,"i","j+k")
    if vinner == "Ingen":
      vinner = sjekk_for_vinner(brett,3,6,0,4,"i-k","j+k")
  """
  vinner = "Ingen"
  for i in range(fra_rad,til_rad):
    for j in range(fra_kol,til_kol):
      sjekkliste = []
      for k in range(4):
        sjekkliste.append(brett[eval(rad_ref)][eval(kol_ref)])
      if alle_like(sjekkliste) and sjekkliste[0] != "_":
        vinner = sjekkliste[0]
  return vinner


brett = [["_"]*7 for i in range(6)]

fortsett = True
ikon = "X"
vinner = "Ingen"

while fortsett:
  print(1,2,3,4,5,6,7)
  for rad in brett:
    for kolonne in rad:
      print(kolonne, end=" ")
    print()
  if vinner != "Ingen":
    print()
    print("Vinneren er:",vinner)
    print()
    fortsett = False
  else:
    print()
    print("Spiller: ",ikon)
    print()
    svar = input("Hvor vil du slippe en brikke? Kolonne 1-7 eller S for å slutte: ")
    if svar == "s" or svar == "S":
      fortsett = False
    else:
      try:
        indeks = int(svar)-1
        if indeks < 0 or indeks > 6:
          raise Exception("Kolonne utenfor godkjent område")
      except:
        print()
        print("Skriv et heltall fra og med 1 til og med 7, eller s")
        print()
      else:
        plass = False
        for i in range(5,-1,-1):
          if brett[i][indeks] == "_":
            plass = True
            brett[i][indeks] = ikon
            if ikon == "X":
              ikon = "O"
            else:
              ikon = "X"
            break
        if not plass:
          print()
          print("Kolonnen er full, velg en annen!")
          print()
        else:
          vinner = sjekk_for_vinner(brett,0,6,0,4,"i","j+k")
          if vinner == "Ingen":
            vinner = sjekk_for_vinner(brett,0,3,0,7,"i+k","j")
            if vinner == "Ingen":
              vinner = sjekk_for_vinner(brett,0,3,0,4,"i+k","j+k")
              if vinner == "Ingen":
                vinner = sjekk_for_vinner(brett,3,6,0,4,"i-k","j+k")