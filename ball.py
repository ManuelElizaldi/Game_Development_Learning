import pygame

pygame.init()

# screen stuff
screen_width = 1000
screen_hight = 600

screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Bouncing Ball")

# defining rgb colors
black = (0,0,0)
red = (255, 0, 0)

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
            
    pygame.display.update()

    # move the ball
    ball_object = ball_object.move(speed)
    
    if ball_object.left <= 0 or ball_object.right >= screen_width:
        speed[0] = -speed[0]
    if ball_object.top <= 0 or ball_object.bottom >= screen_hight:
        speed[1] = -speed[1]
    
pygame.quit()