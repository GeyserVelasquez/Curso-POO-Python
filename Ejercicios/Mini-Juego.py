# Ejercicio: Clases

    # 1 - Clase Personaje: Crear una clase base que sirva como plantilla para personajes de un juego

    # Especificaciones: 
        # Debe tener estadisticas basicas como HP, ATK , DEF, VEL
        # Debe tener un Nombre
        # Debe poder Atacar, quitandole a otros personajes la siguiente formula: ` Enemigo.HP = Enemigo.HP - Personaje.ATK / Personaje.DEF `
        # Debe poder Esquivar, variando la probabilidad de esquive en funcion a su velocidad
        # Debe poder Defenderse, reduciendo el daño de la formula anterior a la mitad
        # Cada vez que lo ataquen debe validar si su vida llega a cero, lo pueden hacer con condicionales
        # Las estadisticas se deben ingresar con input()

    # 2 - Sub Clases Personaje: Crear 3 sub clase de personaje ( caballero, mercenario, arquero )

    # Especificaciones:
        # El caballero debe tener mucha defensa
        # El mercenario debe tener mucho ataque
        # El arquero debe tener mucha velocidad
        # Al usar los metodos atacar, cada sub clase debe mostrar una accion distinta ( Por ej: X lanzo su lanza, Y uso su espada, Z disparo una flecha )
        # A la hora de crear los personajes para jugar se debe mostrar los 3 posibles personajes que existen y que el jugador escoja ( Pueden darle un numero a cada tipo )

    # 3 - Clase Combate: Crear una clase que maneje la logica de un combate

    # Especificaciones:
        # Debe tomar en cuenta que en un combate primero ataca uno y luego ataca el otro, para decidir quien ataca primero, se hace un condicional con la velocidad
        # Debe tomar en cuenta los dos personajes que estan en el combate como atributos de la clase
        # Esta clase debe validar cuando uno de los dos pierda
        # El combate debe contar los turnos que se han hecho
        # El combate debe estar monitoreando constantemente el estado de los personajes, e ir mostrando su cantidad de vida cada turno
        # Cada turno debe aparecer un pequenio menu que indique las acciones que se pueden hacer y el personaje que esta escogiendo ( como tipico RPG )
        # Deben usar un While para repetir la eleccion de acciones de los jugadores hasta que uno de los personajes muera

