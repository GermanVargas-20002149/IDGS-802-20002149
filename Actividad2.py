# Permite limpiar la pantalla
import os

class OperasBas:
    # declaracion de propiedades 
    num1 = 0
    num2 = 0
    res = 0
    opc = 0

    # declaracion de constructor
    def __init__(self):
        pass

    # declaracion de metodos de clase
    def suma(self):
        self.num1 = int(input("Ingresa el primer numero"))
        self.num2 = int(input("Ingresa el segundo numero"))
        self.res = self.num1 + self.num2
        print("La suma es: {}".format(self.res))
    
    def resta(self):
        self.num1 = int(input("Ingresa el primer numero"))
        self.num2 = int(input("Ingresa el segundo numero"))
        self.res = self.num2 - self.num1
        print("La resta es: {}".format(self.res))

    def mul(self):
        self.num1 = int(input("Ingresa el primer numero"))
        self.num2 = int(input("Ingresa el segundo numero"))
        self.res = self.num1 * self.num2
        print("La multiplicacion es: {}".format(self.res))

    def div(self):
        self.num1 = int(input("Ingresa el primer numero"))
        self.num2 = int(input("Ingresa el segundo numero"))
        self.res = self.num2 / self.num1
        print("La division es: {}".format(self.res))
    
    def menu(self):
        print("Menu de opciones")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicacion")
        print("4.- Division")
        print("5.- Salir")
        self.opc = int(input("Ingresa el numero de la operacion que deseas realizar"))
        return self.opc
        

def main():
    #Linea para limpiar la terminal
    os.system('cls')
    obj = OperasBas()
    opc = obj.menu()

    while opc < 5:
        os.system('cls')
        if opc == 1:
            obj.suma()
        elif opc == 2:
            obj.resta()
        elif opc == 3:
            obj.mul()
        elif opc == 4:
            obj.div()
        opc = obj.menu()


if __name__ == "__main__":
    main()
