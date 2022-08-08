#!/bin/bash

count=1

read -p "Donne ton nom: " name

while [[ -z ${name} ]]
do

  # cassage de la boucle si nom pas saisi après 5 demandes
  if [[ ${count} -gt 5 ]]
  then
    break
  fi


  ((count++))
  echo "Tu n'as rien saisi !"
  read -p "Ton nom please ! " name
done

#echo "count: ${count}"

if ! [[ -z ${name} ]]
then 
  echo "Salut ${name}, labesse ?"
fi



