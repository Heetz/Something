# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n>
#  y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.


num1 = input("Ingrese dos numeros enteros : ")
num2 = input("Ingrese el sgte numero entero : ")

cociente = (float(num1) / float(num2) )

resto = (float(num1) % float(num2))

print("Los numeros introducidos son: " +str(num1) + " y " +str(num2)) 
print("El cociente es : " +str(cociente) , " \nEl resto de la division es : " +str(resto))

