from pygame import Surface

class Entity:
    def __init__(self, game, sprites: list[Surface], delay: int = 1, overflow: int = 0):
        self.game = game
        self.sprites = sprites
        self.delay = delay
        self.overflow = overflow
        self.index = 0
    
    def update(self):
        self.index = (self.index + 1) % (len(self.sprites) + self.overflow)

    def draw(self, pos: tuple[int, int]):
        if self.index < len(self.sprites):
            self.game.screen.blit(self.sprites[self.index], pos)
