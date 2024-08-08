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

######## MAIN SELECTION MENU FOR EACH CALCULATION VARIANT ########

echo -e ${CYAN}"${TAB4}    NXT PROBABILITY CALCULATOR\n${GREEN}" 
echo -e ${REVERSE}"${TAB4}\tSELECT AN OPTION:\n${NONE}${RED}${BOLD}"

option=("Dumpsters" "Recycling Center" "Treasure Maps" "Weed" "Drug Precursor Harvesting" "Exit")

select opt in "${option[@]}"
do
    case $opt in
    
    "Dumpsters")
        clear

        option2=("Item List" "Personal Item Tracking" "Probability Calculator" "Main Menu" "Debugging")
        select opt2 in "${option2[@]}"
        do
            case $opt2 in
            "Item List")
                clear
                echo -e "TEST"

            ;;

            "Personal Item Tracking")
                clear
                echo -e "${TAB3}${BLINK}STARTING DUMPSTER TRACKER${NONE}"
                sleep 2
                clear
                echo -e "${CYAN}${REVERSE}DUMPSTER LOOT TRACKER\n${NONE}${GREEN}"
                sudo python3 python/dumpsters.py
            ;;

            "Probability Calculator")
            
            ;;
            
            "Main Menu")
                clear
                cd extras
                sh ./out.sh
                
            ;;

            "Debugging")
            echo -e "${HIDDEN}"
            pwd
            echo -e "${UNDERLINE}\nIF CAT MAIN.SH WORKS, IT'LL BE BELOW THIS TEXT${NONE}${GREEN}"
            
            sleep 2
            #cd ..
            cat 'main.sh' | grep "#PASS" | cut -d " " -f 4
            #cat main.sh
            ;;
            esac
        done

        python3 dumpsters.py
    ;;

    "Recycling Center")
    
    ;;

    "Treasure Maps")
    clear
    echo -e "${TAB3}${BLINK}STARTING TREASURE MAP TRACKER${NONE}"
    sleep 2
    clear
    echo -e "${CYAN}${REVERSE}TREASURE MAP LOOT TRACKER\n${NONE}${GREEN}"
    sudo python3 python/treasures.py
    ;;

    "Weed")
    #### TO BE FILLED IN ####
    ;;

    "Drug Precursor Harvesting")
    #### TO BE FILLED IN ####
    ;;

    "Exit")
        clear
        exit 0
    ;;
    *) echo "Invalid Option $REPLY";;
    esac
done
exit 0



#PASS