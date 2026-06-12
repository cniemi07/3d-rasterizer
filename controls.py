import pygame as pg
import camera as cm
import drawing as dw
import util 
PLAYER_SPEED = .02

def update(keys):
   running = True
   for event in pg.event.get():
    if event.type == pg.QUIT:
        running = False
    if event.type == pg.MOUSEWHEEL:
        if event.y > 0:
            dw.focal_length += 5
        elif event.y < 0:
            dw.focal_length -= 5
        dw.focal_length = util.clamp(dw.focal_length, 150, 500)

   if keys[pg.K_ESCAPE]:
    run = False
   if keys[pg.K_UP] or keys[pg.K_w]:
    cm.cam_z += PLAYER_SPEED
   if keys[pg.K_DOWN] or keys[pg.K_s]:
      cm.cam_z -= PLAYER_SPEED
   if keys[pg.K_LEFT] or keys[pg.K_a]:
      cm.cam_x -= PLAYER_SPEED
   if keys[pg.K_RIGHT] or keys[pg.K_d]:
      cm.cam_x += PLAYER_SPEED
   return running

