## CAMBIA LOS STATS DEL JUEGO EN NIVEL ESCAPADA
def level_running(game):
    opciones = ["ACTIVAR TURBO", "BEBER", "COMER", "VELOCIDAD ESTABLE"]
    selecciones = ["A","B","C","D"]
    for i in range(len(opciones)):
        print("\t"+selecciones[i] + ". " +opciones[i])
    seleccion = input("\n").upper()

    while seleccion not in selecciones:
        for i in range(len(opciones)):
            print("\t"+selecciones[i] + ". " +opciones[i])
        seleccion = input("\n").upper()


    if seleccion == "A":    ## VELOCIDAD 
        if game[0][2] == 0:     ## NO TURBO
            game[0][0] = 0
            print("HAS INTENTADO USAR EL TURBO, CUANDO NO TENIAS, Y HAS PERDIDO TODO EL FUEL AL ACTIVAR EL TURBO")
        else:
            ## PLAYER
            game[0][0] -= 30            ## FUEL 
            game[0][1] -= 10            ## ARMADURA 
            game[0][2] -= 1             ## TURBO
            game[1][0] += 50            ## DISTANCIA 
            game[1][1] += 10            ## SED 
            game[1][2] += 10            ## HAMBRE 
            game[1][3] += 5             ## SUEÑO 

            ## ENEMIGO
            game[2][0] += 20            ## DISTANCIA 

    elif seleccion == "B":  ## BEBER
        game[1][1] = 0   ## RESTAURA SED JUGADOR
        game[1][0] += 5  ## JUGADOR DISTANCIA
        game[2][0] += 20 ## ENEMIGO DISTANCA  

    elif seleccion == "C":  ## HAMBRE
        game[1][1] = 0   ## RESTAURA HAMBRE JUGADOR
        game[1][0] += 5  ## JUGADOR DISTANCIA
        game[2][0] += 20 ## ENEMIGO DISTANCA

    elif seleccion == "D":  ## VELOCIDAD ESTABLE
        game[2][0] += 20 ## ENEMIGO DISTANCA
        game[1][0] += 30 ## JUGADOR DISTANCIA
        game[0][0] -= 10 ## FUEL 

    else:
        return None

## CAMBIA LOS STATS DEL JUEGO NIVEL PUEBLO
def level_village(game):
    opciones = ["DORMIR", "REPOSTAR", "REPARAR", "ACCION"]
    selecciones = ["A","B","C","D"]

    for i in range(2):      ## DOS OPCIONES DISPONIBLES EN PUEBLO

        for i in range(len(opciones)):
            print("\t"+selecciones[i] + ". " +opciones[i])
        seleccion = input("\n").upper()

        while seleccion not in selecciones:
            for i in range(len(opciones)):
                print("\t"+selecciones[i] + ". " +opciones[i])
            seleccion = input("\n").upper()
        
        if seleccion == "A":            ## DORMIR
            ## PLAYER
            game[1][1] = 0            ## RESTAURAR SED
            game[1][2] = 0            ## RESTAURAR HAMBRE 
            game[1][3] = 0            ## RESTAURAR SUEÑO 

            ## ENEMIGO
            game[2][0] += 20            ## DISTANCIA 

        elif seleccion == "B":          ## REPOSTAR
            game[0][0] = 100            ## RESTAURAR FUEL
            game[2][0] += 20            ## DISTANCIA  

        elif seleccion == "C":          ## REPARAR
            game[0][1] = 100            ## RESTAURAR ARMADURA 

        elif seleccion == "D":          ## ACCION
            if game[2][1] <= 2 and game[0][3] >= 1 :
                game[2][1] == 0

            game[2][0] += 20            ## ENEMIGO DISTANCA

        else:
            return None

