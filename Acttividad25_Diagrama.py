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
# total = int(input("Introduce el total de la compra: "))
# if total > 100:
#     descuento = total * 0.10
#     pre_final = total - descuento
#     print("El total supera $100. Se aplica un descuento del 10%.")
#     print("Precio final: ", pre_final)
# else:
#     print("No se aplica descuento. Precio final: ", total)

#Verificar si una persona puede votar (mayor o igual a 18 años).
# persona=int(input("Ingresa tu edad: "))
# if persona>=18:
#     print("Puedes votar, tienes la edad requerida")
# else:
#     print("No puedes votar, aun no cumples con la edad requerida")

#Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP.
# cliente=input("Coloca el tipo de cliente que eres: VIP o NORMAL: ")
# precio=float(input("Ahora ingresa el precio: "))
# if cliente=="vip":
#     descuento=precio*0.20
#     pre_final=precio-descuento
#     print("Eres VIP, tienes un 20% de descuento")
#     print("Precio final: " ,pre_final)
# else:
#     print("Como eres tipo NORMAL de cliente, no se aplica el descuento. Por consiguiente tu precio es: " ,precio)

#Determinar si un número es múltiplo de 5 y de 3 al mismo tiempo.
# numer=int(input("Ingresa un numero entero: "))
# if numer % 3 == 0 and numer % 5 == 0:
#     print("El número es múltiplo de 3 y de 5 al mismo tiempo")
# elif numer % 3 == 0:
#     print("El número es múltiplo solo de 3")
# elif numer % 5 == 0:
#     print("El número es múltiplo solo de 5")
# else:
#     print("El número no es múltiplo de 3 ni de 5")

#Verificar si es divisible entre dos números dados.
# numero = int(input("Introduce el número a verificar: "))
# divi1 = int(input("Introduce el primer divisor: "))
# divi2 = int(input("Introduce el segundo divisor: "))
# if numero % divi1 == 0 and numero % divi2 == 0:
#     print("El número " ,numero ,"es divisible entre" ,divi1 ,"y" ,divi2)
# elif numero % divi1 == 0:
#     print("El número" ,numero ,"es divisible solo entre" ,divi1)
# elif numero % divi2 == 0:
#     print("El número" ,numero ,"es divisible solo entre" ,divi2)
# else:
#     print("El número" ,numero ,"no es divisible entre" ,divi1 ,"ni entre" ,divi2)


#EJERCICIOS CON LISTAS(CON CONDICIONALES)

#Crear lista y si el tercer número es mayor que 10, muestra “Mayor a 10”, si no, muestra “Menor o igual a 10”.
# lista1 = [1, 3, 4, 7, 11]
# if lista1[2] > 10:
#     print("Mayor a 10")
# else:
#     print("Menor o igual a 10")

#Verificar si el número 7 está en la lista [3, 5, 7, 9]. Si está, muestra “Está en la lista”, si no, muestra “No está en la lista”
# lista2=[3, 5, 7, 9]
# if lista2 [2]==7:
#     print("Está en la lista")
# else:
#     print("No está en la lista")

#Sumar los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”.
# lista3= [4, 6, 2, 8]
# suma=lista3[0]+lista3[1]
# if suma >10:
#     print("Suma alta")
# else:
#     print("Suma baja")

#Dada la lista ["Ana", "Luis", "Pedro", "Marta"], muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”.
# lista4=["Ana", "Luis", "Pedro", "Marta"]
# nom=lista4[3]
# if nom:
#     print("Nombre correcto")
# else:
#     print("Nombre diferente")

#Crear una lista con tres colores. Cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada.
# lista5=["Blanco","Verde","Morado"]
# print(lista5)
# lista5[1]="Azul"
# print("Nuevo color" ,lista5)


#EJERCICIOS CON TUPLAS (CON CONDICIONALES)

#Crear una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”.
# tupla1=(5, 8, 12, 20)
# if tupla1[0] < tupla1[3]:
#     print("Es de Orden ascendente")
# else:
#     print("Es de Orden descendente")

