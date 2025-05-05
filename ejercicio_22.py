

# Definir variable por lo que ingresa el usuario

entero = int(input("Ingrese un número entero: "))

#Imprimir información 

print("Los número impares menores a", entero, "son:")

# Crear ciclo del número 1 al ingresado por el usuario que cumpla la condicion de ser impar


for i in range(1, entero):
    if i % 2 != 0:          # si el resto de la division es diferente de 0, osea impar, va a imprimirse
        print(i," ")





