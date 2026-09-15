# Hurtigversjon av tabeller slik matematikere liker dem:
# Tekst er venstrestilt
# Tall er høyrestilt
# Desimaltall er justert etter desimaltegnet

from tabulate import tabulate

tabell_data = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]
print(tabulate(tabell_data))
