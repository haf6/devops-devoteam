postCodes = [
   67200, 75012, 68520, 15000, 75020, 
   67200, 75012, 68520, 15000, 75020, 
   67275, 75013, 68520, 17750, 75020, 
   75007, 75012, 75520, 15000, 75020
]

# Combien de parisiens ?
# 1. variable d'accumlation
# 2. parcourir la liste
# 3. recherche tout ce qui commence par 75
# 4. incrémenter l'accu quand un parisien est trouvé

numParis = 0 # accu
for postCode in postCodes:
    # Meilleure approche: on travaille directement avec des valeurs numériques
    # if postCode >= 75000 and postCode <= 75999:
    #     numParis += 1

    # Approche par "commence par" (conversion int => str)
    postCodeStr = str(postCode)
    #dpt = postCodeStr[0] + postCodeStr[1]
    dpt = postCodeStr[:2] # équivalent par "slicing". Slice des 2 premiers caractères
    if dpt == "75":
        numParis += 1

print("Nombre de codes postaux parisiens trouvés:", numParis)

# Autre exemple de slicing
# Affichage des 3 derniers codes postaux de la liste initiale
print(postCodes[-3:])

for p in postCodes[-3:]:
    print(p)
