import pygame

pygame.init()

# screen stuff
screen_width = 1000
screen_hight = 600

screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Bouncing Ball")

# screen color 
black = (0,0,0)

# defining circle properties
red = (255, 0, 0)
circle_center_x = 400
circle_center_y = 300
circle_radius = 50

# creating ball object
ball = pygame.draw.circle(surface = screen, color = red, center = [100, 100], radius = 40)

# defining speed
# speed args [x axis speed, y axis speed]
# everytime the program updates (30fps) it will move
speed = [1, 1]

run = True
while run:
    screen.fill(black)
    
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    ball = pygame.draw.circle(screen, red, center = [100, 100], radius = 40)
    ball = ball.move(speed)
    
    pygame.display.update()

    
pygame.quit()