import pygame
import drawing as dw
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
theta = 0

    
            
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

front_3d = [(-1, 1, 3), (1, 1, 3), (1, -1, 3), (-1, -1, 3)]
back_3d  = [(-1, 1, 5), (1, 1, 5), (1, -1, 5), (-1, -1, 5)]

front_3d_2 = [(1, 1, 3), (3, 1, 3), (3, -1, 3), (1, -1, 3)]
back_3d_2  = [(1, 1, 5), (3, 1, 5), (3, -1, 5), (1, -1, 5)]


run = True
while run:

   screen.fill((0, 0, 0))
   front_shifted = [(x, y, z - 4) for (x, y, z) in front_3d]
   back_shifted = [(x, y, z - 4) for (x, y, z) in back_3d]

   front_rotated = [dw.rotateY(*p, theta) for p in front_shifted]
   back_rotated = [dw.rotateY(*p, theta) for p in back_shifted]
   front_rotated = [(x, y, z + 4) for (x, y, z) in front_rotated]
   back_rotated = [(x, y, z + 4) for (x, y, z) in back_rotated]

   front_2d = [dw.project(*p) for p in front_rotated]
   back_2d = [dw.project(*p) for p in back_rotated]

   dw.draw_cube(screen, front_2d, back_2d)
   

   keys = pygame.key.get_pressed() 

   for event in pygame.event.get():
       
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
          run = False
        if keys[pygame.K_UP] or keys[pygame.K_w]:
           dw.focal_length += 10
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
           dw.focal_length -= 10
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
           theta += .05
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] or pygame.MOUSEBUTTONDOWN:
           theta -= .05
        
        
    


   pygame.display.update()

pygame.quit()

