# variabler, kapittel 1F

# global variabel
tall = 4 

print("test1: if-else")
a = 3 # 30
c = None

if a < 10:
  b = 2
  tall = 1
  print(b, tall)
else:
  c = 5


if c != None:
  print(c)

print(b)
print(c)
print(tall)

print("test2: funksjoner")
#v1 = None

def f(x):
  #global v1 # bruker den eksisterende globale variabelen, eller lager den om den mangler
  v1 = x
  tall = 6
  print(v1, tall)

f(7)
print(tall)
#print(v1)

print("test3: parametre og return")

v3 = 8

def g(x):
  x += 1
  return x


v4 = g(v3)
print(v4)
print(v3)

v3 = g(v3)
print(v3)