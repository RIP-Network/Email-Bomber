#!/bin/bash

red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

echo "Instalando requisitos esto puede tardar un poco..."

ping -c 1 google.com > /dev/null 2>&1
if [[ "$?" == 0 ]]; then
echo ""
echo -e "$green[✔][Internet Connection]............[ OK ]"
sleep 1.5
else
echo ""
echo -e $red"[!][Internet Connection].........[ NOT FOUND ]"
echo ""
exit
fi

clear
pip3 install -r requeriments.txt
apt-get update
apt-get upgrade
clear

echo -e $green
echo -e "╔───────────────────────────╗"
echo -e "|[✔] Instalacion completada |"
echo -e "┖───────────────────────────┙"
sleep 4
python2 Bomb.py
