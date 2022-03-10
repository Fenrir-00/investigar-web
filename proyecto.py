import sys
from sys import *
import os 
from os import *
import time
from io import *
class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'



def banner():
 os.system("clear")
 print(f"""{color.cyan}
███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝""")
 print(f"{color.fin}")

def carga():
    print(f"{color.verde}")
    print("""Loading…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    banner()

def incorrecto():
    os.system("clear")
    print(f"""{color.rojo}
░█████╗░██████╗░░█████╗░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
██║░░██║██████╔╝██║░░╚═╝██║██║░░██║██╔██╗██║
██║░░██║██╔═══╝░██║░░██╗██║██║░░██║██║╚████║
╚█████╔╝██║░░░░░╚█████╔╝██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝


██╗███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░
██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║░░╚═╝██║░░██║██████╔╝██████╔╝
██║██║╚████║██║░░██╗██║░░██║██╔══██╗██╔══██╗
██║██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██║░░██║
╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

███████╗░█████╗░████████╗░█████╗░
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗░░██║░░╚═╝░░░██║░░░███████║
██╔══╝░░██║░░██╗░░░██║░░░██╔══██║
███████╗╚█████╔╝░░░██║░░░██║░░██║
╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝{color.fin}""")
    time.sleep(4)
    menu()

def salir():
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    print(f"{color.fin}")
    sys.exit()

def menu():
    os.system("clear")
    banner()
    carga()
    print(f"{color.morado}    QUE PAGINA TE GUSTARIA INVESTIGAR")
    print("")
    print(f"{color.verde}[1]MANDAR PING")
    print(f"{color.verde}[2]BUSCAR SUBDOMINIOS OCULTOS")
    print(f"{color.verde}[3]VER PUERTOS Y SERVICIOS")
    print(f"{color.rojo}[0]SALIR{color.fin}")
    eleccion =input(f"{color.cyan}ELIJE UN NUMERO >>{color.fin} ")
    if eleccion == "1" :
     ping()
    elif eleccion == "2" :
     dirb()
    elif eleccion == "3" :
     nmap()
    elif eleccion == "0" :
     banner()
     salir() 
    else:
        incorrecto()

def ping():
 banner()
 print()
 print(f"{color.morado}QUE PAGINA QUEIRES HACER PING{color.fin}")
 print()
 print(f"{color.amarillo}EJEMPLO GOOGLE.ES    {color.rojo}NO PONER HTTP://WWW.{color.fin}")
 print()
 var=input(f"{color.cyan}INTRODUCE LA DIRECCION >> {color.fin}")
 os.system(f"ping -c 1 {var} >ttl.txt")
 var2=os.system('grep -o "ttl=[0-9]\+" ttl.txt  >bueno.txt')
 fd = open("bueno.txt","r")
 leer = fd.read()
 fd.close()
 banner()
 print(f"{color.verde}INFORMACION OBTENIDA")
 print()
 print(f"{color.amarillo}ESTE ES EL " + (leer))
 os.system('grep -o "([0-9]\+.[0-9]\+.[0-9]\+.[0-9]\+.)" ttl.txt >bueno.txt')
 os.system('grep -o "[0-9]\+.[0-9]\+.[0-9]\+.[0-9]\+" bueno.txt >ttl.txt')
 fd = open("ttl.txt","r")
 leer = fd.readline()
 fd.close()
 print(f"ESTA ES LA DIRECCION WEB: " + (leer))
 print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
 print()
 print(f"{color.azul}[1] VOLVER")
 print(f"{color.rojo}[2] SALIR{color.fin}")
 print()
 var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if var == "1":
  menu()
 elif var == "2":
  salir()
 else :
  incorrecto()

def dirb():
 os.system("pkg install dirb")
 banner()
 print()
 print(f"{color.morado}QUE SUBDOMINIO QUEIRES INVESTIGAR{color.fin}")
 print()
 print(f"{color.amarillo}EJEMPLO HTTPS://WWW.GOOGLE.ES{color.fin}")
 print()
 var1=input(f"{color.cyan}INTRODUCE LA PAGINA >> {color.fin}")
 banner()
 print()
 print(f"{color.amarillo}TEN PACIENCIA ESTO PUEDE TARDAR UNOS MINUTOS{color.fin}")
 time.sleep(3)
 os.system(f"dirb {var1}")
def nmap():
 os.system("pkg install nmap")
 banner()
 print(f"{color.morado}ESCANEO DE PUERTOS Y SERVICIOS{color.fin}")
 print()
 print(f"{color.amarillo}EJEMPLO GOOGLE.ES    {color.rojo}NO PONER HTTP://WWW.{color.fin}")
 print()
 var1=input(f"{color.cyan}INTRODUCE LA PAGINA >> {color.fin}")
 banner()
 print()
 print(f"{color.amarillo}TEN PACIENCIA ESTO PUEDE TARDAR UNOS MINUTOS{color.fin}")
 time.sleep(3)
 os.system(f"nmap -v -sV {var1} -oN bueno.txt")
 banner()
 var2=os.system('grep open bueno.txt >ttl.txt')
 fd = open("ttl.txt","r")
 leer = fd.read()
 fd.close()
 print()
 print(f"{color.morado}ESTON SON LOS PUERTOS DESCUBIERTOS{color.amarillo}")
 print()
 print("PORT     STATE   SERVICE       VERSION")
 print(leer) 
menu()
