#!/bin/bash

# déclaration de fonctions
function hello() {
  echo "Hello World from function !"
}

function add() {
  # calcul de la somme des premiers arguments reçus par la fonction
  result=$(($1+$2))
  
  # affichage du résultat
  echo ${result}
}

function return_test() {
  # on ne peut pas retourner autre chose qu'une valeur numérique
  #return "test"

  # appel (imbriqué) à fonction
  add 41 3

  # return code de la fonction indiquant que l'exécution s'est bien déroulée
  return 0

}

function return_test_again() {
  echo "test"
}

# appels
hello
add 5 7
return_test

# capture de la sortie (echo) d'une fonction
capt=$(return_test_again)

echo ${capt}
