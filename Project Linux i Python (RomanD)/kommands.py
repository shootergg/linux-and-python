#! /usr/bin/env python

# Zadanie Nr.1 ustalenie adresu IP
from scapy.all import *
from netaddr import *

""" Ustalenie adresu ip"""

ip = get_if_addr(conf.iface)
ip = get_if_addr("eth0")
ip
print("AdressIP")
print(ip)

# x = os.system("ip route show | awk '/eth0.*scope/ {print $1}'") link interaktywny

print("-----------------------------------")
# zadanie 2 "ustalenie maski podsieci

#Zadanie Nr.2 Ustalenie maski podsieci
y = IPNetwork('192.168.1.0/24')
# y.netmask
#Wyszukiwanie maski podsieci
print("netmask:") #
print(y.netmask)

# print("Adress ip to :")
# print(os.system("ip a s eth0 | egrep -o 'inet [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | cut -d' ' -f4"))

# name = os.system('uname -a')


# os.system('nmap -sV y.netmask ')






