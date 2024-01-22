import pygame, sys
from pygame.locals import QUIT

pygame.init()
w = 400
h = 400
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))

# we'll define our functions in a different file
# we'll call our functions here
import my_file
# grid
my_file.grid(screen, w, h)

# random lines
my_file.random_lines(screen, 0,0, 200, 200, 100)
# TODO fill another quadrant

# horizontal lines
my_file.horiz_lines(screen, 250, 50, 100)
# TODO fill another quadrant



pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


