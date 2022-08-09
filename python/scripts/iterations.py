# Les itérations ou boucles consistent
# à reproduire des instructions un certain nombre de fois

# Affiche "bonjour" sans itérations (manuellement)
'''
print("bonjour 1")
print("bonjour 2")
print("bonjour 3")
print("bonjour 4")
print("bonjour 5")
'''

# Boucle while
count = 1
while count <= 5:
    print("bonjour", count)
    count += 1 # incrémentation de 1

count2 = 5
while count2 > 0:
    print("bye", count2)
    count2 -= 1 # décrémentation de 1


# Boucle for..in
# La fonction range(n) renvoie une liste (itérable) de n éléments
for n in range(5):
    print("coucou", n + 1)
    if n == 2: # sortie de boucle prématurée (break)
        break

