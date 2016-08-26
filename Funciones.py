import Tarea1_Programón as T1p
import random
import ClasesProgramonRojo as CpR
from collections import namedtuple


def restaurar_vida(entrenador):

    for x in entrenador.lista_programones:
        x.vida = x.vidatotal


def daño(PA, PD, A, D):

    dano = None
    modificador = None

    P = random.randint(0, 256)
    T = PA.velocidadbase / 2

    if PD.tipo in T1p.DictTypes[A.tipo]:
        Tip = T1p.DictTypes[A.tipo][PD.tipo]

    else:
        Tip = 1

    if PA.tipo == A.tipo:
        STAB = 1.5

    else:
        STAB = 1

    if P < T:
        Critico = 2
    else:
        Critico = 1

    while True:
        shu = random.random()

        if shu >= 0.85:
            modificador = STAB * Tip * Critico * shu
            break

        else:
            pass

    if A.tipo in T1p.lista_categoria_physic and D.tipo in T1p.lista_categoria_physic:
        dano = ((2 * PA.nivel + 10) / 250) * (((PA.ataque / PD.defensa) * PA.ataquebase) + 2) * modificador

    elif A.tipo in T1p.lista_categoria_physic and D.tipo in T1p.lista_categoria_special:
        dano = ((2 * PA.nivel + 10) / 250) * (((PA.ataque / PD.defensa_especial) * PA.ataquebase) + 2) * modificador

    elif A.tipo in T1p.lista_categoria_special and D.tipo in T1p.lista_categoria_physic:
        dano = ((2 * PA.nivel + 10) / 250) * (
        ((PA.ataque_especial / PD.defensa) * PA.ataque_especialbase) + 2) * modificador

    elif A.tipo in T1p.lista_categoria_special and D.tipo in T1p.lista_categoria_special:
        dano = ((2 * PA.nivel + 10) / 250) * (((PA.ataque_especial / PD.defensa_especial) *
                                               PA.ataque_especialbase) + 2) * modificador

    else:
        pass

    return dano


def actualizar(pokemon):

    selid = T1p.Programon_actual_jugador.id
    selnombre = T1p.Programon_actual_jugador.nombre
    selmovimientos = T1p.Programon_actual_jugador.movimientos
    seltipo = T1p.Programon_actual_jugador.tipo
    selvida = T1p.Programon_actual_jugador.vida
    selvelocidad = T1p.Programon_actual_jugador.velocidad
    selvelocidadbase = T1p.Programon_actual_jugador.velocidadbase
    selataque = T1p.Programon_actual_jugador.ataque
    selataquebase = T1p.Programon_actual_jugador.ataquebase
    selataque_especial = T1p.Programon_actual_jugador.ataque_especial
    selataque_especialbase = T1p.Programon_actual_jugador.ataque_especialbase
    seldefensa = T1p.Programon_actual_jugador.defensa
    seldefensabase = T1p.Programon_actual_jugador.defensabase
    seldefensa_especial = T1p.Programon_actual_jugador.defensa_especial
    seldefensa_especialbase = T1p.Programon_actual_jugador.defensa_especialbase
    selnivel = T1p.Programon_actual_jugador.nivel
    selnivel_evolucion = T1p.Programon_actual_jugador.nivel_evolucion
    selid_evolucion = T1p.Programon_actual_jugador.id_evolucion
    selcapturado = T1p.Programon_actual_jugador.capturado
    selvidabase = T1p.Programon_actual_jugador.vidabase
    selvidatotal = T1p.Programon_actual_jugador.vidatotal
    selidanterior = T1p.Programon_actual_jugador.idanterior

    for no in range(0, len(T1p.Jugador_actual.lista_programones)):

        if T1p.Jugador_actual.lista_programones[no].id == T1p.Programon_actual_jugador.id:

            T1p.Programon_actual_jugador.id = selid
            T1p.Programon_actual_jugador.nombre = selnombre
            T1p.Programon_actual_jugador.movimientos = selmovimientos
            T1p.Programon_actual_jugador.tipo = seltipo
            T1p.Programon_actual_jugador.vida = selvida
            T1p.Programon_actual_jugador.velocidad = selvelocidad
            T1p.Programon_actual_jugador.velocidadbase = selvelocidadbase
            T1p.Programon_actual_jugador.ataque = selataque
            T1p.Programon_actual_jugador.ataquebase = selataquebase
            T1p.Programon_actual_jugador.ataque_especial = selataque_especial
            T1p.Programon_actual_jugador.ataque_especialbase = selataque_especialbase
            T1p.Programon_actual_jugador.defensa = seldefensa
            T1p.Programon_actual_jugador.defensabase = seldefensabase
            T1p.Programon_actual_jugador.defensa_especial = seldefensa_especial
            T1p.Programon_actual_jugador.defensa_especialbase = seldefensa_especialbase
            T1p.Programon_actual_jugador.nivel = selnivel
            T1p.Programon_actual_jugador.nivel_evolucion = selnivel_evolucion
            T1p.Programon_actual_jugador.id_evolucion = selid_evolucion
            T1p.Programon_actual_jugador.capturado = selcapturado
            T1p.Programon_actual_jugador.vidabase = selvidabase
            T1p.Programon_actual_jugador.vidatotal = selvidatotal
            T1p.Programon_actual_jugador.idanterior = selidanterior

        else:
            pass


