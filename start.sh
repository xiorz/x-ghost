#!/bin/bash

# Warna
hijau="\e[32m"
merah="\e[31m"
kuning="\e[33m"
biru="\e[34m"
cyan="\e[36m"
tebal="\e[1m"
miring="\e[2m"
reset="\e[0m"

# Menonaktifkan CTRL + Z dan menangani CTRL + C
trap '' SIGTSTP
trap 'echo -e "\n${merah}${tebal}${miring}Udah gw kasih menu keluar, masih aja CTRL+C? 😑\n"; exit 1' SIGINT

# Fungsi banner
banner() {
    clear
    chafa -s 55 jangan-dihapus.png
}

# Efek loading
loading() {
    echo -ne "${cyan}${miring}Loading"
    for i in {1..3}; do
        sleep 0.5
        echo -ne "${kuning}."
    done
    sleep 0.5
    echo -e "\n"
}

# Menu interaktif
while true; do
    banner
    echo -e "${biru}${tebal}Menu"
    echo -e "${merah}${tebal}------------------------------"
    echo -e "${merah}[ 1 ]${reset} ENCRYPT PYTHON"
    echo -e "${merah}[ 2 ]${reset} USER-AGENT GENERATOR"
    echo -e "${merah}[ 3 ]${reset} WEBSITE TOOLS"
    echo -e "${merah}[ 4 ]${reset} PEMBUAT NIK PALSU"
    echo -e "${merah}[ 5 ]${reset} ENCRYPT PYTHON V2"
    echo -e "${merah}[ 6 ]${reset} Deface Website ASIK"
    echo -e "${merah}[ 7 ]${reset} INFORMASI PERANGKAT SAYA (ERROR)"
    echo -e "${merah}[ 8 ]${reset} DOWNLOAD LAGU YOUTUBE"
    echo -e "${merah}[ 9 ]${reset} ENC BASH"
    echo -e "${merah}[ 10 ]${reset} OSINT NOMOR HP"
    echo -e "${merah}[ 11 ]${reset} OSINT NIK"
    echo -e "${merah}[ 12 ]${reset} INSTALL BAHAN"
    echo -e "${kuning}[ 0 ]${reset} Keluar"
    
    echo -ne "${hijau}${tebal}>> ${hijau}"
    read pilihan
    
    case $pilihan in
        1) loading; python x/e.py ;;
        2) loading; python x/u.py ;;
        3) loading; python x/a.py ;;
        4) loading; python x/nik.py ;;
        5) loading; python x/ku.py ;;
        6) loading; python x/def.py ;;
        7) loading; python x/d.py ;;
        8) loading; python x/mp3.py ;;
        9) loading; python x/esh.py ;;
        10) loading; python x/pn.py_E.py ;;
        11) loading; python x/onik.py_E.py ;;
        12) loading; bash install ;;
        0) clear; echo -e "\n${biru}${tebal}Byee...! ${cyan}\n"; exit 0 ;;
        *) echo -e "${kuning}\n${cyan}[ ${merah}! ${cyan}] ${kuning}${tebal}Pilihan tidak valid, coba lagi!\n"; sleep 1 ;;
    esac
done
