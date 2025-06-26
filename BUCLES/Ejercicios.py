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
# contador=0
# par=0
# impar=0
# while contador < 10:
#     numer=int(input("Ingresa un numero entero: "))
#     if numer %2==0:
#         par= par + 1
#     else:
#         impar = impar + 1
#     contador = contador + 1
# print(f"Pares {par} Impar {impar}")

#5. PROMEDIO DE CALIFICACIONES
notas=[ ]
entrada=(input("Ingresa la primera nota de 0 a 5.0 (ingresa 'salir' para terminar): "))
while entrada !="salir":
    nota=float(entrada)
    if 0.0 <= nota <= 5.0:
        notas.append(nota)
    else: 
        print("Nota invalida. Debe estar entre 0 y 5.0")
        entrada=input("Ingresa otra nota: ")
if notas:
    promedio=sum(notas)/len(notas)
    print(f"El promedio de notas es: {promedio, 2}")
else:
    print("No se ingresaron notaas validad.")