import random

class Battle:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.actual_turn = 0

    def is_finished(self):
        finished = self.player.ps <= 0 or self.enemy.ps <= 0
        if finished:
            self.print_winner()
        return finished

    def print_winner(self):
        if self.player.ps <= 0 < self.enemy.ps:
            print(enemy.name+" te ha ganado en "+str(self.actual_turn)+" turnos.")
        elif self.enemy.ps <= 0 < self.player.ps:
            print("Has ganado a "+self.enemy.name+" en "+str(self.actual_turn)+" turnos.")
        else:
            print("Double KO!!")

    def execute_turn(self, turn):
        #Pillamos los comandos
        command1 = turn.command1
        command2 = turn.command2
        #Inicializamos los ataques a NULL
        attack1 = None
        attack2 = None
        #Comprobamos si quieren atacar
        if 'atacar' in command1.action.keys():
            attack1 = self.player.attacks[command1.action['atacar']]
        if 'atacar' in command2.action.keys():
            attack2 = self.enemy.attacks[command2.action['atacar']]

        #Se producen los ataques
        self.enemy.ps -= attack1.dmg
        if self.enemy.ps > 0:
            self.player.ps -= attack2.dmg
        
        #En caso de que la vida sea negativa la dejamos a cero
        self.enemy.ps = max(0, self.enemy.ps)
        self.player.ps = max(0, self.player.ps)

        self.actual_turn += 1


    def print_current_status(self):
        print(self.player.name+" tiene "+str(self.player.ps)+" hp.")
        print(self.enemy.name+" tiene "+str(self.enemy.ps)+" hp.")


class Turn:
    def __init__(self):
        self.command1 = None
        self.command2 = None

    def can_start(self):
        return self.command1 is not None and self.command2 is not None


class Command:
    def __init__(self, action):
        self.action = action