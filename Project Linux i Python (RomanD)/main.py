from scapy.all import *
#Zadanie Nr.3 Na podstawie powyższych informacji ustalenie adresow IP innych aktywnych hostów w
# tej samej sieci
target_ip = "192.168.1.1/24"
# wyszukiwanie adresow ip
arp = ARP(pdst=target_ip)
# tworzenie broadkast pakietu

ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp
result = srp(packet, timeout=3, verbose=0)[0]
# lista klientow
clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})
# printujemy clientow
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))