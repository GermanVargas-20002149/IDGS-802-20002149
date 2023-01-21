num1 = 20
num2 = 0

#print("La divicion de {} / {} es:".format(num1, num2, num1/num2))

try:
    resultado = num1/num2
except ZeroDivisionError:
    print("Error en el programa......................................")
finally:
    print("Yo siempre aparezco")