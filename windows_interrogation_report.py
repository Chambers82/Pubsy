import Pubsy
import datetime
import warnings
warnings.filterwarnings("ignore")

pup = Pubsy.Pub()

IPADDRESS = raw_input("Enter IP Address For Automated Windows Security Assessment: ")
pup.store_new_report("Windows System Interrogation Report_" + IPADDRESS)
pup.pub_subheader("Windows System Interrogation Report v1.0 "+IPADDRESS)
now = datetime.datetime.now()
stamp = now.ctime()
reportDetails = ""
reportDetails += "Security System Assessment Report v1.0\n"
reportDetails += "Date: \n"
reportDetails += "System: "+ IPADDRESS + "\n"
pup.store_textbox(reportDetails)

pup.pub_header("")
pup.pub_header("Windows System: "+IPADDRESS)
#TCP/80 Adversarial Enumeration Runbook



# Identify the Platform
#pup.pub_subheader("Web Service Identification")
#pup.store_command("whatweb http://" + IPADDRESS)

print("\n[+] Running Common SMB Vulnerability Check...")
pup.pub_subheader("Common SMB Vulnerability Check")
pup.store_command("nmap -p135,139,445 --script=\'smb-vuln-*\' " + IPADDRESS)
print("Complete.")

print("\n[+] Running Common SMB Protocol Check...")
pup.pub_subheader("Common SMB Protocol Check")
pup.store_command("nmap -p445 --script smb-protocols " + IPADDRESS)
print("Complete.")

print("\n[+] Running General Windows Enumeration...")
pup.pub_subheader("General Windows Enumeration")
pup.store_command("enum4linux -a " + IPADDRESS)
print("Complete")

#pup.store_command("rpcclient -U " + IPADDRESS)
pup.save_report()
