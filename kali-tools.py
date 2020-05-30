#!/usr/bin/python

import os
import time
import sys, traceback


if os.getuid() != 0:
	print "Sorry. This script requires sudo privledges"
	sys.exit()

print ('''
\033[1;91m
.%%..%%...%%%%...%%......%%%%%%..........................%%%%%%...%%%%....%%%%...%%.......%%%%..
.%%.%%...%%..%%..%%........%%..............................%%....%%..%%..%%..%%..%%......%%.....
.%%%%....%%%%%%..%%........%%............%%%%%%............%%....%%..%%..%%..%%..%%.......%%%%..
.%%.%%...%%..%%..%%........%%..............................%%....%%..%%..%%..%%..%%..........%%.
.%%..%%..%%..%%..%%%%%%..%%%%%%............................%%.....%%%%....%%%%...%%%%%%...%%%%..
................................................................................................\033[1;m
							 \033[1;34m Creator: Jeevan Chandra
							 \033[1;35m 100+ Tools  \033[1;m
	''')
def MainMenu():
	time.sleep(1)
	print("Please add and update the repository before installing	")
	time.sleep(1)
	print('''\033[1;91m
	
	
	
Note: Installing all the tools will consume 2 Gigs of data and 10+ gigs of Disk Space \033[1;m
	
	
	
	''')
	time.sleep(3)
	print('''\033[1;33m
HOUDY ROOT# 
 1.Add and update Repository
 2.Install Information gathering tools
 3.Install Vulnerability Analysis tools
 4.Install Web Applications tools
 5.Install Database Assessment tools
 6.Install Password Attacks tools
 7.Install Wireless Attacks tools
 8.Install Reverse Engineering tools
 9.Install Exploitation Tools 
 10.Install Sniffng and Spoofing tools
 11.Install Post Exploitation tools
 12.Install Forensics tools
 13.Install Mislinious tools
 14.Install Android Debugging Tools
 15.Install Hardware Hacking tools
 16.Install Kali-Menu
 17.Exit the tool
 
 00.Install All Kali-linux tools
	 \033[1;m''')

	selection = int (input("Enter Your Choice: "))
	
	if selection == 1:
		time.sleep(2)
		print("Getting the required key")
		time.sleep(2)
		cmd= os.system("wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add")
		time.sleep(2)
		cmd= os.system("echo '# Kali linux repositories | Added by kali-tools\ndeb https://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
		time.sleep(3)
		print("Repo Added Successfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		time.sleep(3)
		cmd= os.system("apt update")
		MainMenu()		
	
	elif selection == 2:
		print ('''\033[1;36m**************************** Install Information gathering tools *****************************\033[1;m''')
		cmd= os.system("apt install -y dnsenum dnsrecon fierce lbd wafw00f arping fping hping3 masscan nmap maltego theharvester netdiscover netmask enum4linux nbtscan smbmap swaks onesixtyone snmpcheck ssldump sslh sslscan sslyze dmitry ike-scan recon-ng" )
		print ("\033[1;36m*************************************************************************************************1\033[1;m ")
		MainMenu()
		
	elif selection == 3:
		print ('''\033[1;36m**************************** Installing Vulnerability Analysis tools *****************************\033[1;m''')
		cmd= os.system("apt install -y nikto openvas sqlmap yersinia spike voiphopper unix-privesc-check" )
		print ("\033[1;36m****************************************************************************************************1\033[1;m ")
		MainMenu()
	
	elif selection == 4:
		print ('''\033[1;36m**************************** Installing Web Applications tools *****************************\033[1;m''')
		cmd= os.system("apt install -y  burpsuite zaproxy dirb dirbuster jsql skipfish wfuzz wpscan skipfish cutycapt cadaver davtest whatweb commix" )
		print ("\033[1;36m**********************************************************************************************1\033[1;m ")
		MainMenu()
	
	elif selection == 5:
		print ('''\033[1;36m**************************** Installing Database Assessment tools *****************************\033[1;m''')
		cmd= os.system("apt install -y  sqlmap sqlitebrowser" )
		print ("\033[1;36m*************************************************************************************************1\033[1;m ")
		MainMenu()
	
	elif selection == 6:
		print ('''\033[1;36m**************************** Installing Password Attack tools *****************************\033[1;m''')
		cmd= os.system("apt install -y  hashcat hashid hash-identifier hydra medusa ncrack gpp-decrypt crunch cewl john johnny ophcrack chntpw samdump2 seclists rainbowcrack wordlists patator" )
		print ("\033[1;36m*********************************************************************************************1\033[1;m ")
		MainMenu()
	
	elif selection == 7:
		print ('''\033[1;36m**************************** Installing Wireless Attack tools *****************************\033[1;m''')
		cmd= os.system("apt install -y kismet wifite reaver bully" )
		print ("\033[1;36m*********************************************************************************************1\033[1;m ")
		MainMenu()
	
	elif selection == 8:
		print ('''\033[1;36m**************************** Installing Reverse Engineering tools *****************************\033[1;m''')
		cmd= os.system("apt install -y   binwalk volatility reaver radare2 clang yara")
		print ("\033[1;36m*********************************************************************************************1\033[1;m ")
		MainMenu()
		
	elif selection == 9:
		print ('''\033[1;36m**************************** Installing Exploitation tools *****************************\033[1;m''')
		cmd= os.system("apt install -y   armitage empire beef-xss nishang powersploit linux-exploit-suggester routersploit" )
		print ("\033[1;36m*********************************************************************************************1\033[1;m ")
		MainMenu()
		
	elif selection == 10:
		print ('''\033[1;36m**************************** Installing Sniffng and Spoofing tools *****************************\033[1;m''')
		cmd= os.system("apt install -y   mitmproxy responder wireshark netcat ncat ettercap-graphical dnschef netsniff-ng macchanger rebind sslsplit tcpreplay" )
		print ("\033[1;36m**************************************************************************************************1\033[1;m ")
		MainMenu()
		
	elif selection == 11:
		print ('''\033[1;36m**************************** Installing Post Exploitation tools *****************************\033[1;m''')
		cmd= os.system("apt install -y  dbd powersploit nishang sbd laudanum weevely proxychains" )
		print ("\033[1;36m***********************************************************************************************1\033[1;m ")
		MainMenu()
		
	elif selection == 12:
		print ('''\033[1;36m**************************** Installing Forensic tools *****************************\033[1;m''')
		cmd= os.system("apt install -y binwalk bulk-extractor hashdeep " )
		print ("\033[1;36m**************************************************************************************1\033[1;m ")
		MainMenu()
		
	elif selection == 13:
		print ('''\033[1;36m************************** Installing Mislinious tools *****************************\033[1;m''')
		cmd= os.system("apt install -y  crackmapexec bloodhound powershell mimikatz " )
		cmd= os.system("gem install evil-winrm")	
		print ("\033[1;36m**************************************************************************************1\033[1;m ")
		MainMenu()
		
	elif selection == 14:
		print ('''\033[1;36m**************************** Installing Android Debuggin tools *****************************\033[1;m''')
		cmd= os.system("apt install -y apktool dex2jar smali " )
		print ("\033[1;36m*********************************************************************************1\033[1;m ")
		MainMenu()
		
	elif selection == 15:
		print ('''\033[1;36m**************************** Installing Hardware Hacking tools *****************************\033[1;m''')
		cmd= os.system("apt install -y android-sdk apktool arduino dex2jar sakis3g smali " )
		print ("\033[1;36m*********************************************************************************1\033[1;m ")
		MainMenu()
		
	elif selection == 16:
		print ('''\033[1;36m**************************** Installing Kali Menu *****************************\033[1;m''')
		cmd= os.system("apt install -y  kali-menu " )
		print ("\033[1;36m*********************************************************************************1\033[1;m ")
		MainMenu()
		
	elif selection == 00:
		print ('''\033[1;36m**************************** Installing ALL KALI LINUX TOOLS *****************************\033[1;m''')
		
		print ('''\033[1;35m                                                                                                                  
|   |                             ,---.     ,---.,---.                                                            
|---|,---..    ,,---.    ,---.    |    ,---.|__. |__. ,---.,---.,---.,---.,---.,---.,---.,---.,---.,---.,---.,---.
|   |,---| \  / |---'    ,---|    |    |   ||    |    |---'|---'|---'|---'|---'|---'|---'|---'|---'|---'|---'|---'
`   '`---^  `'  `---'    `---^    `---'`---'`    `    `---'`---'`---'`---'`---'`---'`---'`---'`---'`---'`---'`---'
===================================This might takesome time=======================================================
		\033[1;m ''')
		print ('''\033[1;36m******************************************************************************************\033[1;m''')
		
		time.sleep(8)
		
		cmd= os.system("apt install -y  dnsenum dnsrecon fierce lbd wafw00f arping fping hping3 masscan nmap maltego theharvester netdiscover netmask enum4linux nbtscan smbmap swaks onesixtyone snmpcheck ssldump sslh sslscan sslyze dmitry ike-scan recon-ng nikto openvas sqlmap yersinia spike voiphopper unix-privesc-check burpsuite zaproxy dirb dirbuster jsql skipfish wfuzz wpscan skipfish cutycapt cadaver davtest whatweb commix sqlmap sqlitebrowser hashcat hashid hash-identifier hydra medusa ncrack gpp-decrypt crunch cewl john johnny ophcrack chntpw samdump2 patator kismet wifite reaver bully binwalk volatility reaver radare2 clang yara armitage empire routersploit beef-xss nishang powersploit linux-exploit-suggester mitmproxy responder wireshark netcat ncat ettercap-graphical dnschef netsniff-ng macchanger rebind sslsplit tcpreplay dbd powersploit nishang sbd laudanum weevely proxychains binwalk bulk-extractor hashdeep crackmapexec bloodhound powershell mimikatz apktool dex2jar smali android-sdk apktool arduino dex2jar sakis3g seclists rainbowcrack wordlists  " )

		print ("\033[1;36m********************************************************************************************\033[1;m ")
		print ('''\033[1;32m
   ___     _  _      __       __       ___      ___      ___   
  (_-<    | +| |    / _|     / _|     / -_)    (_-<     (_-<   
  /__/_    \_,_|    \__|_    \__|_    \___|    /__/_    /__/_  
_|"""""| _|"""""| _|"""""| _|"""""| _|"""""| _|"""""| _|"""""| 
"`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' 
			\033[1;m''')
		print ("\033[1;36m********************************************************************************************\033[1;m ")
		MainMenu()	
			
			
	if selection == 17:
		print ("\033[1;33mBYE BYE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[1;m ")
		exit()
		
MainMenu()

