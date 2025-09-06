import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

def ball_to_center(ball_x, ball_y):
    ball_x = screen_width // 2
    ball_y = screen_height // 2 
    return ball_x, ball_y

# colors
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# ball
ball_x = 200 
ball_y = 100
ball_x_velocity = 0.4
ball_y_velocity = 0.4
ball_radius = 30


# paddles - these could be 1 variable
left_paddle_y = 0
right_paddle_y = 0

paddle_velocity = 0.7
paddle_height = 100
paddle_width = 20

# wait period
wait_period = 700

# paddles pygame.Rect(left, top, width, height)
# left (x) → The x-coordinate of the rectangle’s left edge.
# top (y) → The y-coordinate of the rectangle’s top edge.
# width (w) → The width of the rectangle.
# height (h) → The height of the rectangle.

# we never declared a paddle_x - interesting
left_paddle = pygame.Rect((0, left_paddle_y, paddle_width, paddle_height))
right_paddle = pygame.Rect((785, right_paddle_y, paddle_width, paddle_height))

# game loop
run = True
while run:
    # screen color
    screen.fill(black)
     
    # drawing paddles 
    ball = pygame.draw.circle(surface = screen, color = yellow, center = [ball_x, ball_y], radius = 50)
    # this allows movment
    ball = ball.move([ball_x_velocity, ball_y_velocity])
    
    # this acually moves it ball movement speed
    ball_x += ball_x_velocity
    ball_y += ball_y_velocity
    
    pygame.draw.rect(screen, blue, left_paddle)
    pygame.draw.rect(screen, red, right_paddle)

    # left wall
    # only bounce if the ball is inside the left paddle 
    if ball_x < 0:
        if (ball_y > left_paddle_y) and (ball_y < left_paddle_y + paddle_height):
            ball_x_velocity = abs(ball_x_velocity)
        else:
            pygame.time.wait(wait_period)
            ball_x, ball_y = ball_to_center(ball_x, ball_y)
    
    # right wall    
    # right wall, only bounce if its inside the right paddle
    if ball_x > screen_width:
        if (ball_y > right_paddle_y) and (ball_y < right_paddle_y + paddle_height):
            ball_x_velocity = -abs(ball_x_velocity)
        else:
            pygame.time.wait(wait_period)
            ball_x, ball_y = ball_to_center(ball_x, ball_y)
    
    # bottom wall
    elif ball_y > screen_height:
        ball_y_velocity = -abs(ball_y_velocity)
        
    # top wall
    elif ball_y < 0:
        ball_y_velocity = abs(ball_y_velocity)
      
    #paddle movement
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        left_paddle_y -= paddle_velocity
    elif key[pygame.K_s]:
        left_paddle_y += paddle_velocity

    if key[pygame.K_o]:
        right_paddle_y -= paddle_velocity
    elif key[pygame.K_l]:
        right_paddle_y += paddle_velocity


    # Paddle maximum and minimums - this prevents the paddle to go flying off the screen
    if left_paddle_y < 0:
        left_paddle_y = 0
    elif left_paddle_y > screen_height - paddle_height:
        left_paddle_y = screen_height - paddle_height
    
    if right_paddle_y < 0:
        right_paddle_y = 0
    elif right_paddle_y > screen_height - paddle_height:
        right_paddle_y = screen_height - paddle_height


    # important to sync up variables
    left_paddle.y = left_paddle_y
    right_paddle.y = right_paddle_y

    # event handler - we are looking at all events
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    
pygame.quit()