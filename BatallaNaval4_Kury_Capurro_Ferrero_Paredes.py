'''
Objetivo del programa (descripción del problema que resuelve): Crear el juego "Batalla Naval" donde una persona juege contra la computadora 

Autor/es: Juan Segundo Kury, Tomas Ferrero, Nicolas Capurro, Bryan Paredes 

Versión: 4

Fecha: 20/07/2021

Análisis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba del programa):
Pedir que elijan la dificulad del tablero - posisionar los barcos - empiecen a elegir cordennadas xy para disparar - marcar al ganador cuando llegue a los 14 puntos 

Síntesis de Casos (composición de casos para la generalización):
Distintas dificultades de tablero (facil, medio, dificil) cuanto mas dificil sea menor cantidad de barcos habra en el tablero


Recursos (variables y funciones del programa -nombre y propósito)

    Datos a solicitar al usuario (sea en el prólogo o sea durante la resolución):
    Dificultad de tablero
    Cordenada inicial y final de los barcos para posisionarlos en el tablero
    Cordenadas xy donde queremos "disparar"
    
    Auxiliares (necesarios para transformaciones intermedias):
    
    Resultados (a informar sea durante el desarrollo o en el epílogo):
    En el tablero donde impacto el "disparo" (x o O)
    Ganador del juego

    Funciones propias (necesarias para la descomposición del problema en subproblemas):

'''
# DEFINICIÓN DE FUNCIONES (si se requieren para descomponer la solución del problema)
#def nom_función():
'''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):

    Objetivo (descripción de lo que hace o devuelve):

    Análisis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba
    de la función):

    Síntesis de Casos (composición de casos para la generalización):

    Recursos (variables o funciones internas -nombre y propósito)

    Auxiliares (necesarios para transformaciones intermedias):
    
    Resultados (si la función devuelve):

    Funciones internas (necesarias para la descomposición del problema en subproblemas):

    '''
    #1 PRÓLOGO
    # Establecimiento de valores iniciales para datos auxiliares o que se transformarán en resultados (opcional)

    #2 RESOLUCIÓN
    # Descomposición del problema en subproblemas 2.x que a su vez pueden requerir inicialización de datos o mostrar resultados

    #3 EPÍLOGO
    # Devolución de valor o valores o muestra de resultados

# PROGRAMA    
#1 PRÓLOGO
#1.1 Presentación
#1.1.1 Impresión del título del programa en pantalla
print("Bienvenido a la Batalla Naval")

#1.1.2 Descripción o aclaraciones al usuario (opcional)
print("El juego tiene disponible 3 dificultades")
print("Facil: tablero de 10x10 en el cual hay que ubicar 4 barcos de 2,3,4 y 5 casillas correspondientemente")
print("Medio: tablero de 10x10 en el cual hay que ubicar 3 barcos de 2,3 y 4 casillas correspondientemente")
print("Dificil: tablero de 10x10 en el cual hay que ubicar 2 barcos de 2 y 3 casillas correspondientemente")
    

#1.2 Datos iniciales 
#1.2.1 Solicitud e ingreso de datos desde teclado (opcional, si los datos se piden durante la resolución)

#1.2.2 Establecimiento de valores iniciales para datos auxiliares o que se transformarán en resultados (opcional)

#2 RESOLUCIÓN
# Descomposición del problema en subproblemas 2.x que a su vez pueden requerir ingreso o inicialización de datos o mostrar resultados
import random #se importa la libreria random
dif=input("Elija la dificultad del juego: ").lower()
while dif != "facil" and dif!= "medio" and dif!="dificil" and dif != "test":
    print("Por favor ingrese una dificltad valida")
    dif=input("Ingrese en que dificultad desea jugar: ").lower()
nombre=input("ingrese su nombre/apodo: ").upper()
def mostrarTablero(Tablero): #muestra un tablero especifico donde se añaden numeros para que el jugador pueda guiarse
    print("             ",nombre)
    print("    0  1  2  3  4  5  6  7  8  9")#se imprimen los numeros de arriba
    for i in range(0, len(Tablero)):
        s = str(i) + (" ") #se añade el numero de fila
        for j in range(0, len(Tablero[i])):
            s = (s) + (" ") + str(Tablero[i][j]) #y al numero de fila se le añade lo que tiene guardado la matriz
        print (s) #se imprime

