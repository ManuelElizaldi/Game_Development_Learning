import pygame

pygame.init()

screen_width = 800
screen_hight = 600

screen = pygame.display.set_mode((screen_width, screen_hight))

player = pygame.circle((300, 250, 50, 50))


run = True
while run:
    
    screen.fill((0,0,0))
    
    
    
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            