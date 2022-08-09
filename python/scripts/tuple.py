#t = () # tuple vide
#print(type(t))

coordsGps = (45.9632, 21.7891)
print(coordsGps)
print("Latitude:", coordsGps[0])
print("Longitude:", coordsGps[1])

# non permis sur un tuple
#coordsGps[0] = 46.3322

# pas possible, "AttributeError"
#coordsGps.append(89.2658)

lat, lng = coordsGps # tuple unpacked
print(lat, lng)
lat = 30.6954
print(lat)
print(coordsGps)

for c in coordsGps:
    print(c)

client = ("Bob", "Ba", "Toulouse", "développeur")
fname, lname, city, job = client
print(fname, "occupe le poste de ", job)

listCoords = [
    (48.85, 2.34),
    (48.22, 3.34),
    (50.85, 7.20)
]

# itération sur la liste de tuples avec "unpackaging"
for c in listCoords:
    lat, lng = c
    print("Latitude:", lat, "Longitude:", lng)


