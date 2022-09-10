import os, sys, time, io,re
while True:
 try:
  import requests
  break
 except ModuleNotFoundError:
  os.system("pip install requests")
while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")

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
print(r)
if r != "version=1.7\n":
 os.system("clear")
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
 os.system("clear")
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
 | Version                : Version  1.7                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """ 
 lol_py(texto)
 print()
def cabecera():
 os.system("clear")
 print(f"""{color.cyan}

 ██╗       ██╗███████╗██████╗  ██████╗░█████╗  █████╗ ███╗  ██╗
 ██║  ██╗  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗ ██║
 ╚██╗████╗██╔╝█████╗  ██████╦╝╚█████╗░██║  ╚═╝███████║██╔██╗██║
  ████╔═████║ ██╔══╝  ██╔══██╗ ╚═══██╗██║  ██╗██╔══██║██║╚████║
  ╚██╔╝ ╚██╔╝ ███████╗██████╦╝██████╔╝╚█████╔╝██║  ██║██║ ╚███║
   ╚═╝   ╚═╝  ╚══════╝╚═════╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚══╝""")
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
 print(f"{color.rojo}[0] SALIR{color.fin}")
 print()
 var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if var == "1":
  menu()
 elif var == "0":
  salir()
 else :
  incorrecto()

def ip ():
 os.system("ifconfig &>buenos.txt")
 with open('buenos.txt') as f:
  data = f.read()
 resultado = re.search('inet 192.[0-9]+\.[0-9]+\.[0-9]+', data)
 var3=(resultado.group())
 return var3


def dirb():
 banner()
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
  banner()
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
  banner()
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
  banner()
  print()
  print(f"{color.rojo}EL ESCANEO PUEDE DURAR 2 HORAS{color.fin}")
  print()
  print(f"{color.verde}[1] CONTINUAR")
  print(f"{color.azul}[2] VOLVER")
  print(f"{color.rojo}[0] SALIR{color.fin}")
  print()
  var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
  if var =="1":
   banner()
   print()
   print("EJEMPLO : https://google.com")
   url = input(f"{color.cyan}introduce pagina >> {color.fin}")
   fd = open("commun.txt","r")
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
 banner()
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
  banner()
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
  banner()
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
  banner()
  print()
  print(f"{color.rojo}EL ESCANEO PUEDE DURAR 2 HORAS{color.fin}")
  print()
  print(f"{color.verde}[1] CONTINUAR")
  print(f"{color.azul}[2] VOLVER")
  print(f"{color.rojo}[0] SALIR{color.fin}")
  print()
  var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
  if var =="1":
   banner()
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
   banner()
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
menu()
