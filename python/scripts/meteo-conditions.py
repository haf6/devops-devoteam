temperature = 32

'''
if temperature < -20:
    print("Glacial")

if temperature < -10:
    print("Très froid")

if temperature < 0:
    print("Froid")

if temperature < 10:
    print("Doux")
'''

if temperature < -20:
    print("Glacial")
elif temperature < -10:
    print("Très froid")
elif temperature < 0:
    print("Froid")
elif temperature < 10:
    print("Doux")
elif temperature < 20:
    print("Chaud")
elif temperature < 30:
    print("Très chaud")
else:
    print("Situation climatique inquiétante")