def event(game,random_event):
    
    if random_event == 1: ## TORMENTA
        print("< TORMENTA >")

        opciones = ["ATRAVESAR EN RECTO", "REFUGIARSE", "REPARAR", "ENFRENTAMIENTO"]
        selecciones = ["A","B","C","D"]

        for i in range(len(opciones)):
            print("\t"+selecciones[i] + ". " +opciones[i])
        seleccion = input("\n").upper()

        while seleccion not in selecciones:
            for i in range(len(opciones)):
                print("\t"+selecciones[i] + ". " +opciones[i])
            seleccion = input("\n").upper()

        if seleccion == "A":            ## HACIA DELANTE
            ## PLAYER
            game[1][1] += 30            ##  SED
            game[1][2] += 30            ##  HAMBRE 
            game[1][3] += 20            ##  SUEÑO 
            game[0][1] -= 40           ## ARMADURA 
            game[1][0] += 15           ## DISTANCIA
            game[0][0] -= 40            ## FUEL 


            ## ENEMIGO
            game[2][0] += 30            ## DISTANCIA 

        elif seleccion == "B":        ## REFUGIARSE
            game[1][1] = 0            ##  SED
            game[1][2] = 0            ##  HAMBRE 
            game[1][3] = 0            ##  SUEÑO 
            game[1][0] += 5           ## DISTANCIA

        elif seleccion == "C":          ## REPARAR
            game[0][1] = 100            ## RESTAURAR ARMADURA 
            game[2][0] += 20            ## DISTANCIA ENEMIGO

        elif seleccion == "D":          ## ENFRENTARSE
            game[0][0] -= 20            ## FUEL 
            game[0][1] -= 30            ## ARMADURA 
            game[0][3] -= 1             ## -1 ARMAMENTO
            game[1][0] += 10            ## DISTANCIA
            game[2][1] -= 2             ## ENEMIGO CANTIDAD
            game[2][0] += 10            ## ENEMIGO DISTANCIA
            

        else:
            return None


    elif random_event == 2: ## EMBOSCADA
        print("< EMBOSCADA >")
        opciones = ["ATRAVESAR EN RECTO", "EVITAR", "ENFRENTAMIENTO"]
        selecciones = ["A","B","C",""]

        for i in range(len(opciones)):
            print("\t"+selecciones[i] + ". " +opciones[i])
        seleccion = input("\n").upper()

        while seleccion not in selecciones:
            for i in range(len(opciones)):
                print("\t"+selecciones[i] + ". " +opciones[i])
            seleccion = input("\n").upper()

        if seleccion == "A":            ## ATRAVESARLO A LA FUERZA
            ## PLAYER
            game[0][0] -= 40            ## FUEL 
            game[0][1] -= 60            ## ARMADURA 
            game[1][1] += 20            ## SED 
            game[1][2] += 20            ## HAMBRE 
            game[1][3] += 30            ## SUEÑO 
            game[1][0] += 1             ## DISTANCIA

            ## ENEMIGO
            game[2][0] += 10            ## DISTANCIA 

        elif seleccion == "B":          ## EVITARLA
            game[1][1] += 30            ## SED
            game[1][2] += 30            ## HAMBRE
            game[1][0] += 10           ## DISTANCIA
            game[2][0] += 30            ## ENEMIGO DISTANCA

        elif seleccion == "C":          ## ENFRENTAMIENTO
            game[1][1] += 30            ## SED
            game[1][2] += 30            ## HAMBRE
            game[0][3] -= 1             ## -1 ARMAMENTO
            game[1][0] += 10           ## DISTANCIA
            game[2][1] -= 2             ## ENEMIGO CANTIDAD
            game[2][0] += 30            ## ENEMIGO DISTANCA

        else:
            return None

## CONDICIONES PARA PERDER LA PARTIDA // DEVUELVE TRUE SI PIERDE, FALSE SI PUEDE CONTINUAR
def lose_condittion(game):
    if game[1][1] >= 100 or game[1][2] >= 100 or game[1][3] >= 100:     ## SI LA SED, HAMBRE O SUEÑO SOBREPASAN O SON IGUALES A 100%
        return True
    elif game[0][0] <= 0 or game[0][1] <= 0:                            ## SI EL FUEL O LA ARMADURA ES INFERIOR O IGUAL AL 0%
        return True
    elif game[1][0] <= game[2][0]:                                      ## SI LA DISTANCIA DEL JUGADOR ES MENOR O IGUAL A LA DISTANCIA DE LOS ENEMIGOD
        return True

    return False

## CONDICIONES PARA GANAR LA PARTIDA // DEVUELVE TRUE SI GANA, FALSE SI PUEDE CONTINUAR
def win_condittion(game):
    if game[1][0] >= 200:   ## SI HAS RECORRIDO MAS DE 300 KM
        return True
    elif game[2][1] <= 0:   ## SI HAN MUERTO TODOS LOS ENEMIGOS
        print("HAS CONSEGUIDO ACABAR CON LOS ENEMIGOS")
        return True

    return False

