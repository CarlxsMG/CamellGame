## INTRODUCCION A LA HISTORIA DEL JUEGO

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





levels = [[0],["EL REINO"]]
level_game = levels[0][0]
game = [[100,100,2,5],[0,0,0,00],[-20,5]]

title_interface()
condittions_interface()
main_story_interface()
level_title_interface(levels,level_game)
level_stats_interface(game)

    


