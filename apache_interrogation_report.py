import Pubsy
import datetime
pup = Pubsy.Pub()
IPADDRESS = raw_input("Enter IP Address For Automated Apache Assessment: ")
pup.store_new_report("Apache Server Interrogation Report v1.0-" + IPADDRESS)
pup.pub_subheader("Apache Web Server Interrogation Report v1.0- "+IPADDRESS)
pup.pub_header("http://"+IPADDRESS)
#TCP/80 Adversarial Enumeration Runbook

now = datetime.datetime.now()
now.strftime("%Y-%m-%d %H:%M")
reportDetails = ""
reportDetails += "Security System Assessment Report v1.0\n"
reportDetails += "Date: " #, now.strftime("%Y-%m-%d_%H-%M")
reportDetails += "System: "+IPADDRESS+"\n"

pup.store_textbox(reportDetails)

# Identify the Platform
pup.pub_subheader("Web Service Identification")
pup.store_command("whatweb http://" + IPADDRESS)

# Dirbuster Apache Files
pup.pub_subheader("Apache Directory Brute Force Attack")
pup.store_command("dirb http://" + IPADDRESS + " /opt/SecLists/Discovery/Web-Content/apache.txt")

# msf apache scans
pup.pub_subheader("nMap SMB/RPC/DCOM Interrogation Report")
pup.store_command("nmap --debug -n -vv -Pn -sV " + IPADDRESS + " -pT:139,445,U:137 --script='smb-vuln-*' | tee ")

# Dirbuster Apache Files
pup.pub_subheader("Apache Directory Brute Force Attack")
pup.store_command("dirb http://" + IPADDRESS + " /opt/SecLists/Discovery/Web-Content/apache.txt")

# nikto apache stuff
pup.pub_subheader("Web Server Vulnerability Analysis")
pub.store_command("nikto -h http://" + IPADDRESS)



pup.save_report()
