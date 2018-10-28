## DrawObjectBuilding

"""
## Creates a building object with attributes like the top left corner
## this will make it easier to store the position of each individual building (as they will be seperate)
## and also allow for size increases while reducing the overall lines of code
"""

import pygame
import random
import DrawObjectBuilding
screen = pygame.display.set_mode((1356,720))
WHITE = (255,255,255)
screen.fill(WHITE)
clock = pygame.time.Clock()
image = pygame.image.load("BuildingLevelOne.png").convert_alpha()


class BuildObject(object):
    """Class to hold Building sprite properties"""

    def __init__(self,x,y,image):
        #build.append(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def getXY(self,x,y,image):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, 20, 20)
        print(self.rect.x,self.rect.y)
            
    def drawBlit(self,x,y,image):
        screen.blit(image, (self.rect.x, self.rect.y))

x = 1
while x == 1:
    for i in range(1,6):
        clock.tick(60)
        x = random.randrange(0,1356,20)
        y = random.randrange(0,720,20)
        create = DrawObjectBuilding.BuildObject(x,y,image)
        create.getXY(x,y,image)
        create.drawBlit(x,y,image)
        clock.tick(60)
        x += 1
