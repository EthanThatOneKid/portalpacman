from pygame import Surface
from spritesheet import Spritesheet

class PacmanSpritesheet():
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

         # Title sprites.
        "title_pacman": (424, 172, 192,48),

        # Text sprites.
        "text_200": (339, 136, 8, 8),
        "text_400": (356, 136, 8, 8),
        "text_800": (373, 136, 8, 8),
        "text_1600": (390, 136, 8, 8),
        "text_100": (339, 153, 8, 8),
        "text_300": (356, 153, 8, 8),
        "text_500": (373, 153, 8, 8),
        "text_700": (390, 153, 8, 8),
        "text_1000": (407, 153, 8, 8),

        # Textsheet sprites.
        "text_a": (0, 0, 8, 8),
        "text_b": (8, 0, 8, 8),
        "text_c": (16, 0, 8, 8),
        "text_d": (24, 0, 8, 8),
        "text_e": (32, 0, 8, 8),
        "text_f": (40, 0, 8, 8),
        "text_g": (48, 0, 8, 8),
        "text_h": (56, 0, 8, 8),
        "text_i": (64, 0, 8, 8),
        "text_j": (72, 0, 8, 8),
        "text_k": (80, 0, 8, 8),
        "text_l": (88, 0, 8, 8),
        "text_m": (96, 0, 8, 8),
        "text_n": (104, 0, 8, 8),
        "text_o": (112, 0, 8, 8),
        "text_p": (0, 8, 8, 8),
        "text_q": (8, 8, 8, 8),
        "text_r": (16, 8, 8, 8),
        "text_s": (24, 8, 8, 8),
        "text_t": (32, 8, 8, 8),
        "text_u": (40, 8, 8, 8),
        "text_v": (48, 8, 8, 8),
        "text_w": (56, 8, 8, 8),
        "text_x": (64, 8, 8, 8),
        "text_y": (72, 8, 8, 8),
        "text_z": (80, 8, 8, 8),
        "text_exclamation": (88, 8, 8, 8),
        "text_copyright": (96, 8, 8, 8),
        "text_pts": (104, 8, 16, 8),
        "text_0": (0, 16, 8, 8),
        "text_1": (8, 16, 8, 8),
        "text_2": (16, 16, 8, 8),
        "text_3": (24, 16, 8, 8),
        "text_4": (32, 16, 8, 8),
        "text_5": (40, 16, 8, 8),
        "text_6": (48, 16, 8, 8),
        "text_7": (56, 16, 8, 8),
        "text_8": (64, 16, 8, 8),
        "text_9": (72, 16, 8, 8),
        "text_forward_slash": (80, 16, 8, 8),
        "text_hyphen": (88, 16, 8, 8),
        "text_double_quote": (96, 16, 8, 8),
    }

    def __init__(self, game):
        self.spritesheet = Spritesheet("cgi/spritesheet.png")
        self.textsheet = Spritesheet("cgi/textsheet.png")
        
        self.pacman_right_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_right_1"]))
        self.pacman_right_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_right_2"]))
        self.pacman_left_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_left_1"]))
        self.pacman_left_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_left_2"]))
        self.pacman_up_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_up_1"]))
        self.pacman_up_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_up_2"]))
        self.pacman_down_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_down_1"]))
        self.pacman_down_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_down_2"]))
        self.pacman_dying_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_dying_1"]))
        self.pacman_dying_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_dying_2"]))
        self.pacman_dying_3 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_dying_3"]))
        self.pacman_dying_4 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_dying_4"]))
        self.pacman_dying_5 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_dying_5"]))
        self.pacman_dying_6 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_dying_6"]))
        self.pacman_dying_7 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_dying_7"]))
        self.pacman_dying_8 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_dying_8"]))
        self.pacman_dying_9 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_dying_9"]))
        self.pacman_dying_10 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pacman_dying_10"]))
        
        self.blinky_right_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["blinky_right_1"]))
        self.blinky_right_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["blinky_right_2"]))
        self.blinky_left_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["blinky_left_1"]))
        self.blinky_left_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["blinky_left_2"]))
        self.blinky_up_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["blinky_up_1"]))
        self.blinky_up_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["blinky_up_2"]))
        self.blinky_down_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["blinky_down_1"]))
        self.blinky_down_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["blinky_down_2"]))

        self.pinky_right_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pinky_right_1"]))
        self.pinky_right_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pinky_right_2"]))
        self.pinky_left_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pinky_left_1"]))
        self.pinky_left_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pinky_left_2"]))
        self.pinky_up_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pinky_up_1"]))
        self.pinky_up_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pinky_up_2"]))
        self.pinky_down_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pinky_down_1"]))
        self.pinky_down_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pinky_down_2"]))

        self.inky_right_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["inky_right_1"]))
        self.inky_right_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["inky_right_2"]))
        self.inky_left_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["inky_left_1"]))
        self.inky_left_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["inky_left_2"]))
        self.inky_up_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["inky_up_1"]))
        self.inky_up_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["inky_up_2"]))
        self.inky_down_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["inky_down_1"]))
        self.inky_down_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["inky_down_2"]))

        self.clyde_right_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["clyde_right_1"]))
        self.clyde_right_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["clyde_right_2"]))
        self.clyde_left_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["clyde_left_1"]))
        self.clyde_left_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["clyde_left_2"]))
        self.clyde_up_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["clyde_up_1"]))
        self.clyde_up_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["clyde_up_2"]))
        self.clyde_down_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["clyde_down_1"]))
        self.clyde_down_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["clyde_down_2"]))

        self.ttb_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["ttb_1"]))
        self.ttb_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["ttb_2"]))
        self.ttb_3 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["ttb_3"]))
        self.ttb_4 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["ttb_4"]))

        self.eyes_1 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["eyes_1"]))
        self.eyes_2 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["eyes_2"]))
        self.eyes_3 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["eyes_3"]))
        self.eyes_4 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["eyes_4"]))

        self.cherry = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["cherry"]))
        self.strawberry = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["strawberry"]))
        self.orange = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["orange"]))
        self.apple = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["apple"]))
        self.melon = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["melon"]))
        self.galaxian = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["galaxian"]))
        self.bell = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["bell"]))
        self.key = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["key"]))

        self.pellet = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["pellet"]))
        self.power_pellet = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["power_pellet"]))

        self.maze = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["maze"]))

        self.title_pacman = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["title_pacman"]))

        self.text_200 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["text_200"]))
        self.text_400 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["text_400"]))
        self.text_800 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["text_800"]))
        self.text_1600 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["text_1600"]))
        self.text_100 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["text_100"]))
        self.text_300 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["text_300"]))
        self.text_500 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["text_500"]))
        self.text_700 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["text_700"]))
        self.text_1000 = PacmanSprite(game, self.spritesheet.get_sprite(self.DATA["text_1000"]))
        
        self.text_a = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_a"]))
        self.text_b = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_b"]))
        self.text_c = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_c"]))
        self.text_d = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_d"]))
        self.text_e = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_e"]))
        self.text_f = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_f"]))
        self.text_g = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_g"]))
        self.text_h = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_h"]))
        self.text_i = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_i"]))
        self.text_j = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_j"]))
        self.text_k = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_k"]))
        self.text_l = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_l"]))
        self.text_m = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_m"]))
        self.text_n = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_n"]))
        self.text_o = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_o"]))
        self.text_p = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_p"]))
        self.text_q = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_q"]))
        self.text_r = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_r"]))
        self.text_s = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_s"]))
        self.text_t = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_t"]))
        self.text_u = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_u"]))
        self.text_v = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_v"]))
        self.text_w = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_w"]))
        self.text_x = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_x"]))
        self.text_y = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_y"]))
        self.text_z = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_z"]))
        self.text_exclamation = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_exclamation"]))
        self.text_copyright = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_copyright"]))
        self.text_pts = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_pts"]))
        self.text_0 = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_0"]))
        self.text_1 = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_1"]))
        self.text_2 = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_2"]))
        self.text_3 = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_3"]))
        self.text_4 = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_4"]))
        self.text_5 = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_5"]))
        self.text_6 = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_6"]))
        self.text_7 = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_7"]))
        self.text_8 = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_8"]))
        self.text_9 = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_9"]))
        self.text_forward_slash = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_forward_slash"]))
        self.text_hyphen = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_hyphen"]))
        self.text_double_quote = PacmanSprite(game, self.textsheet.get_sprite(self.DATA["text_double_quote"]))

    def spell(self, text: str, pos: tuple[int, int]):
        x, y = pos
        sep = 8
        for i, char in enumerate(text):
            curr_pos = (x + (i * sep), y)
            if char == " ":
                continue
            elif char == "a":
                self.text_a.draw(curr_pos)
            elif char == "b":
                self.text_b.draw(curr_pos)
            elif char == "c":
                self.text_c.draw(curr_pos)
            elif char == "d":
                self.text_d.draw(curr_pos)
            elif char == "e":
                self.text_e.draw(curr_pos)
            elif char == "f":
                self.text_f.draw(curr_pos)
            elif char == "g":
                self.text_g.draw(curr_pos)
            elif char == "h":
                self.text_h.draw(curr_pos)
            elif char == "i":
                self.text_i.draw(curr_pos)
            elif char == "j":
                self.text_j.draw(curr_pos)
            elif char == "k":
                self.text_k.draw(curr_pos)
            elif char == "l":
                self.text_l.draw(curr_pos)
            elif char == "m":
                self.text_m.draw(curr_pos)
            elif char == "n":
                self.text_n.draw(curr_pos)
            elif char == "o":
                self.text_o.draw(curr_pos)
            elif char == "p":
                self.text_p.draw(curr_pos)
            elif char == "q":
                self.text_q.draw(curr_pos)
            elif char == "r":
                self.text_r.draw(curr_pos)
            elif char == "s":
                self.text_s.draw(curr_pos)
            elif char == "t":
                self.text_t.draw(curr_pos)
            elif char == "u":
                self.text_u.draw(curr_pos)
            elif char == "v":
                self.text_v.draw(curr_pos)
            elif char == "w":
                self.text_w.draw(curr_pos)
            elif char == "x":
                self.text_x.draw(curr_pos)
            elif char == "y":
                self.text_y.draw(curr_pos)
            elif char == "z":
                self.text_z.draw(curr_pos)
            elif char == "!":
                self.text_exclamation.draw(curr_pos)
            elif char == "C":
                self.text_copyright.draw(curr_pos)
            elif char == "0":
                self.text_0.draw(curr_pos)
            elif char == "1":
                self.text_1.draw(curr_pos)
            elif char == "2":
                self.text_2.draw(curr_pos)
            elif char == "3":
                self.text_3.draw(curr_pos)
            elif char == "4":
                self.text_4.draw(curr_pos)
            elif char == "5":
                self.text_5.draw(curr_pos)
            elif char == "6":
                self.text_6.draw(curr_pos)
            elif char == "7":
                self.text_7.draw(curr_pos)
            elif char == "8":
                self.text_8.draw(curr_pos)
            elif char == "9":
                self.text_9.draw(curr_pos)
            elif char == "/":
                self.text_forward_slash.draw(curr_pos)
            elif char == "-":
                self.text_hyphen.draw(curr_pos)
            elif char == '"':
                self.text_double_quote.draw(curr_pos)
            elif char == "P":
                self.text_pts.draw(curr_pos)


class PacmanSprite():
    """A Pacman sprite."""

    def __init__(self, game, sprite: Surface):
        self.game = game
        self.sprite = sprite

    def draw(self, pos: tuple[int, int]):
        """Draw the sprite at the given center position of the sprite."""
        (x, y), (w, h) = pos, self.sprite.get_size()
        self.game.screen.blit(self.sprite, (x - (w // 2), y - (h // 2)))