def crear_charmander():

    for NombreProgramon in T1p.lista_de_todos_programones:

        if NombreProgramon.nombre == "Charmander":
            retorno = CpR.Programon(NombreProgramon.id, NombreProgramon.nombre, NombreProgramon.movimientos,
                                    NombreProgramon.tipo, NombreProgramon.vida, NombreProgramon.velocidad,
                                    NombreProgramon.ataque, NombreProgramon.ataque_especial, NombreProgramon.defensa,
                                    NombreProgramon.defensa_especial, NombreProgramon.id_evolucion,
                                    NombreProgramon.nivel_evolucion)

            retorno.nivel = 5
            retorno.capturado = True
            retorno.calculo_stats()

            return retorno

        else:
            pass


def crear_bulbasaur():

    for NombreProgramon in T1p.lista_de_todos_programones:

        if NombreProgramon.nombre == "Bulbasaur":
            retorno = CpR.Programon(NombreProgramon.id, NombreProgramon.nombre, NombreProgramon.movimientos,
                                    NombreProgramon.tipo, NombreProgramon.vida, NombreProgramon.velocidad,
                                    NombreProgramon.ataque, NombreProgramon.ataque_especial, NombreProgramon.defensa,
                                    NombreProgramon.defensa_especial, NombreProgramon.id_evolucion,
                                    NombreProgramon.nivel_evolucion)

            retorno.nivel = 5
            retorno.capturado = True
            retorno.calculo_stats()

            return retorno

        else:
            pass


def crear_squirtle():

    for NombreProgramon in T1p.lista_de_todos_programones:

        if NombreProgramon.nombre == "Squirtle":
            retorno = CpR.Programon(NombreProgramon.id, NombreProgramon.nombre, NombreProgramon.movimientos,
                                    NombreProgramon.tipo, NombreProgramon.vida, NombreProgramon.velocidad,
                                    NombreProgramon.ataque, NombreProgramon.ataque_especial, NombreProgramon.defensa,
                                    NombreProgramon.defensa_especial, NombreProgramon.id_evolucion,
                                    NombreProgramon.nivel_evolucion)

            retorno.nivel = 5
            retorno.capturado = True
            retorno.calculo_stats()

            return retorno

        else:
            pass


def crear_salvaje():

    jy = random.randrange(0, len(T1p.lista_de_todos_programones))
    NombreProgramon = T1p.lista_de_todos_programones[jy]
    retorno = CpR.Programon(NombreProgramon.id, NombreProgramon.nombre, NombreProgramon.movimientos,
                            NombreProgramon.tipo, NombreProgramon.vida, NombreProgramon.velocidad,
                            NombreProgramon.ataque, NombreProgramon.ataque_especial, NombreProgramon.defensa,
                            NombreProgramon.defensa_especial, NombreProgramon.id_evolucion,
                            NombreProgramon.nivel_evolucion)

    retorno.calculo_stats()

    return retorno


