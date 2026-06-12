import pygame
import drawing as dw
import camera as cm
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
theta = 0
clock = pygame.time.Clock
player_speed = 5

    
            
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

front_3d = [(-1, 1, 3), (1, 1, 3), (1, -1, 3), (-1, -1, 3)]
back_3d  = [(-1, 1, 5), (1, 1, 5), (1, -1, 5), (-1, -1, 5)]

front_3d_2 = [(1, 1, 3), (3, 1, 3), (3, -1, 3), (1, -1, 3)]
back_3d_2  = [(1, 1, 5), (3, 1, 5), (3, -1, 5), (1, -1, 5)]


run = True
while run:

   screen.fill((30, 30, 30))
  

   front_view = [cm.world_to_view(*p) for p in front_3d]
   back_view = [cm.world_to_view(*p) for p in back_3d]
   front_view_2 = [cm.world_to_view(*p) for p in front_3d_2]
   back_view_2 = [cm.world_to_view(*p) for p in back_3d_2]

   front_2d = [dw.project(*p) for p in front_view]
   back_2d = [dw.project(*p) for p in back_view]
   front_2d_2 = [dw.project(*p) for p in front_view_2]
   back_2d_2 = [dw.project(*p) for p in back_view_2]

   dw.draw_cube(screen, front_2d, back_2d)
   dw.draw_cube(screen, front_2d_2, back_2d_2)
   

   keys = pygame.key.get_pressed() 

   for event in pygame.event.get():
       
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
          run = False
        if keys[pygame.K_UP] or keys[pygame.K_w]:
           cm.cam_z += .1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
           cm.cam_z -= .1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
           cm.cam_x -= .1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
           cm.cam_x += .1
        if event.type == pygame.MOUSEWHEEL:
           if event.y > 0:
              dw.focal_length +=5
           elif event.y < 0:
              dw.focal_length -=5
        

        
    


   pygame.display.flip()
   #clock.tick(60)

pygame.quit()

#  front_shifted = [(x, y, z - 4) for (x, y, z) in front_3d]
#   back_shifted = [(x, y, z - 4) for (x, y, z) in back_3d]

 #  front_rotated = [dw.rotateY(*p, theta) for p in front_shifted]
 #  back_rotated = [dw.rotateY(*p, theta) for p in back_shifted]
 #  front_rotated = [(x, y, z + 4) for (x, y, z) in front_rotated]
 #  back_rotated = [(x, y, z + 4) for (x, y, z) in back_rotated]