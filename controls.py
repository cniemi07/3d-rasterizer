import pygame as pg
import camera as cm
import drawing as dw
import util 
import math
PLAYER_SPEED = .02
YAW_SPEED = .02
MOUSE_SENSITIVITY = 0.002
PITCH_LIMIT = 1.5  # radians, just under 90 degrees



def update(keys):
    running = True

    forward_x = math.sin(cm.cam_yaw)
    forward_z = math.cos(cm.cam_yaw)
    right_x = math.cos(cm.cam_yaw)
    right_z = -math.sin(cm.cam_yaw)

    dx, dy = pg.mouse.get_rel()
    cm.cam_yaw += dx * MOUSE_SENSITIVITY
    cm.cam_pitch -= dy * MOUSE_SENSITIVITY
    cm.cam_pitch = util.clamp(cm.cam_pitch, -PITCH_LIMIT, PITCH_LIMIT)

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
        running = False
    if keys[pg.K_w]:
        cm.cam_x += forward_x * PLAYER_SPEED
        cm.cam_z += forward_z * PLAYER_SPEED
    if keys[pg.K_s]:
        cm.cam_x -= forward_x * PLAYER_SPEED
        cm.cam_z -= forward_z * PLAYER_SPEED
    if keys[pg.K_d]:
        cm.cam_x += right_x * PLAYER_SPEED
        cm.cam_z += right_z * PLAYER_SPEED
    if keys[pg.K_a]:
        cm.cam_x -= right_x * PLAYER_SPEED
        cm.cam_z -= right_z * PLAYER_SPEED

    return running
