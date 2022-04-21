#-Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.


user_peso = input("Ingrese su peso (kg) : ")
user_estatura = input("Ingrese su estatura (metros) : ")
user_imc = (float(user_peso) / float(user_estatura))

print("Tu indice de masa corporal es : " +str(round(user_imc, 2)) )
