import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# colors
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# ball
ball_x = 200 
ball_y = 100
ball_x_velocity = 5
ball_y_velocity = 5
ball_radius = 30


# paddles
left_paddle_y = 0
right_paddle_y = 0

paddle_velocity = 5
paddle_height = 100
paddle_width = 20

# paddles
left_paddle = pygame.Rect((0, left_paddle_y, paddle_width, paddle_height))
right_paddle = pygame.Rect((785, right_paddle_y, paddle_width, paddle_height))

# ball
ball = pygame.draw.circle(surface = screen, color = yellow, center = [ball_x, ball_y], radius = 30)

run = True
while run:
    # screen color
    screen.fill(black)
    
    # drawing paddles 
    ball = pygame.draw.circle(surface = screen, color = yellow, center = [ball_x, ball_y], radius = 50)
    ball = ball.move([ball_x_velocity, ball_y_velocity])
    
    pygame.draw.rect(screen, blue, left_paddle)
    pygame.draw.rect(screen, red, right_paddle)
    
    
    # ball movement speed
    ball_x += ball_x_velocity
    ball_y += ball_y_velocity

    # left wall
    if ball_x < 0:
        ball_x_velocity = abs(ball_x_velocity)
    
    # right wall    
    elif ball_x > screen_width:
        ball_x_velocity = -abs(ball_x_velocity)
    
    # bottom wall
    elif ball_y > screen_height:
        ball_y_velocity = -abs(ball_y_velocity)
        
    # top wall
    elif ball_y < 0:
        ball_y_velocity = abs(ball_y_velocity)
        
    # paddle movement
    key = pygame.key.get_pressed()
    # left paddle moves up
    if key[pygame.K_w] == True:
        left_paddle.move_ip(0, -abs(paddle_velocity))
    # left paddle moves down
    elif key[pygame.K_s] == True:
        left_paddle.move_ip(0, paddle_velocity)
    
    if key[pygame.K_o] == True:
        right_paddle.move_ip(0, -abs(paddle_velocity))
        
    elif key[pygame.K_l] == True:
        right_paddle.move_ip(0, paddle_velocity)
    
    
    # event handler - we are looking at all events
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    
pygame.quit()