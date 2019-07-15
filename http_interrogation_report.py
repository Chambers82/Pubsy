import time
import Pubsy
import datetime
import warnings
warnings.filterwarnings("ignore")

pup = Pubsy.Pub()

IPADDRESS = raw_input("Enter IP Address For Automated HTTP Assessment: ")
PORT = raw_input("Enter Service Port: ")
pup.store_new_report("HTTP Server Interrogation Report v1.0-" + IPADDRESS+":"+PORT)
pup.pub_subheader("HTTP Web Server Interrogation Report v1.0- "+IPADDRESS+":"+PORT)
pup.pub_header("http://"+IPADDRESS)
#TCP/80 Adversarial Enumeration Runbook

ts = time.time()
stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
reportDetails = ""
reportDetails += "Security System Assessment Report v1.0"
reportDetails += ("Date: \n " + stamp)
reportDetails += "System: "+IPADDRESS+"\n"

pup.store_textbox(reportDetails)

# Dirbuster Apache Files
print("[!] Running Dirbuster with SecLists apache.txt discovery file")
pup.pub_subheader("Apache Directory Brute Force Attack")
pup.store_command("dirb http://" + IPADDRESS +":"+PORT+ " /usr/share/wordlists/dirb/h_custom_small.txt | tee ")
print("[*] Complete.")

# msf apache scans
print("[!] Running Nmap HTTP Vulnerability Assessment using all HTTP-VULN NSE Scripts")
pup.pub_subheader("nMap HTTP Service Interrogation Report")
pup.store_command("nmap --debug -n -vv -Pn -sV " + IPADDRESS+" -pT:"+PORT+" --script='http-vuln-*' | tee ")
print("[*] Complete.")

# nikto apache stuff
print("[!] Running Nikto Web Vulnerabillity Scanner on the Target")
pup.pub_subheader("Web Server Vulnerability Analysis")
pup.store_command("nikto -h http://" + IPADDRESS+":"+PORT + " |tee ")
print("[*] Complete.")

pup.save_report()
