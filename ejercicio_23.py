
# definir funcion llamada euclides que usa el algoritmo "euclides"

def euclides(x , y):

    while y:
        x , y =  y , x % y  # en el ciclo, "x" va tomar el valor de "y" despues "y" va a tomar el valor del residuo entre x/y
    return x            # al fin del ciclo devuelve el valor de "X"
    

entero1 = int(input("Ingrese el número entero que es mayor: "))

entero2 = int(input("Ingrese el número entero que es menor: "))

gcd = euclides(entero1 , entero2)

print("El Máximo Común Divisor (gcd) de", entero1 , "y" , entero2 , "es:" , gcd)
