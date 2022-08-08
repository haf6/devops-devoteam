#!/bin/bash
# idelete: supprime un fichier par son inode (id de noeud)

ARGCOUNT=1
E_WRONGARGS=70
E_FILE_NOT_EXIST=71
E_CHANGED_MIND=72

if [ $# -ne "$ARGCOUNT" ]
then
  echo "Mauvais nombre d'arguments"
  exit $E_WRONGARGS
fi

if [ ! -e "$1" ]
then
  echo "Le fichier n'existe pas"
  exit $E_FILE_NOT_EXIST
fi

inum=`ls -i | grep "$1" | awk '{print $1}'`

echo; echo -n "Sûr de vouloir supprimer ce fichier ? (y/n) "

read answer
case "$answer" in 
  [nN])
    echo "Ok, tu as changé d'avis"
    exit E_CHANGED_MIND
    ;;
esac

find . -inum $inum -exec rm {} \;

echo "Fichier supprimé !"

ls

exit 0 
