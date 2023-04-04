from pygame import Surface
from spritesheet import Spritesheet

class PacmanSpritesheet(Spritesheet):
    DATA = {
        # Pacman player sprites and animations.
        "pacman_right_1": (339, 0, 16, 16),
        "pacman_right_2": (356, 0, 16, 16),
        "pacman_left_1": (339, 17, 16, 16),
        "pacman_left_2": (356, 17, 16, 16),
        "pacman_up_1": (339, 34, 16, 16),
        "pacman_up_2": (356, 34, 16, 16),
        "pacman_down_1": (339, 51, 16, 16),
        "pacman_down_2": (356, 51, 16, 16),
        "pacman_dying_1": (373, 0, 16, 16),
        "pacman_dying_2": (390, 0, 16, 16),
        "pacman_dying_3": (407, 0, 16, 16),
        "pacman_dying_4": (424, 0, 16, 16),
        "pacman_dying_5": (441, 0, 16, 16),
        "pacman_dying_6": (458, 0, 16, 16),
        "pacman_dying_7": (475, 0, 16, 16),
        "pacman_dying_8": (492, 0, 16, 16),
        "pacman_dying_9": (509, 0, 16, 16),
        "pacman_dying_10": (526, 0, 16, 16),

        # Blinky enemy (red ghost) sprites and animations.
        "blinky_right_1": (339, 68, 16, 16),
        "blinky_right_2": (356, 68, 16, 16),
        "blinky_left_1": (339, 85, 16, 16),
        "blinky_left_2": (356, 85, 16, 16),
        "blinky_up_1": (339, 102, 16, 16),
        "blinky_up_2": (356, 102, 16, 16),
        "blinky_down_1": (339, 119, 16, 16),
        "blinky_down_2": (356, 119, 16, 16),
        
        # Pinky enemy (pink ghost) sprites and animations.
        "pinky_right_1": (339, 85, 16, 16),
        "pinky_right_2": (356, 85, 16, 16),
        "pinky_left_1": (339, 85, 16, 16),
        "pinky_left_2": (356, 85, 16, 16),
        "pinky_up_1": (339, 85, 16, 16),
        "pinky_up_2": (356, 85, 16, 16),
        "pinky_down_1": (339, 85, 16, 16),
        "pinky_down_2": (356, 85, 16, 16),

        # Inky enemy (cyan ghost) sprites and animations.
        "inky_right_1": (339, 102, 16, 16),
        "inky_right_2": (356, 102, 16, 16),
        "inky_left_1": (339, 102, 16, 16),
        "inky_left_2": (356, 102, 16, 16),
        "inky_up_1": (339, 102, 16, 16),
        "inky_up_2": (356, 102, 16, 16),
        "inky_down_1": (339, 102, 16, 16),
        "inky_down_2": (356, 102, 16, 16),

        # Clyde enemy (orange ghost) sprites and animations.
        "clyde_right_1": (339, 119, 16, 16),
        "clyde_right_2": (356, 119, 16, 16),
        "clyde_left_1": (339, 119, 16, 16),
        "clyde_left_2": (356, 119, 16, 16),
        "clyde_up_1": (339, 119, 16, 16),
        "clyde_up_2": (356, 119, 16, 16),
        "clyde_down_1": (339, 119, 16, 16),
        "clyde_down_2": (356, 119, 16, 16),

        # Turn-to-Blue enemy sprites and animations.
        "ttb_1": (475, 68, 16, 16),
        "ttb_2": (492, 68, 16, 16),
        "ttb_3": (509, 68, 16, 16),
        "ttb_4": (526, 68, 16, 16),

        # Eyes enemy sprites and animations.
        "eyes_1": (475, 85, 16, 16),
        "eyes_2": (492, 85, 16, 16),
        "eyes_3": (509, 85, 16, 16),
        "eyes_4": (526, 85, 16, 16),

        # Food sprites.
        "cherry": (373, 51, 16, 16),
        "strawberry": (390, 51, 16, 16),
        "orange": (407, 51, 16, 16),
        "apple": (424, 51, 16, 16),
        "melon": (441, 51, 16, 16),
        "galaxian": (458, 51, 16, 16),
        "bell": (475, 51, 16, 16),
        "key": (492, 51, 16, 16),

        # Pellet sprites.
        "pellet": (535, 44, 8, 8),
        "power_pellet": (544, 44, 8, 8),

        # Maze sprites.
        "maze": (170, 0, 168, 216),

        # Text sprites.
        "text_200": (339, 136, 16, 16),
        "text_400": (356, 136, 16, 16),
        "text_800": (373, 136, 16, 16),
        "text_1600": (390, 136, 16, 16),
        "text_100": (339, 153, 16, 16),
        "text_300": (356, 153, 16, 16),
        "text_500": (373, 153, 16, 16),
        "text_700": (390, 153, 16, 16),
        "text_1000": (407, 153, 16, 16),

        # Title sprites.
        "title_pacman": (424, 172, 192,48),
    }

    def __init__(self, game):
        super().__init__("cgi/spritesheet.png")
        
        self.pacman_right_1 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_right_1"]))
        self.pacman_right_2 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_right_2"]))
        self.pacman_left_1 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_left_1"]))
        self.pacman_left_2 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_left_2"]))
        self.pacman_up_1 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_up_1"]))
        self.pacman_up_2 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_up_2"]))
        self.pacman_down_1 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_down_1"]))
        self.pacman_down_2 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_down_2"]))
        self.pacman_dying_1 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_dying_1"]))
        self.pacman_dying_2 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_dying_2"]))
        self.pacman_dying_3 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_dying_3"]))
        self.pacman_dying_4 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_dying_4"]))
        self.pacman_dying_5 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_dying_5"]))
        self.pacman_dying_6 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_dying_6"]))
        self.pacman_dying_7 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_dying_7"]))
        self.pacman_dying_8 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_dying_8"]))
        self.pacman_dying_9 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_dying_9"]))
        self.pacman_dying_10 = PacmanSprite(game, self.get_sprite(self.DATA["pacman_dying_10"]))
        
        self.blinky_right_1 = PacmanSprite(game, self.get_sprite(self.DATA["blinky_right_1"]))
        self.blinky_right_2 = PacmanSprite(game, self.get_sprite(self.DATA["blinky_right_2"]))
        self.blinky_left_1 = PacmanSprite(game, self.get_sprite(self.DATA["blinky_left_1"]))
        self.blinky_left_2 = PacmanSprite(game, self.get_sprite(self.DATA["blinky_left_2"]))
        self.blinky_up_1 = PacmanSprite(game, self.get_sprite(self.DATA["blinky_up_1"]))
        self.blinky_up_2 = PacmanSprite(game, self.get_sprite(self.DATA["blinky_up_2"]))
        self.blinky_down_1 = PacmanSprite(game, self.get_sprite(self.DATA["blinky_down_1"]))
        self.blinky_down_2 = PacmanSprite(game, self.get_sprite(self.DATA["blinky_down_2"]))

        self.pinky_right_1 = PacmanSprite(game, self.get_sprite(self.DATA["pinky_right_1"]))
        self.pinky_right_2 = PacmanSprite(game, self.get_sprite(self.DATA["pinky_right_2"]))
        self.pinky_left_1 = PacmanSprite(game, self.get_sprite(self.DATA["pinky_left_1"]))
        self.pinky_left_2 = PacmanSprite(game, self.get_sprite(self.DATA["pinky_left_2"]))
        self.pinky_up_1 = PacmanSprite(game, self.get_sprite(self.DATA["pinky_up_1"]))
        self.pinky_up_2 = PacmanSprite(game, self.get_sprite(self.DATA["pinky_up_2"]))
        self.pinky_down_1 = PacmanSprite(game, self.get_sprite(self.DATA["pinky_down_1"]))
        self.pinky_down_2 = PacmanSprite(game, self.get_sprite(self.DATA["pinky_down_2"]))

        self.inky_right_1 = PacmanSprite(game, self.get_sprite(self.DATA["inky_right_1"]))
        self.inky_right_2 = PacmanSprite(game, self.get_sprite(self.DATA["inky_right_2"]))
        self.inky_left_1 = PacmanSprite(game, self.get_sprite(self.DATA["inky_left_1"]))
        self.inky_left_2 = PacmanSprite(game, self.get_sprite(self.DATA["inky_left_2"]))
        self.inky_up_1 = PacmanSprite(game, self.get_sprite(self.DATA["inky_up_1"]))
        self.inky_up_2 = PacmanSprite(game, self.get_sprite(self.DATA["inky_up_2"]))
        self.inky_down_1 = PacmanSprite(game, self.get_sprite(self.DATA["inky_down_1"]))
        self.inky_down_2 = PacmanSprite(game, self.get_sprite(self.DATA["inky_down_2"]))

        self.clyde_right_1 = PacmanSprite(game, self.get_sprite(self.DATA["clyde_right_1"]))
        self.clyde_right_2 = PacmanSprite(game, self.get_sprite(self.DATA["clyde_right_2"]))
        self.clyde_left_1 = PacmanSprite(game, self.get_sprite(self.DATA["clyde_left_1"]))
        self.clyde_left_2 = PacmanSprite(game, self.get_sprite(self.DATA["clyde_left_2"]))
        self.clyde_up_1 = PacmanSprite(game, self.get_sprite(self.DATA["clyde_up_1"]))
        self.clyde_up_2 = PacmanSprite(game, self.get_sprite(self.DATA["clyde_up_2"]))
        self.clyde_down_1 = PacmanSprite(game, self.get_sprite(self.DATA["clyde_down_1"]))
        self.clyde_down_2 = PacmanSprite(game, self.get_sprite(self.DATA["clyde_down_2"]))

        self.ttb_1 = PacmanSprite(game, self.get_sprite(self.DATA["ttb_1"]))
        self.ttb_2 = PacmanSprite(game, self.get_sprite(self.DATA["ttb_2"]))
        self.ttb_3 = PacmanSprite(game, self.get_sprite(self.DATA["ttb_3"]))
        self.ttb_4 = PacmanSprite(game, self.get_sprite(self.DATA["ttb_4"]))

        self.eyes_1 = PacmanSprite(game, self.get_sprite(self.DATA["eyes_1"]))
        self.eyes_2 = PacmanSprite(game, self.get_sprite(self.DATA["eyes_2"]))
        self.eyes_3 = PacmanSprite(game, self.get_sprite(self.DATA["eyes_3"]))
        self.eyes_4 = PacmanSprite(game, self.get_sprite(self.DATA["eyes_4"]))

        self.cherry = PacmanSprite(game, self.get_sprite(self.DATA["cherry"]))
        self.strawberry = PacmanSprite(game, self.get_sprite(self.DATA["strawberry"]))
        self.orange = PacmanSprite(game, self.get_sprite(self.DATA["orange"]))
        self.apple = PacmanSprite(game, self.get_sprite(self.DATA["apple"]))
        self.melon = PacmanSprite(game, self.get_sprite(self.DATA["melon"]))
        self.galaxian = PacmanSprite(game, self.get_sprite(self.DATA["galaxian"]))
        self.bell = PacmanSprite(game, self.get_sprite(self.DATA["bell"]))
        self.key = PacmanSprite(game, self.get_sprite(self.DATA["key"]))

        self.pellet = PacmanSprite(game, self.get_sprite(self.DATA["pellet"]))
        self.power_pellet = PacmanSprite(game, self.get_sprite(self.DATA["power_pellet"]))

        self.maze = PacmanSprite(game, self.get_sprite(self.DATA["maze"]))

        self.text_200 = PacmanSprite(game, self.get_sprite(self.DATA["text_200"]))
        self.text_400 = PacmanSprite(game, self.get_sprite(self.DATA["text_400"]))
        self.text_800 = PacmanSprite(game, self.get_sprite(self.DATA["text_800"]))
        self.text_1600 = PacmanSprite(game, self.get_sprite(self.DATA["text_1600"]))
        self.text_100 = PacmanSprite(game, self.get_sprite(self.DATA["text_100"]))
        self.text_300 = PacmanSprite(game, self.get_sprite(self.DATA["text_300"]))
        self.text_500 = PacmanSprite(game, self.get_sprite(self.DATA["text_500"]))
        self.text_700 = PacmanSprite(game, self.get_sprite(self.DATA["text_700"]))
        self.text_1000 = PacmanSprite(game, self.get_sprite(self.DATA["text_1000"]))

        self.title_pacman = PacmanSprite(game, self.get_sprite(self.DATA["title_pacman"]))


class PacmanSprite():
    """A Pacman sprite."""

    def __init__(self, game, sprite: Surface):
        self.game = game
        self.sprite = sprite

    def draw(self, pos: tuple[int, int]):
        """Draw the sprite at the given center position of the sprite."""
        (x, y), (w, h) = pos, self.sprite.get_size()
        self.game.screen.blit(self.sprite, (x - (w // 2), y - (h // 2)))
