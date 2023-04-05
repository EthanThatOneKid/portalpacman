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
        self.playing_scene = PlayingScene()
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

            # Update the game
            self.frames.update()
            self.screen.fill((0, 0, 0))
            self.scene.update_current_scene()

            # Draw the game
            self.scene.draw_current_scene()

            # Update the display
            pygame.display.flip()

            # Limit the frame rate to 60 fps
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
                       (Game.WIDTH * 0.15, Game.HEIGHT * 0.5))
        self.sheet.spell(self.screen, "enter to start!!!",
                         (Game.WIDTH * 0.3, Game.HEIGHT * 0.95))


class PlayingScene():
    def __init__(self):
        pass

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
