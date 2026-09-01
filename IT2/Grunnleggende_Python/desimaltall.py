a = 0.1
b = 0.2
c = a + b
if a + b == 0.3:
  print(f"{a} + {b} er lik 0.3")
else:
  print(f"{a} + {b} er ikke lik 0.3")
  print(f"Resultat: {c}")

print()
d = 0.5
print(f"{d} rundes av til {round(d)}")
e = 5.5
print(f"{e} rundes av til {round(e)}")





print()

# google AI - løsning
from decimal import Decimal, ROUND_HALF_UP, localcontext
# Example: round(4.5, 0) returns 4, while round(5.5, 0) returns 6
with localcontext() as ctx:
    ctx.rounding = ROUND_HALF_UP
    # Represent the number as a string for exactness with Decimal
    # ... virket uten str(d) også...?
    print(f"{d} rundes av til {round(Decimal(d), 0)}") # Output: 5
    
    print(f"{e} rundes av til {round(Decimal(e), 0)}") # Output: 6
