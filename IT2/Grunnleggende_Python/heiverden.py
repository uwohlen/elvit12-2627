print("hello world")
print("hei","verden",end="!!! ")
print("livet","går","videre",sep="---")

import random as rd
fortsett = True
while fortsett:
  i = rd.randint(0,10)
  if i == 0:
    print("Null")
    continue
  print(i)
  if i == 10:
    fortsett = False # eller break, men da virker ikke else
else: # hvorfor bruke else?
  print(f"Siste tallet var: {i}")