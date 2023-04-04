from pygame import Surface
from pacman_game import PacmanGame

class Entity:
    def __init__(self, game: PacmanGame, sprites: list[Surface], delay: int = 1):
        self.game = game
        self.sprites = sprites
        self.delay = delay
        self.index = 0
    
    def update(self):
        frame = self.game.frames.get()
        if frame % self.delay == 0:
            self.index = (self.index + 1) % len(self.sprites)

    def draw(self, canvas: Surface, pos: tuple[int, int]):
        canvas.blit(self.sprites[self.index], pos)
