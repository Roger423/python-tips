#The purpose of this script is to generate a random MAC address

import random

mac_al = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
mac_al_2 = ['0', '2', '4', '6', '8', 'A', 'C', 'E']
mac_ls = []

for i in range(6):
    if i == 0:
        mac_se = random.choice(mac_al) + random.choice(mac_al_2)
    else:
        mac_se = random.choice(mac_al) + random.choice(mac_al)
    mac_ls.append(mac_se)

mac = ':'.join(mac_ls)
print("---" * 20)
print("The random MAC address generated is : " + mac)