#Verificar si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30” de la siguiente tupla: (25, 32, 28)".
# tupla2=(25, 32, 28)
# if tupla2[1] >30:
#     print("Edad mayor a 30")
# else: 
#     print("Edad menor o igual a 30")

#Convertir la tupla (1, 2, 3) a lista, cambiar el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.
# tupla3=(1, 2, 3)
# print("Tupla: " ,tupla3)
# lista = list(tupla3)
# if lista[1] == 2:
#     lista[1] = 10
#     print("Es posible cambiarla")
# else:
#     print("No es posible")

# tupla = tuple(lista)
# print("Nueva tupla:", tupla)

#Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra “Coordenada alta”, si no, “Coordenada baja”.
# tupla4= (4, 9)
# if tupla4[1]>5:
#     print("Coordenada alta")
# else: 
#     print("Coordenada baja")

#Comparar si las tuplas (3, 4) y (3, 5) son iguales. Si lo son, muestra “Tuplas iguales”, si no, “Tuplas diferentes”.
# tup1=(3, 4)
# tup2=(3, 5)
# if tup1==tup2:
#     print("Tuplas iguales")
# else: 
#     print("Tuplas diferentes")


#EJERCICIOS CON DICCIONARIOS (CON CONDICIONALES)

#Crear un diccionario con {"nombre": "Juan", "edad": 17}. Si la edad es mayor o igual a 18, muestra “Adulto”, si no, muestra “Menor de edad”
# diccionario1={
#     "Nombre":"Juan",
#     "Edad":17 }
# if diccionario1["Edad"]>=18:
#     print("Adulto")
# else:
#     print("Menor de edad")

#Crea un diccionario {"nombre": "Lucía", "edad": 20}. Si la edad es mayor a 18, cambia el valor de “edad” a 21. Luego muestra el diccionario.
# diccionario2 = {
#     "Nombre": "Lucía",
#     "Edad": 20
# }
# if diccionario2["Edad"] > 18:
#     print("El valor será modificado")
#     diccionario2["Edad"] = 21 
#     print("El nuevo diccionario es:", diccionario2)
# else:
#     print("El valor no será modificado")

#Crear un diccionario con {"Nombre":"Carlos"}. Si la clave "Ciudad" no existe, agregala con el valor "Bogotá" y muestra el diccionario
# Crear el diccionario inicial
# diccionario4 = {"Nombre": "Carlos"}
# if "Ciudad" in diccionario4:
#     print("La clave 'Ciudad' ya existe en el diccionario.")
# elif "Ciudad" not in diccionario4:
#     diccionario4["Ciudad"] = "Bogotá"
#     print("Se agregó la clave 'Ciudad' con el valor 'Bogotá'.")
# else:
#     print("No se pudo verificar la clave 'Ciudad'.")
# print(diccionario4)

#   Dado el diccionario {"Producto":"pan","Precio":1200} verificar si la clave "Precio" existe. Si existe, muestra su valor, si no, muestra "No hay precio"
# diccionario5={"Producto":"pan","Precio":1200}
# if "Precio" in diccionario5:
#     print("La clave 'Precio' ya existe en el diccionario")
#     print("El precio de la clave 'Precio' es de: " ,diccionario5["Precio"])
# elif "Precio" not in diccionario5:
#     print("No hay precio")
# else:
#     print("No se puede verificar la clave 'Precio'")

#Crear un diccionario con {"Pan":1200,"Leche":2000}. Si "pan" está en el diccionario, muestra su precio:si no, muestra "Producto no disponible"
# diccionario6={"Pan":1200,"Leche":2000}
# if "Pan" in diccionario6:
#     print("La clave 'Pan' está en el diccionario, su precio es: " ,diccionario6["Pan"])
# elif "Pan" not in diccionario6:
#     print(" Producto no disponible")
# else:
#     print("No se puede verificar la palabra 'Pan'")
