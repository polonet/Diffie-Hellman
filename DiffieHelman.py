import sys

def exp_rapida(base, exponente, modulo):
    x = 1
    y = base % modulo
    b = exponente

    while b > 0:

        if (b % 2) == 0:  # Si b es par...
            y = (y * y) % modulo
            b = b / 2
        else:  # Si b es impar...
            x = (x * y) % modulo
            b = b - 1
    return x



try:
    if sys.argv[1]== '-h':
        print("-----------------------------------------------------------")
        print("-----------------------------------------------------------")
        print("---------Algoritmo Diffie/Hellman--------------------------")
        print("-----------------Intercambio de Claves---------------------")
        print("|                                                         |")
        print("| Sintaxis:                                               |")
        print("| python3 DiffieHelman.py -hc <opcion>                    |")
        print("|                             <valores p alfa sec_A sec_B>|")
        print("|                                                         |")
        print("| <opcion> : -h  Ayuda, muestra la informacion de ayuda   |")
        print("|            -c  Inicia el programa y se deben colocar    |")
        print("|                 Los valores separados por espacios      |")
        print("|                                                         |")
        print("|                                                         |")
        print("| Ejemplo:                                                |")
        print("| python3 DiffieHelman -c 23 5 6 15                       |")
        print("|                                                         |")
        print("| Elaborado por:                                          |")
        print("| Jaime Alberto Gomez     jaime_alberto.gomez@uao.edu.co  |")
        print("| Hector Fabio Polanco    hector_fabio.polanco@uao.edu.co |")
        print(" ----------------------------------------------------------")
        print("| Universidad Autonoma de Occidente                       |")
        print("| Especialización en Seguridad Informatica                |")
        print("|                                                         |")
        print("| Profesor : Siler Amador D.    samador@unicauca.edu.co   |")	
        print(" ----------------------------------------------------------")		
        print("| Programa fuente:                                        |")
        print("| Universidad de La Laguna                                |")
        print("| Escuela Superior de Ingeniería y Tecnología             |")
        print("| Grado en Ingeniería Informática                         |")
        print("| Seguridad en Sistemas Informáticos                      |")
        print("| Autor : Kevin Estévez Expósito  (alu0100821390)         |")	
        print(" ----------------------------------------------------------")		


		
    else:
        if '-c' == sys.argv[1]:
            usu_a = {}  # datos necesarios para el usuario A
            usu_b = {}  # datos necesarios para el usuario B

			#p = Número primo público
            p = int(sys.argv[2])

            # alpha = Es la base público
            alpha = int(sys.argv[3])
            print()

            # usu_a['x'] = Es la clave secreta del usuario A
            usu_a['x'] = int(sys.argv[4])
            print("Usuario A: Calculando 'yA'... ", end="")

            # Se calcula el valor de yA, teniendo en cuenta que la clave de A debe ser menor que 'p' 
            usu_a['y'] = exp_rapida(alpha, usu_a['x'], p)
            print("'yA' = " + str(usu_a['y']))
            print()

            # usu_b['x'] = Es la clave secreta del usuario B
            usu_b['x'] = int(sys.argv[5])
            print("Usuario B: Calculando 'yB'... ", end="")

            # se calcula el valor de yB, teniendo en cuenta que la clave de B debe ser menor que 'p'
            usu_b['y'] = exp_rapida(alpha, usu_b['x'], p)
            print("'yB' = " + str(usu_b['y']))
            print()

            # Se simula el envío de yA al usuario B
            print("Transmitiendo'yA' al usuario B... ", end="")
            usu_b['y_prim'] = usu_a['y']
            print("Realizando el envio!")

            # Se simula el envío de yB al usuario A
            print("Transmitiendo 'yB' al usuario A... ", end="")
            usu_a['y_prim'] = usu_b['y']
            print("Realizando el envio!")
            print()
            print("Usuario A: Resultado clave 'k'... ", end="")

            # Se calcula el valor final de la clave para el usuario A
            usu_a['k'] = exp_rapida(usu_a['y_prim'], usu_a['x'], p)
            print("'k' = " + str(usu_a['k']))
            print("Usuario B: Resultado clave 'k'... ", end="")

            # Se calcula el valor final de la clave para el usuario B
            usu_b['k'] = exp_rapida(usu_b['y_prim'], usu_b['x'], p)
            print("'k' = " + str(usu_b['k']))
            print()

            # comprueba que las claves de los usuarios A y B coinciden
            print()
            if usu_a['k'] == usu_b['k'] :
                print("Muy Bien !!!!! Las claves coinciden!")
            else :
                print("Por favor revise sus datos iniciales! Las claves generadas NO coinciden!")
            sys.exit(0)
        else:
            print("comando invalido")
except:
    print("debe incluir el argumento -c o -h")
