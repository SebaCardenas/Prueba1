El alcance de este programa es poder jugar con todo el potencial de Programón Rojo.
Al iniciar el juego, se puede crear un nuevo jugador, ingresando el nombre que desea y la clave que quiera.
Al crear un jugador aparece en la consola la posibilad de elejir cualquiera de los 3 primeros programones, si se escribe una opcion no válida, se imprime
un mensaje de alerta y se vuelve a preguntar la opcion que desea el jugador.
Se inicia en Pallet town, si se trata de retroceder, arroja un mensaje de alerta ya que esta es la primera ciudad del mapa.
se inicia el recorrido por las rutas y aparecen programones salvajes con un 35% de probabilidad.
se pueden capturar y atacar, al cambiar un programon el oponente ataca automaticamente. 
al terminar una pelea, se regenera la vida de los programones.
en el item consulta, se expresan todas las especificaciones del enunciado de la tarea.
la progradex puede imprimir todos los programones vistos y capturados sin repetirlos.
entrando a la ciudad menciona un mensaje de bienvenidos y todas las opciones etan disponibles.
el centro programon uno puede entrar al pc de bastian, de aqui tomar y dejar programones si un jugador tiene 6 programones,
el proximo programon capturado va directo al pc, ademas si tiene 6 en su lista, no puede sacar un programon sin que deje otro ante.
el jugador no se puede quedar sin programones.
en el gimnasio, se pelea primero con los entrenadores, siesque uno abandona el gimnacio y vuelve a entrar, se empieza con el entrenador que quedo anteriormente.
al vencerlos todos, se enfrenta al lider de gimnasio y al ganar, se recibe una medalla. al vencer un gimnasio no se puede
volver a enfrentar.
tienda programon vende prograbolas, los que cuestan 500 yenes cada una, al no tener dinero se muestra una alerta.
cada ruta tiene niveles de programones relacionados a medida que el jugador se aleja de Pallet town, los programones salvajes se vuelven más fuertes.
Ahora hablemos del programa, este contiene 4 archivos, ClasesProgramonRojo, Funciones, Tarea1_Programon y Menu
ClasesProgramonRojo es un archivo donde contiene todas las clases escenciales del juego, programones, jugador, entrenador, etc... ademas contienen todos los metodos 
relacionados con los distintos objetos se importaron las funciones randrange, random, randint de la libreria random y sqrt de la libreria math para 
poder calcular las estadisticas de los programones.
El archivo Tarea1_programon contiene los diccionarios obtenidos de jasonReader, asi poder tener la base de datos de los programones, gym, etc. aqui lo que se hizo fue 
instanciar todo lo necesario del juego para tener un respaldo y asi poder crear una copia del programon necesario, ruta etc. en el archivo se instancio todo y se mantiene las 
variables jugador actual para saber quien esta jugando, programon actual jugador para ver que programon esta siendo utilizado y programon actual salvaje que es el programon contrincante
de aqui se obtiene toda la informacion del juego.
El archivo Funciones, contiene clases con funciones escenciales para actualizar datos, crear los programones copia de la otra lista, comprobar la evolucion de un programon y por ultimo 
guardar en un diccionario toda la informacion del jugador acual, para luego transcribirla en un archivo. esto fue lo ultimo que se hizo puede que no funcione al 100%
Por último esta el archivo menú, este archivo es toda la clase que va a interactuar con el usuario, es decir es la que se utilizara como interfaz.
Lo que no se logro fue ingresar un usuario existente y el archivo jasonReader. 
