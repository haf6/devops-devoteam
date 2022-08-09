GOOD_PASSWORD = "password"
LIMIT = 3
numAttempts = 0
userInput = ""

# boucle tant que mot de passe incorrect

while userInput != GOOD_PASSWORD and numAttempts < LIMIT:
    userInput = input("Votre mot de passe:")
    numAttempts += 1 # incr du nb de tentatives
    print("Nombre de tentatives:", numAttempts)


# le code suivant est exécuté uniqument après la sortie de boucle
if userInput != GOOD_PASSWORD:
    print(LIMIT, "mauvaises saisies, compte bloqué")
else:
    print("Connecté")
