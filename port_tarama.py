import os 

hedef = input("HEDEF IP ADRESİNİ GİRİNİZ !: ")

os.system("nmap -A -v"+""+hedef)
os.system("nmap -v -sA"+""+hedef)
os.system("nmap -PN "+hedef)