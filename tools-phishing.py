#!/usr/bin/python
# -*- coding: utf-8 -*-
#Copyright 2019 tools_phishing
#Written by: Adrian Guillermo
#Facebook: Adrian Guillero
#Github: https://www.github.com/AdrMXR

from time import sleep
from sys import stdout, argv, exit
import os
import time 
import string

BLUE, RED, WHITE, CYAN, DEFAULT, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\033[36m', '\033[0m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def HiddenEye():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop):\n--> ")
  os.system('cd {} && mkdir HiddenEye && git clone https://github.com/DarkSecDevelopers/HiddenEye.git'.format(directory))
  print("Instalando requerimientos...")
  time.sleep(3)
  os.system('cd {} && chmod 777 HiddenEye && sudo apt install python3-pip && cd HiddenEye/ && sudo pip3 install -r requirements.txt'.format(directory))
  if raw_input("¿Desea ejecutar la herramienta? (y/n)\n--> ").upper() != "Y":
    print("GRACIAS POR UTILIZAR TOOLS-PHISHING").format(END) 
    exit(0)
  print("Ejecutando herramienta...")
  time.sleep(3)
  os.system('cd {} && cd HiddenEye/ && python3 HiddenEye.py'.format(directory))
  os.system('cd {} && cd HiddenEye/ && python3 HiddenEye.py'.format(directory)) # Segunda Ejecucion de HiddenEye para evitar el problema de conexiòn de internet.
  exit(0)
  
def SocialPhish():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop): \n--> ")
  os.system('cd {} && mkdir SocialPhish && git clone https://github.com/xHak9x/SocialPhish.git'.format(directory))
  print("Ingresando permisos...")
  time.sleep(3)
  os.system('cd {} && cd SocialPhish && chmod +x socialphish.sh'.format(directory))
  if raw_input("¿Desea ejecutar la herramienta? (y/n)\n--> ").upper() != "Y":
    print("GRACIAS POR UTILIZAR TOOLS-PHISHING").format(END)
    exit(0)
  print("Ejecutando herramienta...")
  time.sleep(3)
  os.system('clear && cd {} && cd SocialPhish && ./socialphish.sh'.format(directory))
  exit(0)

def SocialFish():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop): \n--> ")
  os.system('cd {} && mkdir SocialFish && git clone https://github.com/UndeadSec/SocialFish.git'.format(directory))
  print("Instalando requerimientos...")
  time.sleep(3)
  os.system('sudo apt-get install python3 python3-pip python3-dev -y && cd {} && cd SocialFish && python3 -m pip install -r requirements.txt '.format(directory))
  if raw_input("¿Desea ejecutar la herramienta? (y/n)\n--> ").upper() != "Y":
    print("GRACIAS POR UTILIZAR TOOLS-PHISHING").format(END)
    exit(0)
  print("Ejecutando herramienta...")
  time.sleep(3)
  os.system('clear && cd {} && cd SocialFish && python3 SocialFish.py'.format(directory))
  exit(0)

def PhisherMan():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop): \n--> ")
  os.system('cd {} && mkdir Phisher-man && git clone https://github.com/FDX100/Phisher-man.git'.format(directory))
  if raw_input("¿Desea ejecutar la herramienta? (y/n)\n--> ").upper() != "Y":
    print("GRACIAS POR UTILIZAR TOOLS-PHISHING").format(END)
    exit(0)
  print("Ejecutando herramienta...")
  time.sleep(3)
  os.system('cd {} && cd Phisher-man && python phisherman.py'.format(directory))
  exit(0)

def Shellphish():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop): \n--> ")
  os.system('cd {} && git clone https://github.com/thelinuxchoice/shellphish.git'.format(directory))
  if raw_input("¿Desea ejecutar la herramienta? (y/n)\n--> ").upper() != "Y":
    print("GRACIAS POR UTILIZAR TOOLS-PHISHING").format(END)
    exit(0)
  print("Ejecutando herramienta...")
  time.sleep(3)
  os.system('clear && cd {} && cd shellphish && bash shellphish.sh'.format(directory))
  exit(0)

def Wifiphisher():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop): \n--> ")
  os.system('cd {} && git clone https://github.com/wifiphisher/wifiphisher.git'.format(directory))
  print("Instalando requerimientos...")
  time.sleep(3)
  os.system('cd {} && cd wifiphisher && sudo python setup.py install'.format(directory))
  if raw_input("¿Desea ejecutar la herramienta? (y/n)\n--> ").upper() != "Y":
    print("GRACIAS POR UTILIZAR TOOLS-PHISHING").format(END)
    exit(0)
  print("Ejecutando herramienta...")
  time.sleep(3)
  os.system('wifiphisher')

def Modlishka():
  print("Esta herramienta se instalara por default en /usr/local para que funcione correctamente.")
  if raw_input("¿Desea continuar? (y/n)\n--> ").upper() != "Y":
    print("GRACIAS POR UTILIZAR TOOLS-PHISHING").format(END)
  print("Instalando requerimientos...")
  time.sleep(3)
  os.system('cd /usr/local && sudo curl -O https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz && sudo tar -xzvf go1.9.linux-amd64.tar.gz && echo export PATH=$PATH:/usr/local/go/bin >> /etc/profile')
  if raw_input("Se necesita reiniciar su equipo para efectuar los cambios ¿Desea continuar? (y/n)\n--> ").upper() != "Y":
    print("GRACIAS POR UTILIZAR TOOLS-PHISHING").format(END)
    exit(0)
  print("Reiniciando equipo...")
  time.sleep(2)
  os.system('sudo reboot')
  exit(0)

