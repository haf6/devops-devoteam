#!/bin/bash

# déclaration et initialisation d'une variable tableau (3 chaînes)
fruits=("fraise" "abricot" "banane")

# affichage du premier fruit
echo "Premier fruit: ${fruits[0]}"

# le dernier
echo "Dernier fruit:" ${fruits[2]}

# ajout (append, à la fin) d'un fruit
fruits+=("poire")

# affichage du dernier fruit
echo "Dernier fruit: ${fruits[-1]}"

# affichage de tous les fruits
echo "Tous les fruits: " ${fruits[@]}
