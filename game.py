import pygame

from spritesheet import PacmanSpritesheet
from counter import Counter
from scene_manager import SceneManager
from maze import MainMenuMaze


class Game:
    (WIDTH, HEIGHT) = (256, 216)
    SCREEN = (WIDTH, HEIGHT)

    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode(self.SCREEN)
        self.clock = pygame.time.Clock()

        # Initialize the game
        self.sheet = PacmanSpritesheet()
        self.frames = Counter()
        self.main_menu_scene = MainMenuScene(self.screen, self.sheet)
        self.playing_scene = PlayingScene(self.screen, self.sheet)
        self.paused_scene = PausedScene()
        self.scene = SceneManager(self.main_menu_scene, self.playing_scene,
                                  self.paused_scene)

    def run(self):
        # Game loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.state.toggle()

            # Check key presses
            keys = pygame.key.get_pressed()
            if self.scene.is_main_menu():
                if keys[pygame.K_RIGHT]:
                    self.scene.main_menu_scene.maze.move_right()
                if keys[pygame.K_UP]:
                    self.scene.main_menu_scene.maze.move_up()
                if keys[pygame.K_DOWN]:
                    self.scene.main_menu_scene.maze.move_down()
                if keys[pygame.K_LEFT]:
                    self.scene.main_menu_scene.maze.move_left()

            # Update the game
            self.frames.update()
            self.screen.fill((0, 0, 0))
            self.scene.update_current_scene()

            # Draw the game
            self.scene.draw_current_scene()

            # Update the display
            pygame.display.flip()

            # Limit the frame rate
            self.clock.tick(60)

        # Quit Pygame properly
        pygame.quit()


class MainMenuScene():
    def __init__(self, screen: pygame.Surface, sheet: PacmanSpritesheet):
        self.screen = screen
        self.sheet = sheet
        self.maze = MainMenuMaze()

    def update(self):
        pass

    def draw(self):
        self.sheet.spell(self.screen, "portal",
                         (Game.WIDTH * 0.4, Game.HEIGHT * 0.1))
        self.sheet.title_pacman.draw(
            self.screen, (Game.WIDTH * 0.5, Game.HEIGHT * 0.25))
        self.sheet.spell(self.screen, "by ethan davidson C 2023",
                         (Game.WIDTH * 0.14, Game.HEIGHT * 0.4))
        self.maze.draw(self.screen,
                       (Game.WIDTH * 0.3, Game.HEIGHT * 0.5))
        self.sheet.spell(self.screen, "enter to start!!!",
                         (Game.WIDTH * 0.3, Game.HEIGHT * 0.95))


class PlayingScene():
    def __init__(self, screen: pygame.Surface, sheet: PacmanSpritesheet):
        self.screen = screen
        self.sheet = sheet

    def update(self):
        pass

    def draw(self):
        pass


class PausedScene():
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.run()
