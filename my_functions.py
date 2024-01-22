import pygame, random

def grid(screen, w, h):
    pygame.draw.line(screen, (0,0,0), (0,w//2), (h,w//2))
    pygame.draw.line(screen, (0,0,0), (h//2, 0), (h//2, w))


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


# --- examples ---
def random_lines(screen, xmin, ymin, xmax, ymax, num):
    for i in range(num):
        x1 = random.randint(xmin, xmax)
        y1 = random.randint(xmin, xmax)
        x2 = random.randint(ymin, ymax)
        y2 = random.randint(ymin, ymax)
        pygame.draw.line(screen, random_color(), (x1, y1), (x2, y2))


def horiz_lines(screen, x1, y1, size):
    gap = size // 5
    x2 = x1 + size
    y2 = y1
    for i in range(5):
        pygame.draw.line(screen, random_color(), (x1, y1), (x2, y2))
        y1 += gap
        y2 = y1