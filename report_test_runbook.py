import Pubsy
pup = Pubsy.Pub()
pup.store_new_report("System_Security_Assessment v.19842")
pup.pub_header(IPADDRESS)
#TCP/80 Adversarial Enumeration Runbook
tcp80run = ["


#pup.pub_subheader("TCP/80 Interrogation Report")
#pup.run_command(CMD)
#pup.pub_subheader("TCP/21 Interrogation Report")
#pup.run_command(CMD1)
pub.pub_subheader("SMB/RPC/DCOM Interrogation Report")
pup.run_command("nmap -n -vv -Pn -sV " + IP + " -pT:139,445,U:137 --script='smb-vuln-*'")
