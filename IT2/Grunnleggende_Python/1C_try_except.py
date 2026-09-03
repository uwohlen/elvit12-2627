svar = input("skriv noe: ")

try:
  print("det var et tall")
  tall = float(svar)
except:
  print("det var ikke et tall")
else:
  pass
finally:
  pass

print("testen er ferdig")
print("dette er ikke en del av try-except")