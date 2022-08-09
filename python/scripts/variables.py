
# variables primitives en Python
training = "Initiation à Python"
temperature = 15
pi = 3.14
isEarthRound = True

# affiche les types des variables (valeurs associées)
print(type(training))
print(type(temperature))
print(type(pi))
print(type(isEarthRound))

'''
# Block comment
print(2+2)
print(training)
training = "Perfectionnement à Python"
print(training)
'''

# Opérations sur les variables
print(temperature + 10) # addition entre deux entiers
print(training + "10") # concaténation entre deux chaînes
print(pi + 10) # addition entre un flotant et un entier
print(isEarthRound + 10) # addition entre un booléen et un entier. Conversion implice True => 1

print("Le double de pi est: " + str(pi * 2))

doublePi = pi * 2 # stockage en variable du retour de l'expression
print(type(doublePi)) # class float
doublePiStr = str(doublePi)
print(type(doublePiStr)) # class str
print("Le double de pi est:", doublePiStr)

