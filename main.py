import pygame as pg
import drawing as dw
import camera as cm
import util
import controls as ctl
pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
theta = 0
clock = pg.time.Clock()


screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pg.mouse.set_visible(False)
pg.event.set_grab(True)
pg.mouse.get_rel() 

front_3d = [(-1, 1, 3), (1, 1, 3), (1, -1, 3), (-1, -1, 3)]
back_3d  = [(-1, 1, 5), (1, 1, 5), (1, -1, 5), (-1, -1, 5)]

front_3d_2 = [(1, 1, 3), (3, 1, 3), (3, -1, 3), (1, -1, 3)]
back_3d_2  = [(1, 1, 5), (3, 1, 5), (3, -1, 5), (1, -1, 5)]
cubes = [
    {"front": front_3d, "back": back_3d},
    {"front": front_3d_2, "back": back_3d_2},
]

run = True
while run:

   screen.fill((30, 30, 30))
   keys = pg.key.get_pressed()
   run =  ctl.update(keys)
   dw.render(screen, cubes) 
   pg.display.flip()
   clock.tick(60)

pg.quit()