def check_events(game,action_events,event):
    import random
    event_txt = "< -- EVENTO ADVERSO -- >"
    
    ## SOLO 4 EVENTOS DISPONIBLES, 2 DE CADA DE FORMA ALEATORIA
    if action_events[0] != 2 and action_events[1] != 2:     ## SI NO HAN HABIDO 2 EVENTOS[0] Y NO HAN HABIDO 2 EVENTOS[1]
        
        

        random_event = random.randrange(3)
        if random_event == 1:       ## TORMENTA
            print(event_txt)
            level_stats_interface(game)
            event(game,random_event)
            action_events[0] += 1

        elif random_event == 2:     ## EMBOSCADA
            print(event_txt)
            level_stats_interface(game)
            event(game,random_event)
            action_events[1] += 1

    elif action_events[0]==2:                               ## SI YA HAN HABIDO 2 TORMENTAS
        random_event = random.randrange(0,3,2)
        if random_event == 2:                               ## EMBOSCADA
            print(event_txt)
            level_stats_interface(game)
            event(game,random_event)
            action_events[1] += 1
    
    elif action_events[1]==2:                                ## SI YA HAN HABIDO 2 EMBOSCADAS
        random_event = random.randrange(2)
        if random_event == 1:                                ## TORMENTA
            print(event_txt)
            level_stats_interface(game)
            event(game,random_event)
            action_events[0] += 1

## CONSOLA INTERFACE ## 
def start_game():

    ## VARIABLES DIBUJO
    arriba_izq="╔"
    abajo_izq="╚"
    arriba_der="╗"
    abajo_der="╝"
    horizontal="═"
    vertical="║"
    espacio=" "

    mode = ["< 𝕊𝕋𝔸ℝ𝕋 >","1. INTRO PARA COMENZAR","0. SALIR"]
    opciones = ["","0"]

    ancho = 40

    print(arriba_izq + horizontal*(ancho) + arriba_der)
    print(vertical + espacio*(ancho) + vertical)
    print(vertical + (mode[0]).center(int(ancho),espacio) + vertical)
    print(vertical + espacio*(ancho) + vertical)

    for i in range (1,len(mode)):
        print(vertical + horizontal*(ancho) + vertical)
        print(vertical + (mode[i]).center(int(ancho), espacio) + vertical)
        print(vertical + horizontal*(ancho) + vertical)
  
    print(abajo_izq + horizontal*(ancho) + abajo_der)

    level_mode = input("Introduzca una opcion\n")

    while level_mode not in opciones:
        level_mode = input("Introduzca una opcion valida!\n")

    return level_mode

## CONSOLA INTERFACE

def title_interface():
    print("""
         █████╗  █████╗ ██████╗ ██████╗ ███████╗     █████╗     ███╗   ███╗██╗   ██╗███████╗██████╗ ███████╗
        ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝    ██╔══██╗    ████╗ ████║██║   ██║██╔════╝██╔══██╗██╔════╝
        ██║  ╚═╝██║  ██║██████╔╝██████╔╝█████╗      ██║  ██║    ██╔████╔██║██║   ██║█████╗  ██████╔╝█████╗
        ██║  ██╗██║  ██║██╔══██╗██╔══██╗██╔══╝      ██║  ██║    ██║╚██╔╝██║██║   ██║██╔══╝  ██╔══██╗██╔══╝
        ╚█████╔╝╚█████╔╝██║  ██║██║  ██║███████╗    ╚█████╔╝    ██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║███████╗
         ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     ╚════╝     ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝
        """)

    print("-"*120)

def condittions_interface():
    print("""
       -----------------------------------------               -----------------------------------------
       |                                       |               |                                       |
       |       C̲O̲N̲D̲I̲C̲I̲O̲N̲E̲S̲ P̲A̲R̲A̲ G̲A̲N̲A̲R̲          |               |        C̲O̲N̲D̲I̲C̲I̲O̲N̲E̲S̲ P̲A̲R̲A̲ P̲E̲R̲D̲E̲R̲        |
       |                                       |               |                                       |
       |                                       |               |                                       |
       |   -QUE NO TE ALCANCEN LOS ENEMIGOS    |               |   -SER ALCANZADO POR LOS ENEMIGOS     |
       |                                       |               |                                       |             
       |   -CRUZAR LA FRONTERA                 |               |   -QUE LA MOTO NO FUNICONE            |                          
       |                                       |               |                                       |
       |   -ADMINISTRARSE LOS RECURSOS         |               |   -MALA ADMINISTRACION RECURSOS       |
       |                                       |               |                                       |
       |                                       |               |                                       |
       -----------------------------------------               -----------------------------------------
    """)

    print("\n")

