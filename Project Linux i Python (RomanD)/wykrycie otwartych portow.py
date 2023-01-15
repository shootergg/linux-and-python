import os
#Zadanie Nr.4Ustalenie otwartych portow na wszystkich znalezionych hostach
#Zadanie Nr.5  Ustalenie nazwę oraz wersję oprogramowania dla wszystkich usług na wszystkich hostach
"""Skanowanie wszsystkich otwartych portow"""
os.system('nmap -sV 192.168.1.108')