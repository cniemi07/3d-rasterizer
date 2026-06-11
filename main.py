import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_lineH(x0, y0, x1, y1):

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    dir = -1 if dy < 0 else 1
    dy *= dir

    if dx != 0:

        y = y0
        p = 2*dy - dx  # initial decision value

        for i in range(dx + 1):
            pygame.Surface.set_at(screen, (x0 + i, y), (255, 0, 0))

            if p >= 0:
                y += dir
                p = p + 2*dy - 2*dx
            else:
                p = p + 2*dy
def draw_lineV(x0, y0, x1, y1):

    if y0 > y1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    dir = -1 if dx < 0 else 1
    dx *= dir

    if dy != 0:

        x = x0
        p = 2*dx - dy  # initial decision value

        for i in range(dy + 1):
            pygame.Surface.set_at(screen, (x, y0 + i), (255, 0, 0))

            if p >= 0:
                x += dir
                p = p + 2*dx - 2*dy
            else:
                p = p + 2*dx    
def draw_line(x0, y0, x1, y1):
    if abs(x1-x0) > abs(y1-y0):
        draw_lineH(x0, y0, x1, y1)
    else: draw_lineV(x0, y0, x1, y1)
def draw_cube(front, back):
    for i in range(len(front)):
        draw_line(*front[i], *back[i])
    for i in range(len(front)):
        draw_line(*front[i], *front[(i + 1) % 4])
    for i in range(len(front)):
        draw_line(*back[i], *back[(i + 1) % 4])
    
    
            
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
front = [(300, 200), (500, 200), (500, 400), (300, 400)]
back =  [(380, 120), (580, 120), (580, 320), (380, 320)]
draw_cube(front, back)

run = True
while run:

 
            

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False

    pygame.display.update()

pygame.quit()