def main_story_interface():
    title = "-"*5 + " BRASIL - AMAZONIA " + "-"*5

    print("\n"+title)
    print("""
        La guerra del 2031, activa durante 7 años, estaba a punto de terminar, gracias a la investigacion sobre el "Eye of God". Justo antes
        de iniciar el programa, para buscar a los dirigentes de ambos bandos de la guerra. El genio cientifico de Ronald Wayne, resulto ser un
        espia, que consiguio robar el software y escapar, sin ninguna sospecha.

        Inmediatamente Teraflops Statement contrato secretamente a Larry Tesler, especialista en infiltracion, robos y situaciones adversas. 
        Al dia siguiente Larry entro en accion. Siguio la pista de Ronald hasta encontrarlo en unas instalaciones militares secretas en Brasil.

        Enorabuena Larry Tesler! Has conseguido entrar en las intalaciones "Not 404 Found". Acabas de recuperar el software "Eye of God",
        este software es un arma de busqueda especifica, compuesto por una IA con conexion global, capaz de hackear cualquier 
        dispositivo que registre video, audio o posicion gps.

        Ten mucho cuidado con no romperlo, ni perderlo.
    """)

    print("\tMENSAJE ENTRANTE:\n")
    print("\t< - Boolean Office - Capitan: Curtis Priem - >\n")
    print("""\tLarry, sal de ahí mismo ya! Acaba de saltar una alarma por la Deep Web, descodificamos el mensaje, sus mejores agentes 
        se estan desplegando, creemos que son 5 pero pueden ser mas, utiliza tu llave maestra para coger cualquier vehiculo y salir por
        la forntera lo antes posible, te estaremos esperando al otro lado. 
        Suerte, confiamos en ti.
    """)

def level_title_interface(levels,level_game):

    print("-"*120)
    print("\t" + ("|  "+ str(levels[0][level_game])+". ") + levels[1][level_game])
    print("-"*120)

def level_stats_interface(game):
    print(f"""
            | <VEHICULO> | FUEL - {game[0][0]}% | ARMADURA - {game[0][1]}% | TURBO - {game[0][2]} | ARMAMENTO - {game[0][3]} |
            |            |
            | <PLAYER>   | DISTANCIA - {game[1][0]}km | SED - {game[1][1]}% | HAMBRE - {game[1][2]}% | SUEÑO - {game[1][3]}% |
            |            |
            | <ENEMIGOS> | DISTANCIA - {game[2][0]}km | CANTIDAD - {game[2][1]} |
    """)


##----------------
import time

game_start = start_game()         ## MENU INCIO JUEGO

while game_start == "":
    game = [[100,100,2,3],[0,0,0,0],[-20,5]]    ## 0-VEHICULO[ [0]FUEL, [1]ARMADURA, [2]TURBO, [3]ARMAMENTO ], 1-JUGADOR[ [0]DISTANCIA, [1]SED, [2]HAMBRE, [3]SUEÑO], 2-ENEMIGO[DISTANCIA,CANTIDAD] 
    levels = [[0,1,2,3,4,5,6,7,8,9],["EL ROBO","HUIDA RECINTO -- CORRE","JUNGLA -- CORRE","PUEBLO BAJO -- DESCANSO","CARRETERA -- CORRE","MONTAÑA -- CORRE","PUEBLO MINA -- DESCANSO","ACANTILADO -- CORRE","PLAYA -- CORRE","FRONTERA"]]     ## NIVELES DE JUEGO

    game_completed = False      ## VARIABLE JUEGO COMPLETADO
    level_game = 0              ## NIVEL ACTUAL DEL JUEGO
    action_events = [0,0]   ## CUENTA LOS EVENTOS EJECUTADOS // [0]TORMENTAS, [1]EMBOSCADA

    title_interface()
    time.sleep(5)
    condittions_interface()
    time.sleep(5)
    level_title_interface(levels,level_game)
    time.sleep(1)
    main_story_interface()
    time.sleep(10)

    while game_completed == False:  ## SI EL JUEGO NO ESTA COMPLETADO
        level_game += 1
        level_title_interface(levels,level_game)
        time.sleep(1)
        level_stats_interface(game)
        time.sleep(1)

        if level_game == 9:
            game_completed = True

        elif level_game == 3 or level_game == 6:
            level_village(game)

        else:
            level_running(game)
            if lose_condittion(game)==True:
                game_completed = True
                print("TE HAN CAPTURADO! HAS PERDIDO EL 'EYE OF GOD' Y LA VIDA...")
                break
            check_events(game,action_events,event)

        if lose_condittion(game)==True:
            game_completed = True
            print("TE HAN CAPTURADO! HAS PERDIDO EL 'EYE OF GOD' Y LA VIDA...")
            break
        elif win_condittion(game)==True:
            game_completed = True
            break

            

    if game_completed== True:    ## SI EL JUEGO SE HA COMPLETADO
        break

if win_condittion(game)==True:
    print("HAS ESCAPADO CON EXITO, Y SIN DAÑAR EL 'EYE OF GOD'. ENORABUENA!")

