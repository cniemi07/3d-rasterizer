import pygame
import math
import camera as cm
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
focal_length = 350

NEAR_PLANE = 0.5

def clip_and_project(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    if z1 < NEAR_PLANE and z2 < NEAR_PLANE:
        return None  # entire edge is behind the near plane, skip it

    if z1 < NEAR_PLANE:
        t = (NEAR_PLANE - z1) / (z2 - z1)
        p1 = (x1 + t * (x2 - x1), y1 + t * (y2 - y1), NEAR_PLANE)
    elif z2 < NEAR_PLANE:
        t = (NEAR_PLANE - z2) / (z1 - z2)
        p2 = (x2 + t * (x1 - x2), y2 + t * (y1 - y2), NEAR_PLANE)

    return (project(*p1), project(*p2))

   
def rotateY(x, y, z, theta):
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
def draw_clipped_edge(screen, p1, p2):
    result = clip_and_project(p1, p2)
    if result is not None:
        a, b = result
        draw_line(screen, *a, *b)    
def draw_cube(screen, front, back):
    for i in range(len(front)):
        draw_clipped_edge(screen, front[i], back[i])
    for i in range(4):
        draw_clipped_edge(screen, front[i], front[(i+1) % 4])
    for i in range(4):
        draw_clipped_edge(screen, back[i], back[(i+1) % 4])

def project(x, y, z):

    min_z = 0.001  # just large enough to avoid division blowup
    if z > min_z:
        x_screen = (x * focal_length) / z
        y_screen = (y * focal_length) / z
        x_pixel = x_screen + (SCREEN_WIDTH / 2)
        y_pixel = -y_screen + (SCREEN_HEIGHT / 2)
        return (int(x_pixel), int(y_pixel))
    else:
        return None
def render(screen, objects):
   for obj in objects:
        front_view = [cm.world_to_view(*p) for p in obj["front"]]
        back_view = [cm.world_to_view(*p) for p in obj["back"]]
        draw_cube(screen, front_view, back_view)

        