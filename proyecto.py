import os, sys, time, io,re
from colores import colorverde,colorazul,colorclasic,colormorado,colornaraja,coloramarillo
import random
import platform
import threading
while True:
 try:
  import requests
  break
 except ModuleNotFoundError:
  os.system("pip install requests")

while True:
 try:
  import whois
  break
 except:
  os.system("pip install python-whois")

  
sistema = platform.system()
limpieza = ""

if sistema == "Linux":
  limpieza = "clear"
elif sistema == "Windows":
  limpieza ="cls"  

class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

r= requests.get("https://raw.githubusercontent.com/Fenrir-00/investigar-web/main/version.txt")
r=r.text
if r != "version=2.1\n":
 os.system(f"{limpieza}")
 print(f"""{color.rojo}HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO""")
 time.sleep(5)

def banner():
 os.system(f"{limpieza}")
 print(f"""{color.cyan}
███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{color.fin}""")
def version():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  2.1                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """ 

 suerte = random.randint(0,5)
 if suerte == 0:
   coloramarillo(texto)
 elif suerte == 1:
   colorazul(texto)
 elif suerte == 2 :
   colorclasic(texto)
 elif suerte == 3 :
   colormorado(texto)
 elif suerte == 4 :
   colornaraja(texto)
 elif suerte == 5:
   colorverde(texto)      

def cabecera():
 os.system(f"{limpieza}")
 print(f"""{color.cyan}

 ██╗       ██╗███████╗██████╗  ██████╗░█████╗  █████╗ ███╗  ██╗
 ██║  ██╗  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗ ██║
 ╚██╗████╗██╔╝█████╗  ██████╦╝╚█████╗░██║  ╚═╝███████║██╔██╗██║
  ████╔═████║ ██╔══╝  ██╔══██╗ ╚═══██╗██║  ██╗██╔══██║██║╚████║
  ╚██╔╝ ╚██╔╝ ███████╗██████╦╝██████╔╝╚█████╔╝██║  ██║██║ ╚███║
   ╚═╝   ╚═╝  ╚══════╝╚═════╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚══╝""")


def incorrecto():
    os.system(f"{limpieza}")
    print(f"""{color.rojo}
 █████╗ ██████╗  █████╗ ██╗ █████╗ ███╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗ ██║
██║  ██║██████╔╝██║  ╚═╝██║██║  ██║██╔██╗██║
██║  ██║██╔═══╝ ██║  ██╗██║██║  ██║██║╚████║
╚█████╔╝██║     ╚█████╔╝██║╚█████╔╝██║ ╚███║
 ╚════╝ ╚═╝      ╚════╝ ╚═╝ ╚════╝ ╚═╝  ╚══╝
██╗███╗  ██╗ █████╗  █████╗ ██████╗ ██████╗
██║████╗ ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║  ╚═╝██║  ██║██████╔╝██████╔╝
██║██║╚████║██║  ██╗██║  ██║██╔══██╗██╔══██╗
██║██║ ╚███║╚█████╔╝╚█████╔╝██║  ██║██║  ██║
╚═╝╚═╝  ╚══╝ ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
███████╗ █████╗ ████████╗ █████╗
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗  ██║  ╚═╝   ██║   ███████║
██╔══╝  ██║  ██╗   ██║   ██╔══██║
███████╗╚█████╔╝   ██║   ██║  ██║
╚══════╝ ╚════╝    ╚═╝   ╚═╝  ╚═╝{color.fin}""")
    time.sleep(4)
    menu()

def salir():
    os.system(f"{limpieza}")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system(f"{limpieza}")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system(f"{limpieza}")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system(f"{limpieza}")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system(f"{limpieza}")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system(f"{limpieza}")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…100%
    ███████████████████""")
    time.sleep(1)
    os.system(f"{limpieza}")
    print(f"{color.fin}")
    

