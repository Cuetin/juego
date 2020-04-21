from .gameobject import GameObject
from .razas import Goblin, Elf
import random

#Hay que revisar como conseguir comparar el nombre ignorando mayusculas y minusculas para las funciones hit y examine
#Finalmente almaceno los nombres en mayusculas porque queda mas vistoso que minusculas y los comparo con upper pero ojala exista algo mejor

def ayuda(noun):
    """
Muestra la informacion sobre los comandos disponibles y el funcionamiento de los mismos. 
Recibe el comando del cual mostrar la informacion y retorna la informacion solicitada.
    """
    if noun.lower() == 'registrar':
        msg = 'El comando registrar te permite crear un nuevo personaje con el formato "registrar nombre_personaje"'
    elif noun.lower() == 'golpear':
        msg = 'El comando golpear hace que tu guerrero aseste un golpe a otro personaje con el formato "golpear nombre_a_golpear"'
    elif noun.lower() == 'consultar':
        msg = 'El comando consultar te muestra la informacion detallada de un personaje con el formato "consultar nombre_personaje"'
    elif noun.lower() == 'decir':
        msg = 'El comando decir muestra un mensaje con el formato "decir mensaje_a_decir"'
    elif noun.lower() == 'general':
        msg = 'Los comandos son:\n"decir"\n"registrar"\n"consultar"\n"golpear"\nPara conocer cada comando en especifico use "info comando_a_conocer".\nPara ver esta ayuda de nuevo usa el comando info general.'
    else:
        msg = 'Comando no reconocido. Usa info general para ver la lista de comandos disponibles.'
    return msg

def register(noun):
    """
Crea un nuevo personaje en el juego mediante la clase GameObject y una subclase del tipo raza. 
Recibe el nombre del personaje a crear y comprueba si el personaje ya existe y despues comprueba de que raza debe ser, retorna un mensaje con la accion realizada.
    """
    if noun in GameObject.objects:
        return noun + " ya existe!!!"
    raza = input("Que raza es " + noun + ": ")
    if raza.lower() == "duende":
        Goblin(noun)
        return "Se ha creado el personaje " + noun + " con exito."
    elif raza.lower() == "elfo":
        Elf(noun)
        return "Se ha creado el personaje " + noun + " con exito."
    else:
        return "Esa raza no existe."

def hit(noun):
    """
Permite golpear a un personaje, los golpes tienen un 20% de probabilidad de ser criticos, en cuyo caso quitan el doble de vida.
Recibe el nombre del personaje a golpear y comprueba si existe y si esta vivo y despues le cambia el atributo de ps en funcion del golpe y retorna un mensaje con la accion realizada.
    """
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if thing.ps > 0:
            if type(thing) == Goblin or type(thing) == Elf:
                if random.randint(0, 100) <= 20: #Aqui es donde se implementa la probabilidad de critico
                    thing.ps = thing.ps - 2
                    msg = "GOLPE CRITICO!!! Has golpeado a {}, su estado es {} y su salud {} hp.".format(thing.name, thing.state, thing.ps)
                else:
                    thing.ps = thing.ps - 1
                    msg = "Has golpeado a {}, su estado es {} y su salud {} hp.".format(thing.name, thing.state, thing.ps)
                if thing.ps <= 0:
                    msg = msg + " Has matado a {}.".format(thing.name)
        else:
            msg = "{} esta ya muerto no quieras ensañarte!!!!".format(thing.name)
    else:
        msg = "No hay {} para luchar.".format(noun)
    return msg


def examine(noun):
    """
Muestra toda la informacion de un personaje.
Recibe el nombre del personaje que deseamos mostrar, comprueba si esta registrado y retorna su información.
    """
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_description()
    else:
        return "No has registrado {} todavia.".format(noun)

def get_input():
    """
Esta funcion recibe los comandos del usuario y ejecuta la funcion correspondiente.
Recibe un string el cual divide por palabras y comprueba si el comando existe en el diccionario de acciones y ejecuta esa funcion con la segunda palabra del comando como parametro.
    """
    command = input("Introduzca su comando: ").split() #Uso el separador espacio para separar por palabras
    key_word = command[0].lower()
    if key_word in command_dict:
        action = command_dict[key_word]
    else:
        print("No existe el comando {}. Para ver la lista de comandos usa info general".format(key_word))
        return

    if len(command) >=2:
        if key_word == "registrar" or key_word == "golpear" or key_word == "consultar": #Esta transformacion a mayusculas se produce para almacenarlo y comparar los nombres sin problemas de como lo introduzca el usuario
            noun_word = command[1].upper()
        else:
            noun_word = command[1]
        print(action(noun_word))
    else:
        print(action("nothing"))


def say(noun):
    """
Me siento ridiculo poniendole documentacion a esto.
    """
    return 'Has dicho "{}"'.format(noun)

command_dict = {    #Diccionario de acciones que se puede de realizar, es decir, lista de comandos
    "decir":say,
    "consultar":examine,
    "golpear":hit,
    "registrar":register,
    "info":ayuda,
    }