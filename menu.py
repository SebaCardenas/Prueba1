import sys
import ClasesProgramonRojo as CpR
import Tarea1_Programón as T1p
import math as m
import random
import Funciones as Fu


class Menu:
    def __init__(self):
        self.j = 0
        self.inicio = {
            "1": self.ingresar,
            "2": self.nuevo_jugador
        }

        self.elegir_programon = {
            "1": self.charmander,
            "2": self.bulbasaur,
            "3": self.squirtle,
            "4": self.salirr
        }

        self.acciones = {
            "1": self.caminar,
            "2": self.progradex,
            "3": self.datos_del_jugador,
            "4": self.consultas,
            "5": self.salir
        }

        self.caminarr = {
            "1": self.avanzar,
            "2": self.retroceder,
            "3": self.salir_menu_principal
        }

        self.entrar_ciudad = {
            "1": self.centro_programon,
            "2": self.gimnasio,
            "3": self.tienda_programon,
            "4": self.caminar,
            "5": self.salir_menu_principal
        }

        self.programon_salvaje = {
            "1": self.pelear,
            "2": self.retirarse
        }

        self.pelear = {
            "1": self.elegir_movimiento,
            "2": self.capturar,
            "3": self.cambiar_programon,
            "4": self.retirarse
        }

        self.pelear2 = {
            "1": self.batallar,
            "2": self.cambiar_programon,
            "3": self.retirarse2
        }




        self.consulta = {
            "1": self.batalla_por_programon,
            "2": self.ranking,
            "3": self.jugador,
            "4": self.salir_menu_principal
        }

        self.centro_programon = {
            "1": self.pc_bastian,
            "2": self.salir_a_la_ciudad
        }

        self.pc_de_bastian = {
            "1": self.dejar_programon,
            "2": self.sacar_programon,
            "3": self.mostrar_programones_pc,
            "4": self.salir_a_la_ciudad
        }

        self.gimnasio = {
            "1": self.batallar_entrenadoress,
            "2": self.salir_a_la_ciudad
        }

        self.tienda_prograbolas = {
            "1": self.comprar,
            "2": self.salir_a_la_ciudad
        }

    def display_menu(self):
        print("""
            Menu:
                1: Ingresar
                2: Nuevo Jugador
            """)

    def mostrar_programones(self):
        print("""

        Felicitaciones!!!! Ahora para ser un verdadero entrenador Programón, debes elegir tu primer Pregramón!

        ¿Qué Programón te gustaría como tu primer acompañante?

            Menu:
                1: Charmander
                2: bulbasaur
                3: squirtle
                4: salir
            """)

    def mostrar_acciones(self):
        print("""
            Menu:
                1: Caminar
                2: Progradex
                3: Datos del Jugador
                4: Consultas
                5: Salir del Sistema
            """)

    def mostrar_caminar(self):
        print("""
            Menu:
                1: Avanzar
                2: Retroceder
                3: Salir
            """)

    def mostrar_ciudad(self):
        print("""
            Menu:
                1: Centro Programon
                2: Gimnasio
                3: Tienda programon
                4: Caminar
                5: Salir
            """)

    def sorpresa_programon_salvaje(self):
        print("""
            Menu:
                1: Pelear
                2: Retirarse
            """)

    def mostrar_pelear(self):
        print("""
            Menu:
                1: Elegir movimiento
                2: Capturar
                3: Cambiar Programon
                4: Retirarse
            """)

    def mostrar_pelear2(self):
        print("""
            Menu:
                1: Elegir movimiento
                2: Cambiar Programon
                3: Retirarse
            """)

    def mostrar_consulta(self):
        print("""
            Menu:
                1: Batallas por Programon
                2: Ranking
                3: Jugador
                4: salir
            """)

    def mostrar_centro_programon(self):
        print("""
            Menu:
                1: PC de Bastian
                2: Salir
            """)

    def mostrar_pc_de_bastian(self):
        print("""
            Menu:
                1: Dejar Programon
                2: Sacar Programon
                3: Entrar al PC,
                4: salir
            """)

    def mostrar_gimnasio(self):
        print("""
            Menu:
                1: Batallar
                2: Salir
            """)

    def mostrar_tienda_prograbolas(self):
        print("""
            Menu:
                1: Comprar Prograbolas
                2: Salir
            """)
    def run(self):

        while True:
            self.display_menu()
            eleccion = input("Ingrese Opcion: ")
            accion = self.inicio.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

    def ingresar(self):
        nombre_ingresado = input("Ingrese Nombre")
        contraseña_ingresada = input("Ingrese Contraseña")
        for Jugado in T1p.lista_de_todos_los_jugadores:

            if Jugado.nombre == nombre_ingresado and Jugado.contraseña == contraseña_ingresada:
                T1p.Jugador_actual = Jugado
            else:
                pass

        while True:
            self.mostrar_acciones()
            eleccion = input("Ingrese Opcion: ")
            accion = self.acciones.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

    def nuevo_jugador(self):
        nombre_nuevo = input(" Bienvenido! Escribe el nombre que más desees")
        contraseña_nueva = input("Escribe una contraseña")
        globals()['jugador%s' % self.j] = CpR.Jugador(self.j, nombre_nuevo, contraseña_nueva)
        T1p.lista_de_todos_los_jugadores.append(globals()['jugador%s' % self.j])
        T1p.Jugador_actual = globals()['jugador%s' % self.j]
        self.j += 1
        for poke in range (0,100):
            T1p.Jugador_actual.prograbolas.append(CpR.Prograbola())
        T1p.Jugador_actual.ubicacion = 0


        while True:
            self.mostrar_programones()
            eleccion = input("Ingrese Opcion: ")
            accion = self.elegir_programon.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))


    def charmander(self):

        nuevo_programon_5 = Fu.crear_charmander()
        T1p.dicc_progradex[nuevo_programon_5] = nuevo_programon_5
        T1p.Jugador_actual.lista_programones.append(nuevo_programon_5)
        T1p.Programon_actual_jugador = nuevo_programon_5


        while True:
            self.mostrar_acciones()
            eleccion = input("Ingrese Opcion: ")
            accion = self.acciones.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

    def bulbasaur(self):

        nuevo_programon_5 = Fu.crear_bulbasaur()
        T1p.dicc_progradex[nuevo_programon_5] = nuevo_programon_5
        T1p.Jugador_actual.lista_programones.append(nuevo_programon_5)
        T1p.Programon_actual_jugador = nuevo_programon_5

        while True:
            self.mostrar_acciones()
            eleccion = input("Ingrese Opcion: ")
            accion = self.acciones.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

    def squirtle(self):

        nuevo_programon_5 = Fu.crear_squirtle()
        T1p.dicc_progradex[nuevo_programon_5] = nuevo_programon_5
        T1p.Jugador_actual.lista_programones.append(nuevo_programon_5)
        T1p.Programon_actual_jugador = nuevo_programon_5

        while True:
            self.mostrar_acciones()
            eleccion = input("Ingrese Opcion: ")
            accion = self.acciones.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

    def caminar(self):
        while True:
            self.mostrar_caminar()
            eleccion = input("Ingrese Opcion: ")
            accion = self.caminarr.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))
        pass

    def progradex(self):
        for mip in T1p.dicc_progradex.values():

            if mip.capturado == False:
                print("Programón visto, Nombre: " + mip.nombre + " id: " + str(mip.id))
            else:
                if len(mip.movimientos) == 1:
                    print("Programón capturado, Nombre: " + mip.nombre + " id: " + str(mip.id) + " Tipo: " + mip.tipo +
                          " Movimientos: " + mip.movimientos[0].nombre)
                elif len(mip.movimientos) == 2:
                    print("Programón capturado, Nombre: " + mip.nombre + " id: " + str(mip.id) + " Tipo: " + mip.tipo +
                          " Movimientos: " + mip.movimientos[0].nombre + ", " + mip.movimientos[1].nombre)
                elif len(mip.movimientos) == 3:
                    print("Programón capturado, Nombre: " + mip.nombre + " id: " + str(mip.id) + " Tipo: " + mip.tipo +
                          " Movimientos: " + mip.movimientos[0].nombre + ", " + mip.movimientos[1].nombre
                          + ", " + mip.movimientos[2].nombre)
                elif len(mip.movimientos) == 4:
                    print("Programón capturado, Nombre: " + mip.nombre + " id: " + str(mip.id) + " Tipo: " + mip.tipo +
                          " Movimientos: " + mip.movimientos[0].nombre + ", " + mip.movimientos[1].nombre + ", "
                          + mip.movimientos[2].nombre + ", " + mip.movimientos[3].nombre)
                else:
                    pass
    def datos_del_jugador(self):
        pass

    def consultas(self):
        while True:
            self.mostrar_consulta()
            eleccion = input("Ingrese Opcion: ")
            accion = self.consulta.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

    def avanzar(self):
        if T1p.Jugador_actual.ubicacion == 0:
            T1p.Jugador_actual.ubicacion += 1
            T1p.Jugador_actual.ubicacionaux = 1
        elif T1p.Jugador_actual.ubicacion == 16:
            print("ALERTA!! no se puede avanzar! Retroceda.")

        elif T1p.Jugador_actual.ubicacionaux == 0:
            T1p.Jugador_actual.ubicacion += 1
            T1p.Jugador_actual.ubicacionaux += 1

        elif T1p.Jugador_actual.ubicacionaux == 3:
            T1p.Jugador_actual.ubicacion += 1
            T1p.Jugador_actual.ubicacionaux = 0
        else:
            T1p.Jugador_actual.ubicacionaux += 1

        print(T1p.Jugador_actual.ubicacion)
        print(T1p.Jugador_actual.ubicacionaux)

        if T1p.Jugador_actual.ubicacion == 2 or T1p.Jugador_actual.ubicacion == 4 or T1p.Jugador_actual.ubicacion == 6 \
                or T1p.Jugador_actual.ubicacion == 8 or T1p.Jugador_actual.ubicacion == 10 \
                or T1p.Jugador_actual.ubicacion == 12 or T1p.Jugador_actual.ubicacion == 14 \
                or T1p.Jugador_actual.ubicacion == 16:
            while True:
                print("Bienvenido a " + T1p.mapa[T1p.Jugador_actual.ubicacion].nombre)
                self.mostrar_ciudad()
                eleccion = input("Ingrese Opcion: ")
                accion = self.entrar_ciudad.get(eleccion)
                if accion:
                    accion()  # aqui se llama a la funcion
                else:
                    print("{0} no es una opcion valida".format(eleccion))

        elif T1p.Jugador_actual.ubicacion == 0:

            print("Bienvenido a " + T1p.mapa[T1p.Jugador_actual.ubicacion].nombre)
            while True:
                self.mostrar_acciones()
                eleccion = input("Ingrese Opcion: ")
                accion = self.acciones.get(eleccion)
                if accion:
                    accion()  # aqui se llama a la funcion
                else:
                    print("{0} no es una opcion valida".format(eleccion))

        else:
            print("Esta es la Ruta " + str(T1p.mapa[T1p.Jugador_actual.ubicacion].nombre))
            porcentaje = random.random()
            if porcentaje <= 0.35:
                ProgramonSalvaje = Fu.crear_salvaje()
                ProgramonSalvaje.nivel = random.randint(T1p.mapa[T1p.Jugador_actual.ubicacion].plvl[0],
                                                        T1p.mapa[T1p.Jugador_actual.ubicacion].plvl[1])

                T1p.Programon_actual_salvaje = ProgramonSalvaje
                estaendict = False
                for gt in T1p.dicc_progradex.values():
                    if T1p.Programon_actual_salvaje.nombre == gt.nombre:
                        estaendict = True

                    else:
                        pass
                if estaendict == False:
                    T1p.dicc_progradex[T1p.Programon_actual_salvaje] = T1p.Programon_actual_salvaje

                else:
                    pass

                print("Aparecio un " + T1p.Programon_actual_salvaje.nombre + " Salvaje de nivel: " + str(T1p.Programon_actual_salvaje.nivel) +
                      " Vida: " + str(T1p.Programon_actual_salvaje.vida))

                print(T1p.Jugador_actual.nombre + ": "+ T1p.Programon_actual_jugador.nombre + " Yo te elijo!!!!!!")
                print(T1p.Programon_actual_jugador.nombre + " nivel: " + str(T1p.Programon_actual_jugador.nivel) +
                      " Vida: " + str(T1p.Programon_actual_jugador.vida))

                if T1p.Programon_actual_salvaje.vida > 0:
                    while True:
                        self.mostrar_pelear()
                        eleccion = input("Ingrese Opcion: ")
                        accion = self.pelear.get(eleccion)
                        if accion:
                            accion()  # aqui se llama a la funcion
                        else:
                            print("{0} no es una opcion valida".format(eleccion))

                else:
                    print("Felicitaciones " + T1p.Programon_actual_salvaje.nombre + " Fue derrotado")
                    Fu.restaurar_vida(T1p.Jugador_actual)
                    T1p.Programon_actual_jugador.victoria += 1
                    T1p.Jugador_actual.registro_batalla.append(Fu.registro(T1p.Programon_actual_jugador.nombre,
                                                                           T1p.Programon_actual_salvaje.nombre,
                                                                           "Salvaje",
                                                                           "Victoria"))


    def retroceder(self):

        if T1p.Jugador_actual.ubicacion == 16:
            T1p.Jugador_actual.ubicacion -= 1
            T1p.Jugador_actual.ubicacionaux = 3

        elif T1p.Jugador_actual.ubicacion == 0:
            print("ALERTA!! no se puedes Retroceder! Avanza.")

        elif T1p.Jugador_actual.ubicacionaux == 1:
            T1p.Jugador_actual.ubicacion -= 1
            T1p.Jugador_actual.ubicacionaux -= 1

        elif T1p.Jugador_actual.ubicacionaux == 0:
            T1p.Jugador_actual.ubicacion -= 1
            T1p.Jugador_actual.ubicacionaux = 3

        elif T1p.Jugador_actual.ubicacionaux == 3:
            T1p.Jugador_actual.ubicacionaux -= 1

        else:
            T1p.Jugador_actual.ubicacionaux -= 1

        print(T1p.Jugador_actual.ubicacion)
        print(T1p.Jugador_actual.ubicacionaux)

        if T1p.Jugador_actual.ubicacion == 2 or T1p.Jugador_actual.ubicacion == 4 or T1p.Jugador_actual.ubicacion == 6 \
                or T1p.Jugador_actual.ubicacion == 8 or T1p.Jugador_actual.ubicacion == 10 \
                or T1p.Jugador_actual.ubicacion == 12 or T1p.Jugador_actual.ubicacion == 14 \
                or T1p.Jugador_actual.ubicacion == 16:
            while True:
                print("Bienvenido a " + T1p.mapa[T1p.Jugador_actual.ubicacion].nombre)
                self.mostrar_ciudad()
                eleccion = input("Ingrese Opcion: ")
                accion = self.entrar_ciudad.get(eleccion)
                if accion:
                    accion()  # aqui se llama a la funcion
                else:
                    print("{0} no es una opcion valida".format(eleccion))

        elif T1p.Jugador_actual.ubicacion == 0:

            print("Bienvenido a " + T1p.mapa[T1p.Jugador_actual.ubicacion].nombre)
            while True:
                self.mostrar_acciones()
                eleccion = input("Ingrese Opcion: ")
                accion = self.acciones.get(eleccion)
                if accion:
                    accion()  # aqui se llama a la funcion
                else:
                    print("{0} no es una opcion valida".format(eleccion))

        else:
            print("Esta es la Ruta " + str(T1p.mapa[T1p.Jugador_actual.ubicacion].nombre))
            porcentaje = random.random()
            if porcentaje <= 0.35:
                ProgramonSalvaje = Fu.crear_salvaje()
                ProgramonSalvaje.nivel = random.randint(T1p.mapa[T1p.Jugador_actual.ubicacion].plvl[0],
                                                        T1p.mapa[T1p.Jugador_actual.ubicacion].plvl[1])
                ProgramonSalvaje.calculo_stats()


                T1p.Programon_actual_salvaje = ProgramonSalvaje
                estaendict = False
                for gt in T1p.dicc_progradex.values():
                    if T1p.Programon_actual_salvaje.nombre == gt.nombre:
                        estaendict = True

                    else:
                        pass
                if estaendict == False:
                    T1p.dicc_progradex[T1p.Programon_actual_salvaje] = T1p.Programon_actual_salvaje

                else:
                    pass


                print("Aparecio un " + T1p.Programon_actual_salvaje.nombre + " Salvaje de nivel: " + str(T1p.Programon_actual_salvaje.nivel) +
                      " Vida: " + str(T1p.Programon_actual_salvaje.vida))

                print(T1p.Jugador_actual.nombre + ": " + T1p.Programon_actual_jugador.nombre + " Yo te elijo!!!!!!")
                print(T1p.Programon_actual_jugador.nombre + " nivel: " + str(T1p.Programon_actual_jugador.nivel) +
                      " Vida: " + str(T1p.Programon_actual_jugador.vida))

                if T1p.Programon_actual_salvaje.vida > 0:
                    while True:
                        self.mostrar_pelear()
                        eleccion = input("Ingrese Opcion: ")
                        accion = self.pelear.get(eleccion)
                        if accion:
                            accion()  # aqui se llama a la funcion
                        else:
                            print("{0} no es una opcion valida".format(eleccion))

                else:
                    print("Felicitaciones " + T1p.Programon_actual_salvaje.nombre + " Fue derrotado")
                    Fu.restaurar_vida(T1p.Jugador_actual)
                    T1p.Programon_actual_jugador.victoria += 1
                    T1p.Jugador_actual.registro_batalla.append(Fu.registro(T1p.Programon_actual_jugador.nombre,
                                                                           T1p.Programon_actual_salvaje.nombre,
                                                                           "Salvaje",
                                                                           "Victoria"))
    def centro_programon(self):
        print("Bienvenido al Centro Progremón de: " + T1p.mapa[T1p.Jugador_actual.ubicacion].nombre)
        while True:
            self.mostrar_centro_programon()
            eleccion = input("Ingrese Opcion: ")
            accion = self.centro_programon.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

    def gimnasio(self):
        print("Bienvenido al Bienvenido al Gimnasio de: " + T1p.mapa[T1p.Jugador_actual.ubicacion].nombre)
        while True:
            self.mostrar_gimnasio()
            eleccion = input("Ingrese Opcion: ")
            accion = self.gimnasio.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

    def tienda_programon(self):
        print("Bienvenido a la Tienda Progremón de: " + T1p.mapa[T1p.Jugador_actual.ubicacion].nombre)
        while True:
            self.mostrar_tienda_prograbolas()
            eleccion = input("Ingrese Opcion: ")
            accion = self.tienda_prograbolas.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

    def pelear(self):
        while True:
            self.mostrar_pelear()
            eleccion = input("Ingrese Opcion: ")
            accion = self.pelear.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

    def retirarse(self):
        print("Cobarde te haz retirado!")
        Fu.restaurar_vida(T1p.Jugador_actual)
        T1p.Jugador_actual.registro_batalla.append(Fu.registro(T1p.Programon_actual_jugador.nombre,
                                                                         T1p.Programon_actual_salvaje.nombre,
                                                                         "Salvaje",
                                                                         "Retirada"))
        while True:
            self.mostrar_acciones()
            eleccion = input("Ingrese Opcion: ")
            accion = self.acciones.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))
        pass

    def elegir_movimiento(self):

        opcion2 = Fu.batalla_entrenador()

        if T1p.Programon_actual_salvaje.vida > 0 and T1p.Programon_actual_jugador.vida > 0:
            acertar = random.random()

            if acertar <= int(T1p.Programon_actual_jugador.movimientos[opcion2].prescision):
                mom = random.randrange(0, len(T1p.Programon_actual_salvaje.movimientos))
                daño_inflingido_Jugador = Fu.daño(
                    T1p.Programon_actual_jugador,
                    T1p.Programon_actual_salvaje,
                    T1p.Programon_actual_jugador.movimientos[opcion2],
                    T1p.Programon_actual_salvaje.movimientos[mom])

                print("Usaste " + T1p.Programon_actual_jugador.movimientos[opcion2].nombre)

                print(T1p.Programon_actual_jugador.nombre + " Acertó! ")

                T1p.Programon_actual_salvaje.vida -= float(daño_inflingido_Jugador)

                if T1p.Programon_actual_salvaje.vida <= 0:
                    T1p.Programon_actual_salvaje.vida = 0
                    print(T1p.Programon_actual_salvaje.nombre + " Salvaje de nivel: " +
                          str(T1p.Programon_actual_salvaje.nivel) +
                          " Vida: " + str(T1p.Programon_actual_salvaje.vida))

                    print(T1p.Programon_actual_jugador.nombre + " nivel: " + str(T1p.Programon_actual_jugador.nivel) +
                          " Vida: " + str(T1p.Programon_actual_jugador.vida))

                    print(T1p.Programon_actual_salvaje.nombre + " Fue vencido")
                    T1p.Jugador_actual.dinero += 200
                    print("Ganaste 200 Yenes!")
                    T1p.Programon_actual_jugador.victoria += 1
                    T1p.Jugador_actual.registro_batalla.append(Fu.registro(T1p.Programon_actual_jugador.nombre,
                                                                                  T1p.Programon_actual_salvaje.nombre,
                                                                                  "Salvaje",
                                                                                  "Victoria"))

                    Fu.restaurar_vida(T1p.Jugador_actual)
                    T1p.Programon_actual_jugador.nivel += 1
                    T1p.Programon_actual_jugador.calculo_stats()
                    print(T1p.Programon_actual_jugador.nombre + " Subió a Nivel: " +
                          str(T1p.Programon_actual_jugador.nivel))

                    Fu.comprobar_evol()
                    Fu.actualizar(T1p.Programon_actual_jugador)
                    Fu.agregar_programon_anterior(T1p.Programon_actual_jugador)

                    while True:
                        self.mostrar_acciones()
                        eleccion = input("Ingrese Opcion: ")
                        accion = self.acciones.get(eleccion)
                        if accion:
                            accion()  # aqui se llama a la funcion
                        else:
                            print("{0} no es una opcion valida".format(eleccion))
                else:
                    print(T1p.Programon_actual_salvaje.nombre + " Salvaje de nivel: " +
                          str(T1p.Programon_actual_salvaje.nivel) +
                          " Vida: " + str(T1p.Programon_actual_salvaje.vida))


                    print(T1p.Programon_actual_jugador.nombre + " nivel: " + str(T1p.Programon_actual_jugador.nivel) +
                          " Vida: " + str(T1p.Programon_actual_jugador.vida))


            else:
                print(T1p.Programon_actual_jugador.nombre + " Falló!!")

            acertar2 = random.random()
            rara = random.randrange(
                0,len(T1p.Programon_actual_salvaje.movimientos))
            if acertar2 <= int(T1p.Programon_actual_salvaje.movimientos[rara].prescision):

                daño_inflingido_Programon_salvaje = Fu.daño(
                    T1p.Programon_actual_salvaje,
                    T1p.Programon_actual_jugador,
                    T1p.Programon_actual_jugador.movimientos[opcion2],
                    T1p.Programon_actual_salvaje.movimientos[random.randrange
                    (0,len(T1p.Programon_actual_salvaje.movimientos))])

                print(T1p.Programon_actual_salvaje.nombre + " Usó " +
                      T1p.Programon_actual_salvaje.movimientos[rara].nombre)

                print(T1p.Programon_actual_salvaje.nombre + " Acertó! ")

                T1p.Programon_actual_jugador.vida -= daño_inflingido_Programon_salvaje
                print(T1p.Programon_actual_salvaje.nombre + " Salvaje de nivel: " +
                      str(T1p.Programon_actual_salvaje.nivel) +
                      " Vida: " + str(T1p.Programon_actual_salvaje.vida))


                if T1p.Programon_actual_jugador.vida <= 0:
                    T1p.Programon_actual_jugador.vida = 0
                    print(T1p.Programon_actual_jugador.nombre + " Fue vencido")
                    print(T1p.Programon_actual_jugador.nombre + " REGRESAAA!!!")
                    T1p.Programon_actual_jugador.derrota += 1
                    T1p.Jugador_actual.registro_batalla.append(Fu.registro(T1p.Programon_actual_jugador.nombre,
                                                                                  T1p.Programon_actual_salvaje.nombre,
                                                                                  "Salvaje",
                                                                                  "Derrota"))

                    relacion = False
                    for huhuhu in T1p.Jugador_actual.lista_programones:
                        if huhuhu.vida > 0 :
                            relacion = True
                            while True:
                                ra = random.randrange(0,len(T1p.Jugador_actual.lista_programones))
                                if T1p.Jugador_actual.lista_programones[ra].vida > 0:
                                    T1p.Programon_actual_jugador = T1p.Jugador_actual.lista_programones[ra]
                                    break
                                else:
                                    pass
                        else:
                            pass
                    if relacion == False:
                        print("Perdiste!!!")
                        Fu.restaurar_vida(T1p.Jugador_actual)
                        T1p.Jugador_actual.dinero -= 100

                        while True:
                            self.mostrar_acciones()
                            eleccion = input("Ingrese Opcion: ")
                            accion = self.acciones.get(eleccion)
                            if accion:
                                accion()  # aqui se llama a la funcion
                            else:
                                print("{0} no es una opcion valida".format(eleccion))
                    else:
                        print(T1p.Programon_actual_jugador.nombre + " Yo te elijo!!!!!!")
                else:
                    print(T1p.Programon_actual_jugador.nombre + " nivel: " + str(T1p.Programon_actual_jugador.nivel) +
                          " Vida: " + str(T1p.Programon_actual_jugador.vida))
            else:
                print(T1p.Programon_actual_salvaje.nombre + " Falló!!")
        else:
            pass


    def capturar(self):
        if len(T1p.Jugador_actual.prograbolas)>0:
            proca = T1p.Programon_actual_salvaje.capturar()
            if random.random() < proca:
                T1p.Programon_actual_salvaje.capturado = True
                if len(T1p.Jugador_actual.lista_programones) <= 6:
                    T1p.Jugador_actual.lista_programones.append(T1p.Programon_actual_salvaje)
                else:
                    T1p.Jugador_actual.pcbastian.datos_pc.append(T1p.Programon_actual_salvaje)
                T1p.Jugador_actual.prograbolas.pop()
                print("Felicitaciones!! atrapaste a un " + T1p.Programon_actual_salvaje.nombre)
                Fu.restaurar_vida(T1p.Jugador_actual)
                if T1p.Programon_actual_salvaje not in T1p.dicc_progradex:
                    T1p.dicc_progradex[T1p.Programon_actual_salvaje.nombre] = T1p.Programon_actual_salvaje
                else:
                    pass

                while True:
                    self.mostrar_acciones()
                    eleccion = input("Ingrese Opcion: ")
                    accion = self.acciones.get(eleccion)
                    if accion:
                        accion()  # aqui se llama a la funcion
                    else:
                        print("{0} no es una opcion valida".format(eleccion))

            else:
                print(T1p.Programon_actual_salvaje.nombre + " Escapó")
                T1p.Jugador_actual.prograbolas.pop()
                print("Te quedan " + str(len(T1p.Jugador_actual.prograbolas)) + " Prograbolas")

        else:

            print("No te quedan Prograbolas")


    def cambiar_programon(self):
        for lip in range(0, len( T1p.Jugador_actual.lista_programones)):
            cambio = False
            if  T1p.Jugador_actual.lista_programones[lip].vida > 0 and T1p.Jugador_actual.lista_programones[lip]!= \
                T1p.Programon_actual_jugador:
                print(T1p.Programon_actual_jugador.nombre + " REGRESA!")
                while True:
                    raf = random.randrange(0, len(T1p.Jugador_actual.lista_programones))
                    if T1p.Jugador_actual.lista_programones[raf] != T1p.Programon_actual_jugador:
                        T1p.Programon_actual_jugador = T1p.Jugador_actual.lista_programones[raf]
                        print(T1p.Programon_actual_jugador.nombre + " Yo te elijo!!!!!!")
                        break
                    else:
                        pass
                acertar2 = random.random()
                rara = random.randrange(
                    0, len(T1p.Programon_actual_salvaje.movimientos))
                if acertar2 <= int(T1p.Programon_actual_salvaje.movimientos[rara].prescision):

                    daño_inflingido_Programon_salvaje = Fu.daño(
                        T1p.Programon_actual_salvaje,
                        T1p.Programon_actual_jugador,
                        T1p.Programon_actual_jugador.movimientos[random.randrange
                        (0, len(T1p.Programon_actual_jugador.movimientos))],
                        T1p.Programon_actual_salvaje.movimientos[random.randrange
                        (0, len(T1p.Programon_actual_salvaje.movimientos))])

                    print(T1p.Programon_actual_salvaje.nombre + " Usó " +
                          T1p.Programon_actual_salvaje.movimientos[rara].nombre)

                    print(T1p.Programon_actual_salvaje.nombre + " Acertó! ")

                    T1p.Programon_actual_jugador.vida -= daño_inflingido_Programon_salvaje
                    print(T1p.Programon_actual_salvaje.nombre + " Salvaje de nivel: " +
                          str(T1p.Programon_actual_salvaje.nivel) +
                          " Vida: " + str(T1p.Programon_actual_salvaje.vida))

                    if T1p.Programon_actual_jugador.vida <= 0:
                        T1p.Programon_actual_jugador.vida = 0
                        print(T1p.Programon_actual_jugador.nombre + " Fue vencido")
                        print(T1p.Programon_actual_jugador.nombre + " REGRESAAA!!!")
                        T1p.Programon_actual_jugador.derrota += 1
                        T1p.Jugador_actual.registro_batalla.append(Fu.registro(T1p.Programon_actual_jugador.nombre,
                                                                                      T1p.Programon_actual_salvaje.nombre,
                                                                                      "Salvaje",
                                                                                      "Derrota"))

                        relacion = False
                        for huhuhu in T1p.Jugador_actual.lista_programones:
                            if huhuhu.vida > 0:
                                relacion = True
                                while True:
                                    ra = random.randrange(0, len(T1p.Jugador_actual.lista_programones))
                                    if T1p.Jugador_actual.lista_programones[ra].vida > 0:
                                        T1p.Programon_actual_jugador = T1p.Jugador_actual.lista_programones[ra]
                                        break
                                    else:
                                        pass
                            else:
                                pass
                        if relacion == False:
                            print("Perdiste!!!")
                            Fu.restaurar_vida(T1p.Jugador_actual)
                            T1p.Jugador_actual.dinero -= 100

                            while True:
                                self.mostrar_acciones()
                                eleccion = input("Ingrese Opcion: ")
                                accion = self.acciones.get(eleccion)
                                if accion:
                                    accion()  # aqui se llama a la funcion
                                else:
                                    print("{0} no es una opcion valida".format(eleccion))
                        else:
                            print(T1p.Programon_actual_jugador.nombre + " Yo te elijo!!!!!!")
                    else:
                        print(T1p.Programon_actual_jugador.nombre + " nivel: " + str(T1p.Programon_actual_jugador.nivel) +
                              " Vida: " + str(T1p.Programon_actual_jugador.vida))
                else:
                    print(T1p.Programon_actual_salvaje.nombre + " Falló!!")

    def batalla_por_programon(self):
        variable = len(T1p.Jugador_actual.lista_programones)
        while True:
            for gh in range(0, variable):
                print(str(gh) + ": " + T1p.Jugador_actual.lista_programones[gh].nombre)
            yoyo = input("¿Qué Programón quieres consultar?")

            if yoyo.isdigit():
                yoyo = int(yoyo)
                for gl in T1p.Jugador_actual.registro_batalla:

                    if T1p.Jugador_actual.lista_programones[yoyo].nombre == gl[0]:
                        print("Nombre: " + gl[0] + ", " +
                              " Programón Contrincante: " + gl[1] + ", " +
                              " Dueño: " + gl[2] + ", " +
                              " Resultado: " + gl[3])
                    else:
                        pass
                break
            else:
                print("Ingresa una opcion válida")

    def ranking(self):
        lista_programones_jugador = T1p.Jugador_actual.lista_programones
        lista_programones_jugador.extend(T1p.Jugador_actual.pcbastian.datos_pc)
        print(lista_programones_jugador)
        #lista_programones_jugador.sort(key=lambda x: x.victoria)
        #sorted(lista_programones_jugador, key=lambda obj:obj.victoria)
        contador1 = 0
        for fer in sorted(lista_programones_jugador, key=Fu.byAge_key , reverse = True):
            if contador1 == 10:
                break
            else:
                if fer.victoria + fer.derrota >= 10:
                    print(" Programón: {}, N° Victorias: {}".format(fer.nombre,fer.victoria))
                    contador1 += 1



    def jugador(self):
        print("Nombre: " + T1p.Jugador_actual.nombre + "\n" +
            "Dinero: " + str(T1p.Jugador_actual.dinero) +"\n" +
            "N° de prograbolas: " + str(len(T1p.Jugador_actual.prograbolas)) + "\n")
        print("Medallas: ")
        for t in T1p.Jugador_actual.medallas:
            print(t)

        print("\n Peleas: Nombre de Programón usado/Nombre Programón contrincante/(salvaje o entrenador)/Resultado")
        for gl in T1p.Jugador_actual.registro_batalla:
            print("        " +
                "Nombre: " + gl[0] + ", " +
                " Programón Contrincante: " + gl[1] + ", " +
                " Dueño: " + gl[2] + ", " +
                " Resultado: " + gl[3])




    def mostrar_programones_pc(self):
        for ju in T1p.Jugador_actual.pcbastian.datos_pc:
            print("Programón capturado, Nombre: " + ju.nombre + " id: " + str(ju.id) + " Tipo: " + ju.tipo)

    def pc_bastian(self):
        while True:
            self.mostrar_pc_de_bastian()
            eleccion = input("Ingrese Opcion: ")
            accion = self.pc_de_bastian.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

    def dejar_programon(self):
        variable = len(T1p.Jugador_actual.lista_programones)
        if variable > 1:
            while True:
                for gh in range(0, variable):
                    print(str(gh) + ": " + T1p.Jugador_actual.lista_programones[gh].nombre)
                yoyo = input("¿Qué Programón quieres dejar?")

                if yoyo.isdigit() and int(yoyo) <= variable:
                    yoyo = int(yoyo)

                    T1p.Jugador_actual.pcbastian.datos_pc.append(T1p.Jugador_actual.lista_programones[yoyo])
                    T1p.Jugador_actual.lista_programones.remove(T1p.Jugador_actual.lista_programones[yoyo])
                    break
                else:
                    print("Ingrese una opción válida")

        else:
            print("No puedes quedarte sin Programones.")

        T1p.Programon_actual_jugador = T1p.Jugador_actual.lista_programone[0]

    def sacar_programon(self):
        variable = len(T1p.Jugador_actual.lista_programones)
        variable2 = len(T1p.Jugador_actual.pcbastian.datos_pc)
        if variable <= 6:
            while True:
                for gh in range(0, variable2):
                    print(str(gh) + ": " + T1p.Jugador_actual.pcbastian.datos_pc[gh].nombre)
                y = input("¿Qué Programón quieres sacar?")

                if y.isdigit() and int(y) <= variable2:
                    y = int(y)

                    T1p.Jugador_actual.lista_programones.append(T1p.Jugador_actual.pcbastian.datos_pc[y])
                    T1p.Jugador_actual.pcbastian.datos_pc.remove(T1p.Jugador_actual.pcbastian.datos_pc[y])
                    break

        else:
            print("Tu Canasta de Programones, ya esta llena.")
        T1p.Programon_actual_jugador = T1p.Jugador_actual.lista_programone[0]

    def batallar_entrenadoress(self):
        Gym = None
        for ggg in T1p.lista_de_todos_los_gimnasios:
            if ggg.ciudad == T1p.mapa[T1p.Jugador_actual.ubicacion].nombre:
                Gym = ggg
            else:
                pass

        if Gym.lider.vencido == False:

            contador_entrenador = 1
            for encuentro in Gym.entrenadores:
                T1p.Contrincante_actual = encuentro
                if encuentro.vencido == False:

                    print("Soy: " + encuentro.nombre + ", el entrenador N° " + str(contador_entrenador) + " de "
                          + str(len(Gym.entrenadores)) + ". Tendrás que vencerme para poder llegar al Líder de Gimnasio: "
                          + Gym.lider.nombre)
                    T1p.Programon_actual_salvaje = encuentro.lista_programones[0]

                    print(T1p.Jugador_actual.nombre + ": " + T1p.Programon_actual_jugador.nombre + " Yo te elijo!!!")

                    print(T1p.Programon_actual_jugador.nombre + " nivel: " + str(T1p.Programon_actual_jugador.nivel) +
                          " Vida: " + str(T1p.Programon_actual_jugador.vida))

                    print(T1p.Contrincante_actual.nombre + ": " + T1p.Programon_actual_salvaje.nombre + " Yo te elijo!!!")

                    print(T1p.Programon_actual_salvaje.nombre + " Nivel: " +
                          str(T1p.Programon_actual_salvaje.nivel) +
                          " Vida: " + str(T1p.Programon_actual_salvaje.vida))

                    while True:
                        self.mostrar_pelear2()
                        eleccion = input("Ingrese Opcion: ")
                        accion = self.pelear2.get(eleccion)
                        if accion:
                            accion()  # aqui se llama a la funcion
                        else:
                            print("{0} no es una opcion valida".format(eleccion))

                else:

                    T1p.Contrincante_actual = Gym.lider
                    T1p.Programon_actual_salvaje = Gym.lider.lista_programones[0]
                    print("\n\n\nSoy: " + Gym.lider.nombre + ", el Líder de este Gimnasio, comencemos esta Batalla!!!")

                    print(T1p.Contrincante_actual.nombre + ": " + T1p.Programon_actual_salvaje.nombre + " Yo te elijo!!!")

                    print(T1p.Programon_actual_salvaje.nombre + " Nivel: " +
                          str(T1p.Programon_actual_salvaje.nivel) +
                          " Vida: " + str(T1p.Programon_actual_salvaje.vida))
                    print(T1p.Jugador_actual.nombre + ": " + T1p.Programon_actual_jugador.nombre + " Yo te elijo!!!")

                    print(T1p.Programon_actual_jugador.nombre + " nivel: " + str(T1p.Programon_actual_jugador.nivel) +
                          " Vida: " + str(T1p.Programon_actual_jugador.vida))

                    while True:
                        self.mostrar_pelear2()
                        eleccion = input("Ingrese Opcion: ")
                        accion = self.pelear2.get(eleccion)
                        if accion:
                            accion()  # aqui se llama a la funcion
                        else:
                            print("{0} no es una opcion valida".format(eleccion))

        else:
            if Gym.ciudad not in T1p.Jugador_actual.medallas:
                print("Felicitaciones te ganaste la medalla "+ Gym.ciudad )
                T1p.Jugador_actual.medallas[Gym.ciudad] = Gym.ciudad

            else:
                print("Ya derrotaste este Gimnasio")

            while True:
                self.mostrar_ciudad()
                eleccion = input("Ingrese Opcion: ")
                accion = self.entrar_ciudad.get(eleccion)
                if accion:
                    accion()  # aqui se llama a la funcion
                else:
                    print("{0} no es una opcion valida".format(eleccion))

    def batallar(self):
        opcion2 = Fu.batalla_entrenador()

        if T1p.Programon_actual_salvaje.vida > 0 and T1p.Programon_actual_jugador.vida > 0:
            acertar = random.random()

            if acertar <= int(T1p.Programon_actual_jugador.movimientos[opcion2].prescision):
                mom = random.randrange(0, len(T1p.Programon_actual_salvaje.movimientos))
                daño_inflingido_Jugador = Fu.daño(
                    T1p.Programon_actual_jugador,
                    T1p.Programon_actual_salvaje,
                    T1p.Programon_actual_jugador.movimientos[opcion2],
                    T1p.Programon_actual_salvaje.movimientos[mom])

                print("Usaste " + T1p.Programon_actual_jugador.movimientos[opcion2].nombre)

                print(T1p.Programon_actual_jugador.nombre + " Acertó! ")

                T1p.Programon_actual_salvaje.vida -= float(daño_inflingido_Jugador)

                if T1p.Programon_actual_salvaje.vida <= 0:
                    T1p.Programon_actual_salvaje.vida = 0
                    print(T1p.Programon_actual_salvaje.nombre + " Fue vencido")
                    print(T1p.Programon_actual_salvaje.nombre + " REGRESAAA!!!")
                    T1p.Programon_actual_jugador.victoria += 1
                    T1p.Jugador_actual.registro_batalla.append(Fu.registro(T1p.Programon_actual_jugador.nombre,
                                                                                  T1p.Programon_actual_salvaje.nombre,
                                                                                  "Entrenador: " +
                                                                                  T1p.Contrincante_actual.nombre,
                                                                                  "Victoria"))

                    T1p.Programon_actual_jugador.nivel += 1
                    Fu.comprobar_evol()
                    Fu.actualizar(T1p.Programon_actual_jugador)
                    Fu.agregar_programon_anterior(T1p.Programon_actual_jugador)

                    relacion = False
                    for huhuhu in T1p.Contrincante_actual.lista_programones:
                        if huhuhu.vida > 0:
                            relacion = True
                            while True:
                                ra = random.randrange(0, len(T1p.Contrincante_actual.lista_programones))
                                if T1p.Contrincante_actual.lista_programones[ra].vida > 0:
                                    T1p.Programon_actual_salvaje = T1p.Contrincante_actual.lista_programones[ra]
                                    break
                                else:
                                    pass
                        else:
                            pass
                    if relacion == False:
                        print(T1p.Contrincante_actual.nombre + " Fue derrotado, Ganaste 200 Yenes!")
                        T1p.Jugador_actual.dinero += 200
                        T1p.Contrincante_actual.vencido = True
                        self.batallar_entrenadoress()
                    else:
                        print(T1p.Programon_actual_salvaje.nombre + " Yo te elijo!!!!!!")
                else:
                    print(T1p.Programon_actual_salvaje.nombre + " Nivel: " + str(
                        T1p.Programon_actual_salvaje.nivel) +
                          " Vida: " + str(T1p.Programon_actual_salvaje.vida))
            else:
                print(T1p.Programon_actual_jugador.nombre + " Falló!!")

        acertar2 = random.random()
        rara = random.randrange(
            0, len(T1p.Programon_actual_salvaje.movimientos))

        if acertar2 <= int(T1p.Programon_actual_salvaje.movimientos[rara].prescision):

            daño_inflingido_Programon_salvaje = Fu.daño(
                T1p.Programon_actual_salvaje,
                T1p.Programon_actual_jugador,
                T1p.Programon_actual_jugador.movimientos[opcion2],
                T1p.Programon_actual_salvaje.movimientos[random.randrange
                (0, len(T1p.Programon_actual_salvaje.movimientos))])

            print(T1p.Programon_actual_salvaje.nombre + " Usó " +
                  T1p.Programon_actual_salvaje.movimientos[rara].nombre)

            print(T1p.Programon_actual_salvaje.nombre + " Acertó! ")

            T1p.Programon_actual_jugador.vida -= daño_inflingido_Programon_salvaje
            print(T1p.Programon_actual_salvaje.nombre + " Nivel: " +
                  str(T1p.Programon_actual_salvaje.nivel) +
                  " Vida: " + str(T1p.Programon_actual_salvaje.vida))

            if T1p.Programon_actual_jugador.vida <= 0:
                T1p.Programon_actual_jugador.vida = 0
                print(T1p.Programon_actual_jugador.nombre + " Fue vencido")
                print(T1p.Programon_actual_jugador.nombre + " REGRESAAA!!!")
                T1p.Programon_actual_jugador.derrota += 1
                T1p.Jugador_actual.registro_batalla.append(Fu.registro(T1p.Programon_actual_jugador.nombre,
                                                                              T1p.Programon_actual_salvaje.nombre,
                                                                              "Entrenador: " +
                                                                              T1p.Contrincante_actual.nombre,
                                                                              "Derrota"))

                relacion = False
                for huhuhu in T1p.Jugador_actual.lista_programones:
                    if huhuhu.vida > 0:
                        relacion = True
                        while True:
                            ra = random.randrange(0, len(T1p.Jugador_actual.lista_programones))
                            if T1p.Jugador_actual.lista_programones[ra].vida > 0:
                                T1p.Programon_actual_jugador = T1p.Jugador_actual.lista_programones[ra]
                                break
                            else:
                                pass
                    else:
                        pass
                if relacion == False:
                    print("Perdiste!!! Paga 100 Yenes. Intentalo más Tarde")
                    T1p.Jugador_actual.dinero -= 100
                    Fu.restaurar_vida(T1p.Jugador_actual)
                    while True:
                        self.mostrar_ciudad()
                        eleccion = input("Ingrese Opcion: ")
                        accion = self.entrar_ciudad.get(eleccion)
                        if accion:
                            accion()  # aqui se llama a la funcion
                        else:
                            print("{0} no es una opcion valida".format(eleccion))
                else:
                    print(T1p.Programon_actual_jugador.nombre + " Yo te elijo!!!!!!")
            else:
                print(
                    T1p.Programon_actual_jugador.nombre + " nivel: " + str(T1p.Programon_actual_jugador.nivel) +
                    " Vida: " + str(T1p.Programon_actual_jugador.vida))
        else:
            print(T1p.Programon_actual_salvaje.nombre + " Falló!!")

    def comprar(self):

        if T1p.Jugador_actual.dinero > 0:

            print("Tienes " + str(T1p.Jugador_actual.dinero) + " Yenes")
            compra = input(""" ¿Cuantas prograbolas deseas comprar? Cada prograbola cuesta 500 Yenes:

            """)
            o = int(compra)

            if T1p.Jugador_actual.dinero - 500*o >=0:

                if T1p.Jugador_actual.dinero%500 == 0:
                    for ji in range (0,o):
                        T1p.Jugador_actual.prograbolas.append(CpR.Prograbola())

                T1p.Jugador_actual.dinero = T1p.Jugador_actual.dinero - 500 * o

                print("Felicitaciones compraste " + str(o) + " Prograbolas, ahora tienes " +
                      str(len(T1p.Jugador_actual.prograbolas)))

            else:
                print("No tienes suficiente dinero")

        else:
            print("No tienes suficiente dinero, vuelve cuando no seas POBRE!")

    def salirr(self):
        while True:
            self.display_menu()
            eleccion = input("Ingrese Opcion: ")
            accion = self.inicio.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

    def salir(self):
        print("Gracias por jugar Programón Rojo")
        sys.exit(0)

    def salir_a_la_ciudad(self):
        while True:
            self.mostrar_ciudad()
            eleccion = input("Ingrese Opcion: ")
            accion = self.entrar_ciudad.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))
    def retirarse2(self):
        print("Te haz retirado")
        Fu.restaurar_vida(T1p.Jugador_actual)
        T1p.Jugador_actual.registro_batalla.append(Fu.registro(T1p.Programon_actual_jugador.nombre,
                                                                         T1p.Programon_actual_salvaje.nombre,
                                                                         "Entrenador: " +
                                                                         T1p.Contrincante_actual.nombre,
                                                                         "Retirada"))
        while True:
            self.mostrar_gimnasio()
            eleccion = input("Ingrese Opcion: ")
            accion = self.pelear2.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))
    def salir_menu_principal(self):
        while True:
            self.mostrar_acciones()
            eleccion = input("Ingrese Opcion: ")
            accion = self.acciones.get(eleccion)
            if accion:
                accion()  # aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))

if __name__ == "__main__":  # esto es para que corra en la consola
    Menu().run()