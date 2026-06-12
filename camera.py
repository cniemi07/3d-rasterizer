import pygame

cam_x = 0
cam_y = 0
cam_z = 0

def world_to_view(x, y, z):
    x -= cam_x
    y -= cam_y
    z -= cam_z
    return (x, y, z)