def mostrarTableros(tableroJugador,tableroComputadoraPantalla):#hace lo mismo que la funcion anterior pero muestra 2 tableros, el del jugador y el de la computadora
    print("            ",nombre,"                            Computadora")
    print("    0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9")
    for i in range(0, len(tableroJugador)):
        s = str(i)+(" ")
        s2 = str(i)+(" ")
        for j in range(0, len(tableroJugador[i])):
            s = s + (" ") + str(tableroJugador[i][j])
            s2 = s2 + (" ") + str(tableroComputadoraPantalla[i][j])
        ss = s + ("     ") + s2
        print (ss)

def tablero1(Tablero): #si se llama a esta funcion al  tablero correspondiente (tablero computadora) se le van a añadir los barcos de esta manera
    if dif=="facil":
        for a in range(2,6):
            orientacion =int( random.randint(1,2)) #Decide aleatoriamente si el barco va a estar en horizontal o vertical
            if orientacion == 1:  #Horizontal
                p1X = random.randint(0,9)      # Genera aletoriamente las cordenadas del barco, con las dos X iguales (Horizontal)
                p1Y = random.randint(0,9-a)
                p2X = p1X
                p2Y = random.randint(0,9)
            elif orientacion == 2: #Vertical
                p1X = random.randint(0,9-a)
                p1Y = random.randint(0,9)        # Genera las 4 cordenadas necesarial aletoreamente con  las Y iguales (Vertical)        
                p2X = random.randint(0,9)
                p2Y = p1Y
            posible = check(p1X,p1Y,p2X,p2Y,a,Tablero) #Controla que la ubicacion este permitida
            while posible == "no": #En caso de que la cordenada no sea posible generea otra hasta que sea valida
                orientacion =int( random.randint(1,2)) #Decide aleatoriamente si el barco va a estar en horizontal o vertical
                if orientacion == 1:  #Horizontal
                    p1X = random.randint(0,9)
                    p1Y = random.randint(0,9-a)
                    p2X = p1X
                    p2Y = random.randint(p1Y,9)
                elif orientacion == 2: # Vertical
                    p1X = random.randint(0,9-a)
                    p1Y = random.randint(0,9)                
                    p2X = random.randint(0,9)
                    p2Y = p1Y
                posible = check(p1X,p1Y,p2X,p2Y,a,Tablero) # Vuelve a controlar que la cordenada este permitida
            if((p1X == p2X) or (p1Y == p2Y)): # Cambia el simbolo en donde va a estar el barco de "__" a un "[]"
                if (p1X == p2X):
                    for i in range(p1Y,(p1Y+a)):
                        Tablero[p1X][i]="[]"
                       
                else:
                    for i in range(p1X,(p1X+a)):
                        Tablero[i][p1Y]= "[]"
                       
                              
    elif dif=="medio":
        for a in range(2,5):
            orientacion =int( random.randint(1,2)) #Decide aleatoriamente si el barco va a estar en horizontal o vertical
            if orientacion == 1:  #Horizontal
                p1X = random.randint(0,9)
                p1Y = random.randint(0,9-a)       # Genera aletoriamente las cordenadas del barco, con las dos X iguales (Horizontal)
                p2X = p1X
                p2Y = random.randint(0,9)
            elif orientacion == 2: #Vertical
                p1X = random.randint(0,9-a)
                p1Y = random.randint(0,9)         # Genera las 4 cordenadas necesarial aletoreamente con  las Y iguales (Vertical)        
                p2X = random.randint(0,9)
                p2Y = p1Y
            posible = check(p1X,p1Y,p2X,p2Y,a,Tablero) #Controla que la ubicacion este permitida
            while posible == "no": #En caso de que la cordenada no sea posible nerea otra hasta que sea valida
                orientacion =int( random.randint(1,2)) #Decide aleatoriamente si el barco va a estar en horizontal o vertical
                if orientacion == 1:  #Horizontal
                    p1X = random.randint(0,9)
                    p1Y = random.randint(0,9-a)
                    p2X = p1X
                    p2Y = random.randint(p1Y,9)
                elif orientacion == 2: # Vertical
                    p1X = random.randint(0,9-a)
                    p1Y = random.randint(0,9)                 
                    p2X = random.randint(0,9) 
                    p2Y = p1Y
                posible = check(p1X,p1Y,p2X,p2Y,a,Tablero)
            if((p1X == p2X) or (p1Y == p2Y)): # Cambia el simbolo en donde va a estar el barco de "__" a un "[]"
                if (p1X == p2X):
                    for i in range(p1Y,(p1Y+a)):
                        Tablero[p1X][i]="[]"
                        
                else:
                    for i in range(p1X,(p1X+a)):
                        Tablero[i][p1Y]= "[]"
                        


    elif dif=="dificil":
        for a in range(2,4):
            orientacion =int( random.randint(1,2)) #Decide aleatoriamente si el barco va a estar en horizontal o vertical
            if orientacion == 1:  #Horizontal
                p1X = random.randint(0,9)
                p1Y = random.randint(0,9-a)        # Genera aletoriamente las cordenadas del barco, con las dos X iguales (Horizontal)
                p2X = p1X
                p2Y = random.randint(0,9)
            elif orientacion == 2: #Vertical
                p1X = random.randint(0,9-a)
                p1Y = random.randint(0,9)          # Genera las 4 cordenadas necesarial aletoreamente con  las Y iguales (Vertical) 
                p2X = random.randint(0,9)
                p2Y = p1Y
            posible = check(p1X,p1Y,p2X,p2Y,a,Tablero) #Controla que la ubicacion este permitida
            while posible == "no": #En caso de que la cordenada no sea posible nerea otra hasta que sea valida
                orientacion =int( random.randint(1,2)) #Decide aleatoriamente si el barco va a estar en horizontal o vertical
                if orientacion == 1:  #Horizontal
                    p1X = random.randint(0,9)
                    p1Y = random.randint(0,9-a)
                    p2X = p1X
                    p2Y = random.randint(p1Y,9)
                elif orientacion == 2: # Vertical
                    p1X = random.randint(0,9-a)
                    p1Y = random.randint(0,9)                
                    p2X = random.randint(0,9)
                    p2Y = p1Y
                posible = check(p1X,p1Y,p2X,p2Y,a,Tablero)
            if((p1X == p2X) or (p1Y == p2Y)):     # Cambia el simbolo en donde va a estar el barco de "__" a un "[]"
                if (p1X == p2X):
                    for i in range(p1Y,(p1Y+a)):
                        Tablero[p1X][i]="[]"
                        
                else:
                    for i in range(p1X,(p1X+a)):
                        Tablero[i][p1Y]= "[]"
                        


