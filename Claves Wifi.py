import os
var1=input("Desea crear la carpeta c:/claveswifi para geerar el archivo?  S/N: ").upper()
if var1=="S":
    cmd3="md c:\claveswifi"
    runcmd3=os.popen(cmd3)
        
cmd="netsh wlan show profile"
resultado=os.popen(cmd)
print(resultado.read())
#miarchivo=open('c:/clavesfifi/wifi.csv','a')
miarchivo=open('c:/claveswifi/wifi.csv','a')
red=input("Cual red desea saber la clave: ")
cmd2="netsh wlan show profile "+'"'+red+'"'+" key=clear"
resultado2=os.popen(cmd2)
miarchivo.write(resultado2.read())
print("Archivo csv fue creado en c:\claveswifi\wifi.csv")