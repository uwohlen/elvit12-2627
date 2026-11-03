# Gir 250 mg medisin hver dag
# Kroppen skiller ut 20 % i løpet av et døgn
# Hvor mye virkestoff bygger det seg opp i kroppen?
a = 250
k = 0.8
summen = 0
dager = 1
while abs(summen-1250) > 0.01 and dager < 60:
    summen = summen + a
    print(f"Dag {dager:2}: a={a:10.5f}, summen={summen:12.5f}")
    a = a * k
    dager = dager + 1