def check(x1,y1,x2,y2,a,tablero):
# Esta funcion revisa el tablero para buscar que el barco, el cual va a ser posicionado, no este arriba de otro o en alguna casilla alrededor de este
    if x1 == x2: #Si ocurre esto el barco esta en posicion horizontal
        #En estas tres condiciones analiza los costados horizontales del barco y si esta ubicado en el limite solo analiza el borde que exista
        if y1 == 0: 
            if tablero[x1][a] != "__":
                return "no"
        elif y1 == 9:
            if tablero[x1][9-a] != "__":
                return "no"
        else:
            if tablero[x1][y1+a] != "__" or tablero[x1][y1-1] != "__":
                return "no"
        # Ahora utiliza un for para analizar cada casilla que ocupa el barco y sus casillas superires e inferiores
        for h in range(0,a):
            # El primer if se usa para si el lugar en el que se quiere ubicar el barco no esta ocupado
            if tablero[x1][y1+h] != "__":
                return "no"
            #Las proximas tres condiciones buscan que no haya ningun barco ubicado en las casillas superiores o inferiores de donde se quiere ubicar la embarcacion
            # Si el barco esta en un limite del tablero solo analiza el lado que esta dentro del tablero
            if x1 == 0:
                if tablero[1][y1+h] != "__":
                    return "no"
            elif x1 == 9:
                if tablero[8][y1+h] != "__":
                    return "no"
            else:
                if tablero[x1-1][y1+h] != "__":
                    return "no"
                if tablero[x1+1][y1+h] != "__":
                    return "no"
    if y1 == y2: #Si ocurre esto el barco esta en posicion Vertical
        #En estas tres condiciones analiza los costados verticales del barco y si esta ubicado en el limite solo analiza el borde que exista
        if x1 == 0:
            if tablero[a][y1] != "__":
                return "no"
        elif x1 == 9:
            if tablero[9-a][y1] != "__":
                return "no"
        else:
            if tablero[x1+a][y1] != "__" or tablero[x1-1][y1] != "__":
                return "no"
        # Ahora utiliza un for para analizar cada casilla que ocupa el barco y sus casillas a la derecha e izquierda 
        for h in range(0,a):
            # El primer if se usa para si el lugar en el que se quiere ubicar el barco no esta ocupado
            if tablero[x1+h][y1] != "__":
                return "no"
            #Las proximas tres condiciones buscan que no haya ningun barco ubicado en las casillas a la derecha e izquierda de donde se quiere ubicar la embarcacion
            # Si el barco esta en un limite del tablero solo analiza el lado que esta dentro del tablero
            if y1 == 0:
                if tablero[x1+h][1] != "__":
                    return "no"
            elif y1 == 9:
                if tablero[x1+h][8] != "__":
                    return "no"
            else:
                if tablero[x1+h][y1-1] != "__":
                    return "no"
                if tablero[x1+h][y1+1] != "__":
                    return "no"