def menu():
    os.system(f"{limpieza}")
    cabecera()
    version()
    print(f"{color.morado}    QUE OPCION TE GUSTARIA INVESTIGAR")
    print("")
    print(f"{color.verde}[1]MANDAR PING")
    print(f"{color.verde}[2]BUSCAR SUBCARPETAS OCULTAS")
    print(f"{color.verde}[3]VER PUERTOS Y SERVICIOS")
    print(f"{color.verde}[4]VER MI IP PUBLICA/PRIVADA")
    print(f"{color.verde}[5]BUSCAR SUBDOMINIOS OCULTOS")
    print(f"{color.verde}[6]VER DISPOSITIVOS EN MI RED WIFI")
    print(f"{color.verde}[7]VER REGISTRO DE DOMINIOS")
    print(f"{color.verde}[8]CREAR EMAIL TEMPORAL")
    print(f"{color.rojo}[0]SALIR{color.fin}")
    eleccion =input(f"{color.cyan}ELIJE UN NUMERO >>{color.fin} ")
    if eleccion == "1" :
     ping()
    elif eleccion == "2" :
     dirb()
    elif eleccion == "3" :
     nmap()
    elif eleccion == "4" :
     sacar()
    elif eleccion == "5" :
     sub()
    elif eleccion == "6" :
     wifi()
    elif eleccion == "7" :
     regis()
    elif eleccion == "8" :
      email()
    elif eleccion == "0" :
     banner()
     salir() 
    else:
        incorrecto()

def ping():
 cabecera()
 version()
 print()
 print(f"{color.morado}QUE PAGINA QUEIRES HACER PING{color.fin}")
 print()
 print(f"{color.amarillo}EJEMPLO GOOGLE.ES    {color.rojo}NO PONER HTTP://WWW.{color.fin}")
 print()
 var=input(f"{color.cyan}INTRODUCE LA DIRECCION >> {color.fin}")
 if sistema == "Linux":
   os.system(f"ping -c 1 {var} >ttl.txt")
 if sistema == "Windows":
  os.system(f"ping  {var} >ttl.txt")
 f = open("ttl.txt","r")
 leer = f.read()
 f.close()
 if sistema == "Linux":
  ttl = re.search('ttl=\S*', leer)
 if sistema =="Windows":
  ttl = re.search('TTL=\S*', leer)
 ttl =ttl.group()
 direccion = re.search("[0-9]\S*",leer)
 direccion= direccion.group()
 if int(ttl[4:7]) > 65:
  maquina = "WINDOWS"
 else:
  maquina ="LINUX"
 cabecera()
 version()
 print(f"""
{color.verde}INFORMACION OBTENIDA
""")
 print(f"{color.amarillo}ESTE ES EL " + (ttl),maquina)
 if sistema =="Linux":
  print(f"ESTA ES LA DIRECCION WEB: (" + (direccion))
 if sistema =="Windows":
  print(f"ESTA ES LA DIRECCION WEB: [" + (direccion))
 print(f"""
{color.morado}QUE QUIERES HACER AHORA{color.fin}
""")
 print(f"{color.azul}[1] VOLVER")
 print(f"{color.rojo}[0] SALIR{color.fin}")
 print()
 var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if var == "1":
  menu()
 elif var == "0":
  salir()
 else :
  incorrecto


def ip():
 if sistema == "Linux":
  os.system("ifconfig &>buenos.txt")
 if sistema == "Windows":
  os.system("ipconfig >buenos.txt")
 with open('buenos.txt') as f:
   data = f.read()
 try:
  resultado = re.search('192\S*', data)
  var3=(resultado.group())
 except:
  var3="127.0.0.1"
 return var3 
 

def regis():
 banner()
 print(f"{color.morado} QUE REGISTRO DE DOMINIO QUIERES VER")
 print()
 print(f"{color.amarillo}EJEMPLO GOOGLE.ES    {color.rojo}NO PONER HTTP://WWW.{color.fin}")
 print()
 var=input(f"{color.cyan}INTRODUCE LA DIRECCION >> {color.fin}")
 try:
  r=whois.whois(f'{var}')
  banner()
  print()
  print(f"{color.morado}INFORMACION OBTENIDA")
  print(f"{color.verde}")
  print(r.text)
  print(f"""
         {color.rojo} QUITAR ZOOM PARA LEER MEJOR{color.fin}
""")
  print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
  print()
  print(f"{color.azul}[1] VOLVER")
  print(f"{color.rojo}[0] SALIR{color.fin}")
  print()
  var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
  if var == "1":
   menu()
  elif var == "0":
   salir()
  else :
   incorrecto()
 except:
  incorrecto()


