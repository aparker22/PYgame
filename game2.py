
import pygame
from pygame.locals import *
import math
import random

# Initialize the game
pygame.init()
width, height = 1200, 700
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos=[600, 680]



#  this is a timer for the badguys
badtimer=100
badtimer1=0
badguys=[[640,100]]
bad_list = []


# 3 - Load images
player = pygame.image.load("basketball.png")
player = pygame.transform.scale(player, (100, 100))
grass = pygame.image.load('resources/images/grass.png')
goal = pygame.image.load('goal.png')
goal = pygame.transform.scale(goal, (200, 200))
court = pygame.image.load('halfcourt.jpg')
court = pygame.transform.scale(court, (1200, 700))
badguyimg1 = pygame.image.load("bad_guy.png")
badguyimg1 = pygame.transform.scale(badguyimg1, (100, 100))

#these images don't loop through?
# badguyimg2 = pygame.image.load("bad_guy2.gif")
# badguyimg2 = pygame.transform.scale(badguyimg2, (100, 100))
# badguyimg3 = pygame.image.load("bad_guy3.gif")
# badguyimg3 = pygame.transform.scale(badguyimg3, (100, 100))
# badlist = [badguyimg1, badguyimg2, badguyimg3]


#  Game Logic
while 1:
    badtimer -= 1
    screen.blit(court, (0, 0))
    screen.blit(goal,(487, 0))
    
    #This sets the initital positions
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1) 


    #This makes badguys appear on screen
    if badtimer==0:
        badguys.append([1040, random.randint(50,430)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=7
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg1, badguy)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0) 
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_DOWN:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
    if event.type==pygame.MOUSEBUTTONDOWN:
        position=pygame.mouse.get_pos()
 

            