#se crearon las matrices del jugador y la de la computadora
#la matriz pantalla es la que se muestra con [][][] como si fueran barcos
#y la matriz jugador o computadora la controlan diferenciando cada barco con numeros
tableroJugador=[]
tableroJugadorPantalla=[]
tableroComputadora=[]
tableroComputadoraPantalla=[]

for i in range(0,10):
    tableroJugador.append(["__"])#se agrega una lista
    tableroJugadorPantalla.append(["__"])
    tableroComputadora.append(["__"])
    tableroComputadoraPantalla.append(["__"])
    for j in range(0,9):
        tableroJugador[i].append("__")#a esa lista se le agrega una lista adentro de diez posiciones
        tableroJugadorPantalla[i].append("__")
        tableroComputadora[i].append("__")
        tableroComputadoraPantalla[i].append("__")

print("")
mostrarTablero(tableroJugadorPantalla)#se imprime el tablero del jugador
print("")
""" Para que la computadora no utilize siempre el mismo tablero utilizamos
la funcon "Tablero1" para que genere cordenadas aletorias dependiendo de la
dificultad de juego y genere siempre un tablero distinto al de la partida anterior"""

tablero1(tableroComputadora) # Genera el tablero de la computadora
# mostrarTablero(tableroComputadoraPantalla) 
# mostrarTablero(tableroComputadora)

""" como hay 5 barcos se hace el mismo procedimiento 5 veces
Donde:
-Se pide la coordenada inicial del barco y la coordenada inicial de forma numero, numero ej:01
-Se separa la coordenada en X e Y, ej: en el punto p1X y p1Y es 1
-Como el barco solo puede ser horizontal y vertical, el barco debe tener X o Y igual, X=horizontal Y=vertical
-Si la coordenada no cumple con esto, lo pido hasta hasta que lo haga correctamente
-Si es horizontal entonces agarra el primer punto y le suma el tamaño del barco
y a cada posicion en la matriz jugador le pone el numero, ej un barco de 5 va a tener 55555
y en la pantalla se muestra [][][][][]
-Despues se muestra el tablero"""

if dif=="test":#se usa esta dificultad para revisar problemas que pudiera tener el juego
    a = 0
    coordenadaINICIO = input(f"Ingrese la coordenada INICIAL del barco de tamaño {a+2}: ")#pide la coordenada inicial xy
    coordenadaFINAL = input(f"Ingrese la coordena FINAL del barco de tamaño {a+2}: ")#pide coordenada final x2y2
    p1X = int(coordenadaINICIO[0])#separa las coordenadas p1X=x
    p1Y = int(coordenadaINICIO[1])#p1Y=y
    p2X = int(coordenadaFINAL[0])#p2X=x2
    p2Y = int(coordenadaFINAL[1])#p2Y=y2
    posible = check(p1X,p1Y,p2X,p2Y,a+2,tableroJugadorPantalla)
    while not((p1X == p2X) or (p1Y == p2Y)) or posible =="no": #Pide coordenada hasta que se ingresen bien
        print("Coordenada invalida, ingrese nuevamente.")
        coordenadaINICIO = input(f"Ingrese la coordenada INICIAL del barco de tamaño {a+2}: ")#pide la coordenada inicial xy
        coordenadaFINAL = input(f"Ingrese la coordena FINAL del barco de tamaño {a+2}: ")#pide coordenada final x2y2
        p1X = int(coordenadaINICIO[0])
        p1Y = int(coordenadaINICIO[1])
        p2X = int(coordenadaFINAL[0])
        p2Y = int(coordenadaFINAL[1])
        posible = check(p1X,p1Y,p2X,p2Y,a+2,tableroJugadorPantalla)
    if((p1X == p2X) or (p1Y == p2Y)): #si el barco es horizontal
        if (p1X == p2X):
            for i in range(p1Y,(p1Y+a+2)):#llena la cantidad de casillas del barco con el numero 1, 22, 333, 4444, 55555
                tableroJugador[p1X][1]=str(a)
                tableroJugadorPantalla[p1X][i]="[]"#llena la pantalla que se muestra con el "barco" [], [][], [][][], [][][][], [][][][][]
        else:
            for i in range(p1X,(p1X+a+2)):#llena la cantidad de casillas del barco
                tableroJugador[1][p1Y]=str(a)
                tableroJugadorPantalla[i][p1Y]="[]"
        mostrarTablero(tableroJugadorPantalla)
