colors = [] # liste vide
print(colors)

colors.append('vert')
print(colors)

colors.append('blanc')
print(colors)

colors.append('rouge')
print(colors)

colors.clear() # invocation de la méthode "clear" supprimant tous les éléments de la liste
print(colors)

colors.append('vert')
print(colors)

colors.append('blanc')
print(colors)

colors.append('rouge')
print(colors)

colors[0] = 'bleu'
print(colors)

colors.remove('blanc')
print(colors)