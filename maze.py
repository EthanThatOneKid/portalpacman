import pygame
from player_entity import PlayerEntity

class Maze:
    def __init__(self, adjacency_map: dict[str, tuple[tuple[int, int], list[str]]], pellets: list[str], power_pellets: list[str], pacman: str, pacman_speed: float, ghost_speed: float):
        self.adjacency_map = adjacency_map
        self.pellets = pellets
        self.power_pellets = power_pellets
        self.ghosts = []
        self.pacman_speed = pacman_speed
        self.ghost_speed = ghost_speed
        self.pacman_pos = self.coords[pacman][0]
        self.pacman_direction = PlayerEntity.STATE.RIGHT
        self.show_track = True

    def update_pacman(self):
        # self.pacman_pos  = 
        pass
    
    def update_ghosts(self):
        # for ghost in self.ghosts:
        #     ghost.update()
        pass
    
    def move_left(self):
        self.pacman_direction = PlayerEntity.STATE.LEFT
    
    def move_right(self):
        self.pacman_direction = PlayerEntity.STATE.RIGHT
    
    def move_up(self):
        self.pacman_direction = PlayerEntity.STATE.UP
    
    def move_down(self):
        self.pacman_direction = PlayerEntity.STATE.DOWN
    
    def draw(self, screen: pygame.Surface, pos: tuple[int, int], scale: float = 1.0):
        # if self.show_background:
        #     screen.blit(self.game.sheet.maze, pos)
        # else:
        #     # Blit black square the size of the maze.
        #     surface = pygame.Surface((self.game.sheet.maze.get_width(), self.game.sheet.maze.get_height()))
        #     screen.blit(surface, pos)
        
        if self.show_track:
            for (a, b) in self.adjacency_map.items():
                for c in b:
                    x1, y1 = self.coords[a][0] + pos[0], self.coords[a][1] + pos[1]
                    x2, y2 = self.coords[c][0] + pos[0], self.coords[c][1] + pos[1]
                    pygame.draw.line(self.game.screen, (255, 0, 0), (x1, y1), (x2, y2), 1)

        # for pellet in self.pellets:
        #     self.game.screen.blit(self.game.sheet.pellet, self.coords[pellet])
        
        # for power_pellet in self.power_pellets:
        #     self.game.screen.blit(self.game.sheet.power_pellet, self.coords[power_pellet])
        
        # for ghost in self.ghosts:
        #     ghost.draw(self.coords[ghost.pos])
        
        # self.pacman.draw(self.coords[self.pacman.pos])

MAIN_MENU_MAZE = Maze(
    adjacency_map={
    "top_left": ((0, 0), ["top_01", "left_01"]),
    "top_01": ((1, 0), ["top_02", "top_left"]),
    "top_02": ((2, 0), ["top_03", "top_01"]),
    "top_03": ((3, 0), ["top_04", "top_02"]),
    "top_04": ((4, 0), ["top_05", "top_03"]),
    "top_05": ((5, 0), ["top_06", "top_04"]),
    "top_06": ((6, 0), ["top_right", "top_05"]),
    "top_right": ((7, 0), ["top_06", "right_01"]),
    "right_01": ((7, 1), ["right_02", "top_right"]),
    "right_02": ((7, 2), ["right_03", "right_01"]),
    "right_03": ((7, 3), ["right_04", "right_02"]),
    "right_04": ((7, 4), ["right_05", "right_03"]),
    "right_05": ((7, 5), ["right_06", "right_04"]),
    "right_06": ((7, 6), ["bottom_right", "right_05"]),
    "bottom_right": ((7, 7), ["right_06", "bottom_06"]),
    "bottom_01": ((6, 7), ["bottom_02", "bottom_right"]),
    "bottom_02": ((5, 7), ["bottom_03", "bottom_01"]),
    "bottom_03": ((4, 7), ["bottom_04", "bottom_02"]),
    "bottom_04": ((3, 7), ["bottom_05", "bottom_03"]),
    "bottom_05": ((2, 7), ["bottom_06", "bottom_04"]),
    "bottom_06": ((1, 7), ["bottom_left", "bottom_05"]),
    "bottom_left": ((0, 7), ["bottom_06", "left_01"]),
    "left_01": ((0, 6), ["left_02", "bottom_left"]),
    "left_02": ((0, 5), ["left_03", "left_01"]),
    "left_03": ((0, 4), ["left_04", "left_02"]),
    "left_04": ((0, 3), ["left_05", "left_03"]),
    "left_05": ((0, 2), ["left_06", "left_04"]),
    "left_06": ((0, 1), ["top_left", "left_05"]),
    },
    pellets=[
        # "top_01", "top_02", "top_03", "top_04", "top_05", "top_06",
        # "right_01", "right_02", "right_03", "right_04", "right_05", "right_06",
        # "bottom_01", "bottom_02", "bottom_03", "bottom_04", "bottom_05", "bottom_06",
        # "left_01", "left_02", "left_03", "left_04", "left_05", "left_06",
    ],
    power_pellets=[
        # "top_left", "top_right", "bottom_right", "bottom_left",
    ],
    pacman="top_left",
    pacman_speed=1,
    ghost_speed=1,
)