def dirb():
 cabecera()
 version()
 salto = "\n"
 print()
 print(f"{color.morado}    BUSCAR DIRECTORIOS {color.fin}")
 print()
 print(f"{color.cyan}QUE QUIE TIPO DE SCANEO QUIERES{color.fin}")
 print()
 print(f"{color.verde}[1] ESCANEO RAPIDO")
 print(f"{color.azul}[2] ESCANEO INTENSO")
 print(f"{color.rojo}[0] SALIR{color.fin}")
 print()
 var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if var == "1":
  cabecera()
  version()
  print()
  print("EJEMPLO : https://google.com")
  url = input(f"{color.cyan}introduce pagina >> {color.fin}")
  fd = open("small.txt","r")
  leer = fd.readlines()
  df =open("buenos.txt","w")
  df.write("")
  df.close()
  df =open("buenos.txt","a")
  contador = 0
  otra =requests.get(url+"/!?g7")
  largura1=otra.text
  largura1 = len(largura1)-4
  otra =requests.get(url+"/!8!7")
  largura1=otra.text
  largura1 = len(largura1)-14
  largura2 = largura1+34
  for linea in leer:
   contador +=1
   if contador == 200 :
    print(f"{color.verde} PROBADAS 200 DE 1000 CONTRASEÑAS{color.fin}")
   if contador == 400 :
    print(f"{color.verde} PROBADAS 400 DE 1000 CONTRASEÑAS{color.fin}")
   if contador == 600 :
    print(f"{color.verde} PROBADAS 600 DE 1000 CONTRASEÑAS{color.fin}")
   if contador == 800 :
    print(f"{color.verde} PROBADAS 800 DE 1000 CONTRASEÑAS{color.fin}")
   var = linea.rstrip("\n")
   print(url+"/"+var)
   data = url+"/"+var
 
   try:
    r= requests.get(data)
    largura=r.text
    largura = len(largura)
    largura = largura - len(var)
    if largura1 > largura or largura2 < largura:
     print(f"{color.amarillo}")
     print(data)
     df.write((data) + f"{salto}")
     print(f"{color.fin}")
   except:
    pass
  df.close()
  cabecera()
  version()
  print()
  print(f"{color.morado} RESULTADOS OPTENIDOS {color.amarillo}")
  df = open("buenos.txt","r")
  leer = df.read()
  print(leer)
  print()
  print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
  print()
  print(f"{color.azul}[1] VOLVER")
  print(f"{color.rojo}[0] SALIR{color.fin}")
  print()
  var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
  if var == "1":
   menu()
  elif var == "0":
   salir()
  else :
   incorrecto()
 elif var =="2":
  cabecera()
  version()
  print()
  print(f"{color.rojo}EL ESCANEO PUEDE DURAR 2 HORAS{color.fin}")
  print()
  print(f"{color.verde}[1] CONTINUAR")
  print(f"{color.azul}[2] VOLVER")
  print(f"{color.rojo}[0] SALIR{color.fin}")
  print()
  var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
  if var =="1":
   cabecera()
   version()
   print()
   print("EJEMPLO : https://google.com")
   url = input(f"{color.cyan}introduce pagina >> {color.fin}")
   fd = open("common.txt","r")
   leer = fd.readlines()
   df =open("buenos.txt","w")
   df.write("")
   df.close()
   df =open("buenos.txt","a")
   contador = 0
   otra =requests.get(url+"/!?g7")
   largura1=otra.text
   largura1 = len(largura1)-4
   otra =requests.get(url+"/!8!7")
   largura1=otra.text
   largura1 = len(largura1)-14
   largura2 = largura1+34
   for linea in leer:
    contador +=1
    if contador == 2000 :
     print(f"{color.verde} PROBADAS 2000 de 10000 CONTRASEÑAS{color.fin}")
    if contador == 4000 :
     print(f"{color.verde} PROBADAS 4000 de 10000 CONTRASEÑAS{color.fin}")
    if contador == 6000 :
     print(f"{color.verde} PROBADAS 6000 de 10000 CONTRASEÑAS{color.fin}")
    if contador == 8000 :
     print(f"{color.verde} PROBADAS 8000 de 10000  CONTRASEÑAS{color.fin}")
    var = linea.rstrip("\n")
    print(url+"/"+var)
    data = url+"/"+var
    try:
     r= requests.get(data)
     largura=r.text
     largura = len(largura)
     largura = largura - len(var)
     if largura1 > largura or largura2 < largura:
      print(f"{color.amarillo}")
      print(data)
      df.write((data) + f"{salto}")
      print(f"{color.fin}")
    except:
     pass
   df.close()
   cabecera()
   version()
   print()
   print(f"{color.morado} RESULTADOS OPTENIDOS {color.amarillo}")
   df = open("buenos.txt","r")
   leer = df.read()
   print(leer)
   print()
   print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
   print()
   print(f"{color.azul}[1] VOLVER")
   print(f"{color.rojo}[0] SALIR{color.fin}")
   print()
   var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
   if var == "1":
    menu()
   elif var == "0":
    salir()
   else :
    incorrecto()
  elif var =="2":
   dirb()
  elif var == "0":
   salir()
  else :
   incorrecto()
 elif var == "0":
  salir()
 else :
   incorrecto()

