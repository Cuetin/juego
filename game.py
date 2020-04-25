import pygame
from pygame.locals import *
from gameobjects.button import *
from gameobjects.razas import *
from gameobjects.battle import *
from gameobjects.menu import *
from gameobjects.GUI import GUI

class Game:
    def __init__(self):

        #self.buttons = [Button(690, 590, 100, 40, "Atacar", self.makeTurn)]
        self.buttons = []
        self.menu = Menu()
        self.gui = GUI()
        self.bg = None

        #Inicializamos la libreria pygame
        pygame.init()

        #Creamos la ventana y le ponemos un titulo
        self.screen = pygame.display.set_mode((800, 640))
        pygame.display.set_caption("Goblin Slayer by Cuetin")

        #Creamos un reloj para controlar los frames y los tiempos
        clock = pygame.time.Clock()
        clock.tick(60)

        #Creamos los personajes que van a jugar
        self.player = Player("Marina")
        self.enemy = Elf("Legolas")

        #Cargamos todos los recursos
        self.loadResources()

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
            self.menu.handle_event(event, self)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    print(event.pos)


    def loadResources(self):
        self.loadPlayerImage(self.player)
        self.loadEnemyImage(self.enemy)
        self.gui.loadResources()


    def render(self):
        self.screen.fill((255, 255, 255))
        if (self.bg):
            self.screen.blit(self.bg, (0, 0))
        self.renderPersonajes()
        self.renderButtons()
        self.renderTextMessage()
        pygame.display.update()


    def loadPlayerImage(self, player):
        player_image = pygame.image.load('Imagenes/player.png')
        player_image = pygame.transform.scale(player_image, (300, 310))
        player.renderer = player_image
        self.bg = pygame.image.load('Imagenes/back_ground.png')
        self.bg = pygame.transform.scale(self.bg, (800, 490))


    def loadEnemyImage(self, enemy):
        enemy_name = enemy.class_name.lower()
        enemy_image = pygame.image.load('Imagenes/'+enemy_name+'.png')
        enemy_image = pygame.transform.scale(enemy_image, (300, 310))
        enemy.renderer = enemy_image


    def renderPersonajes(self):
        self.player.render(self.screen, (10, 180))
        self.enemy.render(self.screen, (480, 0))


    def renderButtons(self):
        self.menu.render(self)
        self.gui.render(self)
        if self.player.ps > 0 and self.enemy.ps > 0:
            for button in self.buttons:
                button.render(self)

    def renderTextMessage(self):
        if self.menu.state == 0:
            if self.player.ps > 0 and self.enemy.ps == 0:
                self.gui.renderMessage(self, self.player.name+" ha ganado!", 0)
            elif self.enemy.ps > 0 and self.player.ps == 0:
                self.gui.renderMessage(self, self.enemy.name+" ha ganado!", 0)
            elif self.player.ps == 0 and self.enemy.ps == 0:
                self.gui.renderMessage(self, "DOUBLE KO!!!", 0)
            else:
                self.gui.renderMessage(self, "Que quieres hacer "+self.player.name+"?", 0)
        elif self.menu.state == 1:
            if self.player.ps > 0 and self.enemy.ps == 0:
                self.gui.renderMessage(self, self.player.name+" ha ganado!", 0)
            elif self.enemy.ps > 0 and self.player.ps == 0:
                self.gui.renderMessage(self, self.enemy.name+" ha ganado!", 0)
            elif self.player.ps == 0 and self.enemy.ps == 0:
                self.gui.renderMessage(self, "DOUBLE KO!!!", 0)
            else:
                self.gui.renderMessage(self, "Que quieres hacer "+self.player.name+"?", 0)
        elif self.menu.state == 2:
            self.gui.renderMessage(self, "Raza: "+self.enemy.class_name, 0)
            self.gui.renderMessage(self, "HP: "+str(self.enemy.ps), 1)
            self.gui.renderMessage(self, "Estado: "+self.enemy.state, 2)
        elif self.menu.state == 3:
            self.gui.renderMessage(self, '"Intenta vencerme debilucho"', 0)
            self.gui.renderMessage(self, self.player.name+' le saca la lengua', 1)
        elif self.menu.state == 4:
            self.gui.renderMessage(self, 'Que objeto quieres usar?', 0)


    def makeTurn(self, index):
        print('atacando')
        turn = Turn()
        turn.command1 = Command({'atacar':index})
        turn.command2 = Command({'atacar':0})

        if turn.can_start():
            self.battle.execute_turn(turn)
            self.battle.print_current_status()

    def useObjeto(self, index):
        item = self.player.objetos[index].name
        print(item)
        self.gui.renderMessage(self, "Has usado "+item, 1)



