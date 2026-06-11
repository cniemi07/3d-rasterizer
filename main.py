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
    
    

    front_rotated = [dw.rotateY(theta, *p) for p in front_3d]
    back_rotated = [dw.rotateY(theta, *p) for p in back_3d]

    front_2d = [dw.project(*p) for p in front_rotated]
    back_2d = [dw.project(*p) for p in back_rotated]
    front_2d_2 = [dw.project(*p) for p in front_3d_2]
    back_2d_2 = [dw.project(*p) for p in back_3d_2]
    dw.draw_cube(screen, front_2d, back_2d)
    dw.draw_cube(screen,front_2d_2, back_2d_2)

    keys = pygame.key.get_pressed() 

    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
          run = False
        if keys[pygame.K_UP] or keys[pygame.K_w]:
           dw.focal_length += 10
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
           dw.focal_length -= 10
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
           theta += .05
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
           theta -= .05
        
        
    


    pygame.display.update()

pygame.quit()

