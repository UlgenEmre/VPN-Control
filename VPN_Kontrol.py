#!/usr/bin/env python
# *-* coding: utf-8 *-*

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VPN CONTROL")

print("""
VPN CONTROL 

""")

hedefip = raw_input("Enter Destination ip")

os.system("ike-scan " + hedefip )	

print("Transaction Completed Successfully")


