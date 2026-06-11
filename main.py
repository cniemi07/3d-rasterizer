import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:

    for i in range(100):
        pygame.Surface.set_at(screen, (300 + i, 250), (255, 0, 0))

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False

    pygame.display.update()

pygame.quit()