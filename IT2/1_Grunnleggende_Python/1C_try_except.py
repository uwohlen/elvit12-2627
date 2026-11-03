svar = input("skriv noe: ")

try:
  tall = float(svar)
except:
  print("det var ikke et tall")
else:
  print("det var et tall")
finally:
  print("testen er ferdig")

print("dette er ikke en del av try-except")