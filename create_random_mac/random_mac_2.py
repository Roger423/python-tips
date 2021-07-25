#! python3

import random, sys

def Gen_random_mac():
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
    return mac

if len(sys.argv) != 2:
    print("Arguments Err!")
    print("Usage: python3 random_mac_2.py mac_number")
else:
    mac_num = int(sys.argv[1])

mac_file = open('random_mac_list.txt', 'w')

try:
    for i in range(mac_num):
        mac_file.write(Gen_random_mac())
        mac_file.write('\n')
except:
    pass

mac_file.close()