if dif=="facil":
    for a in range(2,6):
        coordenadaINICIO = input(f"Ingrese la coordenada INICIAL del barco de tamaño {a}: ")#pide la coordenada inicial xy
        coordenadaFINAL = input(f"Ingrese la coordena FINAL del barco de tamaño {a}: ")#pide coordenada final x2y2
        p1X = int(coordenadaINICIO[0])#separa las coordenadas p1X=x
        p1Y = int(coordenadaINICIO[1])#p1Y=y
        p2X = int(coordenadaFINAL[0])#p2X=x2
        p2Y = int(coordenadaFINAL[1])#p2Y=y2
        posible = check(p1X,p1Y,p2X,p2Y,a,tableroJugadorPantalla)
        while not((p1X == p2X) or (p1Y == p2Y)) or posible == "no": #Pide coordenada hasta que se ingresen bien
            print("Coordenada invalida, ingrese nuevamente.")
            coordenadaINICIO = input(f"Ingrese la coordenada INICIAL del barco de tamaño {a}: ")#pide la coordenada inicial xy
            coordenadaFINAL = input(f"Ingrese la coordena FINAL del barco de tamaño {a}: ")#pide coordenada final x2y2
            p1X = int(coordenadaINICIO[0])
            p1Y = int(coordenadaINICIO[1])
            p2X = int(coordenadaFINAL[0])
            p2Y = int(coordenadaFINAL[1])
            posible = check(p1X,p1Y,p2X,p2Y,a,tableroJugadorPantalla)
        if((p1X == p2X) or (p1Y == p2Y)): #si el barco es horizontal
            if (p1X == p2X):
                for i in range(p1Y,(p1Y+a)):#llena la cantidad de casillas del barco con el numero 1, 22, 333, 4444, 55555
                    tableroJugador[p1X][1]=str(a)
                    tableroJugadorPantalla[p1X][i]="[]"#llena la pantalla que se muestra con el "barco" [], [][], [][][], [][][][], [][][][][]
            else:
                for i in range(p1X,(p1X+a)):#llena la cantidad de casillas del barco
                    tableroJugador[1][p1Y]=str(a)
                    tableroJugadorPantalla[i][p1Y]="[]"
            mostrarTablero(tableroJugadorPantalla)
elif dif=="medio":
    for a in range(2,5):
        coordenadaINICIO = input(f"Ingrese la coordenada INICIAL del barco de tamaño {a}: ")#pide la coordenada inicial xy
        coordenadaFINAL = input(f"Ingrese la coordena FINAL del barco de tamaño {a}: ")#pide coordenada final x2y2
        p1X = int(coordenadaINICIO[0])#separa las coordenadas p1X=x
        p1Y = int(coordenadaINICIO[1])#p1Y=y
        p2X = int(coordenadaFINAL[0])#p2X=x2
        p2Y = int(coordenadaFINAL[1])#p2Y=y2
        posible = check(p1X,p1Y,p2X,p2Y,a,tableroJugadorPantalla)
        while not((p1X == p2X) or (p1Y == p2Y)) or posible == "no": #Pide coordenada hasta que se ingresen bien
            print("Coordenada invalida, ingrese nuevamente.")
            coordenadaINICIO = input(f"Ingrese la coordenada INICIAL del barco de tamaño {a}: ")#pide la coordenada inicial xy
            coordenadaFINAL = input(f"Ingrese la coordena FINAL del barco de tamaño {a}: ")#pide coordenada final x2y2
            p1X = int(coordenadaINICIO[0])
            p1Y = int(coordenadaINICIO[1])
            p2X = int(coordenadaFINAL[0])
            p2Y = int(coordenadaFINAL[1])
            posible = check(p1X,p1Y,p2X,p2Y,a,tableroJugadorPantalla)
        if((p1X == p2X) or (p1Y == p2Y)): #si el barco es horizontal
            if (p1X == p2X):
                for i in range(p1Y,(p1Y+a)):#llena la cantidad de casillas del barco con el numero 1, 22, 333, 4444, 55555
                    tableroJugador[p1X][1]=str(a)
                    tableroJugadorPantalla[p1X][i]="[]"#llena la pantalla que se muestra con el "barco" [], [][], [][][], [][][][], [][][][][]
            else:
                for i in range(p1X,(p1X+a)):#llena la cantidad de casillas del barco
                    tableroJugador[1][p1Y]=str(a)
                    tableroJugadorPantalla[i][p1Y]="[]"
            mostrarTablero(tableroJugadorPantalla)
