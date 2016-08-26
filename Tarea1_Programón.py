import jsonReader as Js
import random
import math as m
import ClasesProgramonRojo as CpR


DictProgramones = Js.jsonToDict("programones.json")
DictGyms = Js.jsonToDict("gyms.json")
DictProgramonesMoves = Js.jsonToDict("programonMoves.json")
DictRoutes = Js.jsonToDict("routes.json")
DictTypes = Js.jsonToDict("types.json")
DictMoveCategories = Js.jsonToDict("moveCategories.json")
Jugador_actual = CpR.Jugador(None, None, None)
Programon_actual_salvaje = None
dicc_progradex = {}
Contrincante_actual = None

lista_de_todos_programones = []
lista_de_todos_moves = []
lista_de_todos_los_gimnasios = []
lista_de_todas_las_rutas = []
lista_categoria_physic = None
lista_categoria_special = None
lista_de_todos_los_jugadores = []
lista_de_todas_las_ciudades = []


mapa = []

i = 0
for diccionari in DictProgramonesMoves:
    puntos_de_poder_aux = None
    tipo_aux = None
    nombre_mov_aux = None
    prescision_aux = None
    poder_base_aux = None

    for clav in diccionari:

        if clav == "pp":
            puntos_de_poder_aux = diccionari.get("pp")

        elif clav == "accuracy":
            prescision_aux = diccionari.get("accuracy")

        elif clav == "type":
            tipo_aux = diccionari.get("type")

        elif clav == "name":
            nombre_mov_aux = diccionari.get("name")

        elif clav == "power":
            poder_base_aux = diccionari.get("power")

        else:
            pass
    globals()['movimiento%s' % i] = CpR.Ataque(puntos_de_poder_aux, tipo_aux, nombre_mov_aux, prescision_aux,
                                               poder_base_aux)
    lista_de_todos_moves.append(globals()['movimiento%s' % i])
    i += 1

x = 0
for diccionarios in DictProgramones:
    id_aux = None
    nombre_aux = None
    movimiesntos_aux = None
    type_aux = None
    vida_aux = None
    velocidad_aux = None
    ataque_aux = None
    ataque_especial_aux = None
    defensa_aux = None
    defensa_aespecial_aux = None
    nivel_aux = None
    nivel_evolucion_aux = None

    for claves in diccionarios:

        if claves == "id":
            id_aux = diccionarios.get("id")

        elif claves == "name":
            nombre_aux = diccionarios.get("name")

        elif claves == "moves":
            lista_alternativa_de_ataques = []
            for attack in diccionarios.get("moves"):
                for recorrer in lista_de_todos_moves:
                    if attack == recorrer.nombre:
                        lista_alternativa_de_ataques.append(recorrer)

            movimiesntos_aux = lista_alternativa_de_ataques

        elif claves == "type":
            type_aux = diccionarios.get("type")

        elif claves == "hp":
            vida_aux = diccionarios.get("hp")

        elif claves == "speed":
            velocidad_aux = diccionarios.get("speed")

        elif claves == "attack":
            ataque_aux = diccionarios.get("attack")

        elif claves == "special_attack":
            ataque_especial_aux = diccionarios.get("special_attack")

        elif claves == "defense":
            defensa_aux = diccionarios.get("defense")

        elif claves == "special_defense":
            defensa_aespecial_aux = diccionarios.get("special_defense")

        elif claves == "evolveTo":
            nivel_aux = diccionarios.get("evolveTo")

        elif claves == "evolveLevel":
            nivel_evolucion_aux = diccionarios.get("evolveLevel")

        else:
            pass

    globals()['programon%s' % x] = CpR.Programon(id_aux, nombre_aux, movimiesntos_aux, type_aux, vida_aux,
                                                 velocidad_aux, ataque_aux, ataque_especial_aux, defensa_aux,
                                                 defensa_aespecial_aux, nivel_aux, nivel_evolucion_aux)

    lista_de_todos_programones.append(globals()['programon%s' % x])
    x += 1

g = 0
for diccionarioss in DictGyms:
    ciudad_aux = None
    idd_aux = None
    lider_aux = None
    entrenadores_aux = None

    for cla in diccionarioss:

        if cla == "city":
            ciudad_aux = diccionarioss.get("city")

        elif cla == "id":
            idd_aux = diccionarioss.get("id")

        elif cla == "leader":
            lista_alternativa_de_programones = []
            nombre_lider = diccionarioss["leader"]["name"]

            for programones in diccionarioss["leader"]["programones"]:
                for busqueda in lista_de_todos_programones:
                    po = busqueda.id

                    if po == programones["id"]:
                        busqueda.nivel = programones["level"]
                        busqueda.calculo_stats()
                        lista_alternativa_de_programones.append(busqueda)

                    else:
                        pass

            lider_aux = CpR.Entrenador(nombre_lider, lista_alternativa_de_programones)

        elif cla == "trainers":
            lista_alternativa_de_entrenadores = []

            for trainer in diccionarioss["trainers"]:
                entrenador_aux = None
                lista_alternativa_de_programoness = []
                nombre_entrenador = trainer["name"]

                for programoness in trainer["programones"]:
                    for busquedaa in lista_de_todos_programones:
                        poo = busquedaa.id

                        if poo == programoness["id"]:
                            busquedaa.nivel = programoness["level"]
                            lista_alternativa_de_programoness.append(busquedaa)

                        else:
                            pass

                entrenador_aux = CpR.Entrenador(nombre_entrenador, lista_alternativa_de_programoness)
                lista_alternativa_de_entrenadores.append(entrenador_aux)

            entrenadores_aux = lista_alternativa_de_entrenadores

    globals()['gimnasio%s' % g] = CpR.Gimnasio(ciudad_aux, idd_aux, lider_aux, entrenadores_aux)
    lista_de_todos_los_gimnasios.append(globals()['gimnasio%s' % g])
    g += 1

