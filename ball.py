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
circle_center_x, circle_center_y = [400, 300]
circle_radius = 50

# defining speed
# speed args [x axis speed, y axis speed]
# everytime the program updates (30fps) it will move

x_velocity = 1
y_velocity = 1

# creating ball object
ball = pygame.draw.circle(surface = screen, color = red, center = [circle_center_x, circle_center_y], radius = circle_radius)

# game loop
run = True
while run:
    
    # black background
    screen.fill(black)
    
    # drawing circle
    ball = pygame.draw.circle(screen, red, center = [circle_center_x, circle_center_y], radius = circle_radius)
    ball = ball.move([x_velocity, y_velocity])
    
    # movement - current state: too fast! 
    circle_center_x += x_velocity
    circle_center_y += y_velocity

    # left wall logic 
    if circle_center_x < 0:
        x_velocity = abs(x_velocity)
        
    # right wall logic
    elif circle_center_x > screen_width:
        x_velocity = -abs(x_velocity)
    
    # top wall logic 
    elif circle_center_y < 0:
        y_velocity = abs(y_velocity)
    
    # bottom wall logic
    elif circle_center_y > screen_hight:
        y_velocity = -abs(y_velocity)
    
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()

    
pygame.quit() 