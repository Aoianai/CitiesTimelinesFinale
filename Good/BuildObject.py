## buildObject ##

import pygame, random, sys

WID = 1000
HIG = 720

screen = pygame.display.set_mode((WID,HIG))     ## draws the window
pygame.display.flip()

class BuildObject(pygame.sprite.Sprite):
    """Class to hold Building sprite properties"""

    def __init__(self,x,y,image, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = size
        
    def buildRect(self,x,y,image,size):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.size, self.size)     ## establishes the square for the building
        print("COORDINATES:", self.rect.x,self.rect.y)      ## returns the coordinates to the shell
            
    def blitRect(self,x,y,image,size):
        screen.blit(image, (self.rect.x, self.rect.y))      ## refreshes the area of the screen where the square is so that it appears

    def checkCollision(self, rect):
        return self.rect.colliderect(sprite.rect)
