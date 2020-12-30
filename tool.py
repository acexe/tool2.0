__autor__ = '@alexis.z40'

import socket
from colorama import *
import time
import os
from gtts import gTTS
import platform
import pafy
import geocoder


sistema = platform.system()

if sistema == 'Windows':
    os.system("cls")
else:
    os.system("clear")

print(Fore.BLUE + "░█─▄▀ ░█▀▀▀█ ░█▀▀▄ ─█▀▀█ ▀▀█▀▀ ░█▀▀▀█ ░█▀▀▀█ ░█───" + Fore.RESET) 
print(Fore.BLUE + "░█▀▄─ ░█──░█ ░█─░█ ░█▄▄█ ─░█── ░█──░█ ░█──░█ ░█───" + Fore.RESET)
print(Fore.BLUE + "░█─░█ ░█▄▄▄█ ░█▄▄▀ ░█─░█ ─░█── ░█▄▄▄█ ░█▄▄▄█ ░█▄▄█" + Fore.RESET)
print("\n")
print(time.strftime("%d/%m/%y"))
print(time.strftime("%I:%M:%S"))
print("\n")

print(Fore.GREEN + "OPCIONES" + Fore.RESET)
print("(1) Ipweb")
print("(2) De texto a audio transformador")
print("(3) Descargar videos de YouTube")
print("(4) Localizar ip")
print("(5) Salir \n")
print(Fore.RED + "CODE BY @alexis.z40" + Fore.RESET)

