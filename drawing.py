import pygame
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
focal_length = 350
def rotateY(theta, x, y, z):
    new_x = x*math.cos(theta) +  z*math.sin(theta)
    new_z = -x*math.sin(theta) + z*math.cos(theta)
    new_y = y

    return (new_x, new_y, new_z)


def draw_lineH(screen, x0, y0, x1, y1):

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
def draw_lineV(screen, x0, y0, x1, y1):

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
def draw_line(screen, x0, y0, x1, y1):
    if abs(x1-x0) > abs(y1-y0):
        draw_lineH(screen, x0, y0, x1, y1)
    else: draw_lineV(screen, x0, y0, x1, y1)
    
def draw_cube(screen, front, back):
    for i in range(len(front)):
        if front[i] is not None and back[i] is not None:
            draw_line(screen, *front[i], *back[i])
    for i in range(4):
        if front[i] is not None and front[(i+1)%4] is not None:
            draw_line(screen, *front[i], *front[(i+1)%4])
    for i in range(4):
        if back[i] is not None and back[(i+1)%4] is not None:
            draw_line(screen, *back[i], *back[(i+1)%4])
    
def project(x, y, z):

    if z > 0:
        x_screen = (x * focal_length) / z
        y_screen = (y * focal_length) / z
            
        x_pixel = x_screen + (SCREEN_WIDTH / 2)
        y_pixel = -y_screen + (SCREEN_HEIGHT / 2)

        return (int(x_pixel), int(y_pixel))
    else: 
        return None