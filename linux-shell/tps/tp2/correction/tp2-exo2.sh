#!/bin/bash

<<INFO
Author: Christophe DUFOUR
INFO

# get first line command arg
URL=$1

# capture piped commands output un status variable
status=`curl -Is ${URL} | head -n1 | cut -d" " -f2`

# capture date command output
date=$(date)

# display with tab separator to screen and file (append) with tee command
echo -e "${date}\t${URL}\t${status}" | tee -a check.log