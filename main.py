import pygame
import drawing as dw
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


    
            
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

front_3d = [(-1, 1, 3), (1, 1, 3), (1, -1, 3), (-1, -1, 3)]
back_3d  = [(-1, 1, 5), (1, 1, 5), (1, -1, 5), (-1, -1, 5)]




run = True
while run:

    screen.fill((0, 0, 0))
            
    front_2d = [dw.project(*p) for p in front_3d]
    back_2d = [dw.project(*p) for p in back_3d]
    dw.draw_cube(front_2d, back_2d)

    for event in pygame.event.get():
        keys = pygame.key.get_pressed() 
        if event.type == pygame.QUIT:
          run = False
        if keys[pygame.K_UP] or keys[pygame.K_w]:
           dw.focal_length += 10
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
           dw.focal_length -= 10
    


    pygame.display.update()

pygame.quit()