def nmap():
 os.system("pkg install nmap")
 cabecera()
 version()
 print(f"{color.morado}ESCANEO DE PUERTOS Y SERVICIOS{color.fin}")
 print()
 print(f"{color.amarillo}EJEMPLO GOOGLE.ES    {color.rojo}NO PONER HTTP://WWW.{color.fin}")
 print()
 var1=input(f"{color.cyan}INTRODUCE LA PAGINA >> {color.fin}")
 banner()
 print()
 print(f"{color.amarillo}TEN PACIENCIA ESTO PUEDE TARDAR UNOS MINUTOS{color.fin}")
 time.sleep(3)
 os.system(f"nmap -v -sV -T2 {var1} -oN bueno.txt")
 cabecera()
 version()
 var2=os.system('grep open bueno.txt >ttl.txt')
 fd = open("ttl.txt","r")
 leer = fd.read()
 fd.close()
 print()
 print(f"{color.morado}ESTON SON LOS PUERTOS DESCUBIERTOS{color.amarillo}")
 print()
 print("PORT     STATE   SERVICE       VERSION")
 print(leer) 
 print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
 print()
 print(f"{color.azul}[1] VOLVER")
 print(f"{color.rojo}[0] SALIR{color.fin}")
 print()
 var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if var == "1":
  menu()
 elif var == "0":
  salir()
 else :
  incorrecto()

def sacar ():
 cabecera()
 version()
 print(f"""
{color.morado}INFORMACION OBTENIDA
""")
 print(f"{color.verde}ESTA ES TU IP PUBLICA:")
 r= requests.get("https://ident.me")
 r=r.text
 print(f"{color.amarillo}",r,f"{color.fin}")
 var=ip()
 print(f"{color.verde}ESTA ES TU IP PRIVADA:")
 print(f"{color.amarillo}",var,f"{color.fin}")
 print()
 print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
 print()
 print(f"{color.azul}[1] VOLVER")
 print(f"{color.rojo}[0] SALIR{color.fin}")
 print()
 var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if var == "1":
  menu()
 elif var == "0":
  salir()
 else :
  incorrecto()

