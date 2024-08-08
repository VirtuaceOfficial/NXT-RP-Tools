#!/bin/bash

clear

PATH=/bin:/usr/bin:

### TEXT EFFECTS ###

NONE='\033[00m'
RED='\033[01;31m'
GREEN='\033[01;32m'
YELLOW='\033[01;33m'
PURPLE='\033[01;35m'
CYAN='\033[01;36m'
WHITE='\033[01;37m'
BOLD='\033[1m'
UNDERLINE='\033[4m'
BLINK='\e[5m'
REVERSE='\e[7m'
HIDDEN='\e[8m'

######## OTHER SHIT ########

TAB3='\t\t\t'
TAB4='\t\t\t\t'

######## MAIN SCRIPT ########

echo "RETURNING"
sleep 3
cd ..
sh ./main.sh
