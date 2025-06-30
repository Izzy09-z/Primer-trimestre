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
# notas = []
# entrada = input("Ingresa la primera nota de 0 a 5.0 (ingresa 'salir' para terminar): ")
# while entrada != "salir":
#     try:
#         nota = float(entrada)
#         if 0.0 <= nota <= 5.0:
#             notas.append(nota)
#         else:
#             print("Nota inválida. Debe estar entre 0 y 5.0")
#     except ValueError:
#         print("Entrada inválida. Debe ser un número o 'salir'")
#     entrada = input("Ingresa otra nota (o 'salir' para terminar): ")

# if notas:
#     promedio = sum(notas) / len(notas)
#     print(f"El promedio de notas es: {promedio:.2f}")
# else:
#     print("No se ingresaron notas válidas.")

#6 TABLA DE MULTIPLICAR INTERACTIVA
# num_de_tabla=int(input("Ingresa el numero de la tabla de multiplica que quieras ver: "))
# contador= 1
# while contador<=10:
#     resultado= num_de_tabla*contador
#     print(f"{num_de_tabla}*{contador}={resultado}")
#     contador +=1

#7 ADIVINA EL NUMERO
# numero_secreto = 17
# while True:
#     intento = int(input("Adivina el número secreto: "))
#     if intento == numero_secreto:
#         print("¡Correcto! Has adivinado el número.")
#         break
#     elif intento < numero_secreto:
#         print("El número secreto es mayor.")
#     else:
#         print("El número secreto es menor.")

#8 TUPLA DE FRUTAS
# tupla=("manzana","fresa","mango", "piña")
# while True:
#     fruta=input("Ingresa el nombre de una fruta que creas que está en la tupla: ")
#     if fruta=="manzana":
#         print("Correcto, adivinaste! Esta fruta está en la tupla ")
#         break
#     elif fruta=="fresa":
#         print("Correcto, adivinaste! Esta fruta está en la tupla ")
#         break
#     elif fruta=="mango":
#         print("Correcto, adivinaste! Esta fruta está en la tupla ")
#         break
#     elif fruta=="piña":
#         print("Correcto, adivinaste! Esta fruta está en la tupla ")
#         break
#     else:
#         print("Oh la fruta que escribiste no está en la tupla!.Sigue intando")

#9 DICCIONARIO DE TRADUCCION
# diccionario={"pez":"fish",
#              "leon":"lion",
#              "mono":"monkey",
#              "perro":"dog",
#              "gato":"cat"}
# while True:
#     animal=input("Ingresa un animal para ver su traduccion (se verá solo si está en el diccionario): ").lower()
#     if animal == "salir":
#         print("¡Hasta luego!")
#         break
#     if animal in diccionario:
#         print(f"La traducción de '{animal}' es '{diccionario[animal]}'.")
#     else:
#         print("La palabra no está en el diccionario.")

#10 CALCULADORA BASICA
# menu=input("Escoge una operacion de la lista: SUMA(+),RESTA(-),MULTIPLICACION(*),DIVISION(/) o escribe 'SALIR' para terminar: ").upper()

# while True: 
#     if menu=="+":
#         num1=int(input("Ingresa un numero para la operacion: ")) 
#         num2=int(input("Ingresa un segundo numero para la operacion: "))
#         result= num1+num2
#         print(f"El resultado de {num1}+{num2} es {result}")
#         break
#     elif menu=="-":
#         num1=int(input("Ingresa un numero para la operacion: ")) 
#         num2=int(input("Ingresa un segundo numero para la operacion: "))
#         result= num1-num2
#         print(f"El resultado de {num1}-{num2} es {result}")
#         break
#     elif menu=="*":
#         num1=int(input("Ingresa un numero para la operacion: ")) 
#         num2=int(input("Ingresa un segundo numero para la operacion: "))
#         result= num1*num2
#         print(f"El resultado de {num1}*{num2} es {result}")
#         break
#     elif menu=="/":
#         num1=int(input("Ingresa un numero para la operacion: ")) 
#         num2=int(input("Ingresa un segundo numero para la operacion: "))
#         result= num1/num2
#         print(f"El resultado de {num1}/{num2} es {result}")
#         break
#     elif menu=='SALIR':
#         print("El programa finalizó")

#11 REGISTRO DE EDADES
# personas = {}
# while True:
#     nombre = input("Escribe el nombre de la persona ('salir' para terminar): ")
#     if nombre.lower() == "salir":
#         break
#     edad = input(f"Escribe la edad de {nombre}: ")
#     personas[nombre] = edad

# print("Diccionario de personas y edades:")
# print(personas)

#12 BUSCAR EN LISTA
# colores = ["rojo", "azul", "verde", "amarillo", "negro"]

# while True:
#     color = input("Escribe un color: ").lower()
#     if color in colores:
#         print(f"¡Encontraste un color de la lista: {color}!")
#         break
#     else:
#         print("No está en la lista. Intenta de nuevo.")

#13 POTENCIAS DE UN NUMERO
# numero = int(input("Escribe un número: "))
# potencia = 1
# while potencia <= 5:
#     print(f"{numero}^{potencia} = {numero ** potencia}")
#     potencia += 1

#14 LISTA DE CUADRADOS
# cuadrados = []
# contador = 1
# while contador <= 5:
#     numero = int(input(f"Escribe el número {contador}: "))
#     cuadrados.append(numero ** 2)
#     contador += 1
# print("Lista de cuadrados:", cuadrados)

#15 DICCIONARIO DE ESTUDIANTES
# estudiantes = {}
# while True:
#     nombre = input("Nombre del estudiante (escribe 'fin' para terminar): ")
#     if nombre.lower() == "fin":
#         break
#     nota = float(input(f"Nota final de {nombre}: "))
#     estudiantes[nombre] = nota
# print("Diccionario de estudiantes y sus notas:")
# print(estudiantes)