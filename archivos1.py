from io import open

'''archivo_texto=open('nombres.txt','r')
archivo_texto.write('\n hola')
#print(archivo_texto.read())
#archivo_texto.seek(0)
for lineas in archivo_texto.readlines():
    print(lineas.rsplit())
    
archivo_texto.close()'''

archivo_texto = open('nombres.txt', 'a')  # Abre el archivo en modo de añadir ('a')

archivo_texto.write('\nHola')  # Escribe en el archivo
archivo_texto.close()  # Cierra el archivo después de escribir

# Abre el archivo en modo de lectura ('r')
archivo_texto = open('nombres.txt', 'r')

# Itera sobre cada línea del archivo y la imprime
for linea in archivo_texto.readlines():
    print(linea.strip())  # Utiliza strip() para eliminar los espacios en blanco y saltos de línea

archivo_texto.close()  # Cierra el archivo después de leer
