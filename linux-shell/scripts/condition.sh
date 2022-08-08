#!/bin/bash

# équivalent à [[ 2 -gt 1 ]]
if [[ 2 > 1 ]]
then
  echo "Deux est strictement supérieur à un"
fi

# équivant à [[ 1 -eq 1 ]]
if [[ 1 == 1 ]]
then
  echo "1 à équal à 1" 
fi

if [[ -v ${name} ]]
then
  echo "Valeur de la variable name: ${name}"
else
  echo "La variable name n'existe pas"
fi

v1="Chris"
v2="Chris"

if [[ ${v1} == ${v2} ]]
then
  echo "Les chaînes sont identiques"
else
  echo "Les chaînes sont différentes"
fi


path="/var/www/html"
if [[ -a ${path} ]]
then
  echo "Le chemin existe"
else
  echo "Le chemin n'existe pas"
fi

if [[ -d ${path} ]]
then 
  echo "${path} est un dossier"
else
  echo "${path} n'est pas un dossier"
fi
