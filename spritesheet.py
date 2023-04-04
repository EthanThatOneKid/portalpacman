import pygame

class Spritesheet:
    """
    This class is used to load up a spritesheet and parse it into individual sprites.

    Source code adapted from:
    https://github.com/ChristianD37/YoutubeTutorials/blob/32f1a8a8813bacf2bd2dd7819205724a77c29b02/spritesheet/spritesheet.py
    """
    def __init__(self, filename):
        self.filename = filename
        self.sheet = pygame.image.load(filename).convert()

    def get_sprite(self, rect: tuple[int, int, int, int]):
        x, y, w, h = rect
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sheet, (0, 0), (x, y, w, h))
        return sprite
