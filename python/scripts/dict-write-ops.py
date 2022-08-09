student1 = {
    "age": 18,
    "lname": "PASCAL",
    "fname": "Blaise",
    "email": "b.pascal@edu.fr"
}
print(student1)

# ajout d'une clé/valeur
student1["notes"] = [14,6,20]
print(student1)

# modification d'une valeur associée à la clé ciblée
student1["age"] = 20
print(student1)

# modification multi-clés
student1.update({"age":22, "email": ""})
print(student1)

# suppression d'une clé
student1.pop('email')
print(student1)

# itération sur les valeurs du dict uniquement
for v in student1.values():
    print(v)

# itération avec "unpacking" des tuples renvoyés par la méthode items()
for k,v in student1.items():
    print(k, v)


