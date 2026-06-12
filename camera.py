import pygame
import math
cam_x = 0
cam_y = 0
cam_z = 0
cam_yaw  = 0 # rotation around y-axis in radians
cam_pitch = 0

def world_to_view(x, y, z):
    tx = x - cam_x
    ty = y - cam_y
    tz = z - cam_z

    rx = tx * math.cos(-cam_yaw) + tz*math.sin(-cam_yaw)
    rz = -tx*math.sin(-cam_yaw) +  tz*math.cos(-cam_yaw)
    # pitch: rotate around x-axis
    ry = ty * math.cos(cam_pitch) - rz * math.sin(cam_pitch)
    rz2 = ty * math.sin(cam_pitch) + rz * math.cos(cam_pitch)
    return (rx, ry, rz2)
