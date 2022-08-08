#!/bin/bash

read -p "Donne-moi ton âge: " age

if [[ -z ${age} ]]
then
  echo "Tu n'as rien saisi !"
else
  echo "Ton age dans 10 ans:" $((${age} + 10)) " ans"
fi
