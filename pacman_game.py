import pygame
from pacman_spritesheet import PacmanSpritesheet
from counter import Counter
from state import State
from maze import Maze, MAIN_MENU_MAZE

class PacmanGame:
    (WIDTH, HEIGHT) = (256, 216)
    SCREEN = (WIDTH, HEIGHT)

    def __init__(self):
         # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode(self.SCREEN)
        self.clock = pygame.time.Clock()

        # Initialize the game
        self.sheet = PacmanSpritesheet(self)
        self.frames = Counter()
        self.state = State()

        # Main menu setup
        self.main_menu_maze = MAIN_MENU_MAZE

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

            if self.state.is_main_menu():
                self.main_menu()
            elif self.state.is_playing():
                self.tick()
            elif self.state.is_paused():
                self.pause_menu()

            # Update the display
            pygame.display.flip()

            # Limit the frame rate to 60 fps
            self.clock.tick(60)

        # Quit Pygame properly
        pygame.quit()

    def main_menu(self):
        self.sheet.spell("portal", (self.WIDTH * 0.4, self.HEIGHT * 0.1))
        self.sheet.title_pacman.draw((self.WIDTH * 0.5, self.HEIGHT * 0.25))
        self.sheet.spell("by ethan davidson!", (self.WIDTH * 0.25, self.HEIGHT * 0.4))
        self.sheet.spell("enter to start!!!", (self.WIDTH * 0.3, self.HEIGHT * 0.95))
        

if __name__ == "__main__":
    game = PacmanGame()
    game.run()

"""
TODO: Set up text (https://github.com/EthanThatOneKid/386/blob/cb646e6c4d419de9ca97c6f29140de4ca1419515/sessions/2023_25_01/graphics.py#L25)
import pygame

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# create a font object
font = pygame.font.Font(None, 36)

# render the text "Hello, World!"
text_surface = font.render("Hello, World!", True, (255, 255, 255))

# get the rectangle containing the text surface
text_rect = text_surface.get_rect()

# center the rectangle on the screen
text_rect.center = (screen_width // 2, screen_height // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw the text surface onto the screen
    screen.blit(text_surface, text_rect)

    pygame.display.update()
"""