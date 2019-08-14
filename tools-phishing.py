#!/usr/bin/python
# -*- coding: utf-8 -*-
#Copyright 2019 tools_phishing
#Written by: Adrian Guillermo
#Facebook: Adrian Guillero
#Github: 

from time import sleep
from sys import stdout, argv, exit
import pyfiglet
import os
import time 
import string

BLUE, RED, WHITE, CYAN, DEFAULT, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\033[36m', '\033[0m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def HiddenEye():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop):\n--> ")
  os.system('cd {} && mkdir HiddenEye && git clone https://github.com/DarkSecDevelopers/HiddenEye.git'.format(directory))
  exit(0) 

def SocialPhish():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop): \n--> ")
  os.system('cd {} && mkdir SocialPhish && git clone https://github.com/xHak9x/SocialPhish.git'.format(directory))
  exit(0)

def SocialFish():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop): \n--> ")
  os.system('cd {} && mkdir SocialFish && git clone https://github.com/UndeadSec/SocialFish.git'.format(directory))
  exit(0)

def PhisherMan():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop): \n--> ")
  os.system('cd {} && mkdir Phisher-man && git clone https://github.com/FDX100/Phisher-man.git'.format(directory))
  exit(0)

def Shellphish():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop): \n--> ")
  os.system('cd {} && git clone https://github.com/thelinuxchoice/shellphish.git'.format(directory))
  exit(0)

def Wifiphisher():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop): \n--> ")
  os.system('cd {} && git clone https://github.com/wifiphisher/wifiphisher.git'.format(directory))
  exit(0)

def Modlishka():
  directory = raw_input("Ingrese la ruta donde desea guardar la herramienta (Ej: /root/Desktop): \n--> ")
  os.system('cd {} && mkdir Modlishka && git clone https://github.com/drk1wi/Modlishka.git'.format(directory))
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
    os.system('clear')
    print("\n{}No has elegido ninguna opcion").format(RED)
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



