import pygame
from pygame.locals import *
from gameobjects import actions
from gameobjects.razas import *

#for mier in GameObject.objects:
#    print(mier, ":", GameObject.objects[mier])
player = Player("cuetin")
enemy = Goblin("verdini")
"""
print(actions.ayuda("general"))

print(actions.register.__doc__)

while True:
    actions.get_input()
"""
def render(screen):
    screen.fill((255, 255, 255))
    renderPersonajes(screen, player, enemy)
    pygame.display.update()

def update():
    pass

def loadPlayerImage(player):
    player_image = pygame.image.load('Imagenes/player.png')
    player_image = pygame.transform.scale(player_image, (400, 400))
    player.renderer = player_image

def loadEnemyImage(enemy):
    enemy_name = enemy.class_name.lower()
    enemy_image = pygame.image.load('Imagenes/'+enemy_name+'.png')
    enemy_image = pygame.transform.scale(enemy_image, (400, 400))
    enemy.renderer = enemy_image

def renderPersonajes(screen, player, enemy):
    player.render(screen, (10, 200))
    enemy.render(screen, (440, -40))

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 640))
    pygame.display.set_caption("Follate esos duendes!!!!")

    loadPlayerImage(player)
    loadEnemyImage(enemy)

    clock = pygame.time.Clock()
    stopped = False
    clock.tick(60)
    while not stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopped = True

        update()
        render(screen)

if __name__ == "__main__":
    main()