def menu():
  opcion = input("\nEscoja la herramienta que desea instalar en su equipo: \n\n #1 --- HiddenEye \n\n #2 --- SocialPhish \n\n #3 --- SocialFish \n\n #4 --- Phisher-man \n\n #5 --- Shellphish \n\n #6 --- Wifiphisher \n\n #7 --- Modlishka \n\n--> " )

  if opcion == 1:
    HiddenEye()
  elif opcion == 2:
    SocialPhish()
  elif opcion == 3:
    SocialFish()
  elif opcion == 4:
    PhisherMan()
  elif opcion == 5:
    Shellphish()
  elif opcion == 6:
    Wifiphisher()
  elif opcion == 7:
    Modlishka()
  else:
    return menu()


os.system('clear')

print ('''

---------------------------------------------------------------->
|                                                               |
|       ████████╗ ██████╗  ██████╗ ██╗     ███████╗             |
|       ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝             |
|          ██║   ██║   ██║██║   ██║██║     ███████╗             |
|          ██║   ██║   ██║██║   ██║██║     ╚════██║             |
|          ██║   ╚██████╔╝╚██████╔╝███████╗███████║             |
|                                                               | 
|   ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗    |
|   ██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝    |
|   ██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗   |
|   ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║   |
|   ██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝   |
|   ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝    |
<---------------------------------------------------------------- ''').format(GREEN, END)
print '{}HERRAMIENTAS PHISHING TODO EN UNO'.format(RED, END).center(65) 
print '{} EL ROBO DE CREDENCIALES MEDIANTE ESTA TECNICA ES LA MAS EFICAZ.'.format(GREEN, END)  
print '{0}Creado por: {3}Adrian Guillermo {2}({1}AdrMXR{2}) {0}Version: {3}1.0{2}{3}'.format(YELLOW, RED, YELLOW, BLUE).center(110)
print '{}================================================================='.format(GREEN, END)

if raw_input("¿Acepta utilizar esta herramienta con fines educativos? (y/n)\n--> ").upper() != "Y":
    os.system('clear') 
    print '\n{}NO HAS ACEPTADO UTILIZAR ESTA HERRAMIENTA CON FINES EDUCATIVOS.'.format(RED, END)	
    print ('''

       ▄████  ▒█████   ▒█████  ▓█████▄     ▄▄▄▄ ▓██   ██▓▓█████ 
      ██▒ ▀█▒▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌   ▓█████▄▒██  ██▒▓█   ▀ 
     ▒██░▄▄▄░▒██░  ██▒▒██░  ██▒░██   █▌   ▒██▒ ▄██▒██ ██░▒███   
     ░▓█  ██▓▒██   ██░▒██   ██░░▓█▄   ▌   ▒██░█▀  ░ ▐██▓░▒▓█  ▄ 
     ░▒▓███▀▒░ ████▓▒░░ ████▓▒░░▒████▓    ░▓█  ▀█▓░ ██▒▓░░▒████▒
      ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒    ░▒▓███▀▒ ██▒▒▒ ░░ ▒░ ░
       ░   ░   ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒    ▒░▒   ░▓██ ░▒░  ░ ░  ░
     ░ ░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░     ░    ░▒ ▒ ░░     ░   
           ░     ░ ░      ░ ░     ░        ░     ░ ░        ░  ░
                           ░               ░░ ░            
                           										''').format(RED, END).center(40)
    exit(0)


print ('''
NNNNNNNNNNNNNNNNNNNNNNNNKOo:'.     .'ckX
NNNNNNNNNNNNNNNNNNNNNX0d,.   .';:;'.  .l
NNNNNNNNNNNNNNNNNNNK0d'   .coccxKNXk,  .	
NNNNNNNNNNNNNNNNNN0c..  'd0Xx. 'kNNNo.
NNNNNNNNNNNNNNNNN0:    :0NNNKkdkXNNXc
NNNNNNNX0KNNNNNN0:    :KNNNNNNNNNNXd.  ,
NNNNNXOc'dNNNNNKc     .o0XNNNNNNN0l.  'k
NNNXOc. .xNNNNNd.   .   'o0NNNX0o'   ;ON
NXOc.   'ONNNNO'  .x0x,   .lxo;.   'dKNN
0l.     ;KNNNK:  .oXNXO:        .:xKNNNN
,  .:dc'oXXNNd.  .::;,..    .;lx0XNNNNNN
   cKNX0KXNXk'        ..;cok0XNNNNNNNNNN
   lXNNNNXO:.  .';codxOKXNNNNNNNNNNNNNNN
'  .:dkkd;.  .ckXXNNNNNNNNNNNNNNNNNNNNNN
Oc.        .:kXNNXXKKK00OkkkKXNNNNNNNNNN
NXOoc;,.   lXNNN0o,''.....'o0NNNNNNNNNNN
NNNNNXKl  .lXNNNXk,     .lONNNNNNNNNNNNN
NNNNNNNO,  .:dkxo;.   .l0XNNNNNNNNNNNNNN
NNNNNNNNOc.        .;l0XNNNNNNNNNNNNNNNN
NNNNNNNNNXk:.   .'cOXNNNNNNNNNNNNNNNNNNN ''').format(GREEN, END)

menu()



