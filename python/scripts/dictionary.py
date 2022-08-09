def getAverage(notes):
    s = 0 # accu des notes
    for note in notes:
        s += note
    return round(s / len(notes), 2)

# test isolé
#print(getAverage([7,5,12.5]))
    


d = {} # dict vide

student1 = {
    "age": 18,
    "lname": "PASCAL",
    "fname": "Blaise",
    "email": "b.pascal@edu.fr",
    "isGoodLearner": True,
    "notes": [17, 12, 19.5]
}

student2 = {
    "age": 23,
    "lname": "DEL PIERO",
    "fname": "Alessandro",
    "email": "a.delpiero@juve.int",
    "isGoodLearner": False,
    "notes": [10, 10, 10]
}

student3 = {
    "age": 58,
    "lname": "TOURGUE",
    "fname": "Ivan",
    "email": "i.tourgue@edu.ru",
    "isGoodLearner": True,
    "notes": [19, 7.5, 2.5]
}

# affiche la première note obtenue par student1
print(student1["notes"][0])

for k in student1:
    print(k, "=>", student1[k])


# liste de dict
students = [student1, student2, student3]

evaluation = "bon"
for s in students:
    if not s["isGoodLearner"]:
        evaluation = "mauvais"
    else:
        evaluation = "bon"

    print("%s est un %s étudiant" % (s["fname"], evaluation))
    print("Moyenne de ses notes:", getAverage(s["notes"]))

