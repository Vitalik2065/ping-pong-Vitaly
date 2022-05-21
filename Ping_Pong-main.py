import pygame

pygame.init()
scr_width = 500
scr_height= 500
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Ping_Pong")

FPS = 60

screen.fill((0, 0, 255))

game = True

clock = pygame.time.Clock()

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    pygame.display.update()
    clock.tick(FPS)
