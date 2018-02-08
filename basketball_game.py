import pygame


class Ball(object):
    def __init__(self, x, y):
        self.image = pygame.image.load('basketball.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5
        self.radius = 0
        self.radiusx = 0
        self.radiusy = 100

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x + self.radiusx > width:
            self.speed_x = 0
        if self.y + self.radiusx > height:
            self.speed_y = 0        
        if self.x + self.radiusy > width:
            self.speed_x = 0
        if self.y + self.radiusy > height:
            self.speed_y = 0
        if self.x - self.radius <= 0:
            self.speed_x = 0
        if self.y - self.radius <= 0:
            self.speed_y = 0

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

        

def main():
    # declare the size of the canvas
    width = 1200
    height = 700
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Basketball game')

    # Game initialization
    basketball = Ball((width / 2), (height / 2))
    goal_image = pygame.image.load('goal.png').convert_alpha()
    goal_image = pygame.transform.scale(goal_image, (200, 200))

    
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            # activate the cooresponding speeds
            # when an arrow key is pressed down
            if pressed[pygame.K_UP]:
                basketball.y -= 5
                basketball.speed_y = -5
            elif pressed[pygame.K_DOWN]:
                basketball.y += 5
                basketball.speed_y = 5
            elif pressed[pygame.K_LEFT]:
                basketball.x -= 5
                basketball.speed_x = -5
            elif pressed[pygame.K_RIGHT]:
                basketball.x += 5
                basketball.speed_x = 5
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
        basketball.update(width, height)

        # Draw background
        screen.fill(blue_color)

        # Game display
        
        font = pygame.font.Font(None, 25)
        text = font.render('Use arrow keys to move the ball to the goal', True, (0, 0, 0))
        screen.blit(text, (430, 630))
        screen.blit(goal_image, (500, 50))
        basketball.render(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()