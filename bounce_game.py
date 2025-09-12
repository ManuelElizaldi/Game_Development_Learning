import pygame

pygame.init()

screen_width = 600
screen_height = 900
black = (0, 0, 0)
red = (255, 0, 0)

# paddle stuff
paddle_y = 850
paddle_x = 300
paddle_velocity = 3
paddle_width = 100
paddle_height = 20
paddle_obj = pygame.Rect((paddle_x, paddle_y, paddle_width, paddle_height))

# ball stuff
ball_x = 200 
ball_y = 100
ball_x_velocity = 0.4 
ball_y_velocity = 0.4
ball_radius = 10

# score board set up 
score = 0 
pygame.font.init()
font = pygame.font.SysFont('arial', 30, bold=True)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bounce")

def ball_to_center(ball_x, ball_y):
    ball_x = 350
    ball_y = 100
    return ball_x, ball_y

def display_score(score_x, score_y):
    # RGB Color 	teal -> r: 0, g: 128, b: 128
    score_img = font.render(f"Total Score: {score}", True, [0, 128, 128])
    screen.blit(score_img, (score_x, score_y))
    

# game loop
run = True
while run:
    # screen color
    screen.fill(black)
    
    # drawing paddle
    pygame.draw.rect(screen, red, paddle_obj)
    
    # drawing ball
    ball = pygame.draw.circle(surface = screen, color = red, center = [ball_x, ball_y], radius = ball_radius)
    ball = ball.move([ball_x_velocity, ball_y_velocity])
    
    ball_x += ball_x_velocity
    ball_y += ball_y_velocity
    
    # right wall 
    if ball_x > screen_width:
        ball_x_velocity = -abs(ball_x_velocity)
    
    # left wall 
    if ball_x < 0:
        ball_x_velocity = abs(ball_x_velocity)
        
    # top wall
    if ball_y < 0:
        ball_y_velocity = abs(ball_y_velocity)
    
    # bottom wall
    if ball_y > screen_height:
        ball_x, ball_y = ball_to_center(ball_x, ball_y)
    
    # ball touching paddle -> bounce up  
    if ball_y > paddle_y:    
        if (ball_x > paddle_x) and (ball_x < paddle_x + paddle_width):
            ball_y_velocity = -abs(ball_y_velocity)
            score += 1
    
    # paddle movement 
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        paddle_x -= paddle_velocity  
    elif key[pygame.K_d]:
        paddle_x += paddle_velocity 
    
    # left wall
    if paddle_x < 0:
        paddle_x = 0
    
    elif paddle_x > screen_width - paddle_width:
        paddle_x = screen_width - paddle_width
    
    ## There is an error going on here, fix it later...
    display_score(10, 10)
    
    # sync the paddle obj to the paddle drawing
    paddle_obj.x = paddle_x
    paddle_obj.y = paddle_y
    
    # event handler - we are looking at all events
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    
pygame.quit()