def sub():
 cabecera()
 version()
 salto = "\n"
 print()
 print(f"{color.morado}    BUSCAR SUBDOMINIOS {color.fin}")
 print()
 print(f"{color.cyan}QUE QUIE TIPO DE SCANEO QUIERES{color.fin}")
 print()
 print(f"{color.verde}[1] ESCANEO RAPIDO")
 print(f"{color.azul}[2] ESCANEO INTENSO")
 print(f"{color.rojo}[0] SALIR{color.fin}")
 print()
 var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if var == "1":
  cabecera()
  version()
  print()
  print("EJEMPLO : google.com")
  url = input(f"{color.cyan}introduce pagina >> {color.fin}")
  fd = open("subdominio.txt","r")
  leer = fd.readlines()
  df =open("buenos.txt","w")
  df.write("")
  df.close()
  df =open("buenos.txt","a")
  contador = 0
  for linea in leer:
   contador +=1
   if contador == 200 :
    print(f"{color.verde} PROBADAS 200 DE 1000 CONTRASEÑAS{color.fin}")
   if contador == 400 :
    print(f"{color.verde} PROBADAS 400 DE 1000 CONTRASEÑAS{color.fin}")
   if contador == 600 :
    print(f"{color.verde} PROBADAS 600 DE 1000 CONTRASEÑAS{color.fin}")
   if contador == 800 :
    print(f"{color.verde} PROBADAS 800 DE 1000 CONTRASEÑAS{color.fin}")
   var = linea.rstrip("\n")
   print("https://"+var+"."+url)
   data = "https://"+var+"."+url
   try:
    r= requests.get(data)
    print(f"{color.amarillo}")
    print(data)
    df.write((data) + f"{salto}")
    print(f"{color.fin}")
   except:
    pass
  df.close()
  cabecera()
  version()
  print()
  print(f"{color.morado} RESULTADOS OPTENIDOS {color.amarillo}")
  df = open("buenos.txt","r")
  leer = df.read()
  print(leer)
  print()
  print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
  print()
  print(f"{color.azul}[1] VOLVER")
  print(f"{color.rojo}[0] SALIR{color.fin}")
  print()
  var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
  if var == "1":
   menu()
  elif var == "0":
   salir()
  else :
   incorrecto()
 elif var =="2":
  cabecera()
  version()
  print()
  print(f"{color.rojo}EL ESCANEO PUEDE DURAR 2 HORAS{color.fin}")
  print()
  print(f"{color.verde}[1] CONTINUAR")
  print(f"{color.azul}[2] VOLVER")
  print(f"{color.rojo}[0] SALIR{color.fin}")
  print()
  var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
  if var =="1":
   cabecera()
   version()
   print()
   print("EJEMPLO : google.com")
   url = input(f"{color.cyan}introduce pagina >> {color.fin}")
   fd = open("subdominio1.txt","r")
   leer = fd.readlines()
   df =open("buenos.txt","w")
   df.write("")
   df.close()
   df =open("buenos.txt","a")
   contador = 0
   for linea in leer:
    contador +=1
    if contador == 2000 :
     print(f"{color.verde} PROBADAS 2000 de 10000 CONTRASEÑAS{color.fin}")
    if contador == 4000 :
     print(f"{color.verde} PROBADAS 4000 de 10000 CONTRASEÑAS{color.fin}")
    if contador == 6000 :
     print(f"{color.verde} PROBADAS 6000 de 10000 CONTRASEÑAS{color.fin}")
    if contador == 8000 :
     print(f"{color.verde} PROBADAS 8000 de 10000  CONTRASEÑAS{color.fin}")
    var = linea.rstrip("\n")
    print("https://"+var+"."+url)
    data = "https://"+var+"."+url
    try:
     r= requests.get(data)
     print(f"{color.amarillo}")
     print(data)
     df.write((data) + f"{salto}")
     print(f"{color.fin}")
    except:
     pass
   df.close()
   cabecera()
   version()
   print()
   print(f"{color.morado} RESULTADOS OPTENIDOS {color.amarillo}")
   df = open("buenos.txt","r")
   leer = df.read()
   print(leer)
   print()
   print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
   print()
   print(f"{color.azul}[1] VOLVER")
   print(f"{color.rojo}[0] SALIR{color.fin}")
   print()
   var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
   if var == "1":
    menu()
   elif var == "0":
    salir()
   else :
    incorrecto()
  elif var =="2":
   sub()
  elif var == "0":
   salir()
  else :
   incorrecto()
 elif var == "0":
  salir()
 else :
   incorrecto()

