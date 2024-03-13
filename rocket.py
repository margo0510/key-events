import pygame 
import random
import time 
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,600))

player_x = 200
player_y = 200 

player = pygame.image.load("character.png")
bg_image = pygame.image.load("background.png")

keys = [False, False, False, False]

while player_y < 600:
    screen.blit(bg_image, (0,0))
    screen.blit(player, (player_x, player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            elif event.key == pygame.K_LEFT:
                keys[1] = True
            elif event.key == pygame.K_DOWN:
                keys[2] = True
            elif event.key == pygame.K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_LEFT:
                keys[1] = False
            if event.key == pygame.K_DOWN:
                keys[2] = False
            if event.key == pygame.K_RIGHT:
                keys[3] = False 
      


    time.sleep(0.05)