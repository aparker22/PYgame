import pygame
import random

#classes
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load('basketball.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5
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
        if self.x - self.radiusx <= 0:
            self.speed_x = 0
        if self.y - self.radiusx <= 0:
            self.speed_y = 0

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load('goal.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (220, 220))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Baddie(pygame.sprite.Sprite):
    def __init__(self, x, y, z):
        self.image = pygame.image.load(z).convert_alpha()
        self.image = pygame.transform.scale(self.image, (220, 220))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))



class Banana(pygame.sprite.Sprite):
    def __init__(self):
        super(Banana, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('db1.png'))
        self.images.append(pygame.image.load('db2.jpg'))
        self.images.append(pygame.image.load('db3.gif'))
        self.images.append(pygame.image.load('db4.gif'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]     

def main():
    # basics
    width = 1200
    height = 700

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Basketball game')

##This doesn't work right yet - this adds more bad guys
    # badtimer=100
    # badtimer1=0
    # badguys=[[640,100]]
    # healthvalue=194
    
    # Add Variables
    bananas = Banana()
    banana_group = pygame.sprite.Group(bananas)
    court = pygame.image.load('halfcourt.jpg')
    court = pygame.transform.scale(court, (1200, 700))
    basketball = Ball(50, 50)
    goal = Goal(487, 0)

    # #This doesn't work right yest
    # badguyimg1 = pygame.image.load("bad_guy2.gif")
    # badguyimg1 = pygame.transform.scale(badguyimg1, (100, 100))
    # badguyimg=badguyimg1

    # #These might be my bad guys
    # badguy1 = Baddie(200, 200, 'bad_guy.png')
    # badguy2 = Baddie(500, 200, 'bad_guy2.gif')
    # badguy3 = Baddie(800, 200, 'bad_guy3.gif')
    # badlist = [badguy1, badguy2, badguy3]
    
    stop_game = False



    #main game logic
    while not stop_game:
        
        ####use this with the bad guys
        # badtimer -= 1     
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
            if event.type == pygame.QUIT:
                stop_game = True
        if pygame.sprite.collide_rect(basketball, goal):
            pass
            #     banana_group.update()
            #     banana_group.draw(screen)
            #     pygame.display.flip()
        # if badtimer== 0:
        #     badguys.append([640, random.randint(50,430)])
        #     badtimer=100-(badtimer1*2)
        #     if badtimer1>=35:
        #         badtimer1=35
        #     else:
        #         badtimer1+=5
        # index=0
        # for badguy in badguys:
        #     if badguy[0]<-64:
        #         badguys.pop(index)
        #     badguy[0]-=7
        #     index+=1
        # for badguy in badguys:
        #     screen.blit(badguyimg, badguy)
    # Updating
            basketball.update(width, height)
            screen.blit(court, (0,0))
            font = pygame.font.Font(None, 25)
            text = font.render('Use arrow keys to move the ball to the goal', True, (0, 0, 0))
            screen.blit(text, (430, 630))
            goal.render(screen)
            basketball.render(screen)

            



        
        #This is how I render my bad guys:
        # for i in badlist:
        #     i.render(screen)
        

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()