import pygame
from pygame.locals import *

class GUI:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MC', 50)
        self.rect = pygame.Rect(0, 400, 160*4, 144*4)
        self.rendererPlayer = None
        self.rendererEnemy = None

    def loadResources(self):
        player_gui = pygame.image.load('Imagenes/barra_vida.png')
        size = player_gui.get_rect().size
        aspect_ratio = size[0]/size[1]
        player_gui = pygame.transform.scale(player_gui, (400, int(400*(aspect_ratio))))
        self.rendererPlayer = player_gui

        enemy_gui = pygame.image.load("Imagenes/barra_vida.png")
        size = enemy_gui.get_rect().size
        aspect_ratio = size[0]/size[1]
        enemy_gui = pygame.transform.scale(enemy_gui, (400, int(400*(aspect_ratio))))
        self.rendererEnemy = enemy_gui

    def renderPSBar(self, game, bar_size, total_ps, actual_ps, position):
        percentage = float(actual_ps)/total_ps
        color = "green"
        if percentage < 0.5:
            color = "orange"
        if percentage < 0.15:
            color = "red"
        bar = pygame.Rect(position, (bar_size*percentage, 30))
        game.screen.fill(Color(color), bar)

    def renderMessage(self, game, text):
        text_surface = self.font.render(text, False, (0, 0, 0))
        game.screen.blit(text_surface, (50, 500))

    def render(self, game):
        total_player_ps = game.player.total_ps
        total_enemy_ps = game.enemy.total_ps
        self.renderPSBar(game, 310, total_enemy_ps, game.enemy.ps, (60,50))
        self.renderPSBar(game, 310, total_player_ps, game.player.ps, (440,370))

        if self.rendererEnemy:
            text_surface = self.font.render(game.enemy.name, False, (255, 0, 0))
            game.screen.blit(text_surface, (60, 15))

            #text_surface = self.font.render("Lv: "+str(game.enemy.level), False, (0, 0, 0))
            #game.screen.blit(text_surface, (250, 30))

            text_surface = self.font.render(str(int(game.enemy.ps))+"/"+str(int(game.enemy.total_ps)), False, (0, 0, 0))
            game.screen.blit(text_surface, (200, 90))

            game.screen.blit(self.rendererEnemy, (20, -120))

        if self.rendererPlayer:
            text_surface = self.font.render(game.player.name, False, (0, 0, 0))
            game.screen.blit(text_surface, (440, 330))

            #text_surface = self.font.render("Lv: "+str(game.enemy.level), False, (0, 0, 0))
            #game.screen.blit(text_surface, (530, 278))

            text_surface = self.font.render(str(int(game.player.ps))+"/"+str(int(game.player.total_ps)), False, (0, 0, 0))
            game.screen.blit(text_surface, (570, 410))

            game.screen.blit(self.rendererPlayer, (400, 200))

        self.renderMessage(game, "")