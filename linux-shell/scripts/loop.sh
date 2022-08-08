#!/bin/bash

#fruits="pêche, pomme, poire, abricot"
fruits=("pêche" "pomme" "poire" "abricot")

# itère sour l'ensemble des éléments du tableau fruits
for fruit in ${fruits[@]}
do
  echo "Fruit: ${fruit}"
done

for n in {1..10}
do
  echo "n vaut ${n}"
done


counter=1
while [[ ${counter} -le 10 ]]
do
  echo "counter vaut ${counter}"
  
  # incrémentation de la variable (pour éviter boucle infinie)
  ((counter++))
done