elif dif=="dificil":
    for a in range(2,4):
        coordenadaINICIO = input(f"Ingrese la coordenada INICIAL del barco de tamaño {a}: ")#pide la coordenada inicial xy
        coordenadaFINAL = input(f"Ingrese la coordena FINAL del barco de tamaño {a}: ")#pide coordenada final x2y2
        p1X = int(coordenadaINICIO[0])#separa las coordenadas p1X=x
        p1Y = int(coordenadaINICIO[1])#p1Y=y
        p2X = int(coordenadaFINAL[0])#p2X=x2
        p2Y = int(coordenadaFINAL[1])#p2Y=y2
        posible = check(p1X,p1Y,p2X,p2Y,a,tableroJugadorPantalla)
        while not((p1X == p2X) or (p1Y == p2Y)) or posible == "no": #Pide coordenada hasta que se ingresen bien
            print("Coordenada invalida, ingrese nuevamente.")
            coordenadaINICIO = input(f"Ingrese la coordenada INICIAL del barco de tamaño {a}: ")#pide la coordenada inicial xy
            coordenadaFINAL = input(f"Ingrese la coordena FINAL del barco de tamaño {a}: ")#pide coordenada final x2y2
            p1X = int(coordenadaINICIO[0])
            p1Y = int(coordenadaINICIO[1])
            p2X = int(coordenadaFINAL[0])
            p2Y = int(coordenadaFINAL[1])
            posible = check(p1X,p1Y,p2X,p2Y,a,tableroJugadorPantalla)
        if((p1X == p2X) or (p1Y == p2Y)): #si el barco es horizontal
            if (p1X == p2X):
                for i in range(p1Y,(p1Y+a)):#llena la cantidad de casillas del barco con el numero 1, 22, 333, 4444, 55555
                    tableroJugador[p1X][1]=str(a)
                    tableroJugadorPantalla[p1X][i]="[]"#llena la pantalla que se muestra con el "barco" [], [][], [][][], [][][][], [][][][][]
            else:
                for i in range(p1X,(p1X+a)):#llena la cantidad de casillas del barco
                    tableroJugador[1][p1Y]=str(a)
                    tableroJugadorPantalla[i][p1Y]="[]"
            mostrarTablero(tableroJugadorPantalla)


#estas variables van a guardar cunatos barcos le han hundido al jugador y a la computadora
hundidosJugador=0
hundidosComputadora=0

#guarda el turno
turno = "Jugador"

#esto indica si ya termino el juego
if dif=="facil":
    fin=False
    while(fin==False):#mientras no sea el fin del juego
        if (turno == "Jugador"): #si es el turno del jugador pide las coordenadas en donde quiere dispara el jugador
            px = int(input("Ingrese coordenada en x a la que desea disparar: "))#horizontal
            py = int(input("Ingrese coordenada en y a la que desee desparar: "))#vertical
            while px > 9 or py > 9:
                print("La Cordenada que desea no existe. Por favor, ingrese una nueva")
                px = int(input("Ingrese coordenada en x a la que desea disparar: "))#horizontal
                py = int(input("Ingrese coordenada en y a la que desee desparar: "))#vertical
            tableroComputadoraPantalla[px][py]="O"#pone una O donde se disparo
            disparo=False
            for a in range(0,4): #como hay 4 posibiladades de barco
                if(tableroComputadora[px][py]==str(a)): #busca si el lugar de disparo es uno de esos numeros
                    hundidosComputadora=hundidosComputadora+1 #si es un numero aumenta en 1 el numero de destrucciones
                    tableroComputadoraPantalla[px][py]="X " #le pone una X al barco que disparo si es que el disparo es acertado
                    tableroComputadora[px][py]= " "
                    disparo=True
            if disparo==False:
                turno="Computadora"#cambia el turno al de la computadora
        elif (turno=="Computadora"):#si el turno de la computadora
            px = random.randint(0,9)#genera un numero aleatorio entre 0 y 9, disparo
            py = random.randint(0,9)#genera otro numero vertical
            print("La computadora disparo en la posicion "+str(px)+","+str(py))#le dice al jugador donde disparo la computadora
            tableroJugadorPantalla[px][py]="O "#pone una O donde disparo y realiza lo mismo que el jugador,busca el disparo en un numero y si es asi
            disparo=False
            for a in range(0,4):
                if(tableroJugador[px][py]==str(a)):
                    hundidosJugador=hundidosJugador+1
                    tableroJugadorPantalla[px][py]="X "#pone una X en el barco que disparo si es que el disparo es acertado
                    tableroJugador[px][py]=" "
                    disparo=True
            if disparo==False:
                turno="Jugador"#cambia el turno al jugador
        print("")
        mostrarTableros(tableroJugadorPantalla,tableroComputadoraPantalla)#muestra el tablero del jugador y de la computadora ya que cambio
        print("")

        if(hundidosJugador==14):#verifica si el jugador tiene 14 partes de barcos destruidos
            print("GANO LA COMPUTADORA")#lo que inidca que la computadora gano porque le destruyo todos los barcos
            fin=True#se sale el juego
        elif(hundidosComputadora==14):#alrevez
            print("GANO EL JUGADOR")
            fin=True

