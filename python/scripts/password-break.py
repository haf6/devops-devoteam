GOOD_PASSWORD = "password"
LIMIT = 3
numAttempts = 0
userInput = ""

while True:
    userInput = input("Votre mot de passe:")
    numAttempts += 1

    if userInput == GOOD_PASSWORD:
        print("Connecté, après %d tentatives" % numAttempts)
        break

    if numAttempts >= LIMIT:
        print("Compte bloqué, après %d tentatives" % numAttempts)
        break