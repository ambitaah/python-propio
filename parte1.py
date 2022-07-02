#edad=input("cual es tu edad? ")
#print("tu edad es", edad, "años")

#nombre=input("Cual es tu nombre y apellido? ")
#print("Mi nombre y apellido es", nombre, "Flor Inorreta")

# edad=input("Cual es tu edad? ")
# if int(edad) < 18:
#     print("No podes pasar")
# elif int(edad) > 18:
#     print("Podes pasar :)")
# else:
#     print("edad invalida")

# nombre=input("Cual es tu nombre? ")
# edad=input("Cual es tu edad? ")
# if int(edad) < 18:
#     print("No podes pasar ", nombre)
# elif int(edad) > 18:
#     print("Podes pasar ", nombre)

# nombre="Cual es tu nombre? "
# input(nombre)
# edad="Cual es tu edad? "
# input(edad)

#primero pedir dos numeros
#luego preguntar que operacion hacer con esos numeros
#cuando sepa que hacer entonces hago la operacion y muestro los resultados

# numero1=int(input("Dame un primer numero: "))
# numero2=int(input("Dame un segundo numero: "))
# operacion=input("Dame una operacion para hacer con estos dos numeros: ")

# if operacion == "*":
#     print("El resultado es:", numero1 * numero2)


#La super calculadora

numero1=int(input("Primer numero: "))
numero2=int(input("Segundo numero: "))
operacion=input("Dame una operacion: ")
resultado=0

if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    resultado = numero1 / numero2
print("El resultado es:", resultado)
