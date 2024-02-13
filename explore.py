import pygame, sys
from pygame.locals import QUIT

pygame.init()
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))

# we'll define our functions in a different file
# we'll call our functions here
import my_functions as f
# grid
f.draw_grid(screen, w, h)

# random lines
f.random_lines(screen, 0,0, 400, 300, 100)
# TODO fill another quadrant

# horizontal lines
f.horiz_lines(screen, 450, 0, 200)
# TODO fill another quadrant



pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


