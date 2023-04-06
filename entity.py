from pygame import Surface
from spritesheet import PacmanSpritesheet, PacmanSprite


class Entity:
    def __init__(self, sprites: list[PacmanSprite], delay: int = 1, overflow: int = 0):
        self.sprites = sprites
        self.delay = delay
        self.overflow = overflow
        self.index = 0
        self.changes = 0

    def update(self):
        if self.changes == self.delay:
            self.changes = 0
            self.index = (self.index + 1) % (len(self.sprites) + self.overflow)
        else:
            self.changes += 1

    def draw(self, screen: Surface, pos: tuple[int, int]):
        if self.index < len(self.sprites):
            self.sprites[self.index].draw(screen, pos)


class PlayerEntity():
    DELAY = 1
    STATE = {
        "RIGHT": "right_entity",
        "LEFT": "left_entity",
        "UP": "up_entity",
        "DOWN": "down_entity",
        "DYING": "dying_entity"
    }

    def __init__(self):
        self.state = self.STATE["RIGHT"]
        self.sheet = PacmanSpritesheet()
        self.up_entity = Entity(
            [self.sheet.pacman_up_1, self.sheet.pacman_up_2], self.DELAY)
        self.down_entity = Entity(
            [self.sheet.pacman_down_1, self.sheet.pacman_down_2], self.DELAY)
        self.left_entity = Entity(
            [self.sheet.pacman_left_1, self.sheet.pacman_left_2], self.DELAY)
        self.right_entity = Entity(
            [self.sheet.pacman_right_1, self.sheet.pacman_right_2], self.DELAY)
        self.dying_entity = Entity([self.sheet.pacman_dying_1, self.sheet.pacman_dying_2, self.sheet.pacman_dying_3, self.sheet.pacman_dying_4, self.sheet.pacman_dying_5,
                                   self.sheet.pacman_dying_6, self.sheet.pacman_dying_7, self.sheet.pacman_dying_8, self.sheet.pacman_dying_9, self.sheet.pacman_dying_10], self.DELAY)

    def draw(self, screen: Surface, pos: tuple[int, int]):
        if self.state == self.STATE["RIGHT"]:
            self.right_entity.draw(screen, pos)
        elif self.state == self.STATE["LEFT"]:
            self.left_entity.draw(screen, pos)
        elif self.state == self.STATE["UP"]:
            self.up_entity.draw(screen, pos)
        elif self.state == self.STATE["DOWN"]:
            self.down_entity.draw(screen, pos)
        elif self.state == self.STATE["DYING"]:
            self.dying_entity.draw(self.screen, pos)

    def update(self):
        if self.state == self.STATE["RIGHT"]:
            self.right_entity.update()
        elif self.state == self.STATE["LEFT"]:
            self.left_entity.update()
        elif self.state == self.STATE["UP"]:
            self.up_entity.update()
        elif self.state == self.STATE["DOWN"]:
            self.down_entity.update()
        elif self.state == self.STATE["DYING"]:
            self.dying_entity.update()
