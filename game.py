import pygame
from pygame.locals import *
from gameobjects.button import *
from gameobjects.razas import *
from gameobjects.battle import *
from gameobjects.actions import *

class Game:
    def __init__(self):

        #Creamos los botones
        self.buttons = [Button(690, 590, 100, 40, 'Atacar', self.makeTurn)]

        #Inicializamos la libreria pygame
        pygame.init()

        #Creamos la ventana y le ponemos un titulo
        self.screen = pygame.display.set_mode((800, 640))
        pygame.display.set_caption("Follate esos duendes!!!!")

        #Creamos un reloj para controlar los frames y los tiempos
        clock = pygame.time.Clock()
        clock.tick(60)

        #Creamos los personajes que van a jugar
        self.player = Player("cuetin")
        self.enemy = Goblin("verdini")

        #Cargamos todos los recursos
        self.loadResourses()

        #Comienza la batalla
        self.battle = Battle(self.player, self.enemy)

        #Flag de salida
        self.stopped = False


    def process(self):
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.stopped = True
            for button in self.buttons:
                button.handle_event(event, self)


    def loadResourses(self):
        self.loadPlayerImage(self.player)
        self.loadEnemyImage(self.enemy)


    def render(self):
        self.screen.fill((255, 255, 255))
        self.renderPersonajes()
        self.renderButtons()
        pygame.display.update()


    def loadPlayerImage(self, player):
        player_image = pygame.image.load('Imagenes/player.png')
        player_image = pygame.transform.scale(player_image, (300, 310))
        player.renderer = player_image


    def loadEnemyImage(self, enemy):
        enemy_name = enemy.class_name.lower()
        enemy_image = pygame.image.load('Imagenes/'+enemy_name+'.png')
        enemy_image = pygame.transform.scale(enemy_image, (300, 310))
        enemy.renderer = enemy_image


    def renderPersonajes(self):
        self.player.render(self.screen, (10, 180))
        self.enemy.render(self.screen, (480, 0))


    def renderButtons(self):
        for button in self.buttons:
            button.render(self)


    def makeTurn(self):
        print('atacando')
        turn = Turn()
        turn.command1 = Command({'atacar':1})
        turn.command2 = Command({'atacar':1})

        if turn.can_start():
            self.battle.execute_turn(turn)
            self.battle.print_current_status()
            self.battle.is_finished()



