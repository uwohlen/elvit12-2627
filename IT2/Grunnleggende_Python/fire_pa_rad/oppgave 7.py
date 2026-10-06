def alle_like(liste):
  """
  Sjekker at alle verdiene i listen er like
  Returnerer True hvis alle er like, False hvis minst en er ulik
  NB! Denne versjonen virker bare for lister med akkurat 4 elementer. Dårlig design!
  """
  if liste[0] == liste[1] and liste[1] == liste[2] and liste[2] == liste[3]:
    return True
  else:
    return False

brett = [
  ["_","_","_","_","_","_","_"],
  ["_","_","_","_","_","_","_"],
  ["_","_","_","_","_","_","_"],
  ["_","_","_","_","_","_","_"],
  ["_","_","X","X","X","X","_"],
  ["_","_","_","_","_","_","_"]
]

vinner = "Ingen"

for i in range(6):
  for j in range(4):
    sjekkliste = []
    for k in range(4):
      sjekkliste.append(brett[i][j+k])
    if alle_like(sjekkliste) and sjekkliste[0] != "_":
      vinner = sjekkliste[0]

for i in range(3):
  for j in range(7):
    sjekkliste = []
    for k in range(4):
      sjekkliste.append(brett[i+k][j])
    if alle_like(sjekkliste) and sjekkliste[0] != "_":
      vinner = sjekkliste[0]

for i in range(3):
  for j in range(4):
    sjekkliste = []
    for k in range(4):
      sjekkliste.append(brett[i+k][j+k])
    if alle_like(sjekkliste) and sjekkliste[0] != "_":
      vinner = sjekkliste[0]

for i in range(3,6):
  for j in range(4):
    sjekkliste = []
    for k in range(4):
      sjekkliste.append(brett[i-k][j+k])
    if alle_like(sjekkliste) and sjekkliste[0] != "_":
      vinner = sjekkliste[0]

print("Vinneren er:",vinner)