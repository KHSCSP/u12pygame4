import pygame, sys
from pygame.locals import QUIT

pygame.init()
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))

import my_functions as f
# grid
f.draw_grid(screen, w, h)

# horizontal lines


# squares from the top left


# squares from the bottom left


# circles from the bottom left


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


