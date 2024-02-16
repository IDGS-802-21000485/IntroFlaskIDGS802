from io import open

archivo_texto=open('nombres.txt','r')
#archivo_texto.write('\n datos en el archivo')
#print(archivo_texto.read())
#archivo_texto.seek(0)


for lineas in archivo_texto.readlines():
    print(lineas.rsplit())
    
archivo_texto.close()