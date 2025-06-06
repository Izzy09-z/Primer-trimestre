#EJERCIOS DE CONDICIONALES Y OPERACIONES MATEMATICAS
#Verificacion de numero positivo o negativo
# num=int(input("Ingrese un numero: "))
# if num<0:
#     print("El numero que escribiste es negativo")
# elif num>0:
#     print("El numero que escribiste es positivo")
# else:
#     print("El numero que escribiste es cero")
 
#Calcular el mayor de dos numeros ingresados
# numer1=int(input("Ingresa un numero: "))
# numer2=int(input("Ingresa un segundo numero: "))
# if numer1<numer2:
#     print("El primero numero es menor que el segundo")
# elif numer1>numer2:
#     print("El primer numero es mayor que el segundo")
# else:
#     print("Ambos numeros son iguales")

#Determinar si un número es par o impar
# num=int(input("Ingrese un numero: "))
# if num %2== 0:
#     print("El número es par")
# elif num %2== 1:
#     print("El número es impar")
# else:
#     print("Eso no parece un número entero")

#Verificar si está entre 10 y 20
# numero = int(input("Ingresa un número: "))
# if numero >= 10 and numero <= 20:
#     print("El número está entre 10 y 20.")
# elif numero < 10:
#     print("El número es menor que 10.")
# else:
#     print("El número es mayor que 20.")

# Encuentrar el mayor de los tres numeros usando condicionales.
# Solicitar los tres números al usuario
# num1 = int(input("Ingresa el primer número: "))
# num2 = int(input("Ingresa el segundo número: "))
# num3 = int(input("Ingresa el tercer número: "))
# if num1 >= num2 and num1 >= num3:
#     print("El mayor es:", num1)
# elif num2 >= num1 and num2 >= num3:
#     print("El mayor es:", num2)
# else:
#     print("El mayor es:", num3)

#Precio final con un 10% de descuento si el total es mayor a $100.
total = int(input("Introduce el total de la compra: "))
if total > 100:
    descuento = total * 0.10
    pre_final = total - descuento
    print("El total supera $100. Se aplica un descuento del 10%.")
    print("Precio final: ", pre_final)
else:
    print("No se aplica descuento. Precio final: ", total)