#

# defino variable para el comienzo del ciclo

inicio = int(input("Ingrese un número entero: "))

# defino fin del ciclo 

fin = (inicio + 100)

#defino variable para guardar la suma 

suma = 0

# defino variable para no cambiar el valor inicial (inicio)

contador = inicio 

#defino el ciclo e inecuacion para que funcione 

while (contador <= fin) :
    suma = suma + contador
    contador += 1




print("El resultado de la suma de sus cien números siguientes es:", suma)

