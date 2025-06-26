#EJERCICIOS CON WHILE, CONDICIONALES Y ESTRUCTURAS

#1. SUMA HASTA CERO
# total=0
# num1=int(input("Ingresa un numero entero: "))
# while num1 !=0:
#     total +=num1
#     num1=int(input("Ingresa otro numero(0 para terminar): "))
# print(f"La suma total es: {total}. El programa finalizó")

#2. CONTRASEÑA INCORRECTA
# clave= input("Escribe la contraseña: ")
# while clave !="python123":
#     print("Contraseña incorrecta")
#     clave=input("Intentalo de nuevo: ")
# print("Acceso concedido")

#3. LISTA DE COMPRAS
# lista=[ ]
# produc1=input("Ingresa el primer producto('fin' para terminar): ")
# while produc1.lower() != "fin":
#     lista.append(produc1)
#     produc1=input("Ingresa otro producto: ")
# print(f"Tu lista es {lista}")

#4. CONTADOR DE PARES E IMPARES
contador=0
par=0
impar=0
while contador < 10:
    numer=int(input("Ingresa un numero entero: "))
    if numer %2==0:
        par += 1
        print(f"{numer} es par")
    else:
        print(f"{numer} es impar")
        impar += 1
    contador += 1

print(F"Se han ingresado 10 numeros{contador}")

#5. PROMEDIO DE CALIFICACIONES