def wifi():
 cabecera()
 version() 
 var3 = ip()
 print(f"""{color.verde}
 INICIANDO ESCANEO TU IP ES {var3}
 {color.amarillo} """)
 if var3 == "127.0.0.1":
  print(f"""{color.rojo}
  NO ESTAS CONECTADO AL WIFI{color.fin}
  """)
 else:
    for i in range(1,254):
     run =threading.Thread(target=wifiusu, args={i},)
     run.start()
     time.sleep(0.3)
     if i == 253:
      time.sleep(5) 
      print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
      print()
      print(f"{color.azul}[1] VOLVER")
      print(f"{color.rojo}[0] SALIR{color.fin}")
      print()
      var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
      if var == "1":
       menu()
      elif var == "0":
       salir()
      else :
       incorrecto()

def wifiusu(i):
  if sistema =="Windows":
   comando ="ping 192.168.0."+str(i)
  else:
    comando ="ping -c2 192.168.0."+str(i)
  pitido = os.popen(comando).read()
  if "bytes=32"  in pitido or "64 bytes" in pitido:
   print("192.168.0."+str(i))  
 
  

 


def email():
 if sistema == "Linux":
  os.system("termux-open-url https://temp-mail.org/es/")
 if sistema == "Windows": 
  os.system("start https://temp-mail.org/es/")
 menu()

###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################

def nmap1(url):
 os.system("pkg install nmap")
 banner()
 var1= url
 banner()
 print()
 print(f"{color.amarillo}TEN PACIENCIA ESTO PUEDE TARDAR UNOS MINUTOS{color.fin}")
 time.sleep(3)
 os.system(f"nmap -v -sV -T2 {var1} -oN bueno.txt")
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


def wifi1():
 os.system("pkg install nmap")
 banner()
 try:
  var=ip()
  print(f"""
{color.amarillo}TEN PACIENCIA ESTO PUEDE TARDAR UNOS MINUTOS{color.fin}""")
  os.system(f"nmap 192.168.0.1/24 -oN bueno.txt")
  banner()
  print(f"""{color.morado}
ESTOS SON LOS DISPOSITIVOS EN LA RED""")
  var2=os.system('grep report bueno.txt >ttl.txt')
  fd = open("ttl.txt","r")
  print(f"{color.verde}")
  leer = fd.read()
  fd.close()
  print(leer,end="")
  try:
   var=ip()
   print(f"{color.cyan}ESTA ES TU IP PRIVADA:",var)
  except:
   print(f"{color.verde}ESTA ES TU IP PRIVADA:")
   print(f"{color.rojo}NO ESTAS CONECTADO A WIFI{color.fin}")
  print(f"""{color.amarillo}PUEDES TENER MAS INFORMACION PEGANDO LA DIRECCION
QUE QUIERAS EN EL ESCANEO DE PUERTOS
""")
 except:
  print(f"""
{color.rojo}NO ESTAS CONECTADO AL WIFI
""")

