import time
import Pubsy
import datetime
import warnings
warnings.filterwarnings("ignore")

pup = Pubsy.Pub()

IPADDRESS = raw_input("Enter IP Address For SSL Endpoint Assessment: ")
PORT = raw_input("Enter Service Port: ")
pup.store_new_report("SSL Endpoint Assessment Report v1.0-" + IPADDRESS+":"+PORT)


# Generate Common File Header
pup.pub_header("Host: "+IPADDRESS)
ts = time.time()
stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
date_string = "Date: " + stamp + "\n"
reportDetails = ""
reportDetails += "Deliverable: SSL Endpoint System Assessment Report v1.0\n"
reportDetails += date_string
reportDetails += "Target Endpoint: "+IPADDRESS+":"+PORT+"\n"
reportDetails += "Initiated by: Brent Chambers\n"
pup.store_paragraph(reportDetails)

# Report Summary
pup.pub_subheader("SSL Endpoint Assessment Report v1.0- "+IPADDRESS+":"+PORT)
pup.store_paragraph("The Secure Sockets Layer (SSL) and the Transport Layer Security (TLS) cryptographic protocols have had their share of flaws like every other technology. The following are major vulnerabilities in TLS/SSL protocols. They all affect older versions of the protocol (TLSv1.2 and older). At the time of publication, only one major vulnerability was found that affects TLS 1.3. However, like many other attacks listed here, this vulnerability is also based on a forced downgrade attack.")

# Details


# SSL Scanner
print("\n[!] Running SSL Cipher Scan Assessmeent")

pup.pub_subheader("SSL Cipher Scan Assessmeent")
pup.store_paragraph("SSL Cipher scans rule!")
#pup.store_command("tlssled " + IPADDRESS + " " + PORT)
pup.store_command("nmap -sV --script ssl-enum-ciphers -p "+PORT+" "+IPADDRESS)
#pup.store_command("sslscan --verbose " + IPADDRESS +":"+PORT)

print("\n[!] Assessing Vulnerability to HeartBleed...")
pup.pub_subheader("Heartbleed Assesssment")
pup.store_paragraph("Heartbleed was a critical vulnerability that was found in the heartbeat extension of the popular OpenSSL library. This extension is used to keep a connection alive as long as both parties are still there. The Heartbleed vulnerability is registered in the NIST NVD database as CVE-2014-0160.")
pup.store_command("nmap -sV --script ssl-heartbleed.nse -p "+PORT+" "+IPADDRESS)

 
print("\n[!] Checking SSL Date and Expiry...")
pup.pub_subheader("SSL Date and Expiry")
pup.store_command("nmap -sV --script ssl-date.nse -p"+PORT+" "+IPADDRESS)
           

print("\n[!] Copying SSL Certificatee for Review...")
pup.pub_subheader("SSL Certificate")
pup.store_command("nmap -sV --script ssl-cert.nse -p"+PORT+" "+IPADDRESS)

       
#ssl-ccs-injection.nse     

print("\n[!] Assessing Vulnerability to SSLv2 DROWN...")
pup.pub_subheader("SSLv2 DROWN Assesssment")
pup.store_command("nmap -sV --script sslv2-drown.nse -p "+PORT+" "+IPADDRESS)

print("\n[!] Assessing Vulnerability to SSL POODLE...")
pup.pub_subheader("SSL POODLE Attack Assesssment")
pup.store_paragraph("The Padding Oracle On Downgraded Legacy Encryption (POODLE) attack was published in October 2014 and takes advantage of two factors. The first factor is the fact that some servers/clients still support SSL 3.0 for interoperability and compatibility with legacy systems. The second factor is a vulnerability that exists in SSL 3.0, which is related to block padding. The POODLE vulnerability is registered in the NIST NVD database as CVE-2014-3566.")
pup.store_command("nmap -sV --script ssl-poodle.nse -p "+PORT+" "+IPADDRESS)

#ssl-cert-intaddr.nse      
#ssl-dh-params.nse  
#ssl-known-key.nse     
#sslv2.nse



pup.save_report()