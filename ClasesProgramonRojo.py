import random
import math as m


class Ataque:

    def __init__(self, puntos_de_poder, tipo, nombre, prescision, poder_base):
        self.puntos_de_poder = puntos_de_poder
        self.tipo = tipo
        self.nombre = nombre
        self.prescision = prescision
        self.poder_base = poder_base


class Programon:

    def __init__(self, id, nombre, movimientos, tipo, vida, velocidad, ataque, ataque_especial, defensa,
                                                                                                defensa_especial,
                                                                                                id_evol,
                                                                                                nivel_evolucion):
        self.id = id
        self.nombre = nombre
        self.movimientos = movimientos
        self.tipo = tipo
        self.vida = vida
        self.velocidad = velocidad
        self.velocidadbase = velocidad
        self.ataque = ataque
        self.ataquebase = ataque
        self.ataque_especial = ataque_especial
        self.ataque_especialbase = ataque_especial
        self.defensa = defensa
        self.defensabase = defensa
        self.defensa_especial = defensa_especial
        self.defensa_especialbase = defensa_especial
        self.nivel = 1
        self.nivel_evolucion = nivel_evolucion
        self.id_evolucion = id_evol
        self.capturado = False
        self.vidabase = vida
        self.vidatotal = None
        self.idanterior = id
        self.victoria = 0
        self.derrota = 0

    def calculo_stats(self):

        hp = (((self.vidabase + random.randint(0,15))*2 + (m.sqrt(random.randint(0,65535)))/4)*self.nivel)/100 + \
             self.nivel + 10

        self.vida = hp
        self.vidatotal = hp

        otrohpataque = (((self.ataque + random.randint(0, 15)) * 2 + (
            m.sqrt(random.randint(0, 65535))) / 4) * self.nivel) / 100 + 5

        otrohpataqueespecial = (((self.ataque_especial + random.randint(0, 15)) * 2 + (
            m.sqrt(random.randint(0, 65535))) / 4) * self.nivel) / 100 + 5

        otrohpdefensa = (((self.defensa + random.randint(0, 15)) * 2 + (
            m.sqrt(random.randint(0, 65535))) / 4) * self.nivel) / 100 + 5

        otrohpdefensaespecial = (((self.defensa_especial + random.randint(0, 15)) * 2 + (
            m.sqrt(random.randint(0, 65535))) / 4) * self.nivel) / 100 + 5

        otrohpvelocidad = (((self.velocidad + random.randint(0, 15)) * 2 + (
            m.sqrt(random.randint(0, 65535))) / 4) * self.nivel) / 100 + 5

        self.ataque = otrohpataque
        self.ataque_especial = otrohpataqueespecial
        self.defensa = otrohpdefensa
        self.defensa_especial = otrohpdefensaespecial
        self.velocidad = otrohpvelocidad


    def capturar(self):

        procap = 0.2 + ((self.vidatotal-self.vida)/self.vidatotal)*0.8
        return procap

    def evolucionar(self, id, nombre, movimientos, tipo, vida, velocidad, ataque, ataque_especial, defensa,
                                                                                                defensa_especial,
                                                                                                id_evol,
                                                                                                nivel_evolucion):
        self.id = id
        self.nombre = nombre
        self.movimientos = movimientos
        self.tipo = tipo
        self.vidabase = vida
        self.velocidadbase = velocidad
        self.ataquebase = ataque
        self.ataque_especialbase = ataque_especial
        self.defensabase = defensa
        self.defensa_especialbase = defensa_especial
        self.id_evolucion = id_evol
        self.nivel_evolucion = nivel_evolucion



class Prograbola:

    def __init__(self):
        self.estado = None


class Progradex:

    def __init__(self):
        self.programones_vistos = []
        self.programones_capturados = []


class PcDeBastian:

    def __init__(self):
        self.datos_pc = []


class Entrenador:

    def __init__(self, nombre_entrenador, programones):
        self.nombre = nombre_entrenador
        self.lista_programones = programones
        self.vencido = False


class Jugador(Entrenador):

    def __init__(self, id, nombre, contraseña):
        Entrenador.__init__(self, nombre_entrenador = nombre, programones = [])
        self.id = id
        self.name = nombre
        self.contraseña = contraseña
        self.dinero = 1000
        self.progradex = Progradex()
        self.medallas = {}
        self.prograbolas = []
        self.ubicacion = 0
        self.ubicacionaux = 0
        self.pcbastian = PcDeBastian()
        self.registro_batalla = []


class TiendaDePrograbolas:

    def __init__(self):
        pass


class CentroDeProgramon:

    def __init__(self):

        self.pc = PcDeBastian


class Gimnasio:

    def __init__(self, ciudad, id, lider, entrenadores):
        self.ciudad = ciudad
        self.id = id
        self.lider = lider
        self.entrenadores = entrenadores


class Ciudad:

    def __init__(self, nombre, id, gimnasio):
        self.nombre = nombre
        self.id = id
        self.tienda_de_progrbolas = TiendaDePrograbolas()
        self.centro_programon = CentroDeProgramon()
        self.gimnasio = gimnasio


class Route:

    def __init__(self, start, destination, name, plvl):
        self.start = start
        self.destination = destination
        self.nombre = name
        self.plvl = plvl