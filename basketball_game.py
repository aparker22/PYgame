import pygame

class Ball(object):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5
        self.radius = 50

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x + self.radius > width:
            self.speed_x = 0
        if self.y + self.radius > height:
            self.speed_y = 0
        if self.x - self.radius < 0:
            self.speed_x = 0
        if self.y - self.radius < 0:
            self.speed_y = 0

    def render(self, screen):
        pygame.draw.circle(screen, (self.color), (self.x, self.y), self.radius)

        

def main():
    # declare the size of the canvas
    width = 1200
    height = 700
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Basketball game')

    # Game initialization
    ball = Ball((250, 131, 32), 250, 250)
    goal_image = pygame.image.load('goal.png').convert_alpha()
    goal_image = pygame.transform.scale(goal_image, (200, 200))

    
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            # activate the cooresponding speeds
            # when an arrow key is pressed down
            if pressed[pygame.K_UP]:
                ball.y -= 5
                ball.speed_y = -5
            elif pressed[pygame.K_DOWN]:
                ball.y += 5
                ball.speed_y = 5
            elif pressed[pygame.K_LEFT]:
                ball.x -= 5
                ball.speed_x = -5
            elif pressed[pygame.K_RIGHT]:
                ball.x += 5
                ball.speed_x = 5
        # if event.type == pygame.KEYUP:
        #     # deactivate the cooresponding speeds
        #     # when an arrow key is released
        #     if event.key == KEY_DOWN:
        #         ball.speed_y = 0
        #     elif event.key == KEY_UP:
        #         ball.speed_y = 0
        #     elif event.key == KEY_LEFT:
        #         ball.speed_x = 0
        #     elif event.key == KEY_RIGHT:
        #         ball.speed_x = 0
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        ball.update(width, height)

        # Draw background
        screen.fill(blue_color)

        # Game display
        ball.render(screen)
        font = pygame.font.Font(None, 25)
        text = font.render('Use arrow keys to move the ball to the goal', True, (0, 0, 0))
        screen.blit(text, (80, 230))
        screen.blit(goal_image, (500, 50))

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