def comprobar_evol():

    if T1p.Programon_actual_jugador.nivel == T1p.Programon_actual_jugador.nivel_evolucion and \
                    T1p.Programon_actual_jugador.nivel_evolucion != None:

        for evol in T1p.lista_de_todos_programones:

            if evol.id == T1p.Programon_actual_jugador.id_evolucion:
                for nos in range(0, len(T1p.Jugador_actual.lista_programones)):

                    if T1p.Jugador_actual.lista_programones[nos].id == T1p.Programon_actual_jugador.id:
                        print(T1p.Programon_actual_jugador.nombre + " Evolucionó a:")
                        T1p.Jugador_actual.lista_programones[nos].evolucionar(evol.id, evol.nombre,
                                                                              evol.movimientos,
                                                                              evol.tipo,
                                                                              evol.vida,
                                                                              evol.velocidad,
                                                                              evol.ataque,
                                                                              evol.ataque_especial,
                                                                              evol.defensa,
                                                                              evol.defensa_especial,
                                                                              evol.id_evolucion,
                                                                              evol.nivel_evolucion)
                        print(T1p.Programon_actual_jugador.nombre)


def agregar_programon_anterior(programon):

    for NombreProgramongg in T1p.lista_de_todos_programones:

        if NombreProgramongg.id == programon.idanterior:
            T1p.dicc_progradex[NombreProgramongg] = NombreProgramongg

        else:
            pass


def batalla_entrenador():

    opcion2 = None

    if len(T1p.Programon_actual_jugador.movimientos) == 1:
        print("\n    Menu:" + "\n       1: " + T1p.Programon_actual_jugador.movimientos[0].nombre)

        while True:
            opcion = input("\nIngrese opción:")

            if opcion != "1":
                print("{0} no es una opcion valida".format(opcion))
                opcion2 = None

            else:
                opcion = int(opcion)
                opcion2 = opcion - 1
                break

    elif len(T1p.Programon_actual_jugador.movimientos) == 2:
        print(
            "\n    Menu:" + "\n       1: " + T1p.Programon_actual_jugador.movimientos[0].nombre + "\n       2: "
            + T1p.Programon_actual_jugador.movimientos[1].nombre)

        while True:
            opcion = input("\nIngrese opción:")

            if opcion != "1" and opcion != "2":
                print("{0} no es una opcion valida".format(opcion))
                opcion2 = None

            else:
                opcion = int(opcion)
                opcion2 = opcion - 1
                break

    elif len(T1p.Programon_actual_jugador.movimientos) == 3:
        print(
            "\n    Menu:" + "\n       1: " + T1p.Programon_actual_jugador.movimientos[0].nombre + "\n       2: "
            + T1p.Programon_actual_jugador.movimientos[1].nombre
            + "\n       3: " + T1p.Programon_actual_jugador.movimientos[2].nombre)

        while True:
            opcion = input("\nIngrese opción:")

            if opcion != "1" and opcion != "2" and opcion != "3":
                print("{0} no es una opcion valida".format(opcion))
                opcion2 = None

            else:
                opcion = int(opcion)
                opcion2 = opcion - 1
                break

    elif len(T1p.Programon_actual_jugador.movimientos) == 4:
        print(
            "\n    Menu:" + "\n       1: " + T1p.Programon_actual_jugador.movimientos[0].nombre + "\n       2: "
            + T1p.Programon_actual_jugador.movimientos[1].nombre
            + "\n       3: " + T1p.Programon_actual_jugador.movimientos[2].nombre + "\n       4: "
            + T1p.Programon_actual_jugador.movimientos[3].nombre)

        while True:
            opcion = input("\nIngrese opción:")

            if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
                print("{0} no es una opcion valida".format(opcion))
                opcion2 = None

            else:
                opcion = int(opcion)
                opcion2 = opcion - 1
                break

    else:
        pass

    return opcion2


def registro(Nombre_Programon, Nombre_contrincante_programon, Dueño, resultado):

    return Nombre_Programon, Nombre_contrincante_programon, Dueño, resultado


def byAge_key(person):

    return person.victoria


def guardar(jugador):

    diccionadrioJugador = {}
    diccionadrioJugador["Nombre:"] = jugador.nombre
    diccionadrioJugador["Dinero:"] = jugador.dinero
    diccionadrioJugador["Medallas:"] = jugador.medallas
    diccionadrioJugador["ProgramonesVistos:"] = jugador.progradex.programones_vistos
    diccionadrioJugador["ProgramonesCapturados:"] = jugador.progradex.programones_capturados
    diccionadrioJugador["Password:"] = jugador.contraseña
    diccionadrioJugador["Prograbolas:"] = len(jugador.prograbolas)
    diccionadrioJugador["Ubicaion:"] = [jugador.ubicacion, jugador.ubicacionaux]
    diccionadrioJugador["Batallas:"] = jugador.medallas





