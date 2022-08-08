#!/bin/bash

<<INFO
Author: Christophe DUFOUR
Tip: to delete user account with home dir => sudo userdel -f -r $NEW_USER
INFO

E_NOARG=50
NEW_USER=$1

if [ -z ${NEW_USER} ]; then
  echo "[-] You must provide a user name"
  exit ${E_NOARG}
fi

# create user
useradd 1>/dev/null 2>&1 -d "/home/$NEW_USER" $NEW_USER
echo "[+] User $NEW_USER added"

# download files
FILE="tp3-files.zip"
URL="https://github.com/cdufour/devops-devoteam/raw/master/linux-shell/tps/tp3/$FILE"
curl -sL -o /tmp/${FILE} ${URL}
echo "[+] zip file $FILE downloaded in /tmp dir"

# unzip in user home dir (-o, --overwrite)
unzip 1>/dev/null -o /tmp/${FILE} -d /home/${NEW_USER}
echo "[+] File ${FILE} unzipped in /home/${NEW_USER}"

# change files owner
chown -R ${NEW_USER}:${NEW_USER} /home/${NEW_USER}/tp3-files
echo "[+] Ownership updated"

# update user.html
sed -i "s/USER/${NEW_USER}/gi" /home/${NEW_USER}/tp3-files/user.html
echo "[+] user.html file updated"

# copy user.html to /var/www/html (-p, preserve mode for perms)
cp -p /home/${NEW_USER}/tp3-files/user.html /var/www/html/user-${NEW_USER}.html
echo "[+] user.html copied to /var/www/html/user-${NEW_USER}.html"
