#EJEMPLO DE IF
 
edad=int(input("Ingresa una edad: "))
if edad >=18:
    print("Si cumple con la condicion, eres mayor de edad")

#EJEMPLO DE ELSE
numero=24
if numero>36:
   print("El numero es grande")
else:
    print("El numero es chico")

#EJEMPLO DE MULTIPLE IF
x=25
if x > 10:
    print("Por encima de diez")
    if x > 20:
        print("Y tambien por encima de 20!")
    else:
        print("Pero no por encima de 20")