while True:  
    respuesta = int(input("Opcion >> "))
    if respuesta == 1:
        if sistema == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(Fore.GREEN + "██╗██████╗░  ░██╗░░░░░░░██╗███████╗██████╗░" + Fore.RESET)
        print(Fore.GREEN + "██║██╔══██╗  ░██║░░██╗░░██║██╔════╝██╔══██╗" + Fore.RESET)
        print(Fore.GREEN + "██║██████╔╝  ░╚██╗████╗██╔╝█████╗░░██████╦╝" + Fore.RESET)
        print(Fore.GREEN + "██║██╔═══╝░  ░░████╔═████║░██╔══╝░░██╔══██╗" + Fore.RESET)
        print(Fore.GREEN + "██║██║░░░░░  ░░╚██╔╝░╚██╔╝░███████╗██████╦╝" + Fore.RESET)
        print(Fore.GREEN + "╚═╝╚═╝░░░░░  ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░ " + Fore.RESET)
        time.sleep(1)

        print(Fore.RED + "----------------------------" + Fore.RESET)
        print(Fore.RED + "- MANERA DE COLOCAR LA WEB -" + Fore.RESET)
        print(Fore.RED + "----------------------------" + Fore.RESET)
        time.sleep(1)

        print(Fore.GREEN + "www.google.com.mx" + Fore.RESET)
        print(Fore.RED + "https://www.google.com.mx/" + Fore.RESET)
        time.sleep(2)

        url = input(Fore.GREEN + "Introduce URL >> " + Fore.RESET)

        print("IP: ",socket.gethostbyname(url))

    elif respuesta == 2:
        if sistema == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
    
        print(Fore.RED + "░█████╗░██╗░░░██╗██████╗░██╗░█████╗░" + Fore.RESET)
        print(Fore.RED + "██╔══██╗██║░░░██║██╔══██╗██║██╔══██╗" + Fore.RESET)
        print(Fore.RED + "███████║██║░░░██║██║░░██║██║██║░░██║" + Fore.RESET)
        print(Fore.RED + "██╔══██║██║░░░██║██║░░██║██║██║░░██║" + Fore.RESET)
        print(Fore.RED + "██║░░██║╚██████╔╝██████╔╝██║╚█████╔╝" + Fore.RESET)
        print(Fore.RED + "╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░" + Fore.RESET)
        time.sleep(1)


    
        texto = input("Escribe para transformar a audio >> ")
        nombre = input("Nombre para guardar el audio >> ")
        idioma = 'es'
        audio = gTTS(text=texto, lang= idioma, slow = False)
        audio.save(nombre+'.mp3')
        print(Fore.GREEN + "TEXTO A AUDIO SATISFACTORIAMENTE." + Fore.RESET)

    elif respuesta == 3:
        if sistema == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
    
        print(Fore.RED + "██╗░░░██╗██╗██████╗░███████╗░█████╗░" + Fore.RESET)
        print(Fore.RED + "██║░░░██║██║██╔══██╗██╔════╝██╔══██╗" + Fore.RESET)
        print(Fore.RED + "╚██╗░██╔╝██║██║░░██║█████╗░░██║░░██║" + Fore.RESET)
        print(Fore.RED + "░╚████╔╝░██║██║░░██║██╔══╝░░██║░░██║" + Fore.RESET)
        print(Fore.RED + "░░╚██╔╝░░██║██████╔╝███████╗╚█████╔╝" + Fore.RESET)
        print(Fore.RED + "░░░╚═╝░░░╚═╝╚═════╝░╚══════╝░╚════╝░" + Fore.RESET)
        time.sleep(1)
   
        url = input("URL del video >> ")
        ruta = input("Ruta para guardar video >> ")
        video = pafy.new(url)
        streams = video.streams
        for i in streams:
            print(i)
        best = video.getbest()
        print(best.resolution, best.extension)
        best.download(filepath=ruta)
        print(Fore.GREEN + "Descarga finalizada..." + Fore.RESET)


    elif respuesta == 4:
        if sistema == 'Windows':
            os.system("cls")
        else:
            os.system("clear")


    
        print(Fore.RED + '''╭╮╱╱╭━━━┳━━━┳━━━┳━━━━┳━━━┳━━━┳━━┳━━━╮
        ┃┃╱╱┃╭━╮┃╭━╮┃╭━╮┃╭╮╭╮┃╭━╮┃╭━╮┣┫┣┫╭━╮┃
        ┃┃╱╱┃┃╱┃┃┃╱╰┫┃╱┃┣╯┃┃╰┫┃╱┃┃╰━╯┃┃┃┃╰━╯┃
        ┃┃╱╭┫┃╱┃┃┃╱╭┫╰━╯┃╱┃┃╱┃┃╱┃┃╭╮╭╯┃┃┃╭━━╯
        ┃╰━╯┃╰━╯┃╰━╯┃╭━╮┃╱┃┃╱┃╰━╯┃┃┃╰┳┫┣┫┃
        ╰━━━┻━━━┻━━━┻╯╱╰╯╱╰╯╱╰━━━┻╯╰━┻━━┻╯''' + Fore.RESET)


        ip = input("IP >> ")
        myloc = geocoder.ip(ip)
        print(myloc)

    elif respuesta == 5:
        if sistema == 'Windows':
            os.system('cls')
        else:
            os.system("clear")
        print(Fore.GREEN + "Saliendo..." + Fore.RESET)
        time.sleep(2)
        break

         
    else:
        if sistema == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print('''
▒█▀▀▀█ ▒█▀▀█ ▒█▀▀█ ▀█▀ ▒█▀▀▀█ ▒█▄░▒█ 　 ▒█▄░▒█ ▒█▀▀▀█ 　 ▒█▀▀▄ ▀█▀ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▒█▄░▒█ ▀█▀ ▒█▀▀█ ▒█░░░ ▒█▀▀▀ 
▒█░░▒█ ▒█▄▄█ ▒█░░░ ▒█░ ▒█░░▒█ ▒█▒█▒█ 　 ▒█▒█▒█ ▒█░░▒█ 　 ▒█░▒█ ▒█░ ░▀▀▀▄▄ ▒█▄▄█ ▒█░░▒█ ▒█▒█▒█ ▒█░ ▒█▀▀▄ ▒█░░░ ▒█▀▀▀ 
▒█▄▄▄█ ▒█░░░ ▒█▄▄█ ▄█▄ ▒█▄▄▄█ ▒█░░▀█ 　 ▒█░░▀█ ▒█▄▄▄█ 　 ▒█▄▄▀ ▄█▄ ▒█▄▄▄█ ▒█░░░ ▒█▄▄▄█ ▒█░░▀█ ▄█▄ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄''')
    
