import pygame

pygame.init()

# game window 
screen_width = 800
screen_hight = 600

screen = pygame.display.set_mode((screen_width, screen_hight))

# adding feature - character
# doing it before game loop as preparation
player = pygame.Rect((300, 250, 50, 50))

# game loop
run = True
while run:
    
    # this will avoid the rectangel leaving a trail, it refreshes the screen with black
    screen.fill((0, 0, 0))
    
    # things that you are drawing on screen:
    pygame.draw.rect(screen, (255, 0, 0), player)
    
    # movement 
    # move_ip(x,y) -> think of a plain
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_q] == True:
        player.move_ip(-1, -1)
    elif key[pygame.K_e] == True:
        player.move_ip(1, -1)
    
    # event handler - we are looking at all events
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False

    # capture all changes within the game loop
    pygame.display.update()

# this stops the program, you need this to exit the game loop
pygame.quit()

