brett = [["_"]*5 for i in range(5)]
spiller = "X"

trekkliste = [
  [1,1],
  [2,2],
  [2,1],
  [3,1],
  [1,3],
  [2,1]
]

for trekk in trekkliste:
  rad = trekk[0]
  kolonne = trekk[1]
  if brett[rad][kolonne] == "_":
    brett[rad][kolonne] = spiller
    if spiller == "X":
      spiller = "O"
    else:
      spiller = "X"

for rad in brett:
  print(rad)