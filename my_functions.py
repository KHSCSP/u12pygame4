import pygame, random

def draw_grid(screen, w, h):
    pygame.draw.line(screen, (0,0,0), (w//2, 0), (w//2, h))
    pygame.draw.line(screen, (0,0,0), (0,h//2), (w, h//2))


def mycolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


# --- examples ---
def random_lines(screen, xmin, ymin, xmax, ymax, num):
    for i in range(num):
        x1 = random.randint(xmin, xmax)
        y1 = random.randint(ymin, ymax)
        x2 = random.randint(xmin, xmax)
        y2 = random.randint(ymin, ymax)
        pygame.draw.line(screen, mycolor(), (x1, y1), (x2, y2))


def horiz_lines(screen, x, y, size):
    pass


def squares_tl(screen, x, y, size):
    # only 'size' changes
    pass

def squares_bl(screen, x, y, size):
    # size changes, y changes
    pass

def circles_bl(screen, x, y, size):
    # size changes, x&y change
    pass
