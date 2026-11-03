tekst = "123454321"
total = 0
print(f"Total: {total}")
for siffer in tekst: # x viser ikke hva som skjer, bedre med et annet variabelnavn, f.eks. siffer
  if siffer == "5":
    siffer = "6"
  total += int(siffer)
  print(f"+ {siffer} = {total}")
print(total)
print(siffer)
print(tekst)