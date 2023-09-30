#!/bin/bash

OSTEMP="$(mktemp)"
hostnamectl >> $OSTEMP
APT="$(cat $OSTEMP | grep 'Ubuntu\|Kali' | wc -l)"
DNF="$(cat $OSTEMP | grep 'Fedora\|CentOS\|RHEL' | wc -l)" 

if [ $APT -eq 1 ] ; then
APT_NMAP="$(sudo apt-get install gobuster -y)"
    $APT_NMAP
    mkdir ~/.obc
    git clone -b stable --single-branch https://github.com/OozeSec/Havel.git ~/.havel
    echo "alias havel='python3 ~/.havel/bin/havel.py'" >> ~/.bashrc && source ~/.bashrc
    echo "Havel configured- type havel to use."
elif [ $DNF -eq 1 ] ; then
DNF_NMAP='sudo dnf install gobuster -y'
    $DNF_NMAP
    mkdir ~/.obc
    git clone -b stable --single-branch https://github.com/OozeSec/Havel.git ~/.havel
    echo "alias havel='python3 ~/.havel/bin/havel.py'" >> ~/.bashrc && source ~/.bashrc
    echo "Havel configured- type havel to use."
fi