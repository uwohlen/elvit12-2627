# a) Her er det en logisk feil i programmet... 
#   - hva skal til for at vannet koker?
# b) Hva er en svakhet i programmet, som kan føre til at programmet krasjer (gir feilmeldinger)? 
#     (...som kan fikses med try-except, kap 1C)

temperatur = input("Oppgi vannets temperatur: ")
temperatur = float(temperatur)

if temperatur > 0:
  print("Vannet er i flytende form.")
elif temperatur > 100:
  print("Vannet koker.")
else:
  print("Vannet fryser til is.")