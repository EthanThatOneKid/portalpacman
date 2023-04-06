import pygame
from entity import PlayerEntity


class Maze:
    def __init__(self, adjacency_map: dict[str, tuple[tuple[int, int], tuple[str | None, str | None, str | None, str | None]]], pellets: list[str], power_pellets: list[str], pacman: str, pacman_speed: int, ghost_speed: float):
        # { "A": ( (0, 0), (up, right, down, left)) }
        self.adjacency_map = adjacency_map
        self.pellets = pellets
        self.power_pellets = power_pellets
        self.ghosts = []
        self.ghost_speed = ghost_speed
        self.pacman_pos = pacman
        self.pacman_offset = (0, 0)
        self.pacman_speed = pacman_speed
        self.pacman_entity = PlayerEntity()
        self.show_track = True

    def shoot_portal(self):
        # TODO: Shoot a portal.
        pass

    def pacman_update_and_draw(self, screen: pygame.Surface, pos: tuple[int, int], scale: int):
        adjacent_up = self.adjacency_map[self.pacman_pos][1][0]
        adjacent_right = self.adjacency_map[self.pacman_pos][1][1]
        adjacent_down = self.adjacency_map[self.pacman_pos][1][2]
        adjacent_left = self.adjacency_map[self.pacman_pos][1][3]

        if self.pacman_entity.state is PlayerEntity.STATE["UP"]:
            if adjacent_up is not None:
                self.pacman_entity.update()
                self.pacman_offset = (
                    self.pacman_offset[0], self.pacman_offset[1] - self.pacman_speed)
                if self.pacman_offset[1] <= -scale:
                    self.pacman_offset = (0, 0)
                    self.pacman_pos = adjacent_up

        if self.pacman_entity.state is PlayerEntity.STATE["RIGHT"]:
            if adjacent_right is not None:
                self.pacman_entity.update()
                self.pacman_offset = (
                    self.pacman_offset[0] + self.pacman_speed, 0)
                if self.pacman_offset[0] >= scale:
                    self.pacman_offset = (0, 0)
                    self.pacman_pos = adjacent_right

        if self.pacman_entity.state is PlayerEntity.STATE["DOWN"]:
            if adjacent_down is not None:
                self.pacman_entity.update()
                self.pacman_offset = (
                    self.pacman_offset[0], self.pacman_offset[1] + self.pacman_speed)
                if self.pacman_offset[1] >= scale:
                    self.pacman_offset = (0, 0)
                    self.pacman_pos = adjacent_down

        if self.pacman_entity.state is PlayerEntity.STATE["LEFT"]:
            if adjacent_left is not None:
                self.pacman_entity.update()
                self.pacman_offset = (
                    self.pacman_offset[0] - self.pacman_speed, self.pacman_offset[1])
                if self.pacman_offset[0] <= -scale:
                    self.pacman_offset = (0, 0)
                    self.pacman_pos = adjacent_left

        self.pacman_entity.draw(
            screen, self.get_pacman_pos(pos, scale))

    def update_ghosts(self):
        # TODO: Update ghosts.
        # for ghost in self.ghosts:
        #     ghost.update()
        pass

    def move_left(self):
        next_pos = self.adjacency_map[self.pacman_pos][1][3]
        if next_pos is not None and self.pacman_offset[1] == 0:
            self.pacman_entity.state = PlayerEntity.STATE["LEFT"]

    def move_right(self):
        next_pos = self.adjacency_map[self.pacman_pos][1][1]
        if next_pos is not None and self.pacman_offset[1] == 0:
            self.pacman_entity.state = PlayerEntity.STATE["RIGHT"]

    def move_up(self):
        next_pos = self.adjacency_map[self.pacman_pos][1][0]
        if next_pos is not None and self.pacman_offset[0] == 0:
            self.pacman_entity.state = PlayerEntity.STATE["UP"]

    def move_down(self):
        next_pos = self.adjacency_map[self.pacman_pos][1][2]
        if next_pos is not None and self.pacman_offset[0] == 0:
            self.pacman_entity.state = PlayerEntity.STATE["DOWN"]

    def update_and_draw(self, screen: pygame.Surface, pos: tuple[int, int], scale: int = 16):
        if self.show_track:
            self.draw_track(screen, pos, scale)

        # TODO: Draw pellets.
        # for pellet in self.pellets:
        #     self.game.screen.blit(self.game.sheet.pellet, self.coords[pellet])

        # TODO: Draw power pellets.
        # for power_pellet in self.power_pellets:
        #     self.game.screen.blit(self.game.sheet.power_pellet, self.coords[power_pellet])

        # TODO Draw ghosts.
        # for ghost in self.ghosts:
        #     ghost.draw(self.coords[ghost.pos])

        self.pacman_update_and_draw(screen, pos, scale)

    def get_pacman_pos(self, pos: tuple[int, int], scale: int = 1):
        pacman_pos_x = (
            self.adjacency_map[self.pacman_pos][0][0] * scale + self.pacman_offset[0]) + pos[0]
        pacman_pos_y = (
            self.adjacency_map[self.pacman_pos][0][1] * scale + self.pacman_offset[1]) + pos[1]
        return (pacman_pos_x, pacman_pos_y)

    def draw_track(self, screen: pygame.Surface, pos: tuple[int, int], scale: int = 1):
        for (_, ((x1, y1), (up_name, right_name, down_name, left_name))) in self.adjacency_map.items():
            for key in (up_name, right_name, down_name, left_name):
                if key is None:
                    continue

                ((x2, y2), _) = self.adjacency_map[key]
                pygame.draw.line(screen, (255, 255, 255), (x1 * scale +
                                 pos[0], y1 * scale + pos[1]), (x2 * scale + pos[0], y2 * scale + pos[1]), 1)


