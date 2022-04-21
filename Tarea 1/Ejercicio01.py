# 1- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cant_invertir = int(input("Ingrese la cantidad a invertir: "))
cant_interes = int(input("Ingrese el interes anual: "))
cant_anos = int(input("Numero de años : "))

capital_final = cant_invertir + (cant_interes + 1) * cant_anos

print ("-------------------------------------------")
print("Años a invertir: " +str(cant_invertir) )
print("Interes anual: "+str(cant_interes))
print("Numero de años: " +str(cant_anos))
print ("-------------------------------------------")
    
print("Capital obtenido por la inversion : " +str(capital_final))