elif dif=="medio":
    fin=False
    while(fin==False):#mientras no sea el fin del juego
        if (turno == "Jugador"): #si es el turno del jugador pide las coordenadas en donde quiere dispara el jugador
            px = int(input("Ingrese coordenada en x a la que desea disparar: "))#horizontal
            py = int(input("Ingrese coordenada en y a la que desee desparar: "))#vertical
            while px > 9 or py > 9:
                print("La Cordenada que desea no existe. Por favor, ingrese una nueva")
                px = int(input("Ingrese coordenada en x a la que desea disparar: "))#horizontal
                py = int(input("Ingrese coordenada en y a la que desee desparar: "))#vertical
            tableroComputadoraPantalla[px][py]="O"#pone una O donde se disparo
            disparo=False
            for a in range(0,3): #como hay 3 posibiladades de barco
                if(tableroComputadora[px][py]==str(a)): #busca si el lugar de disparo es uno de esos numeros
                    hundidosComputadora=hundidosComputadora+1 #si es un numero aumenta en 1 el numero de destrucciones
                    tableroComputadoraPantalla[px][py]="X " #le pone una X al barco que disparo si es que el disparo es acertado
                    tableroComputadora[px][py]= " "
                    disparo=True
            if disparo==False:
                turno="Computadora"#cambia el turno al de la computadora
        elif (turno=="Computadora"):#si el turno de la computadora
            px = random.randint(0,9)#genera un numero aleatorio entre 0 y 9, disparo
            py = random.randint(0,9)#genera otro numero vertical
            print("La computadora disparo en la posicion "+str(px)+","+str(py))#le dice al jugador donde disparo la computadora
            tableroJugadorPantalla[px][py]="O "#pone una O donde disparo y realiza lo mismo que el jugador,busca el disparo en un numero y si es asi
            disparo=False
            for a in range(0,3):
                if(tableroJugador[px][py]==str(a)):
                    hundidosJugador=hundidosJugador+1
                    tableroJugadorPantalla[px][py]="X "#pone una X en el barco que disparo si es que el disparo es acertado
                    tableroJugador[px][py]=" "
                    disparo=True
            if disparo==False:
                turno="Jugador"#cambia el turno al jugador
        print("")
        mostrarTableros(tableroJugadorPantalla,tableroComputadoraPantalla)#muestra el tablero del jugador y de la computadora ya que cambio
        print("")
        if(hundidosJugador==9):#verifica si el jugador tiene 9 partes de barcos destruidos
            print("GANO LA COMPUTADORA")#lo que inidca que la computadora gano porque le destruyo todos los barcos
            fin=True#se sale el juego
        elif(hundidosComputadora==9):#alrevez
            print("GANO EL JUGADOR")
            fin=True

elif dif=="dificil":
    fin=False
    while(fin==False):#mientras no sea el fin del juego
        if (turno == "Jugador"): #si es el turno del jugador pide las coordenadas en donde quiere dispara el jugador
            px = int(input("Ingrese coordenada en x a la que desea disparar: "))#horizontal
            py = int(input("Ingrese coordenada en y a la que desee desparar: "))#vertical
            while px > 9 or py > 9:
                print("La Cordenada que desea no existe. Por favor, ingrese una nueva")
                px = int(input("Ingrese coordenada en x a la que desea disparar: "))#horizontal
                py = int(input("Ingrese coordenada en y a la que desee desparar: "))#vertical
            tableroComputadoraPantalla[px][py]="O"#pone una O donde se disparo
            disparo=False
            for a in range(0,2): #como hay 2 posibiladades de barco
                if(tableroComputadora[px][py]==str(a)): #busca si el lugar de disparo es uno de esos numeros
                    hundidosComputadora=hundidosComputadora+1 #si es un numero aumenta en 1 el numero de destrucciones
                    tableroComputadoraPantalla[px][py]="X " #le pone una X al barco que disparo si es que el disparo es acertado
                    tableroComputadora[px][py]= " "
                    disparo=True
            if disparo==False:
                turno="Computadora"#cambia el turno al de la computadora
        elif (turno=="Computadora"):#si el turno de la computadora
            px = random.randint(0,9)#genera un numero aleatorio entre 0 y 9, disparo
            py = random.randint(0,9)#genera otro numero vertical
            print("La computadora disparo en la posicion "+str(px)+","+str(py))#le dice al jugador donde disparo la computadora
            tableroJugadorPantalla[px][py]="O "#pone una O donde disparo y realiza lo mismo que el jugador,busca el disparo en un numero y si es asi
            disparo=False
            for a in range(0,2):
                if(tableroJugador[px][py]==str(a)):
                    hundidosJugador=hundidosJugador+1
                    tableroJugadorPantalla[px][py]="X "#pone una X en el barco que disparo si es que el disparo es acertado
                    tableroJugador[px][py]=" "
                    disparo=True
            if disparo==False:
                turno="Jugador"#cambia el turno al jugador
        print("")
        mostrarTableros(tableroJugadorPantalla,tableroComputadoraPantalla)#muestra el tablero del jugador y de la computadora ya que cambio
        print("")
        if(hundidosJugador==5):#verifica si el jugador tiene 5 partes de barcos destruidos
            print("GANO LA COMPUTADORA")#lo que inidca que la computadora gano porque le destruyo todos los barcos
            fin=True#se sale el juego
        elif(hundidosComputadora==5):#alrevez
            print("GANO EL JUGADOR")
            fin=True
