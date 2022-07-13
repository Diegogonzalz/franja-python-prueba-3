
import numpy as np
import random




def escribir_archivo():
    
    nombre_fichero = "./numeros_prueba.txt"
    with open(nombre_fichero, "w", encoding="utf-8") as file:
        for i in range(1, 21):
            numero_aleatorio = random.randint(100, 1000)
            linea = str(numero_aleatorio)

            file.write(linea)
            file.write("\n")

def leer():
    numeros = []
    with open("./numeros_prueba.txt","r") as file:
        for linea in file:
            numeros.append(int(linea))
    num_impar = []
    for n in numeros:
        if n % 2 != 0:
            num_impar.append(n)
    return num_impar

def main ():
    escribir_archivo()
    num_impar = leer()

    print(num_impar)
    arreglo = np.array(num_impar)
    print(arreglo.ndim)
    
if __name__ == '__main__':
    main()