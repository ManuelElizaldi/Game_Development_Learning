import pygame

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))


run = True
while run:
    
    key = pygame.key.get_focused()
    if key == True:
        print(key, "a was pressed")
    
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    
    pygame.display.update()