def ping1(url):
 os.system(f"ping -c 1 {url} >ttl.txt")
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


 
def dirb1(dic,url):
 
 salto = "\n"

 if dic == "-R":
 
  url = url
  fd = open("small.txt","r")
  leer = fd.readlines()
  df =open("buenos.txt","w")
  df.write("")
  df.close()
  df =open("buenos.txt","a")
  contador = 0
  otra =requests.get(url+"/!?g7")
  largura1=otra.text
  largura1 = len(largura1)-4
  otra =requests.get(url+"/!8!7")
  largura1=otra.text
  largura1 = len(largura1)-14
  largura2 = largura1+34
  for linea in leer:
   contador +=1
   if contador == 200 :
    print(f"{color.verde} PROBADAS 200 DE 1000 CONTRASEÑAS{color.fin}")
   if contador == 400 :
    print(f"{color.verde} PROBADAS 400 DE 1000 CONTRASEÑAS{color.fin}")
   if contador == 600 :
    print(f"{color.verde} PROBADAS 600 DE 1000 CONTRASEÑAS{color.fin}")
   if contador == 800 :
    print(f"{color.verde} PROBADAS 800 DE 1000 CONTRASEÑAS{color.fin}")
   var = linea.rstrip("\n")
   print(url+"/"+var)
   data = url+"/"+var
 
   try:
    r= requests.get(data)
    largura=r.text
    largura = len(largura)
    largura = largura - len(var)
    if largura1 > largura or largura2 < largura:
     print(f"{color.amarillo}")
     print(data)
     df.write((data) + f"{salto}")
     print(f"{color.fin}")
   except:
    pass
  df.close()
  banner()
  print(f"{color.morado} RESULTADOS OPTENIDOS {color.amarillo}")
  df = open("buenos.txt","r")
  leer = df.read()
  print(leer)
  
 elif dic =="-L":
 
  if "1" =="1":
   url = url
   fd = open("common.txt","r")
   leer = fd.readlines()
   df =open("buenos.txt","w")
   df.write("")
   df.close()
   df =open("buenos.txt","a")
   contador = 0
   otra =requests.get(url+"/!?g7")
   largura1=otra.text
   largura1 = len(largura1)-4
   otra =requests.get(url+"/!8!7")
   largura1=otra.text
   largura1 = len(largura1)-14
   largura2 = largura1+34
   for linea in leer:
    contador +=1
    if contador == 2000 :
     print(f"{color.verde} PROBADAS 2000 de 10000 CONTRASEÑAS{color.fin}")
    if contador == 4000 :
     print(f"{color.verde} PROBADAS 4000 de 10000 CONTRASEÑAS{color.fin}")
    if contador == 6000 :
     print(f"{color.verde} PROBADAS 6000 de 10000 CONTRASEÑAS{color.fin}")
    if contador == 8000 :
     print(f"{color.verde} PROBADAS 8000 de 10000  CONTRASEÑAS{color.fin}")
    var = linea.rstrip("\n")
    print(url+"/"+var)
    data = url+"/"+var
    try:
     r= requests.get(data)
     largura=r.text
     largura = len(largura)
     largura = largura - len(var)
     if largura1 > largura or largura2 < largura:
      print(f"{color.amarillo}")
      print(data)
      df.write((data) + f"{salto}")
      print(f"{color.fin}")
    except:
     pass
   df.close()
   banner()
   print(f"{color.morado} RESULTADOS OPTENIDOS {color.amarillo}")
   df = open("buenos.txt","r")
   leer = df.read()
   print(leer)
   print()
 else :
   ayuda()



def sub1(dic,url):
 salto = "\n"
 if dic == "-R":
  banner()
  print()
  print("EJEMPLO : google.com")
  url = url
  fd = open("subdominio.txt","r")
  leer = fd.readlines()
  df =open("buenos.txt","w")
  df.write("")
  df.close()
  df =open("buenos.txt","a")
  contador = 0
  for linea in leer:
   contador +=1
   if contador == 200 :
    print(f"{color.verde} PROBADAS 200 DE 1000 CONTRASEÑAS{color.fin}")
   if contador == 400 :
    print(f"{color.verde} PROBADAS 400 DE 1000 CONTRASEÑAS{color.fin}")
   if contador == 600 :
    print(f"{color.verde} PROBADAS 600 DE 1000 CONTRASEÑAS{color.fin}")
   if contador == 800 :
    print(f"{color.verde} PROBADAS 800 DE 1000 CONTRASEÑAS{color.fin}")
   var = linea.rstrip("\n")
   print("https://"+var+"."+url)
   data = "https://"+var+"."+url
   try:
    r= requests.get(data)
    print(f"{color.amarillo}")
    print(data)
    df.write((data) + f"{salto}")
    print(f"{color.fin}")
   except:
    pass
  df.close()
  banner()
  print(f"{color.morado} RESULTADOS OPTENIDOS {color.amarillo}")
  df = open("buenos.txt","r")
  leer = df.read()
  print(leer)
  print()
 elif dic =="-L":
  if "1" =="1":
   url = url
   fd = open("subdominio1.txt","r")
   leer = fd.readlines()
   df =open("buenos.txt","w")
   df.write("")
   df.close()
   df =open("buenos.txt","a")
   contador = 0
   for linea in leer:
    contador +=1
    if contador == 2000 :
     print(f"{color.verde} PROBADAS 2000 de 10000 CONTRASEÑAS{color.fin}")
    if contador == 4000 :
     print(f"{color.verde} PROBADAS 4000 de 10000 CONTRASEÑAS{color.fin}")
    if contador == 6000 :
     print(f"{color.verde} PROBADAS 6000 de 10000 CONTRASEÑAS{color.fin}")
    if contador == 8000 :
     print(f"{color.verde} PROBADAS 8000 de 10000  CONTRASEÑAS{color.fin}")
    var = linea.rstrip("\n")
    print("https://"+var+"."+url)
    data = "https://"+var+"."+url
    try:
     r= requests.get(data)
     print(f"{color.amarillo}")
     print(data)
     df.write((data) + f"{salto}")
     print(f"{color.fin}")
    except:
     pass
   df.close()
   banner()
   print(f"{color.morado} RESULTADOS OPTENIDOS {color.amarillo}")
   df = open("buenos.txt","r")
   leer = df.read()
   print(leer)
   print()
 else :
   ayuda()



