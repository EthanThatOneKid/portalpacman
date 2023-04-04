from entity import Entity
from pacman_game import PacmanGame

class PlayerEntity():
    DELAY = 30
    STATE = {
        "RIGHT": "right_entity",
        "LEFT": "left_entity",
        "UP": "up_entity",
        "DOWN": "down_entity",
        "DYING": "dying_entity"
    }

    def __init__(self, game: PacmanGame):
        self.game = game
        self.state = self.STATE.RIGHT
        self.up_entity = Entity(game, [game.sheet.pacman_up_1, game.sheet.pacman_up_2], self.DELAY)
        self.down_entity = Entity(game, [game.sheet.pacman_down_1, game.sheet.pacman_down_2], self.DELAY)
        self.left_entity = Entity(game, [game.sheet.pacman_left_1, game.sheet.pacman_left_2], self.DELAY)
        self.right_entity = Entity(game, [game.sheet.pacman_right_1, game.sheet.pacman_right_2], self.DELAY)
        self.dying_entity = Entity(game, [game.sheet.pacman_dying_1, game.sheet.pacman_dying_2, game.sheet.pacman_dying_3, game.sheet.pacman_dying_4, game.sheet.pacman_dying_5, game.sheet.pacman_dying_6, game.sheet.pacman_dying_7, game.sheet.pacman_dying_8, game.sheet.pacman_dying_9, game.sheet.pacman_dying_10], self.DELAY)

    def draw(self, pos: tuple[int, int]):
        if self.state == self.STATE.RIGHT:
            self.right_entity.update()
            self.right_entity.draw(pos)
        elif self.state == self.STATE.LEFT:
            self.left_entity.update()
            self.left_entity.draw(pos)
        elif self.state == self.STATE.UP:
            self.up_entity.update()
            self.up_entity.draw(pos)
        elif self.state == self.STATE.DOWN:
            self.down_entity.update()
            self.down_entity.draw(pos)
        elif self.state == self.STATE.DYING:
            self.dying_entity.update()
            self.dying_entity.draw(pos)
        