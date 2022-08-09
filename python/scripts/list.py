# liste de 3 entiers
numbers = [23,140,6]
print(type(numbers))

for n in numbers:
    print(n)

first = numbers[0]
computedIndex = 1 + 1
print(numbers[computedIndex])

index = 0
while index < 3:
    print(numbers[index])
    index += 1

title = "Les Trois Mousquetaires"
# print(title[4])
# for c in title:
#     print(c)
acc = 0 # variable accumulateur
search = "s"
for c in title:
    if c == search:
        acc += 1

print("Le caractère %s a été trouvé %d fois dans le titre %s"
    % (search, acc, title))