def sacar1 ():
 banner()
 print()
 print(f"{color.verde}ESTA ES TU IP PUBLICA:")
 r= requests.get("https://ident.me")
 r=r.text
 print(f"{color.amarillo}",r,f"{color.fin}")
 try:
  var=ip()
  print(f"{color.verde}ESTA ES TU IP PRIVADA:")
  print(f"{color.amarillo}",var,f"{color.fin}")
 except:
  print(f"{color.verde}ESTA ES TU IP PRIVADA:")
  print(f"{color.rojo}NO ESTAS CONECTADO A WIFI{color.fin}")
  print()

def regis1(var):                                                                                          
 try:
  r=whois.whois(f'{var}')                                                                                   
  banner()
  print()                                                                                                   
  print(f"{color.morado}INFORMACION OBTENIDA")
  print(f"{color.verde}")
  print(r.text)
  print(f"""
         {color.rojo} QUITAR ZOOM PARA LEER MEJOR{color.fin}
""")
 except:
   ayuda()

def ayuda():
 os.system(f"{limpieza}")
 print("""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  1.9                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """)
 print("""
              BIENVENIDO AL PANEL DE AYUDA

 webscan es un script dedicado a investigar las paginas web
 y la red wifi podremos usarlo usando la interfaz o pasando
 los siguientes argumentos.

  [-S] para ver los subdominios
  [-C] para ver las carpetas ocultas
  [-R] para escaneo rapido
  [-L] para escaneo lento
  [-P] para ver los puertos
  [-I] para ver ip publica/privada
  [-A] pra hacer un ping
  [-W] para ver dispositivos en mi red
  [-F] para ver registro de dominio

 ejemplos: python proyecto.py -S -R pagina.com
 ejemplos: python proyecto.py -C -R https://pagina.com
 ejemplos: python proyecto.py -P pagina.com
 ejemplos: python proyecto.py -I
 ejemplos: python proyecto.py -A pagina.com
 ejemplos: python proyecto.py -W
 ejemplos: python proyecto.py -F pagina.com
""")
arg=sys.argv
try:
  arg1 = sys.argv[1:]
  arg2= sys.argv[2]
  arg3= sys.argv[3]
except:
  pass

if len(arg) == 1:
  menu() 
else:  
  if "-h" in arg or "--help" in arg or "help" in arg or "-help" in arg:
    ayuda()
  elif "-S" in arg:
    sub1(arg2,arg3)
  elif "-C" in arg:
    dirb1(arg2,arg3) 
  elif "-P" in arg:
    nmap1(arg2) 
  elif "-I" in arg:
    sacar1() 
  elif "-W" in arg:
    wifi1()   
  elif "-F" in arg:
   regis1(arg2)
  elif "-A" in arg:
    try:
      ping1(arg2)
    except:
      ayuda()
  else:
    ayuda()