for dic in DictMoveCategories:

    if dic == "physical_moves":
        lista_categoria_physic = DictMoveCategories["physical_moves"]

    elif dic == "special_moves":
        lista_categoria_special = DictMoveCategories["special_moves"]

    else:
        pass

r = 1
for di in DictRoutes:
    start_aux = None
    destination_aux = None
    name_aux = None
    plvl_aux = None

    for c in di:

        if c == "starting_point":
            start_aux = di.get("starting_point")

        elif c == "destination":
            destination_aux = di.get("destination")

        elif c == "route":
            name_aux = di.get("route")

        elif c == "levels":
            plvl_aux = di.get("levels")

        else:
            pass
    globals()['ruta%s' % r] = CpR.Route(start_aux, destination_aux, name_aux, plvl_aux)
    lista_de_todas_las_rutas.append(globals()['ruta%s' % r])
    r += 1

PalletTown = CpR.Ciudad("Pallet Town", 0, None)
ViridianCity = None
PewterCity = None
CeruleanCity = None
SaffronCity = None
VermilionCity = None
CeladonCity = None
FuchsiaCity = None
CinnabarIsland = None

lista_de_todas_las_ciudades.append(PalletTown)

for p in range (1,10):
    arg1 = None
    arg2 = None
    arg3 = None
    for busqueda_gym in lista_de_todos_los_gimnasios:

        if busqueda_gym.ciudad == "Viridian City":
            arg1 = busqueda_gym.ciudad
            arg2 = 1
            arg3 = busqueda_gym
            ViridianCity = CpR.Ciudad(arg1, arg2, arg3)
            ViridianCity.centro_programon.pc = Jugador_actual.pcbastian
            lista_de_todas_las_ciudades.append(ViridianCity)

        elif busqueda_gym.ciudad == "Pewter City":
            arg1 = busqueda_gym.ciudad
            arg2 = 2
            arg3 = busqueda_gym
            PewterCity = CpR.Ciudad(arg1, arg2, arg3)
            PewterCity.centro_programon.pc = Jugador_actual.pcbastian
            lista_de_todas_las_ciudades.append(PewterCity)

        elif busqueda_gym.ciudad == "Cerulean City":
            arg1 = busqueda_gym.ciudad
            arg2 = 3
            arg3 = busqueda_gym
            CeruleanCity = CpR.Ciudad(arg1, arg2, arg3)
            CeruleanCity.centro_programon.pc = Jugador_actual.pcbastian
            lista_de_todas_las_ciudades.append(CeruleanCity)

        elif busqueda_gym.ciudad == "Saffron City":
            arg1 = busqueda_gym.ciudad
            arg2 = 4
            arg3 = busqueda_gym
            SaffronCity = CpR.Ciudad(arg1, arg2, arg3)
            SaffronCity.centro_programon.pc = Jugador_actual.pcbastian
            lista_de_todas_las_ciudades.append(SaffronCity)

        elif busqueda_gym.ciudad == "Vermilion City":
            arg1 = busqueda_gym.ciudad
            arg2 = 5
            arg3 = busqueda_gym
            VermilionCity = CpR.Ciudad(arg1, arg2, arg3)
            VermilionCity.centro_programon.pc = Jugador_actual.pcbastian
            lista_de_todas_las_ciudades.append(VermilionCity)

        elif busqueda_gym.ciudad == "Celadon City":
            arg1 = busqueda_gym.ciudad
            arg2 = 6
            arg3 = busqueda_gym
            CeladonCity = CpR.Ciudad(arg1, arg2, arg3)
            CeladonCity.centro_programon.pc = Jugador_actual.pcbastian
            lista_de_todas_las_ciudades.append(CeladonCity)

        elif busqueda_gym.ciudad == "Fuchsia City":
            arg1 = busqueda_gym.ciudad
            arg2 = 7
            arg3 = busqueda_gym
            FuchsiaCity = CpR.Ciudad(arg1, arg2, arg3)
            FuchsiaCity.centro_programon.pc = Jugador_actual.pcbastian
            lista_de_todas_las_ciudades.append(FuchsiaCity)

        elif busqueda_gym.ciudad == "Cinnabar Island":
            arg1 = busqueda_gym.ciudad
            arg2 = 8
            arg3 = busqueda_gym
            CinnabarIsland = CpR.Ciudad(arg1, arg2, arg3)
            CinnabarIsland.centro_programon.pc = Jugador_actual.pcbastian
            lista_de_todas_las_ciudades.append(CinnabarIsland)

lista_auxiliar_r = []

for t in range (1,9):
    for r in lista_de_todas_las_rutas:
        if r.nombre == t:
            lista_auxiliar_r.append(r)

for a in range (0,8):
    mapa.append(lista_de_todas_las_ciudades[a])
    mapa.append(lista_auxiliar_r[a])

Programon_actual_jugador = lista_de_todos_programones[0]
mapa.append(lista_de_todas_las_ciudades[8])


