import pygame
class Jeton(pygame.sprite.Sprite):

    def __init__(self, col, coord):
        super().__init__()
        self.col = col
        if col == 'jaune':
            self.image = pygame.image.load('jeton jaune.png')
        else:
            self.image = pygame.image.load('jeton rouge.png')
        self.coord = coord