class MainMenuMaze(Maze):
    def __init__(self):
        super().__init__(adjacency_map={
            "top_left": ((0, 0), (None, "top_01", "left_01", None)),
            "top_01": ((1, 0), (None, "top_02", None, "top_left")),
            "top_02": ((2, 0), (None, "top_03", None, "top_01")),
            "top_03": ((3, 0), (None, "top_04", None, "top_02")),
            "top_04": ((4, 0), (None, "top_05", None, "top_03")),
            "top_05": ((5, 0), (None, "top_06", None, "top_04")),
            "top_06": ((6, 0), (None, "top_right", None, "top_05")),
            "top_right": ((7, 0), (None, None, "right_01", "top_06")),

            "right_01": ((7, 1), ("top_right", None, "right_02", None)),
            "right_02": ((7, 2), ("right_01", None, "right_03", None)),
            "right_03": ((7, 3), ("right_02", None, "bottom_right", None)),

            "bottom_right": ((7, 4), ("right_03", None, None, "bottom_06")),
            "bottom_06": ((6, 4), (None, "bottom_right", None, "bottom_05")),
            "bottom_05": ((5, 4), (None, "bottom_06", None, "bottom_04")),
            "bottom_04": ((4, 4), (None, "bottom_05", None, "bottom_03")),
            "bottom_03": ((3, 4), (None, "bottom_04", None, "bottom_02")),
            "bottom_02": ((2, 4), (None, "bottom_03", None, "bottom_01")),
            "bottom_01": ((1, 4), (None, "bottom_02", None, "bottom_left")),
            "bottom_left": ((0, 4), ("left_03", "bottom_01", None, None)),

            "left_01": ((0, 1), ("top_left", None, "left_02", None)),
            "left_02": ((0, 2), ("left_01", None, "left_03", None)),
            "left_03": ((0, 3), ("left_02", None, "bottom_left", None)),
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


class ClassicMaze(Maze):
    def __init__(self):
        super().__init__(adjacency_map={
            "A1": ((0, 0), (None, "A2", "B1", None)),
            "A2": ((1, 0), (None, "A3", None, "A1")),
            "A3": ((2, 0), (None, "A4", None, "A2")),
            "A4": ((3, 0), (None, "A5", None, "A3")),
            "A5": ((4, 0), (None, "A6", None, "A4")),
            "A6": ((5, 0), (None, "A7", None, "A5")),
            "A7": ((6, 0), (None, "A8", None, "A6")),
            "A8": ((7, 0), (None, "A9", None, "A7")),
            "A9": ((8, 0), (None, None, "B9", "A8")),

            "A11": ((10, 0), (None, "A12", "B11", None)),
            # TODO: Complete classic Pac-Man maze!
            # "A12": (())
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
            pacman="top_left",  # TODO: Pick middle center of classic maze
            pacman_speed=1,
            ghost_speed=1,
        )