elif dif=="test":
    fin=False
    while(fin==False):#mientras no sea el fin del juego
        if (turno == "Jugador"): #si es el turno del jugador pide las coordenadas en donde quiere dispara el jugador
            px = int(input("Ingrese coordenada en x a la que desea disparar: "))#horizontal
            py = int(input("Ingrese coordenada en y a la que desee desparar: "))#vertical
            while px > 9 or py > 9:
                print("La Cordenada que desea no existe. Por favor, ingrese una nueva")
                px = int(input("Ingrese coordenada en x a la que desea disparar: "))#horizontal
                py = int(input("Ingrese coordenada en y a la que desee desparar: "))#vertical
            tableroComputadoraPantalla[px][py]="O"#pone una O donde se disparo
            disparo=False
            for a in range(0,2): #como hay 2 posibiladades de barco
                if(tableroComputadora[px][py]==str(a)): #busca si el lugar de disparo es uno de esos numeros
                    hundidosComputadora=hundidosComputadora+1 #si es un numero aumenta en 1 el numero de destrucciones
                    tableroComputadoraPantalla[px][py]="X " #le pone una X al barco que disparo si es que el disparo es acertado
                    tableroComputadora[px][py]= " "
                    disparo=True
            if disparo==False:
                turno="Computadora"#cambia el turno al de la computadora
        elif (turno=="Computadora"):#si el turno de la computadora
            px = random.randint(0,9)#genera un numero aleatorio entre 0 y 9, disparo
            py = random.randint(0,9)#genera otro numero vertical
            print("La computadora disparo en la posicion "+str(px)+","+str(py))#le dice al jugador donde disparo la computadora
            tableroJugadorPantalla[px][py]="O "#pone una O donde disparo y realiza lo mismo que el jugador,busca el disparo en un numero y si es asi
            disparo=False
            for a in range(0,2):
                if(tableroJugador[px][py]==str(a)):
                    hundidosJugador=hundidosJugador+1
                    tableroJugadorPantalla[px][py]="X "#pone una X en el barco que disparo si es que el disparo es acertado
                    tableroJugador[px][py]=" "
                    disparo=True
            if disparo==False:
                turno="Jugador"#cambia el turno al jugador
        print("El jugador lleva hundidos:", hundidosJugador)
        print("La computadora lleva hundidos:", hundidosComputadora)
        print("")
        mostrarTableros(tableroJugadorPantalla,tableroComputadoraPantalla)#muestra el tablero del jugador y de la computadora ya que cambio
        print("")
        if(hundidosJugador==1):#verifica si el jugador tiene 5 partes de barcos destruidos
            print("GANO LA COMPUTADORA")#lo que inidca que la computadora gano porque le destruyo todos los barcos
            fin=True#se sale el juego
        elif(hundidosComputadora==1):#alrevez
            print("GANO EL JUGADOR")
            fin=True


#3 EPÍLOGO
#3.1 Muestra de la solución del problema por pantalla (opcional, si sólo se muestran resultados durante la resolución)

#3.2 Pausa para ver resultados en pantalla que se puede obviar, si los resultados se van mostrando durante la resolución
print() # salto de línea
input('Pulse tecla Enter para terminar el programa...') # pausa forzada
#Actualizaciones: Para esta version agregamos nuevos tableros precargados, para mejorar la experiencia de juego. Tambien se implemento una dificultad de test
#para identificar posibles problemas en el codigo. Por ultimo pudimos lograr que el juego termine cuando el jugador o la computadora hayan derribado todos los barcos. 
