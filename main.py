# Simple pacman game in pygame

import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()


# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the fonts
font = pygame.font.SysFont('Comic Sans MS', 30)

# Set up the sounds
pygame.mixer.music.load('pacman_beginning.wav')
pygame.mixer.music.play(-1, 0.0)
eatghost = pygame.mixer.Sound('pacman_eatghost.wav')
eatfruit = pygame.mixer.Sound('pacman_eatfruit.wav')
eatghost.set_volume(0.5)
eatfruit.set_volume(0.5)

# Set up the images
pacman = pygame.image.load('pacman.png')
pacman = pygame.transform.scale(pacman, (30, 30))
pacman = pacman.convert()
pacman.set_colorkey(BLACK)

ghost = pygame.image.load('ghost.png')
ghost = pygame.transform.scale(ghost, (30, 30))
ghost = ghost.convert()
ghost.set_colorkey(BLACK)

fruit = pygame.image.load('fruit.png')
fruit = pygame.transform.scale(fruit, (30, 30))
fruit = fruit.convert()
fruit.set_colorkey(BLACK)

# Set up the game variables
score = 0
lives = 3
level = 1
game_over = False
game_won = False
clock = pygame.time.Clock()
FPS = 30

# Set up the game loop
while True:
      # Set up the game
      if game_over or game_won:
          time.sleep(3)
          game_over = False
          game_won = False
          score = 0
          lives = 3
          level = 1
  
      # Set up the player
      player_x = 250
      player_y = 250
      player_x_change = 0
      player_y_change = 0
  
      # Set up the ghost
      ghost_x = 100
      ghost_y = 100
      ghost_x_change = 5
      ghost_y_change = 5
  
      # Set up the fruit
      fruit_x = random.randint(0, 470)
      fruit_y = random.randint(0, 470)
  
      # Set up the game loop
      while not game_over and not game_won:
  
          # Check for events
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
  
              # Check for key presses
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LEFT:
                      player_x_change = -5
                      player_y_change = 0
                  elif event.key == pygame.K_RIGHT:
                      player_x_change = 5
                      player_y_change = 0
                  elif event.key == pygame.K_UP:
                      player_y_change = -5
                      player_x_change = 0
                  elif event.key == pygame.K_DOWN:
                      player_y_change = 5
                      player_x_change = 0
  
          # Draw the background
          screen.fill(BLACK)
  
          # Draw the score
          score_text = font.render('Score: ' + str(score), False, WHITE)
          screen.blit(score_text, (10, 10))
  
          # Draw the lives
          lives_text = font.render('Lives: ' + str(lives), False, WHITE)
          screen.blit(lives_text, (10, 40))
  
          # Draw the level
          level_text = font.render('Level: ' + str(level), False, WHITE)
          screen.blit(level_text, (10, 70))
  
          # Draw the player
          player_x += player_x_change
          player_y += player_y_change
          screen.blit(pacman, (player_x, player_y))
  
          # Draw the ghost
          ghost_x += ghost_x_change
          ghost_y += ghost_y_change
          screen.blit(ghost, (ghost_x, ghost_y))

          # Draw the fruit
          screen.blit(fruit, (fruit_x, fruit_y))

          # Check for collisions relative to bounding boxes of the screen
          if player_x < 0 or player_x > screen.get_width() - 30 or player_y < 0 or player_y > screen.get_height() - 30 or player_x + 30 > ghost_x and player_x < ghost_x + 30 and player_y + 30 > ghost_y and player_y < ghost_y + 30:
              lives -= 1
              if lives == 0:
                  game_over = True
              else:
                  eatghost.play()
                  player_x = 250
                  player_y = 250
                  ghost_x = 100
                  ghost_y = 100
                  fruit_x = random.randint(0, 470)
                  fruit_y = random.randint(0, 470)

          # Check for collisions relative to bounding boxes of the screen
          if player_x + 30 > fruit_x and player_x < fruit_x + 30 and player_y + 30 > fruit_y and player_y < fruit_y + 30:
              score += 10
              eatfruit.play()
              fruit_x = random.randint(0, 470)
              fruit_y = random.randint(0, 470)

          # Check for collisions relative to bounding boxes of the screen
          if ghost_x < 0 or ghost_x > screen.get_width() - 30 or ghost_y < 0 or ghost_y > screen.get_height() - 30:
              ghost_x_change *= -1
              ghost_y_change *= -1
