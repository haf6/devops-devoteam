#!/bin/bash

# script affichant la table d'un nombre fourni en argument de ligne de cmd
# à condition que ce nombre soit compris entre 1 et 1000"

input=$1

if [[ ${input} -le 0 || ${input} -gt 1000 ]]
then
  echo "Le nombre doit être compris entre 1 et 1000"
  
  # sortie du script (suite du code non exécuté)
  exit
fi


echo "*** Table des ${input} ***"

for n in {0..10}
do
  echo "${input} x ${n} = $((${input} * ${n}))"
done

echo "*------------------------*"
