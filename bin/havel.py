#!/usr/bin/env python3
from os import system as sh

print("▄  █ ██       ▄   ▄███▄   █      ▄▄▄▄▄         ▄ ▄   ▄███▄   ███        ▄  █ ██   █▀▄▀█ █▀▄▀█ ▄███▄   █▄▄▄▄ ")
print("█   █ █ █       █  █▀   ▀  █     █     ▀▄      █   █  █▀   ▀  █  █      █   █ █ █  █ █ █ █ █ █ █▀   ▀  █  ▄▀ ")
print("██▀▀█ █▄▄█ █     █ ██▄▄    █   ▄  ▀▀▀▀▄       █ ▄   █ ██▄▄    █ ▀ ▄     ██▀▀█ █▄▄█ █ ▄ █ █ ▄ █ ██▄▄    █▀▀▌  ")
print("█   █ █  █  █    █ █▄   ▄▀ ███▄ ▀▄▄▄▄▀        █  █  █ █▄   ▄▀ █  ▄▀     █   █ █  █ █   █ █   █ █▄   ▄▀ █  █  ")
print("   █     █   █  █  ▀███▀       ▀               █ █ █  ▀███▀   ███          █     █    █     █  ▀███▀     █   ")
print("  ▀     █     █▐                                ▀ ▀                       ▀     █    ▀     ▀            ▀    ")
print("       ▀      ▐                                                                ▀                             ")

while True:
    print("\n>: Equip Havel's Hammer?\n")
    ui = input('')
    if ui == "NO" or ui == "no":
        print('\n>: Bonfire Has Been Lit\n')
        break
    elif ui == "YES" or ui == "yes":
        a = sh('echo "Website" && read target && echo "Campaign" && read campaign && gobuster dir --url $target --wordlist ~/.havel/dict/common.txt --output ~/.havel/logs/$campaign > /dev/null 2>&1')
        b = print("\n>: Target Smashed\n")
    else:
        print("\n>: ... \n")