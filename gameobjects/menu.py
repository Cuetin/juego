import pygame
from functools import partial
from .button import Button
import os

class Menu:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(os.path.join("font", "Cup and Talon.ttf"), 45)
        self.rect = pygame.Rect(0, 400, 160*4, 144*4)
        self.state = 0
        self.mainButtons = [
            Button(690, 590, 100, 40, "Atacar", partial(self.change_menu_state, newState=1)),
            Button(580, 590, 100, 40, "Info", partial(self.change_menu_state, newState=2)),
            Button(580, 540, 100, 40, "Burla", partial(self.change_menu_state, newState=3)),
            Button(690, 540, 100, 40, "Objetos", partial(self.change_menu_state, newState=4))
        ]
        self.attackButtons = []

    def handle_event(self, event, game):
        for button in self.mainButtons:
            button.handle_event(event, game)
        if self.state == 1:
            if len(self.attackButtons) == 0:
                for idx, attack in enumerate(game.player.attacks):
                    functionTurn = partial(game.makeTurn, index=idx)
                    self.attackButtons.append(
                        Button(idx*160, 590, 150, 40, attack.name, functionTurn)
                    )
            for button in self.attackButtons:
                button.handle_event(event, game)

    def change_menu_state(self, newState):
        if (self. state == 1 and newState != 1):
            self.state = 0
            for button in self.mainButtons:
                button.enable()
        else:
            self.state = newState
            for button in self.mainButtons:
                button.disable()

    def render(self, game):
        for button in self.mainButtons:
            button.render(game)
        if self.state == 1:
            for button in self.attackButtons:
                button.render(game)

